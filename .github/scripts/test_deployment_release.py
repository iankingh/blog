"""No network or releases are created by these deployment lifecycle tests."""
import importlib.util
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'deployment_release', Path(__file__).with_name('publish-deployment-release.py'))
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)
SOURCE = 'a' * 40
PAGES = 'b' * 40
TAG = 'deploy-20261007-42'


class FakeGitHub:
    repository = 'owner/blog'

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.calls = []
        self.created = []

    def api(self, endpoint, missing_ok=False):
        self.calls.append(endpoint)
        value = self.responses.get(endpoint)
        if callable(value):
            return value()
        if value is None and not missing_ok:
            raise AssertionError(f'Unexpected API call: {endpoint}')
        return value

    def create_release(self, tag, source_sha, notes, tagged):
        self.created.append((tag, source_sha, notes, tagged))
        self.responses[f'git/ref/tags/{tag}'] = reference(source_sha)
        self.responses[f'releases/tags/{tag}'] = {
            'html_url': f'https://github.com/owner/blog/releases/tag/{tag}',
            'draft': False, 'prerelease': False,
        }


def reference(sha):
    return {'object': {'type': 'commit', 'sha': sha}}


class FakeClock:
    def __init__(self):
        self.now = 0
        self.sleeps = []

    def clock(self):
        return self.now

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.now += seconds


class PagesTests(unittest.TestCase):
    def wait(self, github, timeout=600):
        clock = FakeClock()
        result = release.wait_for_pages(github, PAGES, timeout=timeout,
                                        clock=clock.clock, sleep=clock.sleep)
        return result, clock

    def test_waits_for_matching_build_not_old_success(self):
        replies = iter([
            [{'commit': 'old', 'status': 'built'}],
            [{'commit': PAGES, 'status': 'building'}],
            [{'commit': PAGES, 'status': 'built'}],
        ])
        github = FakeGitHub({'pages/builds?per_page=100': lambda: next(replies)})
        result, clock = self.wait(github)
        self.assertEqual(result['commit'], PAGES)
        self.assertEqual(clock.sleeps, [15, 15])

    def test_failed_build_stops_immediately(self):
        github = FakeGitHub({'pages/builds?per_page=100': [
            {'commit': PAGES, 'status': 'errored', 'error': {'message': 'build error'}}]})
        with self.assertRaisesRegex(RuntimeError, 'build error'):
            self.wait(github)
        self.assertEqual(len(github.calls), 1)

    def test_timeout_does_not_accept_unrelated_success(self):
        github = FakeGitHub({'pages/builds?per_page=100': [
            {'commit': 'old', 'status': 'built'}]})
        clock = FakeClock()
        with self.assertRaisesRegex(RuntimeError, 'Timed out'):
            release.wait_for_pages(github, PAGES, timeout=40,
                                   clock=clock.clock, sleep=clock.sleep)
        self.assertEqual(clock.now, 40)
        self.assertEqual(clock.sleeps, [15, 15, 10])


class ReleaseTests(unittest.TestCase):
    def test_new_release_targets_full_source_sha_and_is_idempotent(self):
        github = FakeGitHub()
        release.ensure_release(github, TAG, SOURCE, 'notes')
        release.ensure_release(github, TAG, SOURCE, 'notes')
        self.assertEqual(github.created, [(TAG, SOURCE, 'notes', False)])

    def test_retry_after_tag_created_without_release(self):
        github = FakeGitHub({f'git/ref/tags/{TAG}': reference(SOURCE)})
        release.ensure_release(github, TAG, SOURCE, 'notes')
        self.assertEqual(github.created[0][3], True)

    def test_wrong_tag_is_never_overwritten(self):
        github = FakeGitHub({f'git/ref/tags/{TAG}': reference('c' * 40)})
        with self.assertRaisesRegex(RuntimeError, 'different source'):
            release.ensure_release(github, TAG, SOURCE, 'notes')
        self.assertEqual(github.created, [])

    def test_annotated_tag_is_dereferenced(self):
        github = FakeGitHub({
            f'git/ref/tags/{TAG}': {'object': {'type': 'tag', 'sha': 'annotation'}},
            'git/tags/annotation': reference(SOURCE),
        })
        release.ensure_release(github, TAG, SOURCE, 'notes')
        self.assertTrue(github.created[0][3])

    def test_draft_is_not_reported_as_success(self):
        github = FakeGitHub({
            f'git/ref/tags/{TAG}': reference(SOURCE),
            f'releases/tags/{TAG}': {'draft': True, 'prerelease': False},
        })
        with self.assertRaisesRegex(RuntimeError, 'inconsistent'):
            release.ensure_release(github, TAG, SOURCE, 'notes')

    def test_created_tag_is_checked(self):
        github = FakeGitHub()
        def wrong_create(*args, **kwargs):
            github.responses[f'git/ref/tags/{TAG}'] = reference('c' * 40)
        github.create_release = wrong_create
        with self.assertRaisesRegex(RuntimeError, 'does not match'):
            release.ensure_release(github, TAG, SOURCE, 'notes')

    def test_creation_failure_is_reported_and_retry_can_recover(self):
        github = FakeGitHub()
        create = github.create_release
        def failed_create(*args, **kwargs):
            github.responses[f'git/ref/tags/{TAG}'] = reference(SOURCE)
            raise subprocess.CalledProcessError(1, ['gh', 'release', 'create'])
        github.create_release = failed_create
        with self.assertRaises(subprocess.CalledProcessError):
            release.ensure_release(github, TAG, SOURCE, 'notes')
        github.create_release = create
        release.ensure_release(github, TAG, SOURCE, 'notes')
        self.assertTrue(github.created[0][3])


class PublishTests(unittest.TestCase):
    def github(self):
        return FakeGitHub({
            'actions/runs/42': {'head_sha': SOURCE, 'created_at': '2026-10-06T16:01:00Z'},
            'commits/gh-pages': {'sha': PAGES, 'commit': {'message': f'deploy: {SOURCE}\n'}},
            'pages/builds?per_page=100': [{'commit': PAGES, 'status': 'built'}],
            'pages': {'html_url': 'https://owner.github.io/blog/'},
        })

    def test_success_links_fixed_source_records(self):
        github = self.github()
        release.publish(github, SOURCE, '42')
        tag, sha, notes, _ = github.created[0]
        self.assertEqual(tag, TAG)
        self.assertEqual(sha, SOURCE)
        self.assertIn(f'/blob/{SOURCE}/docs/note-review.md', notes)
        self.assertIn(f'/commit/{PAGES}', notes)
        self.assertIn('既有技術查核紀錄', notes)
        self.assertIn('不會自動重跑', notes)

    def test_pages_failure_never_reaches_release(self):
        github = self.github()
        with patch.object(release, 'wait_for_pages', side_effect=RuntimeError('failed')):
            with self.assertRaisesRegex(RuntimeError, 'failed'):
                release.publish(github, SOURCE, '42')
        self.assertFalse(any('tags/' in call for call in github.calls))

    def test_other_publisher_is_rejected(self):
        github = self.github()
        github.responses['commits/gh-pages']['commit']['message'] = 'unrelated deploy'
        with self.assertRaisesRegex(RuntimeError, 'does not identify'):
            release.publish(github, SOURCE, '42')
        self.assertEqual(github.created, [])

    def test_run_source_mismatch_is_rejected(self):
        github = self.github()
        github.responses['actions/runs/42']['head_sha'] = 'wrong'
        with self.assertRaisesRegex(RuntimeError, 'does not match'):
            release.publish(github, SOURCE, '42')

    def test_tag_day_uses_taipei_run_creation_not_rerun_clock(self):
        self.assertEqual(release.deployment_tag('2026-10-06T16:01:00Z', '42'), TAG)
        self.assertEqual(release.deployment_tag('2026-10-06T15:59:00Z', '42'),
                         'deploy-20261006-42')


class CLITests(unittest.TestCase):
    def test_only_404_can_mean_missing(self):
        client = release.GitHub('owner/blog')
        with patch.object(release.subprocess, 'run', return_value=subprocess.CompletedProcess(
                [], 1, '', 'gh: Not Found (HTTP 404)')):
            self.assertIsNone(client.api('releases/tags/tag', missing_ok=True))
        with patch.object(release.subprocess, 'run', return_value=subprocess.CompletedProcess(
                [], 1, '', 'gh: Forbidden (HTTP 403)')):
            with self.assertRaisesRegex(RuntimeError, 'HTTP 403'):
                client.api('releases/tags/tag', missing_ok=True)

    def test_create_uses_notes_file_and_target_or_verified_existing_tag(self):
        calls = []
        def run(command, **kwargs):
            calls.append(command)
            self.assertEqual(Path(command[command.index('--notes-file') + 1]).read_text(),
                             'literal notes\nwith newlines')
        with patch.object(release.subprocess, 'run', side_effect=run):
            client = release.GitHub('owner/blog')
            client.create_release(TAG, SOURCE, 'literal notes\nwith newlines', False)
            client.create_release(TAG, SOURCE, 'literal notes\nwith newlines', True)
        self.assertEqual(calls[0][-2:], ['--target', SOURCE])
        self.assertEqual(calls[1][-1], '--verify-tag')


if __name__ == '__main__':
    unittest.main()
