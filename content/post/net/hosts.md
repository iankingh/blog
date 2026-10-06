---
title: "hosts 設定：本地名稱對映與 DNS 診斷"
date: 2021-04-06T09:40:12+08:00
categories:
 - "筆記"
tags:
 - "net"
 - "hosts"
toc: true
draft: false
description: "補上有效格式、平臺路徑與驗證方式，區分 hosts、DNS 快取與 HTTPS 憑證。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上有效格式、平臺路徑與驗證方式，區分 hosts、DNS 快取與 HTTPS 憑證。

<!--more-->

適用：IPv4／IPv6與一般開發網路診斷。平臺專用命令按本文標示的OS使用，不混用Linux與Windows引數。

## 格式與位置

Windows為C:\Windows\System32\drivers\etc\hosts，Linux/macOS為/etc/hosts。以管理許可權修改前備份原內容；新增測試項：

```text
127.0.0.1 note.test
::1 note.test
```

一行先IP再hostname，空白分隔，#註釋。不含http://、path或port，不能用wildcard替换全部subdomain。若本機服務只监听IPv4，先只用IPv4項，避免IPv6優先連線失敗。

## 本地確認

先啟動獨立HTTP服務，如`python3 -m http.server 8086 --bind 127.0.0.1`，再訪問`http://note.test:8086/`。這是HTTP練習，HTTPS憑證仍需匹配note.test，hosts不會建立信任。

Windows使用`ping note.test`看解析地址，Python可用`socket.getaddrinfo('note.test',8086)`檢查系統解析。nslookup常直接問DNS，不證明所有應用會讀取同一hosts結果。瀏覽器DNS／proxy／DoH行為需按實際配置確認。

## 排錯與復原

儲存後確認不是hosts.txt、許可權與檔案編碼正常。Windows可視需要ipconfig /flushdns，macOS/Linux快取機制不同，不套同一命令。企業proxy可能在代理端解析目標，修改本機hosts不一定影響它。

完成練習後移除自己加入的項並確認恢復，不刪除原有系統內容。hosts只能對映名稱，不是防火牆或訪問許可權；共享團隊環境應使用可維護DNS／配置，而不是要求每個人手動改大量hosts。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Windows name resolution](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/troubleshoot-dns-client-resolution-issues)
- [Python socket](https://docs.python.org/3/library/socket.html#socket.getaddrinfo)

### 原始筆記保留的來源

- [轉移網站的過程](https://blog.gtwang.org/wordpress/migrate-wordpress-to-lemp-server/)

### 原始筆記的其他連結

- [原始參考入口 1](https://blog.gtwang.org/windows/windows-linux-hosts-file-configuration/)
