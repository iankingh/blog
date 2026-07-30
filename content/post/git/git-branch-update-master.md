---
title: "同步開發分支與主分支"
date: 2021-02-02T22:04:27+08:00
categories:
 - "筆記"
tags:
 - "git"
toc: true
draft: false
---

## 同步開發分支與主分支

<!--more-->

## 前言

開發功能時通常會從主分支建立獨立分支：

```shell
git switch master
git pull --ff-only
git switch -c dev-1
```

當遠端主分支有新提交時，先更新本機主分支，再把變更合併進開發分支：

```shell
git switch master
git pull --ff-only
git switch dev-1
git merge master
```

若專案慣用 rebase，也可在 `dev-1` 執行 `git rebase master`，但已共享的分支應先與團隊確認，避免改寫他人的提交歷史。

## 參考

[Git: 四種將分支與主線同步的方法 | Summer。桑莫。夏天](https://cythilya.github.io/2018/06/19/git-merge-branch-into-master/)
