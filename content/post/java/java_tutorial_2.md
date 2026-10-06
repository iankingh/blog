---
title: "Java 入門 02：基本型別、預設值與跳脫字元"
date: 2020-05-30T06:22:46+08:00
draft: false
categories:
  - "筆記"
  - "技術"
tags:
- "Java"
- "JDK"
toc: true
description: "修正 boolean 大小與浮點範圍說明，示範數值提升、欄位預設值及字元輸出。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正 boolean 大小與浮點範圍說明，示範數值提升、欄位預設值及字元輸出。

<!--more-->

適用：Java 8 基礎語法；新版練習可使用 JDK 21。先安裝 JDK 並瞭解第 0 篇的編譯／執行環境。

## 八種基本型別

| 型別 | 語言規定的位元／範圍 | 欄位預設值 |
| --- | --- | --- |
| byte | 8 位，-128 到 127 | 0 |
| short | 16 位，-32768 到 32767 | 0 |
| int | 32 位，有號整數 | 0 |
| long | 64 位，有號整數 | 0L |
| float | 32 位 IEEE 754 | 0.0f |
| double | 64 位 IEEE 754 | 0.0d |
| char | 16 位 UTF-16 code unit | '\u0000' |
| boolean | true / false，儲存大小未由語言固定為 8 位 | false |

這些預設值只適用欄位與陣列元素；區域變數在使用前必須明確賦值。Float.MIN_VALUE / Double.MIN_VALUE 表示最小正非零值，不是最小負數。字元 char 不能代表所有 Unicode 字元，一些字元需要一對 surrogate。

## 完整練習

```java
public class PrimitiveDemo {
    static int defaultNumber;
    static boolean defaultFlag;
    public static void main(String[] args) {
        byte a = 10, b = 20;
        int sum = a + b;
        System.out.println(defaultNumber + ":" + defaultFlag);
        System.out.println(sum);
        System.out.println("A\tB");
        System.out.println("quote=\" slash=\\");
        System.out.println(0.1 + 0.2 == 0.3);
    }
}
```

儲存為 PrimitiveDemo.java，以前篇的 javac / java 流程執行：

```text
0:false
30
A	B
quote=" slash=\
false
```

A 與 B 中間是 tab。byte + byte 會數值提升為 int，不能直接賦回 byte 而不考慮轉型與溢位。長整數文字加 L，float 文字加 f；String 是參考型別，不是第九種基本型別。

金額不應用 double 假設十進位完全精確，參考[DecimalFormat 與 BigDecimal]({{< ref "/post/java/java-DecimalFormat.md" >}})。常見跳脫為 `\n` 換行、`\t` tab、`\"` 雙引號、`\\` 反斜線。


先備：[第 01 章]({{< ref "/post/java/java_tutorial_1.md" >}})的基礎概念與已確認的 JDK 編譯環境。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

[上一章]({{< ref "/post/java/java_tutorial_1.md" >}}) · [下一章]({{< ref "/post/java/java_tutorial_3.md" >}})

## 查核範圍

JDK25以--release 8編譯並執行，標準輸出與本文完全一致。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Java 8 基本型別](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
- [Java 21 型別規格](https://docs.oracle.com/en/java/javase/21/jls/se21/html/jls-4.html)

### 原始筆記保留的來源

- [Java中8種基本資料型別及其預設值_飛月程式人生-CSDN部落格_float預設值](https://blog.csdn.net/fysuccess/article/details/40656761)
