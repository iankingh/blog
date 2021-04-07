---
title: "Linux_必裝"
date: 2021-04-07T09:54:34+08:00
draft: true
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

 網路工具

1. 安裝指令
```
 sudo yum -y install net-tools
```
2. 測試
```
netstat
```
3. 觀看服務
```
 sudo netstat -pnltu | grep redis
```

### firewalld 

防火牆管理工具

1. 安裝指令
```
sudo dnf install firewalld
```
2. 啟用

```
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

3. 測試
```
sudo firewall-cmd --state
```
Output
```
public
```


## 參考
How To Set Up a Firewall Using firewalld on CentOS 8 | DigitalOcean
https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-8

netstat Command not found on CentOS 8 / RHEL 8 - Quick Fix - | ITzGeek
https://www.itzgeek.com/how-tos/linux/centos-how-tos/netstat-command-not-found-on-centos-8-rhel-8-quick-fix.html


