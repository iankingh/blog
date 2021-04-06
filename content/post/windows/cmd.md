---
title: "Cmd"
date: 2021-02-04T13:33:19+08:00
draft: true
categories:
 - "筆記"
tags:
 - "windows"
 - "CMD"
toc: true
---

# Windows CMD指令
<!--more-->

Ipconfig  查IP
cls      清空命令
刪除檔案命令DEL 
格式：DEL[d:][path]filename[/P] 
型別：內部命令 
功能：刪除指定的一個或多個檔案，不能用於刪除子目錄。引數/P的功能是使DOS在刪除每個檔案之前，要求使用者先認可，這樣使得使用者可以有選擇地刪除一些檔案 
例如：C:\>DEL TEXT3 
該命令將刪除當前盤的當前目錄下的TEXT3檔案 

查看哪些進程佔用了埠

1.CTRL + R ——打開“運行”
2.在“運行”輸入“cmd”彈出DOS命令列視窗
3.假如我要查的是埠“8080”，則輸入命令：netstat -aon|findstr "8080"

4.如上，得到了進程號“4060”，再輸入命令：tasklist|findstr "4060",得到了進程映射名稱，好了，下一步我們將解決埠號佔用的問題，就是kill掉該進程映射名稱的進程。
5.CTRL + ALT + delete彈出工作管理員，找到名字為"javaw.exe"的進程，點擊它，並殺死它(結束進程)。

6.再在DOS下輸入命令查看下該埠是否還被佔用：
     netstat -aon|findstr "8080"
7.可以看到，再也沒有進程佔用了該埠，OK，佔用該埠的進程被殺死了，那麼埠被佔用也已經解決了。


## 參考
查看哪些進程佔用了埠 - zhuxiongxian的挨踢博客 - CSDN博客
https://blog.csdn.net/cryhelyxx/article/details/17919897

