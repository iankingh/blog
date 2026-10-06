---
title: "Windows 路由：字首、介面與暫時規則"
date: 2021-02-01T18:04:51+08:00
categories:
 - "技術"
tags:
 - "Windows"
 - "Cmd"
 - "route"
toc: true
draft: false
description: "補上最長字首優先與 metric 比較，提供有前提的測試路由及精確移除方式。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上最長字首優先與 metric 比較，提供有前提的測試路由及精確移除方式。

<!--more-->

適用：Windows IPv4路由表。本文新增規則僅示意隔離測試拓撲，本次macOS未修改Windows路由。

## 先讀目前配置

```powershell
route print -4
Get-NetIPConfiguration
Get-NetRoute -AddressFamily IPv4 | Sort-Object DestinationPrefix, RouteMetric
Get-NetIPInterface -AddressFamily IPv4
```

路由先比最長字首，不能單看metric低就一定優先；相同字首比較route與interface等成本。目的網段、遮罩、下一跳與interface要配對，gateway通常需在該介面可達範圍內。

## 隔離測試示意

只有測試機確實有介面12、地址192.168.50.x/24與可用router192.168.50.1時，才使用：

```cmd
route add 10.20.0.0 mask 255.255.255.0 192.168.50.1 metric 20 if 12
route print 10.20.*
route delete 10.20.0.0 mask 255.255.255.0 192.168.50.1 if 12
```

實際介面ID由前述命令取得，本文數字是拓撲示例不是你的電腦資訊。新增後檢查只有這條規則變化，測試目標網段服務，再刪除精確同一規則。不要用route -f清全部路由；遠端操作前準備恢復連線方式。

## 永久規則與限制

route -p add可保留規則，但DHCP、VPN或interface改變後可能失效，不一開始就永久化。Windows PowerShell NetTCPIP提供New-/Remove-NetRoute等另一介面，policy store行為要依命令檔案確認。

新增路由不會讓路由器自動有回程路線，也不開啟遠端防火牆。單向不通檢查回程、NAT與目的服務；tracert星號不代表必然故障，部分裝置不回ICMP。修改前後儲存去識別化route輸出，清楚記錄驗證的網路範圍。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Windows route](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/route_ws2008)
- [Get-NetRoute](https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-netroute)
- [New-NetRoute](https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netroute)

### 原始筆記的其他連結

- [原始參考入口 1](https://jemmywalker.pixnet.net/blog/post/38323627)
- [原始參考入口 2](http://ctwivan.blogspot.com/2010/08/windowsstatic-route.html)
