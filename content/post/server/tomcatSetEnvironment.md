---
title: "Tomcat 設定環境變數"
date: 2021-04-05T16:33:28+08:00
draft: false
categories:
 - "筆記"
tags:
 - "AP Server"
 - "tomcat"
toc: true
---

## Tomcat 設定 環境變數
<!-- 簡介 -->
<!--more-->

可在 `apache-tomcat/conf/context.xml` 的 `<Context>` 節點內設定 JNDI Environment Entry：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Context>
  <Environment name="ENV" value="uat" type="java.lang.String" override="false"/>
  <Environment name="SPRING_PROFILES_ACTIVE" value="sit" type="java.lang.String" override="false"/>
</Context>
```

應用程式需透過 JNDI 讀取這些值。密碼與金鑰不宜直接寫入版本控制中的 `context.xml`，應由部署環境提供。

## 參考
