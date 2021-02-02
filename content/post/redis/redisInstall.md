---
title: "RedisInstall"
date: 2020-05-20T10:11:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "redis"
toc: true
---

## 簡介

Redis是一個使用ANSI C編寫的開源、支援網路、基於記憶體、可選永續性的鍵值對儲存資料庫。

以官方的解釋，Redis是一套Open source的In-memory NoSQL database，可以應用在Cache、Database及簡單的Message broker。
作者則說它是一個Data Structures Server，顧名思義，它提供了很多種資料結構及相對應的指令去操作這些資料。由於它是以In-Memory的方式為主，另一個很明顯的特性就是它很快，非常快，正確使用下可以輕鬆的處理每秒上萬的請求。
由於它具備極高的效能與可靠性，在很多系統中都會看到它的身影，對Backend/Fullstack engineer來說，這已經是必備的技能之一。


<!--more-->

## 安裝

### Window 下 安裝

####  安裝網址

https://github.com/microsoftarchive/redis/releases

####  啟動指令

```powershell
redis-server.exe redis.windows.conf
```

#### 啟動畫面

![runRedisWin](/images/redis/runRedisWin.png)

#### 測試  

```powershell
//連線指令
redis-cli.exe -h 127.0.0.1 -p 6379
// 塞值
Set testkey testvalue
// 取值
Get testkey
```

![redisWinTest](/images/redis/redisWinTest.png)


### Linux 安裝

用wget從Redis官網下載最新的Redis安裝包，
下載完成後解壓縮到你想要放的位置，然後執行make進行編譯


```shell
$ wget http://download.redis.io/releases/redis-6.0.3.tar.gz
$ tar xzf redis-6.0.3.tar.gz
$ cd redis-6.0.3
$ make
```

#### 啟動 
``` shell
src/redis-server
```

![runRedisUbuntu](/images/redis/runRedisUbuntu.png)

#### 測試

![redisUbuntuTest](/images/redis/redisUbuntuTest.png)

```shell
//連線指令
src/redis-cli  
// 塞值
redis> set foo bar  
// 取值
redis> get foo  
```


## 參考

Redis - 維基百科，自由的百科全書  
https://zh.wikipedia.org/wiki/Redis  

Redis - 在 Windows 上建立高可用性的 Redis | 天空的垃圾場  
https://skychang.github.io/2017/04/09/Redis-Create_Redis_HA/  

Redis系列 - 環境建置篇 - Jed's blog  
https://jed1978.github.io/2018/05/02/Redis-Environment-Installation-Configuration.html
