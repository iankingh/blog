---
title: "tomcatSetingUser"
date: 2021-03-03T13:33:50+08:00
draft: false    
categories:
 - "筆記"
tags:
 - "java"
 - "tomcat"
toc: true
---

## 配置Tomcat 的使用者

<!--more-->


## 配置Tomcat 的使用者

於 tomcat 的 conf/tomcat-users.xml

```
  <!-- 配置角色 -->
  <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>

  <!-- 配置管理帳號及權限 -->
  <user username="用戶名" password="密碼" roles="admin-gui,manager-gui"/>

```

參考
tomcat配置管理员-走后门 - WhyWin - 博客园
https://www.cnblogs.com/0201zcr/p/6668010.html

如何进入tomcat的管理页面 - begin27的博客 - CSDN博客
https://blog.csdn.net/begin27/article/details/50966261