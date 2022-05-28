---
title: "Route"
date: 2021-02-01T18:04:51+08:00
categories:
 - "categories"
tags:
 - "Windows"
 - "Cmd"
 - "route"
toc: true
draft: false
---



## 在 Windows 設定 Route
<!-- 簡介 -->
駐點在外，客戶端不能上Internet是件痛苦事。幸虧一位contract介紹用route，可以同時連測試機與無線外網，有陣子可以通，雖然有時秀逗。在DOS下執行以下的command：

前一陣子到總公司上課時，臨時要使用內部網路走VPN連回公司處理問題，而同時間又需要使用Wireless上網。可是當我的Wireless連接上時，Notebook的Default Gateway就會變成Wireless設定的Gateway，此時就無法透過內部的網路走VPN連回公司。

使用Windows的『route』指令可以設定Static Route，變更順序。

<!--more-->



### 一、指令說明：

```
ROUTE [-f] [-p] [command [destination]
                  [MASK netmask]  [gateway] [METRIC metric]  [IF interface]
```

-f      清除路由
-p      保留設定值，不會因電腦重開機而失效。

Command    包含以下命令
   PRINT   列出目前的路由表
   ADD    增加一筆靜態路由
    DELETE  刪除一筆靜態路由
   CHANGE  修改現存的路由

destination  路由的目標IP位址或網段。
netmask    子網路遮罩
gateway     指定要走的Gateway
interface   指定送出封包時的網卡ID
METRIC    可視為封包傳遞的優先權，數字愈低優先權愈高。

intra 內部

DMZ

sticky 黏

subnet

HA 

tls

dtls

render

local decode encode

ipref

checkpoint

bandwidth

question

which

F5 VIP

SNAT

NAT

port forwarding

pass-through

pooling

UDP hole punching

STUN TURN

port mapping

ICMP

high latency



### 一、查詢route：


IPv4 路由表
===========================================================================
route print：
為了閱讀方便，將使用Route Print查詢的結果以表格呈現如下：

| Network Destination網路目的地 | Netmask 網路遮罩 | Gateway 閘道  | Interface 介面 | Metric 公制 |
| ----------------------------- | ---------------- | ------------- | -------------- | ----------- |
| 0.0.0.0                       | 0.0.0.0          | 10.10.1.1     | 10.10.1.101    | 20          |
| 0.0.0.0                       | 0.0.0.0          | 192.168.1.1   | 192.168.1.101  | 20          |
| 127.0.0.0                     | 255.0.0.0        | 127.0.0.1     | 127.0.0.1      | 1           |
| 192.168.1.0                   | 255.255.255.0    | 192.168.1.1   | 192.168.1.101  | 20          |
| 192.168.1.101                 | 255.255.255.255  | 127.0.0.1     | 127.0.0.1      | 20          |
| 192.168.1.255                 | 255.255.255.255  | 192.168.1.101 | 192.168.1.101  | 20          |
| 10.10.1.0                     | 255.255.255.0    | 10.10.1.101   | 10.10.10.101   | 20          |
| 10.10.1.101                   | 255.255.255.255  | 127.0.0.1     | 127.0.0.1      | 20          |
| 10.10.1.255                   | 255.255.255.255  | 10.10.1.101   | 10.10.10.101   | 20          |
| 255.255.255.255               | 255.255.255.255  | 192.168.1.101 | 192.168.1.101  | 1           |
| 255.255.255.255               | 255.255.255.255  | 10.10.1.101   | 10.10.1.101    | 1           |

Network Destination： 表示路由的網路目的地，可以是 IP 網段或IP位址。
Netmask：表示子網路遮罩，用來配合 Network Destination 的運算。
Gateway：是封包欲送往的 IP 位址，如果目的 IP 位址與 Netmask 作 AND 邏輯運算，剛好與 Network Destination 相同，封包就會送到此 Gateway 的 IP 位址。
Interface： 是此電腦送出封包的 IP 位址。
Metric： 則是傳送成本的參考數字，通常與網路連接速度有關，越低的 Metric 表示速度越快。





前2筆代表著，要連至不存在Routing Table中的其他所有位址都由該Gateway出去。
但由於2者的Metric都是20，因此無法控制固定由哪個Gateway出去

因此可使用以下的命令來修改Metric的值【調整Gateway的優先權】，讓所有對外的連線固定透過無線網卡出去。
`route change 0.0.0.0 mask 0.0.0.0 10.10.1.1 if 0x2 metric 10`

另外，若要透過有線網卡連VPN回公司，則可新增下列一筆路由
`route add 192.168.99.0 mask 255.255.255.0 192.168.1.1 if 0x2 metric 20`

如果要刪除新增的路由，則可使用以下命令
`route delete 192.168.99.0 mask 255.255.255.0`



　　上表的紅色粗體字的資訊，介面192.168.11.27是無線網路分配給我的IP，192.168.11.1則是無線站台的Gateway，處在第一列表示為default route，所以會先搜到無線站台，就可以上網；第二列起是Local Network的IP迴路。
至於像胖兄介紹的迴路路徑不是在第二列，而排得那麼後面，不得而知，也許和我下設定的command有關。

二、設定route

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::f0e5:c960:e1a5:7faa%3
   IPv4 Address. . . . . . . . . . . : 192.168.43.246
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.43.1


Wifl 網卡 gateway ip :192.168.43.1

route delete 0.0.0.0
route delete 10.0.0.0
route delete 172.0.0.0
route ADD 0.0.0.0 MASK 0.0.0.0 192.168.43.1
route ADD 10.0.0.0 MASK 255.0.0.0 10.204.1.126
route ADD 172.0.0.0 MASK 255.0.0.0 10.204.1.126
pause


route change 0.0.0.0 mask 0.0.0.0 192.168.43.1
route add 192.168.70.0 mask 255.255.255.0 192.168.14.251
route add 192.168.51.0 mask 255.255.255.0 192.168.14.251
route add 192.168.53.0 mask 255.255.255.0 192.168.14.251
route add 192.168.211.0 mask 255.255.255.0 192.168.14.251
pause

最後一個pause(暫停)是我加的，加pause是為了避免執行後馬上Close DOS視窗。可以看每一條命令是否回應"確定"。

route delete語法還OK，route add語法是：

route ADD <Network Destination> MASK <Netmask> <Gateway> (if <Interface> metric <Metric>)


刪除0.0.0.0 route目的在取代default 

route；刪除10.0.0.0是內部網路的網段，至於刪除172.0.0.0的目的…我猜是和給我這個批次的contract，和他自身設定有關，應該可以忽略。

很妙的是Gateway可以用Local IP替代，而不是尾數是1。


最後還要再執行兩個命令讓重設的route起作用。

ipconfig /release
ipconfig /renew


參考
Windows route初體驗 @ Jemmy Walker :: 痞客邦 ::
https://jemmywalker.pixnet.net/blog/post/38323627

http://ctwivan.blogspot.com/2010/08/windowsstatic-route.html

