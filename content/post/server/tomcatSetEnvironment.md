---
title: "TomcatSetEnvironment"
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

於apache-tomcat-9.0.43/conf/context.xml 中可以設定 Environment


````xml
<?xml version="1.0" encoding="UTF-8"?>
<Context>

<Environment name="ENV" value="uat" type="java.lang.String" override="false"/>
<Environment name="SPRING_PROFILES_ACTIVE" value="sit" type="java.lang.String" override="false"/>

````

## 參考
