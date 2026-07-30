---
title: "EmbracingJUnitwithEclipse"
date: 2020-09-29T22:13:19+08:00
categories:
 - "筆記"
tags:
 - "eclipse"
toc: true
draft: false
---

## Junit with Eclipse
<!--more-->

### 1.新增 Junit 5

#### 設定 Build Path

在專案上按右鍵，選擇 Build Path → Configure Build Path。

![Configure Build Path](/images/eclipse/ConfigureBuildPath.png)

#### 選擇 Libraies >>Classpath >>Add Libray

![ JavaBuildPath](/images/eclipse/JavaBuildPath.png)

#### Add Library  >>>> junit

![AddLibraryJunit.png](/images/eclipse/AddLibraryJunit.png)

#### Add Library  >>>> junit5

![ AddLibraryJunit-2 ](/images/eclipse/AddLibraryJunit-2.png)

#### 加入完成

![ JavaBuildPath-2.png](/images/eclipse/JavaBuildPath-2.png)

### 2.Junit 引數設定

1.點選 於 Test.java(測試的類別) 點右鍵 >>>Run AS >>>>Run Configuations 

![JUnit 測試結果](/images/eclipse/junit.png)

2.開啟設定

Test runner : 可以選擇 版本

Enbironment  : 可以選擇 環境變數



![JUnit 執行設定](/images/eclipse/junit2.png)




![JUnit 執行結果](/images/eclipse/junit3.png)




## 參考

[Embracing JUnit 5 with Eclipse | The Eclipse Foundation](https://www.eclipse.org/community/eclipse_newsletter/2017/october/article5.php)

