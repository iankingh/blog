---
title: "Tomcat server.xml：上傳限制與應用部署"
date: 2021-04-06T09:29:21+08:00
draft: false
categories:
 - "筆記"
tags:
 - "AP Server"
 - "Tomcat"
toc: true
description: "修正 maxPostSize 的範圍，補上 Connector、multipart 與獨立 Context 設定方式。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正 maxPostSize 的範圍，補上 Connector、multipart 與獨立 Context 設定方式。

<!--more-->

適用：Tomcat 9 與 Spring Boot 2 的歷史部署情境。使用其他 major 時依對應檔案調整。

## Connector 不是所有上傳的總開關

在 CATALINA_BASE/conf/server.xml 的既有 Connector 核對：

```xml
<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" maxPostSize="209715200" redirectPort="8443"/>
```

maxPostSize限制Tomcat將請求體解析成引數的某些情況，不是所有HTTP body的全域性上限。multipart 上傳還受Servlet multipart config、Spring `spring.servlet.multipart.max-file-size` 與 `max-request-size`、代理限制影響。不要盲目設-1取消全部限制。

## 應用路徑

優先以WAR命名或獨立context描述檔管理。例如 conf/Catalina/localhost/restApi.xml：

```xml
<Context docBase="/srv/apps/restApi.war" reloadable="false"/>
```

檔名決定 /restApi context path；不需在Host內重複嵌入同一Context。docBase使用部署主機的真實路徑，避免放同一appBase內造成重複部署。reloadable不宜在生產無條件開啟。

## 修改與確認

先備份既有配置、核對xml格式、在測試環境重新啟動，查Catalina日誌。用小檔、超過單檔限制與超過總請求限制的樣本分開測；HTTP413可能來自代理而不是Tomcat，需檢查每層日誌。redirectPort只指定需TLS時的轉向目的port，不會自動啟用HTTPS connector。

配置尺寸還需配合臨時目錄、磁碟空間、時間限制與應用驗證。成功上傳一個小檔不能證明200MB檔案能處理，更不能證明服務承受得住併發上傳。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [HTTP Connector](https://tomcat.apache.org/tomcat-9.0-doc/config/http.html)
- [Context](https://tomcat.apache.org/tomcat-9.0-doc/config/context.html)
- [Spring multipart](https://docs.spring.io/spring-boot/docs/2.7.18/reference/html/application-properties.html#application-properties.web.spring.servlet.multipart.max-file-size)
