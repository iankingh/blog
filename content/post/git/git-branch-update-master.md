---
title: "Git 分支同步：把主分支更新帶入工作分支"
date: 2021-02-02T22:04:27+08:00
categories:
 - "筆記"
tags:
 - "git"
toc: true
draft: false
description: "說明 fetch、fast-forward 與 merge 的差異，補上衝突處理及中止方式。"
lastmod: 2026-10-07T20:50:40+08:00
---

說明 fetch、fast-forward 與 merge 的差異，補上衝突處理及中止方式。

<!--more-->

適用：Git 2.x，repository 有 origin/master 和自己的工作分支。若主分支為 main，按實際名稱替換。

## 操作前

用 `git status` 確認未完成修改已提交或 stash，`git branch --show-current` 核對目前分支，`git remote -v` 確認來源。以下 feature-note 代表已存在的工作分支，不要套用到別人的分支。

```bash
git fetch origin
git switch master
git pull --ff-only origin master
git switch feature-note
git merge master
```

pull --ff-only 在本機與遠端已分岔時拒絕前進，讓你先判斷本機提交用途。只要取得最新主分支不一定要切換，可從工作分支直接 `git merge origin/master`，fetch 仍須先做。

## 衝突處理

merge 衝突時 status 列出檔案。檢查衝突區段兩側的意圖，修改成最終內容，移除標記，執行相關測試，再 `git add 具體檔案`、`git commit` 完成 merge。若需回到操作前，使用 `git merge --abort`，不是 reset --hard。

確認 `git log --oneline --graph --decorate -10`，看主分支提交是否已在工作分支歷史，並檢查實際功能。`git rebase origin/master` 是重排自己的提交而非建立 merge commit；已共享的歷史需團隊協調，不能把兩者當無差異替換。這個同步流程沒有替你推送分支。

## 參考資料

- [git-merge](https://git-scm.com/docs/git-merge)
- [git-pull](https://git-scm.com/docs/git-pull)
- [git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: 四種將分支與主線同步的方法 | Summer。桑莫。夏天](https://cythilya.github.io/2018/06/19/git-merge-branch-into-master/)
