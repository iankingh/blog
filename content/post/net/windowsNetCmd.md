---
title: "Windows 網路排錯：IP、DNS、TCP 與程式"
date: 2021-01-10T18:04:51+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Windows"
 - "Cmd"
toc: true
description: "修正 Run 快捷鍵及混用 Linux netstat 引數，建立分層診斷順序。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 Run 快捷鍵及混用 Linux netstat 引數，建立分層診斷順序。

<!--more-->

適用：Windows10/11與PowerShell NetTCPIP；外部example.com只是可替換測試目的，不聲稱本次執行Windows指令。

## 開啟與資訊

Win+R輸入cmd或PowerShell，不是Ctrl+R。先查配置：

```powershell
ipconfig /all
route print -4
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
netstat -ano -p tcp
```

ipconfig看介面、DHCP、DNS與gateway；Resolve-DnsName看DNS回答；Test-NetConnection的TcpTestSucceeded測port能否建立TCP，不保證HTTPS業務成功。netstat -ano顯示數字地址與PID，-at/-au是一些Linux寫法，不當Windows通用。

## 找到程式與症狀

用Task Manager或`Get-Process -Id 實際PID`對應監聽程式；可能需管理許可權讀取詳細資訊。ping測ICMP，不是主機一定「開ping service」；無回應可能防火牆阻擋，不能直接結論不存在。

`tracert example.com`觀察路徑回應，星號可能該裝置不回TTL-expired，並不證明整條路徑中斷。Telnet是舊協議，可臨時測試TCP但常未安裝，優先Test-NetConnection，不用它傳秘密。

## 排錯順序

本機地址→default route→DNS→目的TCP port→TLS→HTTP狀態→業務響應。若IP能連、域名不能連才聚焦解析；TCP成功但403應看授權；多網絡卡／VPN先檢查選路。cls只清畫面、不清網路狀態。

ipconfig /release、/renew等會影響連線，不當每次排錯的第一步。記錄目標、時間、OS與測試結果，公開輸出先去掉內部地址／host資訊；對真實主機的修正仍需實際拓撲。

## 參考資料

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig)
- [netstat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat)
- [Test-NetConnection](https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection)
- [檢視哪些程式佔用了埠 - zhuxiongxian的挨踢部落格 - CSDN部落格](https://blog.csdn.net/cryhelyxx/article/details/17919897)
- [ping、telnet、tracert簡介與使用 - IT閱讀](https://www.itread01.com/content/1550289784.html)
- [windows網路命令：ping、ipconfig、tracert、netstat、arp - 每日頭條](https://kknews.cc/zh-tw/code/o3jx8z5.html)
- [原始參考入口 1](https://medium.com/@CarterTsai/%E5%88%A9%E7%94%A8powershell%E7%9A%84test-netconnection%E4%BE%86%E5%8F%96%E4%BB%A3telnet%E4%BE%86%E6%AA%A2%E6%9F%A5%E7%B6%B2%E7%AB%99%E7%9A%84port%E6%9C%89%E6%B2%92%E6%9C%89%E8%A2%AB%E9%96%8B%E5%95%9F-5bc18909ce67)
