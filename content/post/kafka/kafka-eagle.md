---
title: "Kafka Eagle／EFAK：歷史監控配置與 Kafka 版本界線"
date: 2023-08-29T10:50:12Z
categories:
- "筆記"
tags:
- "tag1"
- "tag2"
toc: true
draft: false
description: "重整舊 ZooKeeper 配置，補上 listener、JMX、認證與 KRaft 替代的核對順序。"
lastmod: 2026-10-07T20:50:40+08:00
---

重整舊 ZooKeeper 配置，補上 listener、JMX、認證與 KRaft 替代的核對順序。

<!--more-->

適用：原Kafka Eagle／EFAK的ZooKeeper時代部署筆記；版本與Kafka支援需檢視所選工具release，不套用到全部Kafka版本。

## 使用前確認

先列出EFAK release、JDK、Kafka與metadata模式。舊system-config.properties使用ZooKeeper cluster地址與efak.*，較新工具／版本可能改變配置來源；不可直接把完整舊樣本貼進新包並認為啟用。下載官方release、核對示例配置與啟動指令碼，再設KE_HOME為實際工具目錄。

## Listener 與安全協定

listeners是broker實際監聽，advertised.listeners是client取得metadata後連線的地址；容器內／外網必須都能解析實際公佈的地址。SASL_PLAINTEXT有認證但無傳輸加密，PLAINTEXT既非認證亦非加密；SASL_SSL加入TLS與SASL，不能將SSL概括為自動授權。

如果bootstrap地址能連但topic操作超時，檢查metadata中的advertised地址，而不是只ping第一臺broker。Kafka命令列client先以相同認證設定測cluster，再加入UI，可區分broker與工具問題。

## 舊配置的分類

- 叢集連線：cluster別名、ZooKeeper或支援的bootstrap入口。
- 監控：JMX／metrics地址、port與認證；不同於Kafka業務port。
- 工具storage：自己的DB、帳號與遷移設定，不能使用公開demo弱密碼。
- Web介面：監聽位置、使用者許可權與管理入口。

原硬編碼的內網地址、資料庫與認證樣本不當可直接用的環境，按實際部署提供秘密與最小許可權。JMX若開放遠端，核對認證、TLS與網路範圍，不能為圖表方便關閉所有保護。

## KRaft與替代

Kafka4移除ZooKeeper模式，新建Kafka不能照舊ZK配置啟動。工具是否支援KRaft、SASL、ACL及metrics，按對應release確認；不支援時評估支援bootstrap/KRaft的監控UI與Prometheus類指標系統。

## 驗收

在測試cluster讀broker／topic與消費者lag，與Kafka原生命令結果比對；停一個測試broker觀察狀態，再恢復。lag只是消費進度差，不等於業務成功。本文未建立Kafka叢集或寫入外部服務，配置概念僅官方核對，不聲稱GUI所有版本可重現。

## 參考資料

- [EFAK 官方](https://www.kafka-eagle.org/)
- [EFAK 原始庫](https://github.com/smartloli/kafka-eagle)
- [Kafka4 upgrade](https://kafka.apache.org/40/documentation/#upgrade)
- [Kafka broker配置](https://kafka.apache.org/40/configuration/broker-configs/)
- [Kafka Eagle分散式模式 - 哥不是小蘿莉 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/15732794.html)
- [Kafka Eagle 3.0.1功能預覽 - 哥不是小蘿莉 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/16728995.html)
- [大資料Hadoop之——Kafka 圖形化工具 EFAK（EFAK環境部署） - 大資料老司機 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16307589.html)
- [大資料Hadoop之——EFAK和Confluent KSQL簡單使用（kafka listeners 和 advertised.listeners） - 大資料老司機 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16898002.html)
- [(2條訊息) 【kafka視覺化工具】kafka-eagle在windows環境的下載、安裝、啟動與訪問_kafka eagle windows_No8g攻城獅的部落格-CSDN部落格](https://blog.csdn.net/weixin_44299027/article/details/125378413)
- [【kafka視覺化工具】kafka-eagle在windows環境的下載、安裝、啟動與訪問_51CTO部落格_kafka 視覺化工具](https://blog.51cto.com/no8g/6344266)
