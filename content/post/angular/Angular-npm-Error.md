---
title: "AngularNpmError"
date: 2021-07-04T18:05:34+08:00
categories:
 - "技術"
tags:
 - "Angular"
 - "npm"
toc: true
draft: false
---

## 紀錄 Angular 安裝 npm 套件時遇到的錯誤
<!-- 簡介 -->
<!--more-->

### 問題

舊版 Angular 專案安裝套件時可能出現相依性錯誤；這不一定代表 npm 本身有問題，應先確認專案要求的 Node.js、npm 與 Angular 版本。
![Angular 安裝 npm 套件錯誤](/images/Angular/AngularInstallNPMError-01.png)

### 解決方法如下

如果既有專案的 lockfile 明確要求 npm 6，可暫時切換到專案指定版本：

```shell
npm install npm@6.14.13 -g
```

若專案原本使用 Yarn，應沿用對應的 `yarn.lock`，不要混用不同套件管理器。

團隊開發時應固定 Node.js 與套件管理器版本，提交 lockfile，並在 CI 使用 `npm ci` 重現安裝結果。

升級套件前先閱讀 breaking changes，逐步升級並執行測試，不要把降級 npm 當成所有相依性問題的通用解法。


## 參考
