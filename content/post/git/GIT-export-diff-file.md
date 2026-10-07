---
title: "Git 匯出版本差異：固定目標提交並保留空白路徑"
date: 2022-02-23T18:13:27+08:00
categories:
 - "筆記"
tags:
 - "git"
 - "版控"
toc: true
draft: false
description: "補齊從兩個版本匯出改動檔案的可靠指令碼，排除刪除檔並記錄刪除清單。"
lastmod: 2026-10-07T20:50:40+08:00
---

補齊從兩個版本匯出改動檔案的可靠指令碼，排除刪除檔並記錄刪除清單。

<!--more-->

適用：Git 2.x 與 Python 3；匯出的是已提交目標版本，不包含未提交的工作目錄。

## 完整匯出指令碼

原 `git archive HEAD $(git diff-tree ...)` 會錯用 HEAD，且空白路徑被 shell 拆開。儲存為 export_diff.py：

```python
import json
import subprocess
import sys
from pathlib import Path

def git(*args):
    return subprocess.check_output(['git', *args])

if len(sys.argv) != 4:
    raise SystemExit('usage: python3 export_diff.py BASE TARGET OUTPUT_DIR')
base, target, output = sys.argv[1:]
base = git('rev-parse', '--verify', base + '^{commit}').decode().strip()
target = git('rev-parse', '--verify', target + '^{commit}').decode().strip()
destination = Path(output)
destination.mkdir(parents=True, exist_ok=True)
changed = git('diff', '--name-only', '-z', '--diff-filter=ACMRT', '--no-renames', base, target)
paths = [value.decode('utf-8') for value in changed.split(b'\0') if value]
deleted = git('diff', '--name-only', '-z', '--diff-filter=D', '--no-renames', base, target)
(destination / 'deleted.json').write_text(json.dumps([p.decode('utf-8') for p in deleted.split(b'\0') if p], ensure_ascii=False, indent=2), encoding='utf-8')
archive = destination / 'changed.zip'
if paths:
    subprocess.run(['git', 'archive', '--format=zip', '-o', str(archive.resolve()), target, '--', *paths], check=True)
else:
    import zipfile
    with zipfile.ZipFile(archive, 'w'): pass
print(f'exported {len(paths)} paths from {target}')
```

```bash
python3 export_diff.py HEAD~1 HEAD ./export-result
```

## 確認與限制

changed.zip 包含 TARGET 的新增／修改檔，deleted.json 列出部署時需另外處理的刪除路徑；rename 以刪除＋新增記錄。以含空白檔名、只有刪除、無差異三種情境核對，解壓後再比對目標提交。

此指令碼選用 UTF-8 路徑，非 UTF-8 repository 需另設編碼策略；大量路徑可能超過 OS argv 上限，應改批次或先匯出完整版本再取檔。Git submodule 的內容不由父 repository 的 archive 打包。差異檔也不是完整可部署成品，仍需建置與依賴確認。

## 參考資料

- [git-archive](https://git-scm.com/docs/git-archive)
- [git-diff](https://git-scm.com/docs/git-diff)
- [匯出 Git Commit 檔案並維持資料夾結構-黑暗執行緒 (darkthread.net)](https://blog.darkthread.net/blog/export-git-commit-files/)
- [GIT 檢視/匯出差異檔案 - LinYoYo_攻城獅_學習筆記 (hank7891.github.io)](https://hank7891.github.io/2021/08/11/GIT%E6%9F%A5%E7%9C%8B:%E5%8C%AF%E5%87%BA%E5%B7%AE%E7%95%B0%E6%AA%94%E6%A1%88/)
- [git 匯出差異清單和檔案. 匯出特定版本中新增或修改過的檔案 | by Jingle Lin | Jiingler | Medium](https://medium.com/jiingler/git-%E5%8C%AF%E5%87%BA%E5%B7%AE%E7%95%B0%E6%B8%85%E5%96%AE%E5%92%8C%E6%AA%94%E6%A1%88-42b6ab9c7594)
