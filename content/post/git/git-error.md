---
title: "Git 排錯：本機修改阻擋切換與合併衝突"
date: 2020-10-06T21:45:42+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
 - "版控"
toc: true
description: "以儲存修改為起點，補上 stash、衝突診斷與復原確認，移除無條件 hard reset 的建議。"
lastmod: 2026-10-07T20:50:40+08:00
---

以儲存修改為起點，補上 stash、衝突診斷與復原確認，移除無條件 hard reset 的建議。

<!--more-->

適用：Git 2.x；操作前能取得本機修改的備份或可辨識的提交。

## local changes would be overwritten

這表示切換／合併可能覆蓋修改，先看 `git status --short`、`git diff`、`git diff --cached`。不要直接 reset --hard。已完成內容正常提交；未完成內容可 stash：

```bash
git stash push -u -m "切換分支前保存練習修改"
git stash list
git switch target-branch
git switch original-branch
git stash apply 'stash@{0}'
git status
```

兩個 branch 名稱依實際替換。-u 包含未追蹤但不含 ignored 檔，重要 ignored 檔要自行備份。apply 保留 stash，確認內容與功能正確後才 `git stash drop 'stash@{0}'`。

## merge conflict

先辨識是否仍有 MERGE_HEAD 等未完成操作，再依 status 提示處理。合併衝突檔包含雙方修改，逐段判斷後 add、commit；放棄這次合併用 `git merge --abort`。rebase 的 continue/abort 是另一組命令，不要交叉使用。

## 遠端與歷史

fetch 更新遠端追蹤分支，不會自動丟掉工作目錄修改；pull 會接著整合，所以先讀清狀態。找不到遠端分支先 `git fetch --prune origin`、`git branch -r` 檢視，而非隨意刪除本機分支。

已提交但誤刪的歷史可從 reflog 找到候選 commit，再建立新的救援分支檢查；reflog 有儲存期限且不能恢復從未進 Git 的檔案。確認修復以 status、diff、log 及功能測試為準，不只命令退出碼。

## 參考資料

- [git-stash](https://git-scm.com/docs/git-stash)
- [git-reflog](https://git-scm.com/docs/git-reflog)
- [git-merge](https://git-scm.com/docs/git-merge)
- [git pull遇到錯誤：error: Your local changes to the following files would be overwritten by merge:解決方法](https://www.itread01.com/content/1545046022.html)
- [【狀況題】手邊的工作做到一半，臨時要切換到別的任務 - 為你自己學 Git | 高見龍](https://gitbook.tw/chapters/faq/stash.html)
