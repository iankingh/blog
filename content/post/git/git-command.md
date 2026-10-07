---
title: "Git 基本流程：檢查、暫存與提交"
date: 2021-07-14T09:21:29+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
toc: true
description: "補齊 status、diff、add、commit 的操作順序，區分工作目錄與暫存區。"
lastmod: 2026-10-07T20:50:40+08:00
---

補齊 status、diff、add、commit 的操作順序，區分工作目錄與暫存區。

<!--more-->

適用：Git 2.x；先準備一個可丟棄的本機 repository。

## 最小練習

```bash
mkdir git-note-lab
cd git-note-lab
git init
git config user.name "Note Lab"
git config user.email "note-lab@example.invalid"
printf 'campfire\n' > note.txt
git status --short
git add note.txt
git diff --cached
git commit -m "docs: 新增練習筆記"
git status --short
```

初始 status 顯示 `?? note.txt`，add 後暫存區有新增內容，commit 後 status 無輸出表示乾淨。設定只作用於此 repository，不用 --global 改個人設定。

## 暫存不是提交

`git diff` 比較工作目錄與暫存區；`git diff --cached` 比較暫存區與 HEAD。檔案 add 後再次修改，新修改不會自動進同一個 commit，需再次 add。`git add .` 包括指定目錄內新增、修改與刪除；忽略規則不會停止追蹤已經進 Git 的檔案。

取消暫存可用 `git restore --staged note.txt`（已有 HEAD 時）；這不會刪除工作目錄內容。不要把 `git restore note.txt` 當同一操作，後者會覆蓋尚未暫存修改。提交前檢查 staged diff，避免把 .env、編譯輸出或不相關檔案帶入。

完成後在父目錄自行移除練習資料夾。這裡不含遠端操作，push 前還需確認 branch、remote 與許可權。

## 參考資料

- [git-add](https://git-scm.com/docs/git-add)
- [git-status](https://git-scm.com/docs/git-status)
- [git-diff](https://git-scm.com/docs/git-diff)
