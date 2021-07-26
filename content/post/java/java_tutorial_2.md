---
title: "[從 0 開始的 JAVA 生活]No.2 Java 基本的資料型態(Primitive Data Types)"
date: 2020-05-30T06:22:46+08:00
draft: false
categories:
  - "筆記"
  - "技術"
tags:
 - "java"
toc: true
---


<!-- 簡介 -->

<!--more-->

## Java 基本的資料型態(Primitive Data Types)

基本數據類型（8種）

| 數據類型 | 大小/位 | 封裝類    | 默認值   | 可表示數據范圍                           |
| :------- | ------- | --------- | -------- | ---------------------------------------- |
| byte     | 8bit    | Byte      | 0        | -128~127                                 |
| short    | 16bit   | Short     | 0        | -32768~32767                             |
| int      | 32bit   | Integer   | 0        | -2147483648~2147483647                   |
| long     | 64bit   | Long      | 0L       | -9223372036854775808~9223372036854775807 |
| float    | 32bit   | Float     | 0.0F     | 1.4E-45~3.4028235E38                     |
| double   | 64bit   | Double    | 0.0D     | 4.9E-324~1.7976931348623157E308          |
| char     | 16bit   | Character | '\u0000' | 0~65535                                  |
| boolean  | 8bit    | Boolean   | false    | true或false                              |


如果兩運算為基本型別，至少會轉為int

### 範例

```java
package ch1;

/**
 * 
 * 
 * <p/>
 * Package: ch1 <br>
 * File Name: PrimitiveDataTypesTest <br>
 * <p/>
 * Purpose: <br>
 * 
 * @ClassName: ch1.PrimitiveDataTypesTest
 * @Description: 測試基本數據類型
 * @Copyright : Copyright (c) Corp. 2020. All Rights Reserved.
 * @Company: ian Team.
 * @author ian
 * @version 1.0, 2020年5月18日
 */
public class PrimitiveDataTypesTest {

        static byte b;
        static short s;
        static int i;
        static long l;
        static float f;
        static double d;
        static char c;
        static boolean bo;

        // String不是基本類型
        static String str1 = "";// 生成一個String類型的引用，而且分配記憶體空間來存放"";
        static String str2; // 只生成一個string類型的引用；不分配記憶體空間,預設為null

        public static void main(String[] args) {

                System.out.println("byte的大小：" + Byte.SIZE + " byte的預設值：" + b + " byte的資料範圍：" + Byte.MIN_VALUE + "~"
                                + Byte.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("short的大小：" + Short.SIZE + " short的預設值：" + s + " short的資料範圍：" + Short.MIN_VALUE + "~"
                                + Short.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("int的大小：" + Integer.SIZE + " int的預設值：" + i + " int的資料範圍：" + Integer.MIN_VALUE + "~"
                                + Integer.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("long的大小：" + Long.SIZE + " long的預設值：" + l + " long的資料範圍：" + Long.MIN_VALUE + "~"
                                + Long.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("float的大小：" + Float.SIZE + " float的預設值：" + f + " float的資料範圍：" + Float.MIN_VALUE + "~"
                                + Float.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("double的大小：" + Double.SIZE + " double的預設值：" + d + " double的資料範圍：" + Double.MIN_VALUE
                                + "~" + Double.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("char的大小：" + Character.SIZE + " char的預設值：" + c + " char的資料範圍：" + Character.MIN_VALUE
                                + "~" + Character.MAX_VALUE);
                System.out.println("----------------------------------------------------");
                System.out.println("boolean的大小：" + Byte.SIZE + " boolean的預設值：" + bo + " boolean的資料範圍：" + Byte.MIN_VALUE
                                + "~" + Byte.MAX_VALUE);

                System.out.println("String字串的預設值：" + str1 + "str的默認長度：" + str1.length());
                System.out.println("String字串的預設值：" + str2);

        }
}
```

## JAVA  跳脫字元 Escape Characters 

``` java
- \' : 單引號
- \" : 雙引號
- \\ : 反斜線
- \n : 換行
- \t : tab鍵
- \b : 倒退一格
- \f : 換頁
- \r : Enter 鍵

```

## 參考

[Java中8種基本數據類型默認的默認值_java_飛月程序人生-CSDN博客](https://blog.csdn.net/fysuccess/article/details/40656761)
