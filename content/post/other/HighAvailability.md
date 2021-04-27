---
title: "HighAvailability"
date: 2021-04-18T15:42:33+08:00
draft: true
categories:
 - "xx"
tags:
 - "架構"
 - "xxx"
toc: true
---

## 高可用性網路架構 High Availability  
<!-- 簡介 -->

高可用性網路架構 High Availability   簡稱 HA

高可用就是常常聽到的 HA (High Availability) 機制，建立的 SaaS 雲服務要高可用，首先第一件事情就是要具備容錯能力，避免一時的故障影響到系統運作。

要實現 HA 目前有三種常見的機制，分別是 Master Slave Mode (MS)、Active Active Mode (AA) 與由 AA 進化變形的分散式架構 (Decentralized Architecture)。

<!--more-->


## A-A (Active-Active ) Mode

Active-Active：不中斷服務

兩台（或N台）同時運作，這個要視該應用程式系統的定義而定。

以Microsoft SQL來說，AA Mode就是兩台伺服器上安裝兩個資料庫實例，每台伺服器分別運行一個資料庫實例。當某一台伺服器發生故障時系統將把發生故障的伺服器上的資料庫實例切換到另一台伺服器上運行，也就是說另一台伺服器上同時運行兩個實例，當伺服器恢復正常後再手動將一個資料庫實例切換回另一台伺服器。AA模式保證了兩台伺服器資源都被利用。

所以並不是同一個程式，連到一台認知中的資料庫，就可以啟動AA交易喔，沒有那麼簡單容易的事。如果要完成單一程式碼，連到認知中的單一資料庫，進行IO，然後後面所有的資料庫要起來幫我運算執行，這個就要使用SQL的分散式交易MSDTC。



## A-S (Active-Standby)Mode

一台做活動的伺服器，另一台做待命伺服器，待命的機器也開機。

## A-P (Active-Passive) Mode

一台做活動的伺服器，另一台做待命伺服器，待命的機器，在活動機器正常運作時，基本上就是在那邊睡覺浪費電用。一般在講failover就是屬於這個，也是cluster HA基本款。



## 參考
[高可用性網路架構High Availability,AA Mode | 景佳科技 FansySoft](https://www.fansysoft.com/liferay-high-availability)


[Cluster專用的名詞AP Mode/AA Mode](http://slashview.com/archive2013/20131206.html)

[2個防火牆做HA, 應該設定成Active-Active 還是 Active Standby? - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/questions/10199789)

[Active-Standby Mode](https://docs.tibco.com/pub/trns/1.1.0/doc/html/GUID-6B16E55F-D833-4A96-A8FC-5BB5F8E07E30.html)

