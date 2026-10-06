---
title: "Tomcat 設定：JNDI、環境變數與 JVM 引數"
date: 2021-04-05T16:33:28+08:00
draft: false
categories:
 - "筆記"
tags:
 - "AP Server"
 - "tomcat"
toc: true
description: "保留 context.xml 的 JNDI 情境，說明它與 OS 環境及 Spring profile 的差異。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 context.xml 的 JNDI 情境，說明它與 OS 環境及 Spring profile 的差異。

<!--more-->

適用：Tomcat 9 的 javax 應用；Tomcat 10+ 改為 jakarta，遷移需核對應用與依賴。

## JNDI 不是 OS 環境變數

應用專用設定可放 `CATALINA_BASE/conf/Catalina/localhost/myapp.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Context>
  <Environment name="ENV" value="uat" type="java.lang.String" override="false"/>
</Context>
```

應用以 `new InitialContext().lookup("java:comp/env/ENV")` 讀取，應為 uat；不能預期 `System.getenv("ENV")` 自動讀到此值。全域性 conf/context.xml 會影響多應用，應先判定設定範圍。

## JVM 與 Spring profile

Unix shell 啟動用 `CATALINA_BASE/bin/setenv.sh`：

```bash
CATALINA_OPTS="-Xms256m -Xmx512m -Dspring.profiles.active=uat"
export CATALINA_OPTS
```

該檔案由Tomcat啟動指令碼讀取，不直接手動執行替代catalina。Windows指令碼以setenv.bat設定；Windows service使用服務包裝器的Java選項，可能不會讀取指令碼。JAVA_OPTS/CATALINA_OPTS也不是Java語言內建環境變數。

Spring Boot 某些設定來源可讀取JNDI，但依部署模式與版本而定；standalone jar 不在TomcatJNDI容器內。profile優先順序見[Spring profile]({{< ref "/post/spring-boot/spring-boot-active-profile.md" >}})。

## 確認

重新啟動後通過應用輸出非敏感的ENV值或受控診斷確認，檢查真正的啟動命令／服務設定。不要在日誌列出所有環境秘密；JNDI名稱與大小寫一致。無法lookup時先核對應用context檔名、目錄與java:comp/env字首，再看啟動日誌。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Tomcat JNDI](https://tomcat.apache.org/tomcat-9.0-doc/jndi-resources-howto.html)
- [Tomcat RUNNING](https://github.com/apache/tomcat/blob/9.0.x/RUNNING.txt)
- [迁移指南](https://tomcat.apache.org/migration-10.html)
