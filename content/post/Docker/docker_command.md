---
title: "docker 指令"
date: 2020-05-31T17:40:46+08:00
categories:
  - "筆記"
tags:
 - "docker"
toc: true
draft: false
---


## Docker 指令

<!--more-->

## Images 相關的指令

### bulid images



#### see images(看映像)

```shell
docker images
```

#### docker pull(下載映像)

```sell
docker pull
```

#### see registry images()

```sell
curl -XGET 192.168.x.x:5000/v2/_catalog
```

## container 

### docker container ls (看容器) 

```sell
docker container ls
```

### docker ps (看容器)

```sell
docker ps
```

#### -a : 看到的所有容器

```sell
docker ps -a 
```

#### -l :顯示最新創建的容器(包括所有狀態)

```sell
docker ps -l
```

#### -q :只顯示數字ID

```sell
docker ps -q 
```

#### -f:  過濾器

```shell
docker ps -f id(ContainerId)
```

### Container Stop (停掉Container)

```sell
docker stop 
```

### Container remove(移除停掉的Container)

```sell
docker rm
```

### see log 

```sell
docker logs
```

#### Show Container's logs (once) 

```sell
docker logs ContainerId
```

#### Log countinuing

```sell
docker logs -f ContainerId
```

### See Container ENV

```sell
docker inspect Cid > Y.txt  (獲取容器/鏡像的 ENV。)
```

### Into Container (進入 container 裡面)

```sell
docker exec -it containerID bash 
```

### into 執行命令

```sell
docker exec -it ebbeb7c38404 bash -c 'echo "$envKey"'
```

## stop && rm docker container

```sell
docker stop ContainerId && docker rm ContainerId
```

## Container status (查看docker 容器使用的資源)

```sell
docker stats  
```

## 提交一個commit

```sell
docker commit cID
```

## docker system

### docker system df (空間分佈)

```sell
docker system df
```

可用於查詢鏡像（Images）、容器（Containers）和本地卷（Local Volumes）等空間使用大戶的空間佔用情況。

#### -v 表示細節查看空間佔用細節

```sell
docker system df -v
```

### docker system prune (空間清理)

可以通過 Docker 內置的 CLI 指令 `docker system prune` 來進行自動空間清理。

```sell
docker system prune
```

WARNING! This will remove:

 \- all stopped containers (已經停止的容器（container）)

 \- all networks not used by at least one container(未被使用的網路)

 \- all dangling images(Dangling images are layers that have no relationship to any tagged images.)(所有未打標籤的鏡像(images)。)

 \- all dangling build cache(構建鏡像時產生的緩存)

該指令預設只會清除懸空鏡像，未被使用的鏡像不會被刪除。

·    添加 `-a `或 `--all` 參數後，可以一併清除所有未使用的鏡像和懸空鏡像。

·    可以添加 `-f `或` --force` 參數用以忽略相關告警確認資訊。

·    指令結尾處會顯示總計清理釋放的空間大小。

#### 刪除已經停止的容器：

```sell
docker container prune
```

#### 刪除未被使用的網路：

```sell
docker network prune
```

#### 刪除沒有Tag的鏡像：

```sell
docker image prune
```

#### 刪除沒有容器的鏡像：

````sell
docker image prune -a
````

#### 刪除未被使用的資料卷：

````sell
docker volume prune
````

## Docker swarm

### see swarm service ls

```sell
docker service ls
```

### see swarm service status

```sell
docker service ps serviceID
```

### update service env

```sell
docker service update --env-add envKey=envValue serviceName
```

### update service

```sell
docker service update --image 172.22.11.11:5000/dockerImageName:tag swarmS_Name
```

  

## 參考

[Docker常用命令小记_程序员欣宸的博客-CSDN博客](https://blog.csdn.net/boling_cavalry/article/details/101145739)

[docker container ls命令 - Docker教程™](https://www.yiibai.com/docker/container_ls.html)

[[Docker] Docker 指令小抄 - Miles's Journey](https://mileslin.github.io/2019/04/Docker-%E6%8C%87%E4%BB%A4%E5%B0%8F%E6%8A%84/)

