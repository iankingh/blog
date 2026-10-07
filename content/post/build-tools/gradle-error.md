---
title: "Gradle 編碼排錯：JavaCompile 與 Javadoc"
date: 2021-07-01T10:08:21+08:00
categories:
 - "筆記"
tags:
 - "gradle"
toc: true
draft: false
description: "以有效 build.gradle 取代空白範本，區分來源編碼與 Javadoc 語法錯誤。"
lastmod: 2026-10-07T20:50:40+08:00
---

以有效 build.gradle 取代空白範本，區分來源編碼與 Javadoc 語法錯誤。

<!--more-->

適用：Gradle 8系Java plugin的Groovy DSL示例。既有專案先確認wrapper版本與對應JDK需求。

## 症狀與診斷

`unmappable character for encoding x-windows-950` 表示編譯器以該編碼解讀來源遇到不可對映字元。先確認來源真的以UTF-8儲存，再指定編譯編碼；不能把原Big5來源只標成UTF-8。

build.gradle可採：

```groovy
plugins { id 'java' }

tasks.withType(JavaCompile).configureEach {
    options.encoding = 'UTF-8'
}
tasks.withType(Javadoc).configureEach {
    options.encoding = 'UTF-8'
    options.charSet = 'UTF-8'
    options.docEncoding = 'UTF-8'
}
```

Windows用gradlew.bat，其他平臺用./gradlew：

```bash
./gradlew --version
./gradlew clean compileJava compileTestJava javadoc --stacktrace
```

應先確認compileJava成功，再確認javadoc成功，輸出位於build/docs/javadoc。withType會包含對應型別的tasks，不必只列兩個任務名稱。

## Javadoc 失敗不只編碼

先閱讀第一個錯誤的檔名與行號；無效HTML、缺少引數檔案或JDK doclint更嚴格也會失敗。修正註解的標籤與特殊字元，不先關掉整個Javadoc或忽略所有失敗。若依賴類別找不到，檢查source set與classpath。

`options.encoding`是輸入來源，charSet/docEncoding影響輸出的HTML編碼。Kotlin DSL寫法不同，不能把Groovy片段直接貼入build.gradle.kts。正式建置應使用repository的wrapper而非全域性未知版本Gradle，並維持IDE和CI的JDK一致。

## 參考資料

- [Gradle Java plugin](https://docs.gradle.org/current/userguide/java_plugin.html)
- [Javadoc task](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.javadoc.Javadoc.html)
