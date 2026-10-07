---
title: "Java 入門 00：JDK 安裝與環境確認"
date: 2020-05-19T06:22:46+08:00
draft: false
categories:
  - "筆記"
  - "技術"
tags:
- "Java"
- "JDK"
toc: true
description: "保留 Windows 的 Java 8 設定情境，補上 JDK 選擇、正確版本指令與 PATH 排錯。"
lastmod: 2026-10-07T20:50:40+08:00
---

保留 Windows 的 Java 8 設定情境，補上 JDK 選擇、正確版本指令與 PATH 排錯。

<!--more-->

適用：Java 8 基礎語法；新版練習可使用 JDK 21。先安裝 JDK 並瞭解第 0 篇的編譯／執行環境。

## 安裝與環境變數

原筆記的 `jdk1.8.0_111` 是歷史示意，不應再下載該舊修補版本。維護 Java 8 系統選擇供應商仍支援的 Java 8 更新版本；新練習可安裝 JDK 21。JDK 包含 javac，僅安裝 JRE 不能編譯本系列程式。

Windows 安裝後以實際目錄設定 JAVA_HOME，例如 `C:\Program Files\Java\jdk-21`，不要在值末尾加 `bin` 或引號；將 `%JAVA_HOME%\bin` 加入 Path，重新開終端。

```powershell
java -version
javac -version
where.exe java
where.exe javac
$env:JAVA_HOME
```

java 與 javac 主版本應符合預期。where.exe 若列出多個位置，檢查最前面是否來自舊安裝或 IDE；JAVA_HOME 不會自動改變 Path 的優先順序。

macOS 使用 `/usr/libexec/java_home -V` 檢視已安裝 JDK；Linux 用 `command -v java` 與供應商的安裝流程確認。不同版本並存時，IDE、Maven／Gradle 與終端的 JDK 都要一致，不能只看一次 java -version。

## 第一個環境檢查

```java
public class EnvironmentDemo {
    public static void main(String[] args) {
        System.out.println("JDK can compile and run");
    }
}
```

儲存為 EnvironmentDemo.java，執行 `javac -encoding UTF-8 EnvironmentDemo.java` 再 `java EnvironmentDemo`。

```text
JDK can compile and run
```

若 javac 找不到，先修正 JDK／PATH，不要下載來源不明的 class 或把所有目錄加入 Path。下一篇說明完整的編譯與 classpath。


## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

[下一章]({{< ref "/post/java/java_tutorial_1.md" >}})

## 參考資料

- [JDK 安裝指南](https://docs.oracle.com/en/java/javase/21/install/overview-jdk-installation.html)
- [javac](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html)
