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

# Docker_Compose筆記
<!--more-->



## 安裝Compose

#### 1.下載

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

#### 2.安裝

```shell
chmod +x /usr/local/bin/docker-compose
```

#### 3.查看版本

````shell
docker-compose version
````



測試

### 第一步，創建 Spring boot 服務

在

```

```

### 第二步，创建 Dockerfile

同样在此目录下，我们创建一个 Dockerfile 文件。

```dockerfile
FROM python:3.4-alpine
ADD . /code
WORKDIR /codeDㄟ
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### 第三步，使用 Compose 文件定义一个服务

在当期目录下，我们创建一个 docker-compose.yml 文件，内容如下：

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

使用`docker-compose stop`停止服务。

```
[root@localhost composetest]# docker-compose stop
Stopping composetest_web_1   ... done
Stopping composetest_redis_1 ... done
```

**其它常用命令**

```
#查看帮助
docker-compose -h

# -f  指定使用的 Compose 模板文件，默认为 docker-compose.yml，可以多次指定。
docker-compose -f docker-compose.yml up -d 

#启动所有容器，-d 将会在后台启动并运行所有的容器
docker-compose up -d

#停用移除所有容器以及网络相关
docker-compose down

#查看服务容器的输出
docker-compose logs

#列出项目中目前的所有容器
docker-compose ps

#构建（重新构建）项目中的服务容器。服务容器一旦构建后，将会带上一个标记名，例如对于 web 项目中的一个 db 容器，可能是 web_db。可以随时在项目目录下运行 docker-compose build 来重新构建服务
docker-compose build

#拉取服务依赖的镜像
docker-compose pull

#重启项目中的服务
docker-compose restart

#删除所有（停止状态的）服务容器。推荐先执行 docker-compose stop 命令来停止容器。
docker-compose rm 

#在指定服务上执行一个命令。
docker-compose run ubuntu ping docker.com

#设置指定服务运行的容器个数。通过 service=num 的参数来设置数量
docker-compose scale web=3 db=2

#启动已经存在的服务容器。
docker-compose start

#停止已经处于运行状态的容器，但不删除它。通过 docker-compose start 可以再次启动这些容器。
docker-compose stop
```



### 參考

Docker(四)：Docker 三剑客之 Docker Compose - 纯洁的微笑博客

http://www.ityouknow.com/docker/2018/03/22/docker-compose.htm

https://docs.docker.com/compose/install/