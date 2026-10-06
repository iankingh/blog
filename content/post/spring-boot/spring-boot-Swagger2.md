---
title: "Spring Boot API 文件：Swagger 2 歷史整合與 OpenAPI 3"
date: 2020-07-03T16:01:24+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
description: "保留 Springfox 2.2.2 情境，補上相容界線、現代 springdoc 替代與驗證方式。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 Springfox 2.2.2 情境，補上相容界線、現代 springdoc 替代與驗證方式。

<!--more-->

適用：原 Spring／Spring Boot 歷史筆記；新的可重現練習採 Spring Boot 3.5.0、Java21與Maven，使用jakarta套件。此為固定練習組合，上線另選相容且仍受支援的修補版。

先備：先依[共用 Spring Boot 練習專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})建立 pom.xml 與 NoteApplication，再加入本文檔案。

## 原版本與限制

原筆記使用springfox-swagger2／springfox-swagger-ui 2.2.2與Spring Boot早期版本，配置Docket、@EnableSwagger2與Swagger2註解。不能直接用於Boot3的jakarta架構，亦不建議為遷就舊庫關閉新版框架功能。Swagger2檔案格式與SwaggerUI產品是不同概念，OpenAPI3不是只改頁面名稱。

若維護原系統，先保留依賴／Boot／Spring版本並核對`/v2/api-docs`和`/swagger-ui.html`。原Swagger2Markup → AsciiDoc → HTML/PDF流程還要固定plugin與輸出工具版本，離線產物生成需獨立CI驗證，不能只新增依賴就宣稱完整。

## 新練習：springdoc

使用共用Boot3.5.0專案，在dependencies加入：

```xml
<dependency>
  <groupId>org.springdoc</groupId><artifactId>springdoc-openapi-starter-webmvc-ui</artifactId><version>2.8.9</version>
</dependency>
```

新增src/main/java/notes/HelloController.java：

```java
package notes;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import io.swagger.v3.oas.annotations.Operation;
@RestController
public class HelloController {
    @Operation(summary = "取得練習問候")
    @GetMapping("/api/hello")
    public Map<String, String> hello() { return Map.of("message", "campfire"); }
}
```

## 操作與確認

執行mvn spring-boot:run。GET `/api/hello`應回`{"message":"campfire"}`，`/v3/api-docs`應包含openapi與/api/hello，開`/swagger-ui/index.html`能看到並呼叫介面。WebFlux專案需對應webflux starter，不混用webmvc與webflux UI依賴。

springdoc2.x對應Boot3、3.x對應Boot4的版本線，安裝前檢視相容表與修補版。前端檔案能開啟不代表契約完整，還需描述錯誤回應、認證、DTO欄位與範例。公開API文件不加入真正token，UI endpoint依部署政策授權。

## 查核範圍

本文 HelloController 於 MockMvc 回 /api/hello 與 /v3/api-docs，核對 JSON 與 API 路徑；未用瀏覽器呼叫 Swagger UI 或跑原 Springfox2。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Springfox 原始庫](https://github.com/springfox/springfox)
- [springdoc 相容與設定](https://springdoc.org/)
- [OpenAPI規格](https://spec.openapis.org/oas/latest.html)
