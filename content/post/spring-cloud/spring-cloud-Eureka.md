---
title: "Spring Cloud Eureka：服務註冊與健康確認"
date: 2021-03-04T09:48:06+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring Cloud"
toc: true
description: "補齊 server/client 配置、相容版本與本地雙服務確認，區分註冊和負載平衡。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊 server/client 配置、相容版本與本地雙服務確認，區分註冊和負載平衡。

<!--more-->

適用：Spring Cloud Netflix的歷史Eureka架構；本文舊配置僅檔案查核，未架設外部註冊叢集。

## 版本組合

原筆記是Spring Cloud Netflix的歷史情境。可重現舊組合為Boot2.7.18、Cloud2021.0.9（已屬歷史維護線）；新系統按官方release train對應Boot的major選BOM，不任意拼湊。以下配置概念以舊組合示意，執行前需建立兩個獨立Boot專案，Java與版本遵照該組合。

pom加入Cloud BOM至dependencyManagement、版本固定2021.0.9，server依賴spring-cloud-starter-netflix-eureka-server。啟動類：

```java
package notes.registry;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;
@SpringBootApplication
@EnableEurekaServer
public class RegistryApplication {
    public static void main(String[] args) { SpringApplication.run(RegistryApplication.class, args); }
}
```

server的application.yml：

```yaml
server:
  port: 8761
eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
```

## Client

另一個Boot專案加入spring-cloud-starter-netflix-eureka-client與相同BOM，設定：

```yaml
spring:
  application:
    name: note-service
server:
  port: 8083
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:8761/eureka/
```

先啟動server再client，瀏覽8761，應在Apps看到NOTE-SERVICE與UP。defaultZone是Map的特定key，注意大小寫。多server地址逗號分隔，但不等於已完成HA拓撲。

## 排錯與限制

client註冊有心跳與快取延遲，關掉instance後不一定立刻消失；先看client日誌、server連線與instance地址。Docker內127.0.0.1是自己，需改服務名稱。註冊中心不會自動代理HTTP，也不能提供業務授權；負載均衡client需另配。

生產註冊中心限制網路並認證，保護dashboard。Kubernetes等環境也有其他發現方式，選Eureka需考慮現有生態，而非所有微服務都必須部署。相容版本、實機啟動與故障測試範圍應獨立記錄。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Eureka官方文件](https://docs.spring.io/spring-cloud-netflix/reference/spring-cloud-netflix.html)
- [Release train](https://spring.io/projects/spring-cloud#overview)

### 原始筆記的其他連結

- [原始參考入口 1](http://www.ityouknow.com/springcloud/2017/05/10/springcloud-eureka.html)
