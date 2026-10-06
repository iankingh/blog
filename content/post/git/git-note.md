---
title: "Git 日常筆記：遠端、忽略規則與回復提交"
date: 2021-07-13T22:07:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
toc: true
description: "重整易混淆指令，區分 revert、reset 與工作目錄還原。"
lastmod: 2026-10-07T00:01:00+08:00
---

重整易混淆指令，區分 revert、reset 與工作目錄還原。

<!--more-->

適用：Git 2.x 的已存在專案；需要了解第 1 篇的 staged / unstaged 差異。

## 常用的唯讀檢查

```bash
git status --short
git remote -v
git branch -vv
git log --oneline --graph --decorate -12
git diff --stat
git diff --cached --stat
```

branch -vv 顯示追蹤關係，但 ahead/behind 是根據最近一次 fetch，不保證遠端現在的狀態。remote add 新增來源、remote set-url 修改來源，先確認目的地再推送。

## 忽略與已追蹤檔案

.gitignore 只影響未追蹤檔，不會消除歷史內的密碼。欲停止追蹤特定檔但保留本機檔案，檢查後使用 `git rm --cached 檔案` 並提交規則。已外流憑證應輪替，不能只刪檔當修復。

## 三種回復

| 操作 | 適用目的 | 影響 |
| --- | --- | --- |
| git revert 提交 | 回復已共享修改 | 新增反向提交，保留歷史 |
| git reset --soft 提交 | 重整理自己尚未共享提交 | 移動 HEAD，保留暫存修改 |
| git restore --staged 檔案 | 取消暫存 | 不覆蓋工作目錄 |

reset --hard 會覆蓋 tracked 的未提交內容，不能作為「檢視舊版」的捷徑。只想探索舊提交可建獨立 worktree 或 detached checkout，先儲存當前修改。revert merge commit 還要指定主線，需先理解歷史圖再操作。

確認回復後看 diff 與測試，並在 commit 訊息寫明原始提交與回復理由。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [git-restore](https://git-scm.com/docs/git-restore)
- [git-reset](https://git-scm.com/docs/git-reset)
- [git-revert](https://git-scm.com/docs/git-revert)
- [gitignore](https://git-scm.com/docs/gitignore)
