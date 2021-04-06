---
title: "[從 0 開始的 JAVA 生活]No.0 java環境變數 (Environment Variable)設定"
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

### 於環境變數設定JAVA_HOME

```
C:\Program Files\Java\jdk1.8.0_111(後面為自己的jdk)
```

![JAVA_HOME](/images/java/JAVA_HOME.png)

### 設定Path
```

%JAVA_HOME%\bin;
```


![Path](/images/java/Path.png)

### 測試

``` shell
java -vresion

javac -version
```

![test_java_version](/images/java/test_java_version.png)


 ## 參考