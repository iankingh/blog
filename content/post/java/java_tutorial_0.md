---
title: "[從 0 開始的 JAVA 生活] No.0  JAVA 環境安裝"
date: 2020-05-19T06:22:46+08:00
draft: false
categories:
  - "筆記"
  - "技術"
tags:
 - "java"
toc: true
typora-root-url: ..\..\..\static
---

<!--more-->

## JAVA 環境安裝

### 第一步 設定環境變數-JAVA_HOME

於系統path 添加 java環境變數 (Environment Variable)

```cmd
C:\Program Files\Java\jdk1.8.0_111(後面為自己的jdk)
```

如下圖

![JAVA_HOME](/images/java/JAVA_HOME.png)

### 第二步 Path設定 (environment variable)

於Path設定啟動 (environment variable)

```cmd
%JAVA_HOME%\bin;
```

如下圖
![Path](/images/java/Path.png)

### 第三步 測試

打開terminal，輸入以下指令

``` shell
java -vresion

javac -version
```

輸出如下圖

![test_java_version](/images/java/test_java_version.png)


 ## 參考