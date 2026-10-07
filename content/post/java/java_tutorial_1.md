---
title: "Java 入門 01：編譯並執行第一支程式"
date: 2020-05-29T06:50:51+08:00
draft: false
categories:
- "筆記"
- "技術"
tags:
- "Java"
- "JDK"
toc: true
description: "從 HelloJava.java 到 class 檔，補上檔名規則、classpath、預期輸出與常見錯誤。"
lastmod: 2026-10-07T23:41:34+08:00
---

從 HelloJava.java 到 class 檔，補上檔名規則、classpath、預期輸出與常見錯誤。

<!--more-->

適用：JDK 25 編譯與執行；保留原筆記的基礎語法與教學情境。先安裝 JDK 25，並依第 0 篇確認編譯／執行環境。

## 程式與執行

建立空資料夾，儲存為 `HelloJava.java`：

```java
public class HelloJava {
    public static void main(String[] args) {
        System.out.println("Hello java");
    }
}
```

```bash
javac -encoding UTF-8 HelloJava.java
java -cp . HelloJava
```

編譯成功產生 HelloJava.class，執行結果：

```text
Hello java
```

`public class` 名稱和檔名大小寫一致；java 命令使用類別名稱，不加 .class。`-cp .` 指明目前目錄是 classpath，不依賴電腦既有環境變數。main 是進入點，String[] 接收命令列引數。

## 編譯與執行分開排錯

找不到符號或分號屬於 javac 編譯錯誤，先修正第一個錯誤再重編譯。`Could not find or load main class` 先檢查執行目錄、classpath 與 package；有 package 時用完整類別名稱並以 package 根目錄作 classpath。`UnsupportedClassVersionError` 是執行 JVM 太舊，要將編譯器與執行 JVM 都對齊 JDK 25，不是增加記憶體。

Java 11 以上可以 `java HelloJava.java` 直接執行單一來源檔；本篇以 JDK 25 採用編譯、執行的兩步流程，方便理解產生的 class 與後續多檔案程式。


先備：[第 00 章]({{< ref "/post/java/java_tutorial_0.md" >}})的基礎概念與已確認的 JDK 編譯環境。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

[上一章]({{< ref "/post/java/java_tutorial_0.md" >}}) · [下一章]({{< ref "/post/java/java_tutorial_2.md" >}})

## 參考資料

- [JDK 25 編譯器](https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html)
- [JDK 25 Java 啟動器](https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html)
- [編譯器（Java 21 歷史參考）](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html)
- [Java 啟動器（Java 21 歷史參考）](https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html)
