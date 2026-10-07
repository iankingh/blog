"""Record a release only after Pages builds the exact gh-pages deployment.

Run in the deploy job after publishing. Uses GitHub CLI and its GH_TOKEN;
never prints credentials. Unit tests inject a fake client and clock.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
from datetime import datetime
from zoneinfo import ZoneInfo


class GitHub:
    def __init__(self, repository):
        self.repository = repository

    def api(self, endpoint, missing_ok=False):
        result = subprocess.run(
            ['gh', 'api', f'repos/{self.repository}/{endpoint}'],
            text=True, capture_output=True, timeout=45,
        )
        if result.returncode:
            if missing_ok and re.search(r'\bHTTP 404\b', result.stderr):
                return None
            raise RuntimeError(f'GitHub API failed for {endpoint}: {result.stderr.strip()}')
        return json.loads(result.stdout)

    def create_release(self, tag, source_sha, notes, tagged):
        with tempfile.TemporaryDirectory(prefix='blog-release-') as directory:
            body = Path(directory) / 'release.md'
            body.write_text(notes, encoding='utf-8')
            command = ['gh', 'release', 'create', tag, '--repo', self.repository,
                       '--title', f'正式部署 {tag}', '--notes-file', str(body)]
            command += ['--verify-tag'] if tagged else ['--target', source_sha]
            subprocess.run(command, check=True, timeout=90)


def deployment_tag(created_at, run_id):
    # Use the original run creation date so a rerun on a later day stays idempotent.
    day = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
    day = day.astimezone(ZoneInfo('Asia/Taipei')).strftime('%Y%m%d')
    return f'deploy-{day}-{run_id}'


def wait_for_pages(github, pages_sha, *, timeout=600, interval=15,
                   clock=time.monotonic, sleep=time.sleep):
    deadline = clock() + timeout
    while clock() < deadline:
        builds = github.api('pages/builds?per_page=100')
        build = next((item for item in builds if item['commit'] == pages_sha), None)
        if build:
            if build['status'] == 'built':
                return build
            if build['status'] == 'errored':
                message = (build.get('error') or {}).get('message') or 'unknown error'
                raise RuntimeError(f'Pages build failed for {pages_sha}: {message}')
        remaining = deadline - clock()
        if remaining > 0:
            sleep(min(interval, remaining))
    raise RuntimeError(f'Timed out waiting for Pages build {pages_sha}; no release created')


def tag_commit(github, reference):
    obj = reference['object']
    # Existing annotated tags must be dereferenced before comparing commits.
    for _ in range(10):
        if obj['type'] == 'commit':
            return obj['sha']
        if obj['type'] != 'tag':
            break
        obj = github.api(f'git/tags/{obj["sha"]}')['object']
    raise RuntimeError('Release tag does not resolve to a commit')


def ensure_release(github, tag, source_sha, notes):
    reference = github.api(f'git/ref/tags/{tag}', missing_ok=True)
    if reference and tag_commit(github, reference) != source_sha:
        raise RuntimeError(f'Tag {tag} points to a different source commit; refusing to overwrite')
    release = github.api(f'releases/tags/{tag}', missing_ok=True)
    if release:
        if not reference or release.get('draft') or release.get('prerelease'):
            raise RuntimeError(f'Existing release {tag} is inconsistent with a published deployment')
        print(f'Release already exists: {release["html_url"]}')
        return
    github.create_release(tag, source_sha, notes, tagged=reference is not None)
    # Check the actual tag, rather than trusting release.target_commitish.
    reference = github.api(f'git/ref/tags/{tag}')
    if tag_commit(github, reference) != source_sha:
        raise RuntimeError(f'Created tag {tag} does not match the deployed source')
    print(f'Release created: https://github.com/{github.repository}/releases/tag/{tag}')


def release_notes(repository, source_sha, pages_sha, run_id, site_url):
    root = f'https://github.com/{repository}'
    blob = f'{root}/blob/{source_sha}'
    return f'''本次正式站台已完成 GitHub Pages 建置。

- 正式站台：{site_url}
- 來源提交：{root}/commit/{source_sha}
- 站台產物提交：{root}/commit/{pages_sha}
- 部署工作流程：{root}/actions/runs/{run_id}

## 本次建置檢查

Hugo 正式建置、筆記結構與內部連結、搜尋互動、網站安全，以及自動 Release 邏輯測試通過。
逐項執行結果以本次工作流程日誌為準。

## 既有技術查核紀錄

- [完整查核報告]({blob}/docs/note-review.md)
- [逐篇查核清單]({blob}/docs/note-review.json)
- [範例驗證證據]({blob}/docs/example-results.json)
- [來源查核證據]({blob}/docs/source-checks.json)

以上紀錄固定於本次來源提交；技術驗證日期與範圍依紀錄為準。
每次部署不會自動重跑所有 Java、Vue、Angular、Spring 或平台範例。
'''


def publish(github, source_sha, run_id):
    run = github.api(f'actions/runs/{run_id}')
    if run['head_sha'] != source_sha:
        raise RuntimeError('Workflow run does not match the source SHA')
    tag = deployment_tag(run['created_at'], run_id)
    commit = github.api('commits/gh-pages')
    # Detect another publisher instead of accidentally recording its build.
    marker = f'deploy: {source_sha}'
    if commit['commit']['message'].splitlines()[0] != marker:
        raise RuntimeError('gh-pages does not identify this source deployment')
    pages_sha = commit['sha']
    wait_for_pages(github, pages_sha)
    site = github.api('pages')
    notes = release_notes(github.repository, source_sha, pages_sha, run_id, site['html_url'])
    ensure_release(github, tag, source_sha, notes)


def main():
    repository = os.environ['GITHUB_REPOSITORY']
    source_sha = os.environ['GITHUB_SHA']
    run_id = os.environ['GITHUB_RUN_ID']
    if not re.fullmatch(r'[\w.-]+/[\w.-]+', repository):
        raise RuntimeError('Invalid repository')
    if not re.fullmatch(r'[0-9a-f]{40}', source_sha) or not run_id.isdigit():
        raise RuntimeError('Invalid source SHA or workflow run ID')
    publish(GitHub(repository), source_sha, run_id)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, KeyError, subprocess.SubprocessError, ValueError) as error:
        raise SystemExit(f'Deployment release failed: {error}')
