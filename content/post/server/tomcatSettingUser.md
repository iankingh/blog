---
title: "Tomcat Manager：角色、使用者與存取範圍"
date: 2021-03-03T13:33:50+08:00
aliases:
 - "/post/server/tomcatsetinguser/"
draft: false
categories:
 - "筆記"
tags:
 - "AP Server"
 - "tomcat"
toc: true
description: "修正不合法 XML 佔位值，補上 manager-gui 許可權及 401／403 診斷。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正不合法 XML 佔位值，補上 manager-gui 許可權及 401／403 診斷。

<!--more-->

適用：Tomcat 9 的 MemoryUserDatabase 管理帳號；其他Realm需各自身份來源配置。

## 有效 XML 範例

conf/tomcat-users.xml 的 tomcat-users 節點中加入角色和帳號，示意值需要替換為獨立強密碼：

```xml
<tomcat-users xmlns="http://tomcat.apache.org/xml" version="1.0">
  <role rolename="manager-gui"/>
  <user username="CHANGE_ME_USER" password="CHANGE_ME_STRONG_PASSWORD" roles="manager-gui"/>
</tomcat-users>
```

若檔案已有根節點，只加入role/user，不建立第二個根。原 `<YOUR_USERNAME>` 放在attribute內是無效XML；佔位值應用不含尖括號的字串。密碼含&需XML轉義，設定檔不公開或提交秘密。

## 最小角色

manager-gui 提供GUI管理；manager-script 提供程式介面，因CSRF防護差異避免同一帳號同時給gui與script/jmx。admin-gui屬Host Manager，不是所有Manager操作的必要角色。

本機訪問 `http://127.0.0.1:8080/manager/html`，重新啟動後應要求認證並顯示應用列表。401檢查Realm、賬號與密碼；403檢查role以及Manager的RemoteAddrValve限制。404先確認部署包是否含manager應用。

## 網路限制與確認

保留localhost／可信管理網的訪問限制，不為遠端方便刪除Valve向公網開放。生產最好經VPN或受控管理入口；應用業務使用者不混作管理帳號。確認時只讀取應用列表，不以解除安裝業務app驗證許可權。

若使用外部Realm或容器映象的自訂配置，此檔未必是認證來源，先看server.xml與日誌再修改。帳號輪替與許可權審計屬於維護流程，不是一次建立後永久不管。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Manager 存取](https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html)
- [Realm](https://tomcat.apache.org/tomcat-9.0-doc/realm-howto.html)

### 原始筆記保留的來源

- [tomcat配置管理員-走後門 - WhyWin - 部落格園](https://www.cnblogs.com/0201zcr/p/6668010.html)
- [如何進入tomcat的管理頁面 - begin27的部落格 - CSDN部落格](https://blog.csdn.net/begin27/article/details/50966261)
