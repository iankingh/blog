---
title: "WindowsNetCmd"
date: 2021-01-10T18:04:51+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Windows"
 - "Cmd"
toc: true
---

## WindowsNetCmd筆記
<!--more-->

## 前言

1.CTRL + R ——打開 "運行"

2.在"運行"輸入"cmd"彈出DOS命令列視窗

ipconfig  : 查IP

## 使用

### ipconfig

``` cmd
ipconfig
```

### cls

清空命令


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



網頁出不來故障排除

如果連不上先ping 看看 

如果ping 不成功表示 DNS 或是防火牆沒有設定

nslookup : DNS偵錯工具

powershell指令 : tnc : 測試 port 有沒有通 

Test-NetConnection -ComputerName "www.google.com" -Port 443

可以簡寫tnc

tnc  "www.google.com" -Port 443





### netstat 

查看哪些進程佔用了埠

```cmd


3.假如我要查的是埠"8080"，則輸入命令：netstat -aon|findstr "8080"
4.如上，得到了進程號"4060"，再輸入命令：tasklist|findstr "4060",
  得到了進程映射名稱，好了，下一步我們將解決埠號佔用的問題，就是kill掉該進程映射名稱的進程。
5.CTRL + ALT + delete彈出工作管理員，找到名字為"javaw.exe"的進程，點擊它，並殺死它(結束進程)。
6.再在DOS下輸入命令查看下該埠是否還被佔用：
     netstat -aon|findstr "8080"
7.可以看到，再也沒有進程佔用了該埠，OK，佔用該埠的進程被殺死了，那麼埠被佔用也已經解決了。
```




## 參考

[查看哪些進程佔用了埠 - zhuxiongxian的挨踢博客 - CSDN博客](https://blog.csdn.net/cryhelyxx/article/details/17919897)


[ping、telnet、tracert簡介與使用 - IT閱讀](https://www.itread01.com/content/1550289784.html)  
  

[windows網絡命令：ping、ipconfig、tracert、netstat、arp - 每日頭條](https://kknews.cc/zh-tw/code/o3jx8z5.html)  


https://medium.com/@CarterTsai/%E5%88%A9%E7%94%A8powershell%E7%9A%84test-netconnection%E4%BE%86%E5%8F%96%E4%BB%A3telnet%E4%BE%86%E6%AA%A2%E6%9F%A5%E7%B6%B2%E7%AB%99%E7%9A%84port%E6%9C%89%E6%B2%92%E6%9C%89%E8%A2%AB%E9%96%8B%E5%95%9F-5bc18909ce67