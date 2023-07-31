---
title: "Mongodb_install"
date: 2023-07-30T22:37:01+08:00
categories:
- "筆記"
tags:
- "Mongodb"
- "nosql"
toc: true
draft: false
---

# Windows安裝免安裝版的MongoDB

<!-- 簡介 -->
<!--more-->
## 下載網址

[MongoDB Community Downloads | MongoDB](https://www.mongodb.com/download-center/community/releases)

## 配置變數

### 新增對應的資料夾

- data/db 用来存放數據
- data/log/mongodb.log 用来存放日誌

### 修改 **mongodb.conf**配置文件

建立一個**mongodb.conf**的文件在資料夾中 , 並新增以下內容

```conf
# 數據的位置
dbpath=../data/db
# 日誌的位置
logpath=../data/log/mongodb.log
```

## 啟動

進到 mongodb/bin 輸入以下指令

`mongod.exe --config "../mongodb.conf"`

## 打開瀏覽器

 <http://localhost:27017/>

出現 
 It looks like you are trying to access MongoDB over HTTP on the native driver port.
表示啟動成功

## 參考

[MongoDB免安装版安装_java后端指南的博客-CSDN博客](https://blog.csdn.net/Ting1king/article/details/124757490)

[windowns免安装MongoDB_windows免安装mongodb_花哥码天下的博客-CSDN博客](https://blog.csdn.net/qq_39940205/article/details/120434224)


[Day17 - MongoDB 安裝設定 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天 (ithome.com.tw)](https://ithelp.ithome.com.tw/articles/10186324)
