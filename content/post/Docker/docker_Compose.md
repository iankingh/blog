---
title: "Docker_Compose"
date: 2020-09-28T21:53:46+08:00
draft: false
categories:
  - "筆記"
tags:
 - "docker"
toc: true
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

### 查看版本

````shell
docker-compose version
````

### 測試

#### 第一步，創建 Spring boot 服務

```shell


```

### 第二步，創建 Dockerfile

```dockerfile



```

### 第三步，使用 docker-compose 定義一個文件

```yml
version: '2'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```

這個 compose.yml 定義2個服務，一是Spring boot  一個是 redis 服務。

- Pyhon Web 服务：使用 Dockerfile 构建了当前镜像。将 Web 容器内部的5000端口映射到 host 的5000端口；并将 Web 容器与 redis 容器连接。
- redis服务：该容器直接由官方的 redis 镜像创建。

### 第四步，使用 Compose

使用命令`docker-compose up`启动

```shell
docker-compose up
```

启动成功之后，在浏览器访问：`http://ipaddress:8080/` ，返回如下：

```shell
Hello World! I have been seen 1 times.
```

## img  要放圖片

刷新再次访问返回

```shell
Hello World! I have been seen 2 times.
```

## img 要放圖片

不断的刷新数字会不断的增长。

## Docker Compose 常用命令

使用`docker-compose up -d` 在後台啟動服務

啟動所有容器，-d 將會在後臺啟動並運行所有的容器

```shell
docker-compose up -d
```

使用`docker-compose ps`  查看啟動的服務

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






## docker-compose 命令

### docker-compose -h 查看幫助

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

### stop services 停止已經處於運行狀態的容器，但不刪除它。通過 docker-compose start 可以再次啟動這些容器

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

### 查看服務容器的輸出

```shell
docker-compose logs
```

### 構建（重新構建）專案中的服務容器

服務容器一旦構建後，將會帶上一個標記名，例如對於 web 項目中的一個 db 容器，可能是 web_db。可以隨時在專案目錄下運行 docker-compose build 來重新構建服務

```shell
docker-compose build
```

### 拉取服務依賴的鏡像

```shell
docker-compose pull
```

### 在指定服務上執行一個命令

```shell
docker-compose run ubuntu ping docker.com
```

### 設置指定服務運行的容器個數。通過 service=num 的參數來設置數量

```shell
docker-compose scale web=3 db=2
```



## 參考

[Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

[使用 docker-compose 替代 docker run - 张志敏的技术专栏](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)

[Angular — Local Development With Docker-Compose | by Bhargav Bachina | Bachina Labs | Medium](https://medium.com/bb-tutorials-and-thoughts/angular-local-development-with-docker-compose-13719b998e42)
