---
title: "Install_docker_on_centos"
date: 2021-03-25T10:21:24+08:00
categories:
 - "筆記"
tags:
 - "linux"
 - "docker"
toc: true
draft: true
---

## 安裝 Docker 在 centos8
<!-- 簡介 -->
<!--more-->

## centOS-8_install_docker

### 2.1.install Docker 

```sh
# 更新yum 
$ sudo yum install -y yum-utils

# 更新 repo
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
	
# 安裝 Docker
$ sudo yum install docker-ce docker-ce-cli containerd.io

# 啟動 Docker 
$ sudo systemctl start docker

# 配置Docker以在啟動時啟動
$ sudo systemctl enable docker.service
$ sudo systemctl enable containerd.service

# 確認Docker
$ docker ps

# 確認Docker pull run 
$ docker run hello-world

```

### 2.2.加入docker 群組

```shell
# 新增Docker 群組
$ sudo groupadd docker

# 確認 使用者
$ echo $USER

# 加入Docker 群組
$ sudo usermod -a -G docker $USER

# 重啟Docker
$ sudo systemctl restart docker

# 做完需要重新開機
$ shutdown -r now

# 確認Docker 
$ docker ps

# 如果不想重新開機,可以切換到 Docker 群組
$ newgrp docker
```


## 參考

CentOS 8 install Docker - Pocket Admin
https://pocketadmin.tech/en/centos-8-install-docker/

linux-docker.sock	
https://stackoverflow.com/questions/48568172/docker-sock-permission-denied

https://docs.docker.com/engine/install/linux-postinstall/

https://morosedog.gitlab.io/docker-20190601-docker13/
