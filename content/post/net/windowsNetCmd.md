---
title: "WindowsNetCmd"
date: 2021-01-10T18:04:51+08:00
draft: false
categories:
 - "categories"
tags:
 - "Windows"
 - "Cmd"
toc: true
---

WindowsNetCmd筆記
<!--more-->

## 前言

在網路的世界有 Client 端 及 Server 端 ，有時Server 時要對Cleint 端 開放 特殊服務的Port 才可以正常使用服務 


## Windows網路指令:

### ping ip
   ping命令是用來檢測網路是否暢通的    
   ping指的是端對端連通，通常用來作為可用性的檢查
   一般來說server 都會開 ping service，所以 ping ip，就可以知道該 server 是否存在。


```
ping www.google.com
```

### telnet ip port
   Telnet是一種應用層協定，可以用來確認某個 ip的port 有沒有 TCP 服務。

```
telnet 192.168.70.33 80
```

### netstat
   查看目前所在機器有那些網路連線，包含 TCP 和 UDP。
   了解網絡的整體使用情況。它可以顯示當前正在活動的網絡連接的詳細信息，如採用的協議類型（看tcp，udp）、當前主機與遠端相連主機（一個或多個）的IP位址以及 它們之間的連接狀態等。

   netstat監控TCP/IP網絡的非常有用的工具，它可以顯示路由表、實際的網絡連接以及每一個網絡接口設備的狀態信息。

```
netstat -a # 列出所有埠 
netstat -n #顯示所有已建立的有效連接。 
netstat -at # 列出所有TCP埠 
netstat -au # 列出所有UDP埠 
```
"-a"選項意在顯示所有連接，當不附加"-n"選項時，它顯示的是本地計算機的 netbios名字+埠號。
加了"-n"選項後，它顯示的是本地IP位址+埠號。

### tracert
tracert 是一個簡單的網絡診斷工具，可以列出分組經過的路由節點（通過tracert命令，就能知道本機與目標主機之間經過多台主機，即經過多少路由。）

```
tracert www.google.com
```


參考

ping、telnet、tracert簡介與使用 - IT閱讀  
https://www.itread01.com/content/1550289784.html  

windows網絡命令：ping、ipconfig、tracert、netstat、arp - 每日頭條  
https://kknews.cc/zh-tw/code/o3jx8z5.html
