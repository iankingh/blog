---
title: "Linux指令"
date: 2020-06-22T19:01:50+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Linux"
toc: true
---

## Linux指令
<!--more-->

## 修改檔案權限

```shell
chmod 777 file(資料夾名)
chmod 777 -R file(資料夾名)  
R-->全部
chmod -R 777 * --> 修改權


```



## 看目錄

```shell
pwd --->當前目錄
ll 看目錄
ls -ltr --->看目錄資料權限
ls -al  >>> 看權限
cd   $home  //到現在使用者下的目錄

```


<!-- ps -ef
./XXX.sh 執行目錄下的.sh檔案
Ctrl+c 停止

to-sh.sh 
exit 離開

chown -R

gunzip -d  ‘要解壓縮的檔案’ //-d 表示 刪除壓縮檔 -->


## 參考 :
