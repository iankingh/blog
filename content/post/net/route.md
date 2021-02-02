---
title: "Route"
date: 2021-02-01T18:04:51+08:00
draft: false
categories:
 - "categories"
tags:
 - "Windows"
 - "Cmd"
toc: true
---

駐點在外，客戶端不能上Internet是件痛苦事。幸虧一位contract介紹用route，可以同時連測試機與無線外網，有陣子可以通，雖然有時秀逗。在DOS下執行以下的command：

一、查詢route：

route print：

IPv4 路由表
===========================================================================
使用中的路由:
網路目的地        網路遮罩          閘道       介面  公制

       0.0.0.0          0.0.0.0     192.168.11.1    192.168.11.27    26
      10.0.0.0        255.0.0.0        在連結上      10.204.1.126     21
    10.204.1.0    255.255.255.0        在連結上      10.204.1.126    276
  10.204.1.126  255.255.255.255        在連結上      10.204.1.126    276
  10.204.1.255  255.255.255.255        在連結上      10.204.1.126    276
10.255.255.255  255.255.255.255        在連結上      10.204.1.126    276
     127.0.0.0        255.0.0.0        在連結上         127.0.0.1    306

… (節錄)
===========================================================================

Network Destination： 表示路由的網路目的地，可以是 IP 網段或IP位址。
Netmask：表示子網路遮罩，用來配合 Network Destination 的運算。
Gateway：是封包欲送往的 IP 位址，如果目的 IP 位址與 Netmask 作 AND 邏輯運算，剛好與 Network Destination 相同，封包就會送到此 Gateway 的 IP 位址。
Interface： 是此電腦送出封包的 IP 位址。
Metric： 則是傳送成本的參考數字，通常與網路連接速度有關，越低的 Metric 表示速度越快。

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

http://www.w-type.com.tw/wepalm_email/47.htm

