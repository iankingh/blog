---
title: "GitBranchUpdateMaster"
date: 2021-02-02T22:04:27+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
toc: true
---




# Git dev-branch Update master-branch
<!--more-->

## 前言

一般來說 我們會先 clone 一份到我們的自己的儲存庫 , 再開一個分支開發 checkout -b dev-1 

當主要分支有所變動時 可以使用以下方式更新主要分支

從最新的master checkout 分支出去

再把dev-1  跟新的分支合併



參考
Git: 四種將分支與主線同步的方法 | Summer。桑莫。夏天
https://cythilya.github.io/2018/06/19/git-merge-branch-into-master/