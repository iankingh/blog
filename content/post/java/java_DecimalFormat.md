---
title: "Java DecimalFormat(數字格式)"
date: 2020-05-26T08:59:50+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
toc: true

---
## 簡介

`java.text`提供了`NumberFormat`類別來讓我們更方便的格式化數字的呈現方式

`DecimalFormat`是`NumberFormat`該格式的具體子類， 其格式為小數。它具有多種功能，旨在使可以在任何語言環境中解析和格式化數字，包括對西方，阿拉伯和印度數字的支持。它還支持各種數字，包括整數（123），定點數字（123.4），科學計數法（1.23E4），百分比（12％）和貨幣金額（$ 123）。所有這些都可以本地化。

<!--more-->



## 基本用法

### NumberFormat

```java
//	由於NumberFormat是一個抽象類別，必須用getInstance()來取得他裡面的方法
NumberFormat nf = NumberFormat.getInstance();
//	NumberFormat物件格式化的方式是固定的，都是以每三位數一個逗號的方式格式化數字，浮點數欄位則是有的時候顯示，沒有就不顯示。所以可以得到1,234,567.89。
System.out.println(nf.format(1234567.89));
```

### DecimalFormat

​	DecimalFormat實作了NumberFormat，並提供更客製化的格式選擇，用法如下： 

```java
Double value = 123456.789;
String pattern = "###,###.###" ;
//	宣告了一個DecimalFormat物件，並可以在宣告時帶入要格式化的格式，若不帶入參數，格式規則和NumberFormat相同。
DecimalFormat myFormatter = new DecimalFormat(pattern);
String output = myFormatter.format(value);
System.out.println("執行結果為：" + value + " " + pattern + " " + output);
```

​	下表描述了前幾行代碼的輸出.  `value` 是要格式化的數字(`double`) ,`pattern` 是指定格式設置屬性的字符串.The `output`, 輸出是字符串，表示格式化的數字。

| `value`    | `pattern`         | `output`    | Explanation                                                  |
| ---------- | ----------------- | ----------- | ------------------------------------------------------------ |
| 123456.789 | ###,###.###       | 123,456.789 | 井號（＃）表示一個數字，逗號是分組分隔符的佔位符，句點是十進制分隔符的佔位符。 |
| 123456.789 | ###.##            | 123456.79   | `value` 在小數點右邊有三位數, 而 `pattern` 只有兩位. `format`通過四捨五入來解決這個問題。 |
| 123.78     | 000000.000        | 000123.780  | `pattern` 指定前導零和尾隨零，因為使用0字符代替了井號（＃）。 |
| 12345.67   | $###,###.###      | $12,345.67  | `pattern`中的第一個字符是美元符號（$）。注意，它緊接在格式為`output`的最左邊的數字之前。 |
| 12345.67   | \u00A5###,###.### | ¥12,345.67  | `pattern` 使用Unicode值00A5指定日元（¥）的貨幣符號。         |

## 其他用法

```java
DecimalFormat df = new DecimalFormat("$#,##0.00");
System.out.println(df.format(1234567.2));
```
​		格式化的字串中0代表一定要有值，#則代表不一定要有值，
    因此#,##0.00表示至少要有個位數及小數點後兩位，且每三位數以一個逗號分開，若格式化的數字沒有個位數或小數點後兩位，就會以0代替。

​		根據需求在前後加上需要的文字，例如$符號，所以上例執行的結果就會是$1,234,567.20。

這邊要注意若是我們在格式化字串結尾加上百分比符號『%』，DecimalFormat會自動幫我們將數值乘以100以符合字面意義，例如： 

```java
DecimalFormat df = new DecimalFormat("#,##0.00%");
System.out.println("執行結果為：" + df.format(1234567.2));//  執行結果為：123,456,720.00%
```

DecimalFormat 類主要靠 # 和 0 兩種預留位置號來指定數位長度。

0 表示如果位數不足則以 0 填充，# 表示只要有可能就把數字拉上這個位置。

 ```java

/**
 * DecimalFormatTest
 */
public class DecimalFormatTest {
  public static void main(String[] args) {

    double d = 123456789;
    DecimalFormat decimalFormat = new DecimalFormat("#,###.##");
    System.out.println(decimalFormat.format(d));
    DecimalFormat decimalFormat2 = new DecimalFormat("#,###.00");
    System.out.println(decimalFormat2.format(d));
    double pi = 3.1415927;// 圓周率
    // 取一位元整數

    System.out.println(new DecimalFormat("0").format(pi));// 3

    // 取一位元整數和兩位元小數

    System.out.println(new DecimalFormat("0.00").format(pi));// 3.14

    // 取兩位元整數和三位元小數，整數不足部分以0填補。

    System.out.println(new DecimalFormat("00.000").format(pi));// 03.142

    // 取所有整數部分

    System.out.println(new DecimalFormat("#").format(pi));// 3

    // 以百分比方式計數，並取兩位小數

    System.out.println(new DecimalFormat("#.##%").format(pi));// 314.16%

    long c = 299792458;// 光速

    // 顯示為科學計數法，並取五位小數

    System.out.println(new DecimalFormat("#.#####E0").format(c));// 2.99792E8

    // 顯示為兩位元整數的科學計數法，並取四位小數

    System.out.println(new DecimalFormat("00.####E0").format(c));// 29.9792E7

    // 每三位以逗號進行分隔。

    System.out.println(new DecimalFormat(",###").format(c));// 299,792,458

    // 將格式嵌入文本

    System.out.println(new DecimalFormat("光速大小為每秒,###米").format(c)); // 光速大小為每秒299,792,458米

  }

}

 ```



## 參考

[Java] 13-8 數字輸出格式 @ 給你魚竿 :: 痞客邦  
https://rx1226.pixnet.net/blog/post/335106917

數字格式(NumberFormat、DecimalFormat) @ Penguin 工作室，一起JAVA吧！ :: 隨意窩 Xuite日誌  
https://blog.xuite.net/jane17512001/PenguinDesign/116288108-%E6%95%B8%E5%AD%97%E6%A0%BC%E5%BC%8F%28NumberFormat%E3%80%81DecimalFormat%29

（轉）Java DecimalFormat 用法（數位格式化） - 濫好人 - 博客園  
https://www.cnblogs.com/hq233/p/6539107.html

https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html

https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html



 

