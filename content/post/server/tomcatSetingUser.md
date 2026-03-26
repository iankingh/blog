---
title: "tomcatSetingUser"
date: 2021-03-03T13:33:50+08:00
draft: false    
categories:
 - "筆記"
tags:
 - "AP Server"
 - "tomcat"
toc: true
---

## 配置Tomcat 的使用者

<!--more-->

於 tomcat 的 conf/tomcat-users.xml

```xml
  <!-- 配置角色 -->
  <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>

  <!-- 配置管理帳號及許可權 -->
  <user username="使用者名稱" password="密碼" roles="admin-gui,manager-gui"/>

```

## 參考

[tomcat配置管理員-走後門 - WhyWin - 部落格園](https://www.cnblogs.com/0201zcr/p/6668010.html)

[如何進入tomcat的管理頁面 - begin27的部落格 - CSDN部落格](https://blog.csdn.net/begin27/article/details/50966261)
