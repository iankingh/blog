---
title: "TomcatSetserverxml"
date: 2021-04-06T09:29:21+08:00
draft: false
categories:
 - "筆記"
tags:
 - "AP Server"
 - "Tomcat"
toc: true
---

## Tomcat server set server xml筆記
<!-- 簡介 -->
<!--more-->

### 設定路徑

apache-tomcat/conf/server.xml

### 設定檔案上傳大小

設定大小

```xml
 <Connector connectionTimeout="20000" maxPostSize="209715200" port="8080" protocol="HTTP/1.1" redirectPort="8443"/>
```

**調整如下**
![調整Tomcat上傳檔案大小](../images/tomcat/調整Tomcat上傳檔案大小.png)

### 設定部屬路徑及檔案位址

```xml
  <Host appBase="webapps" autoDeploy="true" name="localhost" unpackWARs="true">
<Context docBase="restApi" path="/restApi" reloadable="true" source="../SpringProjectRestApi"/>
</Host>
```

## 參考
