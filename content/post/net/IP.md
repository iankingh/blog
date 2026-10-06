---
title: "IP 與子網：IPv4、IPv6、私有位址和 CIDR"
date: 2020-10-06T22:18:37+08:00
draft: false
categories:
 - "技術"
tags:
 - "net"
 - "ip"
 - "internet"
toc: true
description: "修正所有 IP 都全域唯一的說法，補上私有範圍、路由與可重現的子網計算。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正所有 IP 都全域唯一的說法，補上私有範圍、路由與可重現的子網計算。

<!--more-->

適用：IPv4／IPv6與一般開發網路診斷。平臺專用命令按本文標示的OS使用，不混用Linux與Windows引數。

## 位址的意義

IPv4是32位、IPv6是128位；位址對應網路介面／配置，不一定一臺主機只有一個。私有位址在不同網路可以重複，NAT、多網絡卡、VIP與anycast也使「每IP唯一一臺機器」過度簡化。

| RFC1918 範圍 | CIDR |
| --- | --- |
| 10.0.0.0–10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0–172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0–192.168.255.255 | 192.168.0.0/16 |

127.0.0.0/8是IPv4 loopback，169.254.0.0/16是link-local，不屬於上面三組。IPv6 loopback為::1、unique local常見fc00::/7，不能套IPv4遮罩模型。

## Python 計算

```python
import ipaddress
network = ipaddress.ip_network('192.168.10.0/24')
print(network.num_addresses)
print(network.netmask)
print(ipaddress.ip_address('192.168.10.7') in network)
print(ipaddress.ip_address('192.168.11.7') in network)
```

```text
256
255.255.255.0
True
False
```

/24表示網路字首24位，總地址256；一般IPv4子網排除network/broadcast有254個host位址，/31與/32等情境另有規則，不能統一減2。

## 封包如何選路

同網段可直接解析對方的鏈路地址，不同網段依路由表經下一跳；預設gateway只是沒有更具體匹配時的候選。網路層與TCP/UDP port是不同層，IP可達不代表服務可用。

檢查OS地址、CIDR、default route與DNS，再測特定目的服務。多個介面重複網段、VPN路由與DHCP變更可能影響結果，不只猜「IP衝突」。

## 查核範圍

Python ipaddress實際執行，四行輸出一致。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [RFC1918](https://www.rfc-editor.org/rfc/rfc1918)
- [IPv6 RFC8200](https://www.rfc-editor.org/rfc/rfc8200)
- [Python ipaddress](https://docs.python.org/3/library/ipaddress.html)

### 原始筆記保留的來源

- [分類網路](https://zh.wikipedia.org/wiki/分类网络)
- [CIDR](https://zh.wikipedia.org/wiki/无类别域间路由)
- [子網路遮罩](https://zh.wikipedia.org/wiki/子网#网络掩码)

### 原始筆記的其他連結

- [原始參考入口 1](http://dns-learning.twnic.net.tw/internet/intro7.html)
- [原始參考入口 2](https://www.netadmin.com.tw/netadmin/zh-tw/technology/EFA52337DD5D4026BB9E594A3B71EC5B)
- [原始參考入口 3](https://zh.wikipedia.org/wiki/%E4%B8%93%E7%94%A8%E7%BD%91%E7%BB%9C)
- [原始參考入口 4](http://kevin.hwai.edu.tw/~kevin/material/EAssistant/IP_Class.htm)
