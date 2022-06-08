---
title: "GitCommitMessage"
date: 2021-02-04T12:52:04+08:00
draft: true
categories:
 - "學習"
tags:
 - "git"
toc: true
---

## Git Commit Message 規範
<!--more-->

## 前言

一般來說Git Commit 要包含 

## Commit Message 規範

### commit message格式

```
<type>: scope : <subject>

```
EX:
```
feat:DAO:新增用戶(Customer)的DAO
```


#### type 的規範：
- feat: 新增/修改功能 (feature)。
- modify：功能上的修正（非 bug）
- fix: 修補 bug (bug fix)。
- delete：刪除檔案
- docs: 文件 (documentation)。
- style: 格式 (不影響程式碼運行的變動 white-space, formatting, missing semi colons, etc)。
- refactor: 重構 (既不是新增功能，也不是修補 bug 的程式碼變動)。
- test: 增加測試 (when adding missing tests)。
- chore: 建構程序或輔助工具的變動 (maintain)。
- revert: 撤銷回覆先前的 commit 例如：revert: type(scope): subject (回覆版本：xxxx)。
- perf: 改善效能 (A code change that improves performance)。

Type 是用來告訴進行 Code Review 的人應該以什麼態度來檢視 Commit 內容。
例如：
看到 Type 為 fix，進行 Code Review 的人就可以用「觀察 Commit 如何解決錯誤」的角度來閱讀程式碼。
若是 refactor，則可以放輕鬆閱讀程式碼如何被重構，因為重構的本質是不會影響既有的功能。
利用不同的 Type 來決定進行 Code Review 檢視的角度，可以提升 Code Review 的速度。因此開發團隊應該要對這些 Type 的使用時機有一致的認同。

#### scope 的規範：

scope 用於說明 commit  影響的範圍，EX:Controller 、 Dao、 view

如果修改影響不只一個scope，可以使用*代替。

#### subject :

subject是commit目的的臨時描述，不超過50個字符。

建議使用中文（感覺中國人用中文描述問題能更清楚一些）。

開頭不加句號或其他標點符號。
根據以上規範git commit message將是如下的格式：

### 總結

### 參考

[如何规范你的Git commit？-阿里云开发者社区](https://developer.aliyun.com/article/770277)

[Git Commit Message 這樣寫會更好，替專案引入規範與範例](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)
