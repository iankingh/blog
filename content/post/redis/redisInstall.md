---
title: "Redis簡介"
date: 2020-05-20T10:11:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "redis"
toc: true
---



## Redis Install

<!-- 簡介 -->



<!--more-->

## Redis簡介

Redis是一個使用ANSI C編寫的開源、支援、基於記憶體、可選永續性的鍵值對儲存資料庫。

`Redis` 是一个使用 `ANSI C` 編寫的開源、支援 **網路**、基於**記憶體(內存)**、**單線程**、**可選永續性 **的 **鍵值儲存資料庫**。

以官方的解釋，Redis是一套Open source的In-memory NoSQL database，可以應用在Cache、Database及簡單的Message broker。

作者則說它是一個Data Structures Server，顧名思義，它提供了很多種資料結構及相對應的指令去操作這些資料。由於它是以In-Memory的方式為主，另一個很明顯的特性就是它很快，非常快，正確使用下可以輕鬆的處理每秒上萬的請求。


<!--more-->

## Redis Install

## 1.Window 下 安裝

### 安裝網址

https://github.com/microsoftarchive/redis/releases

### 啟動指令

```powershell
redis-server.exe redis.windows.conf
```

### 啟動畫面

![runRedisWin](/images/redis/runRedisWin.png)

### 測試  

```powershell
#連線指令
redis-cli.exe -h 127.0.0.1 -p 6379
#塞值
Set testkey testvalue
#取值
Get testkey
```

![redisWinTest](/images/redis/redisWinTest.png)


## 2.Linux 安裝


```shell
#用wget從Redis官網下載最新的Redis安裝包，
#下載完成後解壓縮到你想要放的位置，然後執行make進行編譯
$ wget http://download.redis.io/releases/redis-6.0.3.tar.gz
$ tar xzf redis-6.0.3.tar.gz
$ cd redis-6.0.3
$ make
```

### 啟動 

``` shell
src/redis-server
```

![runRedisUbuntu](/images/redis/runRedisUbuntu.png)

### 測試

![redisUbuntuTest](/images/redis/redisUbuntuTest.png)

```shell
#連線指令
src/redis-cli  
# 塞值
redis> set foo bar  
# 取值
redis> get foo  
```

### 3. cntos install redis

### 更新 dnf

```shell
sudo dnf update -y
```

### 下載 redis 
1. 下載
```
sudo dnf install redis -y
```
2. 啟動
```
sudo systemctl start redis 

sudo systemctl enable redis
```

3. 確認啟動
```
sudo systemctl status redis
```

4. 看占用的port

 sudo netstat -pnltu | grep redis



### 3.使用Docker

#### 安裝

已經安裝好Docker的環境，只要輸入下列指令就能快速的跑起來一個Redis instance

```
docker run --name MyRedisCache -d -p 6379:6369 redis
```

#### 測試

**進入 container 測試**

```
#連線指令
redis-cli
# 塞值
127.0.0.1:6379> set hello "hello world"
# 取值
127.0.0.1:6379> get hello
```



## 參考

Redis - 維基百科，自由的百科全書  
https://zh.wikipedia.org/wiki/Redis  

Redis - 在 Windows 上建立高可用性的 Redis | 天空的垃圾場  
https://skychang.github.io/2017/04/09/Redis-Create_Redis_HA/  

Redis系列 - 環境建置篇 - Jed's blog  
https://jed1978.github.io/2018/05/02/Redis-Environment-Installation-Configuration.html

如何在CentOS 8 / RHEL 8上安裝Redis服務器
https://www.linuxtechi.com/install-redis-server-on-centos-8-rhel-8/



