---
title: "高可用性架構：Active-Active、備援與故障測試"
date: 2021-04-18T15:42:33+08:00
categories:
 - "筆記"
tags:
 - "架構"
toc: true
draft: false
description: "查核原 HA 說明，區分負載平衡、資料一致性、RTO/RPO 與單點故障。"
lastmod: 2026-10-07T20:50:40+08:00
---

查核原 HA 說明，區分負載平衡、資料一致性、RTO/RPO 與單點故障。

<!--more-->

適用：Web／資料庫服務的架構閱讀筆記；概念不能代替特定產品的支援拓撲。

## 先定義目標

可用性是服務在約定時間與條件下正常工作的比例；RTO是容許恢復時間、RPO是容許資料回退量。備份可幫助恢復但不是即時HA，負載平衡也不保證資料層沒有單點。

| 模式 | 工作分配 | 主要代價 |
| --- | --- | --- |
| Active-Active | 多個節點同時提供服務 | 共享狀態、一致性與衝突處理 |
| Active-Standby／Passive | 主要節點服務，備援接手 | 切換時間、備援容量與狀態同步 |
| 多區域／分散式 | 分散故障域 | 網路分割槽、延遲與操作複雜度 |

Active-Active不等於絕不中斷。兩個SQL Server instance互為備援，不等於同一資料庫可任意雙寫；MSDTC是分散式交易協調，不是將一個查詢自動分給兩臺算的機制。

## 資料層與故障域

共用NAS/SAN需產品與檔案系統支援多主機一致訪問，也可能成為單點；不能簡單說SAN必然不可共享或NAS自動安全。資料複寫需區分同步／非同步、誰可寫與故障接手條件，防split-brain需quorum、fencing等設計。

VM HA通常恢復／重啟VM，不直接保證應用交易不中斷。跨同一機房兩臺主機可能仍共享電源、交換器與storage，不是完整獨立故障域。

## 驗證方法

列出元件與依賴，先量正常負載，再在測試環境停單節點、斷網或隔離資料層，觀察錯誤率、切換時間、重試與資料遺失。故障恢復後確認回切不會再次寫錯，備份要實際還原檢查。

把結果對照SLO/RTO/RPO，含容量不足與維護升級的情境。這是設計檢核路徑，本文未聲稱實際做過生產故障演練。

## 參考資料

- [Google SRE Availability](https://sre.google/sre-book/availability-table/)
- [SQL Server HA](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/high-availability-solutions-sql-server)
- [AWS reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Active-Standby Mode](https://docs.tibco.com/pub/trns/1.1.0/doc/html/GUID-6B16E55F-D833-4A96-A8FC-5BB5F8E07E30.html)
- [Cluster專用的名詞AP Mode/AA Mode](http://slashview.com/archive2013/20131206.html)
- [高可用性網路架構High Availability,AA Mode | 景佳科技 FansySoft](https://www.fansysoft.com/liferay-high-availability)
- [企業郵件系統常見高可用性 (HA) 架構整理 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10243564?sc=rss.iron)
- [2個防火牆做HA, 應該設定成Active-Active 還是 Active Standby? - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/questions/10199789)
