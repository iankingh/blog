---
title: "Docker_swarm"
date: 2022-05-22T21:57:48+08:00
categories:
- "筆記"
tags:
- "Docker"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

## 前言

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
docker service update --image 192.x.x.xx:5000/dockerImageName:tag swarmS_Name
```


## Summary

## 參考


