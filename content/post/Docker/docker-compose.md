---
title: "docker-compose"
date: 2020-09-28T21:53:46+08:00
categories:
  - "筆記"
tags:
 - "docker"
 - "compose"
toc: true
draft: false
---

## Docker_Compose 筆記

<!--more-->

## 安裝 docker-compose

### 下載

```shell
curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### 安裝

```shell
chmod +x /usr/local/bin/docker-compose
```

### 檢視版本

````shell
docker-compose version
````

### 測試

#### 第一步，建立 Spring boot 服務

透過Spring Initializru頁面，建立一個 Spring boot 服務，並且指定要使用的專案。

### 第二步，建立 Dockerfile

```dockerfile


```

### 第三步，使用 docker-compose 定義一個檔案

```yml
version: '2'
services:
  web:
    build: .
    ports:
     - "8080:8080"
  redis:
    image: "redis:alpine"
```

這個 compose.yml 定義2個服務，一是Spring boot  一個是 redis 服務。

- Spring Web 服務：使用 Dockerfile 。將 Web 容器內部的5000埠對映到 host 的5000埠；並將 Web 容器與 redis 容器連結。

- redis服務：官網的redis。

### 第四步，使用 Compose

使用命令`docker-compose up`啟動

```shell
docker-compose up
```

執行成功之後，在browser ：`http://ipaddress:8080/` ，返回如下：

```shell
Hello World! I have been seen 1 times.
```

#  img  要放圖片

重新整理再次訪問返回


```shell
Hello World! I have been seen 2 times.
```

# img 要放圖片

不斷的重新整理數字會不斷的增長。

## docker-compose 命令

使用`docker-compose up -d` 在後臺啟動服務

啟動所有容器，-d 將會在後臺啟動並執行所有的容器

```shell
docker-compose up -d
```

使用`docker-compose ps`  檢視啟動的服務

列出專案中目前的所有容器

```shell
docker-compose ps
```

```shell
Name    Command               State           Ports         
-------------------------------------------------------------

```

使用`docker-compose stop`停止服務。

```shell
docker-compose stop
```

```shell
Stopping composetest_web_1   ... done
Stopping composetest_redis_1 ... done
```

`docker-compose restart` ：重啟專案中的服務

### docker-compose -h 檢視幫助

```shell
docker-compose -h 
```

### create and start containers

```shell
docker-compose up
```

### start services with detached mode

```shell
docker-compose -d up
```

### start specific service

```shell
docker-compose up <service-name>
```

### stop services 停止已經處於執行狀態的容器，但不刪除它。透過 docker-compose start 可以再次啟動這些容器

```shell
docker-compose stop
```

### start service 啟動已經存在的服務容器

```shell
docker-compose start
```

### list images

```shell
docker-compose images
```

### list containers

```shell
docker-compose ps
```

### display running containers

```shell
docker-compose top
```

### stop all contaners and remove images, volumes 停用移除所有容器以及網路相關

```shell
docker-compose down
```

### remove stopped containers 刪除所有（停止狀態的）服務容器。推薦先執行 docker-compose stop 命令來停止容器

```shell
docker-compose rm 
```

### kill services

```shell
docker-compose kill
```

### 檢視服務容器的輸出

```shell
docker-compose logs
```

### 構建（重新構建）專案中的服務容器

服務容器一旦構建後，將會帶上一個標記名，例如對於 web 專案中的一個 db 容器，可能是 web_db。可以隨時在專案目錄下執行 docker-compose build 來重新構建服務

```shell
docker-compose build
```

### 拉取服務依賴的映象

```shell
docker-compose pull
```

### 在指定服務上執行一個命令

```shell
docker-compose run ubuntu ping docker.com
```

### 設定指定服務執行的容器個數。透過 service=num 的引數來設定數量

```shell
docker-compose scale web=3 db=2
```

## 參考

[Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

[使用 docker-compose 替代 docker run - 張志敏的技術專欄](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)

[Angular — Local Development With Docker-Compose | by Bhargav Bachina | Bachina Labs | Medium](https://medium.com/bb-tutorials-and-thoughts/angular-local-development-with-docker-compose-13719b998e42)

[Docker(四)：Docker 三劍客之 Docker Compose](https://mp.weixin.qq.com/s/DCqjeXtGoHnM7Wfm5Sme6w?)
