---
title: "Cmd"
date: 2021-02-04T13:33:19+08:00
draft: false
categories:
 - "筆記"
tags:
 - "windows"
 - "CMD"
toc: true
---

## Windows CMD指令
<!--more-->

## 快速打開 cmd

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
