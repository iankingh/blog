---
title: "Java heap space：記憶體不足的診斷與確認"
date: 2021-03-02T14:35:25+08:00
draft: false
categories:
 - "筆記"
tags:
- "Java"
- "JDK"
toc: true
description: "區分堆空間不足、GC 壓力與資源未關閉，補上 heap dump 診斷及 Tomcat 設定位置。"
lastmod: 2026-10-07T23:41:34+08:00
---

區分堆空間不足、GC 壓力與資源未關閉，補上 heap dump 診斷及 Tomcat 設定位置。

<!--more-->

適用：JDK 25 的 JVM 記憶體診斷；以下引數為既有應用的設定示意，本文未提供可執行 app.jar，也未重現實際記憶體不足事故。

## 症狀與診斷順序

`OutOfMemoryError: Java heap space` 表示配置物件時堆空間不足；`GC overhead limit exceeded` 是另一類訊息，不能把 98%/2% 門檻當成所有 heap space 的成因。預設 heap 受 JDK、容器限制與引數影響，不是永遠 64MB 或固定實體記憶體比例。

1. 記錄 JDK、啟動引數、容器／主機上限與發生時的工作量。
2. 比較 GC 日誌與堆使用量，是一次性大量資料還是持續累積。
3. 在受控環境取得 heap dump，分析最大保留物件與引用鏈。
4. 修正無界快取、整批查詢、重複載入或過大的影像；再考慮容量。

## 收集資料

以下是啟動已存在的應用 `app.jar` 的引數示意，不是本文提供的可執行 app：

```bash
java -Xms256m -Xmx512m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=./diagnostics -Xlog:gc*:file=gc.log:time,level,tags -jar app.jar
```

先建立 diagnostics、確認有足夠磁碟，dump 可能含個資與秘密，應限制許可權。`-Xlog` 是 Java 9 以上寫法；Java 8 使用該版 GC 日誌引數。提高 Xmx 需為執行緒堆疊、metaspace、direct buffer 與 OS 留餘裕。

Tomcat shell 啟動在 `CATALINA_BASE/bin/setenv.sh` 設 CATALINA_OPTS；Windows 服務由服務管理器設定，不一定讀取 setenv.bat，見[環境設定]({{< ref "/post/server/tomcatSetEnvironment.md" >}})。JAVA_OPTS 並非所有 Java 程式都會自動辨識。

## 圖片與串流

6480 × 4320 × 4 約 112 MB（約 107 MiB）只算畫素，不含物件與處理副本；JPEG 檔案很小仍可能解碼成大圖。資料庫查詢採分頁／串流並關閉資源；try-with-resources 可以釋放連線與檔案，但不能解決程式仍持有巨量物件的引用。

## 確認結果

以同樣資料量重跑，觀察 full GC 後使用量、延遲、dump 是否再次產生；加入更大但合理的資料量測試。GC 後仍線性增加的保留量值得查引用鏈，而非持續加大記憶體。


## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

## 參考資料

- [JDK 25 記憶體排錯](https://docs.oracle.com/en/java/javase/25/troubleshoot/troubleshooting-memory-leaks.html)
- [JDK 25 Java 啟動參數](https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html)
- [JDK 記憶體排錯（Java 21 歷史參考）](https://docs.oracle.com/en/java/javase/21/troubleshoot/troubleshooting-memory-leaks.html)
- [Java 啟動參數（Java 21 歷史參考）](https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html)
- [若系統執行一段時間後無法連線，且tomcat或jboss的log裡出現java.lang.OutOfMemoryError: Java heap space，應如何避免此狀況?　(2008/11/25) | TAIR User Group](http://ir.org.tw/node/78)
- [讀寫檔案時記憶體溢位問題思考（OutOfMemoryError: Java heap space）_WolfShadow的部落格-CSDN部落格](https://blog.csdn.net/u010188178/article/details/83183321)
- [JAVA遇到大批資料處理時會出現Java heap space的報錯的解決方案 - IT閱讀](https://www.itread01.com/content/1546150350.html)
- [tomcat記憶體溢位設定JAVA_OPTS - IT閱讀](https://www.itread01.com/content/1546839425.html)
- [How to Change JVM Heap Setting (-Xms -Xmx) of Tomcat - Configure setenv.sh file - Run catalina.sh • Crunchify](https://crunchify.com/how-to-change-jvm-heap-setting-xms-xmx-of-tomcat/)
- [How To Increase The Java Heap size in Tomcat Application Server | Aprentis](https://aprentis.net/how-to-increase-the-java-heap-size-in-tomcat-application-server/)
- [OutofMemory while reading JPEG file Using IMAGEIO (Performance forum at Coderanch)](https://coderanch.com/t/604430/java/OutofMemory-reading-JPEG-file-IMAGEIO)
