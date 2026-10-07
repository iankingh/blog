---
title: "Java 排錯：編譯問題、例外與版本不一致"
date: 2020-12-09T13:16:00+08:00
draft: false
categories:
 - "筆記"
tags:
- "Java"
- "JDK"
toc: true
description: "建立編譯、類別載入與執行例外的診斷順序，補齊 Eclipse unresolved compilation problems 的處理。"
lastmod: 2026-10-07T20:50:40+08:00
---

建立編譯、類別載入與執行例外的診斷順序，補齊 Eclipse unresolved compilation problems 的處理。

<!--more-->

適用：Java 8 基礎語法；新版練習可使用 JDK 21。先安裝 JDK 並瞭解第 0 篇的編譯／執行環境。

## 先辨識失敗階段

| 訊息 | 檢查方向 |
| --- | --- |
| cannot find symbol | 名稱、import、依賴或生成來源是否存在 |
| Unresolved compilation problems | IDE 可能仍以有編譯錯誤的產物執行 |
| UnsupportedClassVersionError | class 的目標版本高於執行 JVM |
| ClassNotFoundException | 執行 classpath 缺少指定類別 |
| NullPointerException | 堆疊第一個業務程式行取得了 null |

版本不一致只是其中一種原因，不能看到 unresolved 就只調整 JDK。先在 Problems 視窗修正第一個編譯錯誤；核對 Build Path、Compiler compliance、Maven/Gradle toolchain 與執行配置。修正後重建，再從終端重現以區分 IDE 與專案設定。

## 可重現的例外處理

```java
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            Integer.parseInt("not-a-number");
        } catch (NumberFormatException error) {
            System.out.println("輸入不是整數");
        }
        System.out.println("程式繼續");
    }
}
```

```text
輸入不是整數
程式繼續
```

儲存為 ExceptionDemo.java 後編譯／執行。只捕捉預期可處理的錯誤，避免捕捉所有 Throwable 並忽略它；Error 通常表示更嚴重的環境／VM 問題。保留完整堆疊與 cause，不只貼最後一行訊息。

確認修正時使用相同輸入重跑，再加正常值與邊界值；不要只因 Clean 後暫時沒有紅字便認定修復。


## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

## 參考資料

- [例外教學](https://dev.java/learn/exceptions/)
- [javac 診斷](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html)
- [java.lang.Error: Unresolved compilation problems:解決方案 - huangbaokang的部落格 - CSDN部落格](https://blog.csdn.net/huangbaokang/article/details/75287126)
