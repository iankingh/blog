---
title: "Java 工程師學習地圖：基礎、交付與架構能力"
date: 2021-03-15T09:33:44+08:00
categories:
 - "筆記"
tags:
 - "java"
 - "skill"
toc: true
draft: false
description: "將原技術名單整理為可驗證的能力層級，保留 Spring、容器、資料與測試主題。"
lastmod: 2026-10-07T00:01:00+08:00
---

將原技術名單整理為可驗證的能力層級，保留 Spring、容器、資料與測試主題。

<!--more-->

適用：Java後端／全端的學習規劃，不是職缺一律必備的產品清單。

## 能力與完成證據

| 主題 | 學習重點 | 可交付成果 |
| --- | --- | --- |
| Java基礎 | 型別、集合、例外、資源與併發 | 可執行程式及邊界測試 |
| Spring Boot | DI、設定、HTTP、驗證 | 有錯誤格式與測試的API |
| SQL／JPA | 索引、交易、查詢、分頁 | schema、migration及查詢分析 |
| 測試 | JUnit、mock、integration | 可在CI重現且能抓真錯的測試 |
| Git／CI | 小提交、review、build | 可重現pipeline與發布記錄 |
| 容器／Linux | 映像、volume、日誌、許可權 | 可恢復的本機部署 |

先完成[Java系列]({{< ref "/post/java/java_tutorial_0.md" >}})與Spring最小API，再加入Redis／Kafka／RabbitMQ；引入新元件要說明目的，不只記名字。

## 進階能力

Spring Cloud、Kubernetes、OpenShift與Tanzu是不同維運層級與產品選擇，不需要同時精通才算Java工程師。學習故障診斷、timeouts、重試的冪等性、觀測與資料一致性，再選工具。Netty／Reactor要理解event loop與阻塞邊界。

DDD適合複雜業務模型，先畫業務流程、命名聚合與交易邊界，不以套層目錄代替領域理解。前端Angular或Vue可按團隊選，沒有強制Java一定配Angular。

## 版本與回顧

原名單的CentOS Linux已經結束維護，應選擇受支援平臺；javax→jakarta等變化按框架major核對。每月用同一小專案檢查是否能從空環境建置、測試、診斷和還原，記錄實際結果；這比列出更多logo能看出缺口。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Java learning](https://dev.java/learn/)
- [Spring guides](https://spring.io/guides)
- [JUnit](https://docs.junit.org/current/user-guide/)
- [Reactor](https://projectreactor.io/docs/core/release/reference/)
