---
title: "Gradle Error"
date: 2021-07-01T10:08:21+08:00
categories:
 - "筆記"
tags:
 - "gradle"
toc: true
draft: false
---

## gradle Error

以下為 gradle 錯誤訊息的紀錄
<!-- 簡介 -->
<!--more-->
## Error1. for encoding x-windows-950

表示表編碼是Window 需要指定編碼

於build.gradle 下新增編碼 options.encoding = 'UTF-8'

```build.gradle

plugins {
------------------------------
}
dependencies {
 --------------------
}

//要執行的任務新增即可
javadoc {
    options.encoding = 'UTF-8'
}

```

## Error2  Task :javadoc FAILED

FAILURE: Build failed with an exception.

於 build.gradle 下新增compileJava 編碼 [compileJava, compileTestJava]*.options*.encoding = 'UTF-8'

```build.gradle

plugins {
 -----------------------------------
}
// 新增在這裡
[compileJava, compileTestJava]*.options*.encoding = 'UTF-8'

dependencies {
--------------------------------------
}


javadoc {
    options.encoding = 'UTF-8'
}


```

## 參考
