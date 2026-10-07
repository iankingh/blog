---
title: "Spring Cloud Gateway：路由、過濾與 Actuator 邊界"
date: 2021-04-12T14:08:40+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring Cloud"
toc: true
description: "整理舊 WebFlux Gateway 配置，補上本地後端、路徑改寫與安全的端點確認。"
lastmod: 2026-10-07T20:50:40+08:00
---

整理舊 WebFlux Gateway 配置，補上本地後端、路徑改寫與安全的端點確認。

<!--more-->

適用：原Boot2的WebFlux Gateway歷史配置；新版替代線另列。外部服務以本地HTTP文字檔模擬，Gateway本身未於本次實機啟動。

## 選定架構與版本

原筆記以Boot2／Spring5／Reactor WebFlux Gateway為主，使用Cloud2021.0.x搭Boot2.7.x的舊語法。新版Gateway有WebFlux和Server MVC不同產品線與starter／property字首；按使用版本檔案選，不把spring-boot-starter-web混入WebFlux gateway。

已有相容Boot／Cloud BOM的gateway專案加入spring-cloud-starter-gateway與actuator。舊application.yml示意：

```yaml
server:
  port: 8084
spring:
  cloud:
    gateway:
      routes:
        - id: note-backend
          uri: http://127.0.0.1:8085
          predicates:
            - Path=/notes/**
          filters:
            - StripPrefix=1
management:
  endpoints:
    web:
      exposure:
        include: health
```

新版WebFlux路由可能使用`spring.cloud.gateway.server.webflux.routes`，以對應版本配置索引為準。lb://服務名需discovery與load-balancer配置，本例固定URI不依賴Eureka。

## 本地確認

在另一目錄建立hello.txt內容campfire，使用`python3 -m http.server 8085 --bind 127.0.0.1`提供模擬後端。啟動Gateway後curl `/notes/hello.txt`應回campfire，StripPrefix去掉notes一段；請求`/hello.txt`不應匹配此route。

測後端停止時的錯誤、錯誤path與超時，再看gateway日誌；不是所有5xx都來自後端。Reactor鏈內不要做blocking IO，需按模型選擇適當整合方式。

## Actuator

原筆記公開gateway並提供寫route／refresh示例；現行版本的enabled／access策略不同。若確需診斷，優先版本支援的read-only access、限定管理監聽與授權，再讀routes。不要把建立／刪除route介面當公開除錯功能，不能只靠CORS保護。

確認predicate、filter順序和傳往後端的path，客戶端看到200不代表認證、請求限制和錯誤處理完整。此篇僅檔案核對，未聲稱測完整gateway叢集。

## 參考資料

- [Gateway官方](https://docs.spring.io/spring-cloud-gateway/reference/)
- [Actuator access](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webflux/actuator-api.html)
- [Spring Cloud相容](https://spring.io/projects/spring-cloud#overview)
- [GatewayFilter factories](https://cloud.spring.io/spring-cloud-gateway/multi/multi__actuator_api.html)
- [Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/)
- [SpringCloud gateway （史上最全） - 瘋狂創客圈 - 部落格園](https://www.cnblogs.com/crazymakercircle/p/11704077.html)
- [Spring Cloud Gateway 開發指南（五） Actuator API | OnePiece](https://cdrcool.github.io/2020/02/27/Spring%20Cloud%20Gateway%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97(%E4%BA%94)
