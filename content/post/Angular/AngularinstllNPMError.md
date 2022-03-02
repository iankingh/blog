---
title: "AngularinstllNPMError"
date: 2021-07-04T18:05:34+08:00
draft: false
categories:
 - "Angular"
tags:
 - "Angular"
 - "npm"
toc: true
---

## 紀錄Angualr 安裝 npm 套件時遇到的錯誤
<!-- 簡介 -->
<!--more-->

### 問題

當安裝 npm 安裝如果出現以下錯誤 ,表示你的npm 太新了  
![AngularinstllNPMError-01](/images/java/AngularinstllNPMError-01.png)

### 解決方法如下

安裝 6.X版

```shell
npm install npm@6.14.13 -g
```

或是用Yarn

團隊在開發時建議是可以同步 node.js 及 npm 及Angular 版y本

良心建議如果可以手動解決盡量自己刻,就自己刻,有些套件依賴很嚴重, 一升級就爆了 
## 參考
