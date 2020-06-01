---
title: "docker 指令"
date: 2020-05-31T17:40:46+08:00
draft: true
categories:
  - "筆記"
tags:
 - "docker"
toc: true
---

<!--more-->



##  images



## container 

### 看 運行中的container 

```
docker container ls
```

### 或是這樣  

```
docker ps
```

### 加上-a 看全部

```
docker ps -a 
```

-a :

```
docker pa -lq 
```

-l :显示最新创建的容器(包括所有状态)

-q :只显示数字ID

### 停掉 Container

```docker 
docker stop 
```

移除停掉 Container

```
docker rm
```

  看 log 

```
docker logs
```

進入 container 裡面

```
docker exec -it containerID bash 
```

 查看docker 容器使用的资源

```
docker stats  
```

提交一個commit

docker commit cID 





**Tips** ： **不同狀態的鏡像** 

·    **已使用鏡像（****used image****）**： 指所有已被容器（包括已停止的）關聯的鏡像。即 docker ps -a 看到的所有容器使用的鏡像。

·    **未引用鏡像（****unreferenced image****）**：沒有被分配或使用在容器中的鏡像，但它有 Tag 資訊。

·    **懸空鏡像（****dangling image****）**：未配置任何 Tag （也就無法被引用）的鏡像，所以懸空。這通常是由於鏡像 build 的時候沒有指定 -t 參數配置 Tag 導致的。比如:`REPOSITORY TAG IMAGE ID CREATED SIZE  6ad733544a63 5 days ago 1.13 MB # ``懸空鏡像（``dangling image``）`

**掛起的卷（****dangling Volume)** 類似的，dangling=true 的 Volume 表示沒有被任何容器引用的卷。



## docker system

### 分析 Docker 空間分佈

```
docker system df
```

可用於查詢鏡像（Images）、容器（Containers）和本地卷（Local Volumes）等空間使用大戶的空間佔用情況。

加上-v 表示細節查看空間佔用細節

```
docker system df -v
```

### 自動清理

可以通過 Docker 內置的 CLI 指令 `docker system prune` 來進行自動空間清理。

```
docker system prune
```

WARNING! This will remove:

 \- all stopped containers

 \- all networks not used by at least one container

 \- all dangling images(Dangling images are layers that have no relationship to any tagged images.)

 \- all dangling build cache



```
 docker system prune -a
```





WARNING! This will remove:



 \- all stopped containers

 \- all networks not used by at least one container

 \- all images without at least one container associated to them (表示所有沒有關聯container 的images 清除)

 \- all build cache

**docker system prune** **自動清理說明**：

·    該指令預設會清除所有如下資源： 

o  已停止的容器（container）

o  未被任何容器所使用的卷（volume）

o  未被任何容器所關聯的網路（network）

o  所有懸空鏡像（image）。

·    該指令預設只會清除懸空鏡像，未被使用的鏡像不會被刪除。

·    添加 `-a ``或`` --all` 參數後，可以一併清除所有未使用的鏡像和懸空鏡像。

·    可以添加 `-f ``或`` --force` 參數用以忽略相關告警確認資訊。

·    指令結尾處會顯示總計清理釋放的空間大小。



## 常用

docker pull

docker image : 看鏡像

docker ps :看容器

docker info : 看整體

docker system prune會刪除以下內容：

a. 已經停止的容器；

b. 未被使用的網路；

c. 所有未打標籤的鏡像；

d. 構建鏡像時產生的緩存；



刪除已經停止的容器：docker container prune

刪除未被使用的網路：docker network prune

刪除沒有Tag的鏡像：docker image prune

刪除沒有容器的鏡像：docker image prune -a

刪除未被使用的資料卷：docker volume prune

docker ps -f id=cid

docker inspect Cid > Y.txt 獲取容器/鏡像的 ENV。

參考

https://blog.csdn.net/boling_cavalry/article/details/101145739

參考

docker container ls命令 - Docker教程™

https://www.yiibai.com/docker/container_ls.html

