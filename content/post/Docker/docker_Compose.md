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

## Docker_Compose筆記
<!--more-->



## 安裝 docker-compose

### 下載

```shell
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### 安裝

```shell
$ chmod +x /usr/local/bin/docker-compose
```

### 查看版本

````shell
$ docker-compose version
````

### 測試

#### 第一步，創建 Spring boot 服務

```

```

### 第二步，創建 Dockerfile

```dockerfile

```

### 第三步，使用 docker-compose 定義一個文件


```dockerfile
version: '2'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```

这个 Compose 文件定义了两个服务, 一个 Pyhon Web 服务和 redis 服务。

- Pyhon Web 服务：使用 Dockerfile 构建了当前镜像。将 Web 容器内部的5000端口映射到 host 的5000端口；并将 Web 容器与 redis 容器连接。
- redis服务：该容器直接由官方的 redis 镜像创建。

### 第四步，使用 Compose 

使用命令`docker-compose up`启动

```
version: '2'
services:
  web:
    build: .
    command: python app.py
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: "redis:alpine"
```

启动成功之后，在浏览器访问：`http://ipaddress:5000/` ，返回如下：

```
Hello World! I have been seen 1 times.
```

![img](http://favorites.ren/assets/images/2018/docker/quick-hello-world-1.png)

刷新再次访问返回

```
Hello World! I have been seen 2 times.
```

![img](http://favorites.ren/assets/images/2018/docker/quick-hello-world-2.png)

不断的刷新数字会不断的增长。

## Docker Compose 常用命令

使用`docker-compose up -d`在后台启动服务

```
[root@localhost composetest]# docker-compose up -d
```

使用`docker-compose ps`命令查看启动的服务

```
[root@localhost composetest]# docker-compose ps
       Name                      Command               State           Ports         
-------------------------------------------------------------------------------------
composetest_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp              
composetest_web_1     python app.py                    Up      0.0.0.0:5000->5000/tcp
```

使用`docker-compose stop`停止服務。

```
[root@localhost composetest]# docker-compose stop
Stopping composetest_web_1   ... done
Stopping composetest_redis_1 ... done
```

**其它常用命令**

##### 查看幫助
```
docker-compose -h
```


```
# -f  指定使用的 Compose 範本檔，預設為 docker-compose.yml，可以多次指定。
docker-compose -f docker-compose.yml up -d 

#啟動所有容器，-d 將會在後臺啟動並運行所有的容器
docker-compose up -d

#停用移除所有容器以及網路相關
docker-compose down

#查看服務容器的輸出
docker-compose logs

#列出專案中目前的所有容器
docker-compose ps

#構建（重新構建）專案中的服務容器。服務容器一旦構建後，將會帶上一個標記名，例如對於 web 項目中的一個 db 容器，可能是 web_db。可以隨時在專案目錄下運行 docker-compose build 來重新構建服務
docker-compose build

#拉取服務依賴的鏡像
docker-compose pull

#重啟專案中的服務
docker-compose restart

#刪除所有（停止狀態的）服務容器。推薦先執行 docker-compose stop 命令來停止容器。
docker-compose rm 

#在指定服務上執行一個命令。
docker-compose run ubuntu ping docker.com

#設置指定服務運行的容器個數。通過 service=num 的參數來設置數量
docker-compose scale web=3 db=2

#啟動已經存在的服務容器。
docker-compose start

#停止已經處於運行狀態的容器，但不刪除它。通過 docker-compose start 可以再次啟動這些容器。
docker-compose stop

```



## 參考


[Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

[使用 docker-compose 替代 docker run - 张志敏的技术专栏](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)

