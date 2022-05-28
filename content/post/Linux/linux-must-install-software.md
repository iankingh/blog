---
title: "linux-must-install-software"
date: 2021-04-07T09:54:34+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Linux"
toc: true
---

## Linux_必裝
<!-- 簡介 -->
<!--more-->

### netstat

netstat 是一個網路工具

- 安裝指令

```shell
 sudo yum -y install net-tools
```

-測試

```shell
netstat
```

- 觀看服務

``` shell
 sudo netstat -pnltu | grep redis
```

### firewallds

防火牆管理工具

- 安裝指令

```shell
sudo dnf install firewalld
```

- 啟用

```shell
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

- 測試

```shell 
sudo firewall-cmd --state
```

- Output

``` shell
public
```

## 參考

[How To Set Up a Firewall Using firewalld on CentOS 8 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-8)


netstat Command not found on CentOS 8 / RHEL 8 - Quick Fix - | ITzGeek
https://www.itzgeek.com/how-tos/linux/centos-how-tos/netstat-command-not-found-on-centos-8-rhel-8-quick-fix.html
