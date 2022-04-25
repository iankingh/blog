---
title: "HikariPool-1 - Connection is not available, request timed out after 30000ms"
date: 2021-05-06T21:18:55+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "連線池"
toc: true
---

## HikariPool-1 - Connection is not available, request timed out after 30000ms

<!-- 簡介 -->

HikariPool是連接池管理類，負責管理數據庫連接。

HikariPool-1 - Connection is not available, request timed out after 30000ms

表示資料庫連線池請求超時

<!--more-->

報錯日誌:

```prolog
java.sql.SQLTransientConnectionException: HikariPool-1 - Connection is not available, request timed out after 30000ms.
```

### **原因一 : 由於網絡延遲或某些查詢執行時間過長（超過30000毫秒），因此數據庫未在（30000毫秒，這是默認的connectionTimeout屬性）內未獲得連接。**

可以試看看增加Timeout的時間

YML配置示例：

```yaml
spring:
	datasource:
		hikari:
		#最小連線數
		minimumIdle: 2
		#最大連線數
		maximumPoolSize: 10
		idleTimeout: 120000
		connectionTimeout: 300000
		leakDetectionThreshold: 300000
```

Java Config示例：

```java
HikariConfig config = new HikariConfig();

config.setMaximumPoolSize(20);

config.setConnectionTimeout(300000);

config.setConnectionTimeout(120000);

config.setLeakDetectionThreshold(300000);
```

## **參考**

[java - HikariPool-1 - Connection is not available, request timed out after 30000ms for very tiny load server - Stack Overflow](https://stackoverflow.com/questions/47758091/hikaripool-1-connection-is-not-available-request-timed-out-after-30000ms-for)

[JavaWeb問題集錦: 資料庫連線池請求超時 HikariPool-1 - Connection is not available, request timed out after 30000ms - IT閱讀 (itread01.com)](https://www.itread01.com/content/1543459742.html)
