---
title: "Java 入門 03：變數、初始化與作用域"
date: 2020-06-15T06:20:37+08:00
aliases:
 - "/post/java/java_tutorial_3./"
draft: false
categories:
  - "筆記"
  - "技術"
tags:
- "Java"
- "JDK"
toc: true
description: "補齊區域、實體及靜態變數的差異，使用完整範例觀察兩個物件的狀態。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊區域、實體及靜態變數的差異，使用完整範例觀察兩個物件的狀態。

<!--more-->

適用：Java 8 基礎語法；新版練習可使用 JDK 21。先安裝 JDK 並瞭解第 0 篇的編譯／執行環境。

## 命名與生命週期

一般變數用 lowerCamelCase、常數用 UPPER_SNAKE_CASE；不可使用保留字或以數字開頭。Java 允許部分 Unicode 識別字，但團隊慣例應優先可讀性。Java 9 起單獨 `_` 不能當識別字。

區域變數在方法／區塊內，使用前需初始化；實體欄位每個物件各有一份；static 欄位屬於類別，通常在同一 class loader 下共用。作用域決定名字能否存取，物件存活時間則與引用及 GC 有關，不能等同區塊生命週期。

```java
public class ScopeDemo {
    private int score;
    private static int created;
    public ScopeDemo() { created++; }
    public void add(int amount) {
        int nextScore = score + amount;
        this.score = nextScore;
    }
    public static void main(String[] args) {
        ScopeDemo first = new ScopeDemo();
        ScopeDemo second = new ScopeDemo();
        first.add(3);
        System.out.println(first.score + ":" + second.score);
        System.out.println(created);
    }
}
```

儲存為 ScopeDemo.java，編譯執行：

```text
3:0
2
```

first 與 second 的 score 分開，created 記錄建立兩個物件。amount、nextScore 只在 add 中可見；this.score 指向實體欄位。

## 常見誤解

`final` 禁止變數再次指向其他值，不會讓所指物件自動不可變。`var` 自 Java 10 提供區域變數型別推導，不是動態型別，也不能用於未初始化變數。static 方法不能直接使用 this 或未指定物件的實體欄位；需要先建立物件。


先備：[第 02 章]({{< ref "/post/java/java_tutorial_2.md" >}})的基礎概念與已確認的 JDK 編譯環境。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

[上一章]({{< ref "/post/java/java_tutorial_2.md" >}}) · [下一章]({{< ref "/post/java/java_tutorial_4.md" >}})

## 查核範圍

JDK25以--release 8編譯並執行，標準輸出與本文完全一致。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [變數](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html)
- [變數初始化規格](https://docs.oracle.com/en/java/javase/21/jls/se21/html/jls-16.html)
