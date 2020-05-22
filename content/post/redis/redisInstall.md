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
