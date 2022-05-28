---
title: "HighAvailability"
date: 2021-04-18T15:42:33+08:00
categories:
 - "筆記"
tags:
 - "架構"
toc: true
draft: true
---

## 高可用性網路架構 High Availability  
<!-- 簡介 -->

高可用性網路架構 High Availability   簡稱 HA

高可用就是常常聽到的 HA (High Availability) 機制，建立的 SaaS 雲服務要高可用，首先第一件事情就是要具備容錯能力，避免一時的故障影響到系統運作。

要實現 HA 目前有三種常見的機制，分別是 Master Slave Mode (MS)、Active Active Mode (AA) 與由 AA 進化變形的分散式架構 (Decentralized Architecture)。

高可用性架構 HA (High Availability) 是企業面臨 IT 架構轉型的過程中，維持系統不中斷的重要方案。企業除了雲端服務的選擇外，當選擇自建 (On-Premise) 郵件系統時，就要思考備援方案的架構規劃，自建系統的特點在於可以善用現有的軟硬體資源，以及保有企業內部系統管理彈性。因此對於機敏資料在雲端存取安全性仍有疑慮的企業，繼續使用自建環境仍是相對適合的選擇，以下針對常見的企業郵件系統三種高可用性架構，區分單一主機、多主機、虛擬環境提供架構整理說明。

<!--more-->


## A-A (Active-Active ) Mode

Active-Active：不中斷服務

兩台（或N台）同時運作，這個要視該應用程式系統的定義而定。

以Microsoft SQL來說，AA Mode就是兩台伺服器上安裝兩個資料庫實例，每台伺服器分別運行一個資料庫實例。當某一台伺服器發生故障時系統將把發生故障的伺服器上的資料庫實例切換到另一台伺服器上運行，也就是說另一台伺服器上同時運行兩個實例，當伺服器恢復正常後再手動將一個資料庫實例切換回另一台伺服器。AA模式保證了兩台伺服器資源都被利用。

所以並不是同一個程式，連到一台認知中的資料庫，就可以啟動AA交易喔，沒有那麼簡單容易的事。如果要完成單一程式碼，連到認知中的單一資料庫，進行IO，然後後面所有的資料庫要起來幫我運算執行，這個就要使用SQL的分散式交易MSDTC。


佈署上只少需二台郵件主機運作同時搭配一組 NAS 提供共用儲存空間，從架構上可以區分成應用系統跟資料儲存分別佈署方式，應用系統可多台運作，透過前端搭配 L4-Switch 進行負載平衡 (Load Balance) 同時可以對主機進行定時服務檢查 (Health Check) 監控服務回應狀況。
https://ithelp.ithome.com.tw/upload/images/20200925/20000181kYVKAOpTD1.jpg
各台郵件系統以提供服務為主，資料採用即時抄寫的方式，結合 NAS 功能，提供各台主機相同掛載點，因此不論信件轉送 (SMTP) 或帳號連線登入 (HTTP/HTTPS) 到其中一台都可以正常進行資料讀寫。企業環境如果是使用 SAN 架構，由於 SAN 跟 NAS 不同，無法支援共享存取資料的功能，因此儲存架構上需要搭配 NAS Gateway 來協助控制不同主機對資料的讀寫。就平行擴充而言，郵件系統搭配 NAS 相對適合，資料的備份機制則透過儲存設備的鏡射 (Mirror) 或快照 (Snap shot)進行。


## A-S (Active-Standby)Mode

一台做活動的伺服器，另一台做待命伺服器，待命的機器也開機。


郵件系統單一主機 (Active-Standby) 架構
佈署上需要二台郵件主機Master & Slave 架構搭配本機空間 (DAS) 進行運作，其中 Master 主機為主要的郵件服務器，因此使用較高等級設備，Slave 為備援用途，平常不運作，有需要才開機，因此使用次級可用設備，當 Master 服務異常時，可以接手郵件收發運作，待 Master 主機恢復運作後，再重新成為 Slave 設備。
https://ithelp.ithome.com.tw/upload/images/20200925/20000181MLtJh1ovAp.jpg
但實務上也有企業 Master & Slave 均採用同等級設備，但運作差異在於當 Master 異常時，雖然 Slave 接手處理，但同時角色互換成為 Master 主機，原來主機恢復正常程，角色變成 Slave 主機。資料備份上以時間點進行切分，定期同步 (Rsync) Master 主機上的系統設定檔與郵件資料，政策上可以全備份後每日進行差異化備份。


## A-P (Active-Passive) Mode

一台做活動的伺服器，另一台做待命伺服器，待命的機器，在活動機器正常運作時，基本上就是在那邊睡覺浪費電用。一般在講failover就是屬於這個，也是cluster HA基本款。


## 虛擬化 (Virtualization) 架構

佈署上需要搭配虛擬機完成，郵件系統軟體 (Software) 連同作業系統 (Guest OS) 同時安裝在虛擬機。如果是單台虛擬機運作，則資料直接儲存在本機端，可以針對架構進行壓測，確認單台虛擬機的運作效能以不影響郵件處理反應時間為主，如果有差異建議仍以外部儲存設備的提供資料存取 ; 如果是多台虛擬機運作，由於郵件系統讀寫頻率頻繁，建議搭配外部儲存設備進行運作。
https://ithelp.ithome.com.tw/upload/images/20200925/20000181HRkVDrKMQp.jpg
虛擬機的備援機制建議直接使用虛擬系統本身提供虛擬機擴充功能 (ex. Vmware vMotion) 建立並複製一台虛擬機提供運行。除了用虛擬機達成單台或多台運作架構外，在大型架構下，可以利用虛擬機的優勢，將郵件系統服務分別建立 SMTP、POP3、IMAP、HTTP (WebMail)的服務分散系統負載。

上述三種郵件系統架構，各有其優缺點跟適合範圍，以成本管理角度來看，單一主機架構相對適合一般企業佈署。至於多主機架構，則適合用在中大型企業。虛擬化的方式最彈性，可以同時提供給一般企業或中大型企業，針對超過數萬的帳號數規模，可以彈性將服務從郵件系統內拆解成各自獨立的系統，提供分散式架構服務。但要注意的地方，不論需要導入哪一種架構，網路防火牆、備份機制、系統相關監控機制不可少，才能確保郵件系統基本架構安全。


## 參考

[Cluster專用的名詞AP Mode/AA Mode](http://slashview.com/archive2013/20131206.html)

[Active-Standby Mode](https://docs.tibco.com/pub/trns/1.1.0/doc/html/GUID-6B16E55F-D833-4A96-A8FC-5BB5F8E07E30.html)

[高可用性網路架構High Availability,AA Mode | 景佳科技 FansySoft](https://www.fansysoft.com/liferay-high-availability)

[2個防火牆做HA, 應該設定成Active-Active 還是 Active Standby? - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/questions/10199789)


[企業郵件系統常見高可用性 (HA) 架構整理 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10243564?sc=rss.iron)


