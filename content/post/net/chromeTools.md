---
title: "ChromeTools"
date: 2021-04-11T19:11:37+08:00
categories:
 - "筆記"
tags:
 - "net"
 - "chrome"
toc: true
draft: false
---

## chrome 筆記
<!-- 簡介 -->


<!--more-->

## 使用 overrides

### 前言

overrides 是 chrome 在 65推出的新功能 

其目的是為 可以在重新整理後還可以用使用修改後的 js ,css ...等

本地覆蓋使您可以在DevTools中進行更改，並在頁面加載期間保留這些更改。
以前，重新加載頁面時，您在DevTools中所做的任何更改都將丟失。
本地替代適用於大多數文件類型，但有一些例外。


### 操作步驟

1. Open the Sources panel  - 打開 Sources 

2. Open the Overrides tab  - 點選 Overrides

![ chromeUseDevtoolsSourcesOverrides.png ](/images/chromeTools/chromeUseDevtoolsSourcesOverrides.png) 

3. Select which directory you want to save your changes to

   3.1 點選 +Select folder for overrides 

   3.2 選擇 要存在本地的目錄

![ chromeUseOverridesSelectFolder1.png ](/images/chromeTools/chromeUseOverridesSelectFolder1.png) 

​		3.3 點選 Allows 
![ chromeUseOverridesSelectFolder2.png ](/images/chromeTools/chromeUseOverridesSelectFolder2.png) 

​		3.4 勾選 Enable Local Overrides
![ chromeUseOverridesSelectFolder3.png ](/images/chromeTools/chromeUseOverridesSelectFolder3.png) 

4. test 修改 JS 

   4.1 到 Page 修改 測試的JS

![ chromeUseOverridesModifyPageJs1.png ](/images/chromeTools/chromeUseOverridesModifyPageJs1.png) 

​	4.2 修改後 會有一個紫色點點,表示修改完成

![ chromeUseOverridesModifyPageJs2.png ](/images/chromeTools/chromeUseOverridesModifyPageJs2.png) 

​		4.3 按F5 重新整理 , 就可以看到效果

![ chromeUseOverridesModifyPageJs3.png ](/images/chromeTools/chromeUseOverridesModifyPageJs3.png) 



## 參考

[Chrome Dev Tool 的好用功能 - overrides](https://pvencs.blogspot.com/2019/01/chrome-dev-tool-overrides.html)

https://developer.chrome.com/blog/new-in-devtools-65/#overrides

