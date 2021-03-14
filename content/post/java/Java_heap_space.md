---
title: "Java_heap_space"
date: 2021-03-02T14:35:25+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
toc: true
---

# java.lang.OutOfMemoryError: Java heap space JVM記憶體設定

使用Java程式從資料庫中查詢大量的資料時出現異常:java.lang.OutOfMemoryError: Java heap space
在JVM中如果98%的時間是用於GC且可用的 Heap size 不足2%的時候將丟擲此異常資訊。
JVM堆的設定是指java程式執行過程中JVM可以調配使用的記憶體空間的設定.JVM在啟動的時候會自動設定Heap size的值,其初始空間(即-Xms)是實體記憶體的1/64,最大空間(-Xmx)是實體記憶體的1/4。可以利用JVM提供的-Xmn -Xms -Xmx等選項可進行設定。
<!--more-->


這個問題的根源是jvm虛擬機器的預設Heap大小是64M,可以通過設定其最大和最小值來實現.設定的方法主要是幾個.

1. 可以在windows 更改系統環境變數加上 JAVA_OPTS && CATALINA_OPTS
    ```
    JAVA_OPTS=-Xms1024m -Xmx2048m

    CATALINA_OPTS=-Xms2048M -Xmx4096M
    ```

    EX:
    ```
    Variable name : CATALINA_OPTS
    Variable value: =-Xms2048M -Xmx4096M
    ```

2. 程式的寫法要注意要 close 資料流


3. IMAGEIO讀取JPEG文件

JPEG可以很好地壓縮圖像。但是在內存中，僅用於原始數據的BufferedImage通常每個像素需要4個字節，因此無論文件有多大，其大小均為6480 * 4320 * 4 = 112 MB。
   



參考
若系統運行一段時間後無法連線，且tomcat或jboss的log裡出現java.lang.OutOfMemoryError: Java heap space，應如何避免此狀況?　(2008/11/25) | TAIR User Group
http://ir.org.tw/node/78

读写文件时内存溢出问题思考（OutOfMemoryError: Java heap space）_WolfShadow的博客-CSDN博客
https://blog.csdn.net/u010188178/article/details/83183321

JAVA遇到大批資料處理時會出現Java heap space的報錯的解決方案 - IT閱讀
https://www.itread01.com/content/1546150350.html

tomcat記憶體溢位設定JAVA_OPTS - IT閱讀
https://www.itread01.com/content/1546839425.html

https://crunchify.com/how-to-change-jvm-heap-setting-xms-xmx-of-tomcat/

https://aprentis.net/how-to-increase-the-java-heap-size-in-tomcat-application-server/

https://coderanch.com/t/604430/java/OutofMemory-reading-JPEG-file-IMAGEIO
