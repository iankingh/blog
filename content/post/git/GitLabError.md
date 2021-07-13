---
title: "連線GitLab問題處理"
date: 2020-05-15T16:36:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
 - "gitLab"
toc: true
---



<!--more-->


## 連線GitLab問題處理

### 問題1 : 在連線 gitlab 遇到fatal: Authentication failed for.... 的問題

 可能是有人重灌gitlab 或是改密碼時造成 憑證用舊的對新的 gitlab 密碼

#### Windows 解法

#### 解決方法1 : 到 win10 的控制台/認證管理員/ Windows 認證

或到搜尋輸入
```
Credential Manager / Windows Credentials/ 
```
找到  對應的 gitlab 把他移除

**1.Credential Manager**

![Credential Manager](/images/git/Credential_Manager.png)

**2.Windows Credentials**

![Windows_Credentials](/images/git/Windows_Credentials.png)

## 參考

[在gitlab 遇到fatal: Authentication failed for.... 的問題 | Frank的探索之旅 - 點部落](https://dotblogs.com.tw/zeroade/2018/10/11/111941)

