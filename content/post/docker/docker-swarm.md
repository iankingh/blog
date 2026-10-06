---
title: "Docker Swarm：服務部署、更新與回滾"
date: 2022-05-22T21:57:48+08:00
categories:
- "筆記"
tags:
- "Docker"
toc: true
draft: false
description: "補上 manager 初始化與單節點練習，整理 service、replica、task 與環境變數更新。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上 manager 初始化與單節點練習，整理 service、replica、task 與環境變數更新。

<!--more-->

適用：Docker Engine 與 Compose v2 的 Linux 容器練習。先確認 Docker daemon 已啟動，以獨立測試專案操作，避免和既有服務同名。

## 單節點練習

需在獨立 Linux VM 或未加入其他 Swarm 的 Docker 上操作。多網絡卡時需指定可被其他節點連到的 advertise 地址。

```bash
docker swarm init
docker node ls
docker service create --name note-swarm --replicas 2 --publish published=8082,target=80 nginx:1.28-alpine
docker service ls
docker service ps note-swarm
curl http://127.0.0.1:8082/
```

service ls 應出現 2/2 replicas，service ps 有兩個 running task。service 表示期望狀態，task 是排程的執行單位，container 是實際執行環境。單節點兩個 replica 不等於高可用。

## 更新與回滾

```bash
docker service update --env-add NOTE_MODE=demo note-swarm
docker service inspect --pretty note-swarm
docker service update --rollback note-swarm
docker service ps note-swarm
docker service rm note-swarm
```

環境更新會重建 task，Nginx 不會因 NOTE_MODE 自動改變畫面，應從 inspect 確認。映像更新用 `--image repository:tag`，正式部署保留可回滾的版本並測健康檢查；rollback 還原上一個 service 規格，並不回復資料庫。

## 網路與資料限制

routing mesh 將 published port 分派到 task，多主機要核對 overlay 和管理連線的必要 port。registry 若需認證，部署時按檔案提供認證；不要把密碼寫進 service env，使用 secrets。local volume 不會自動在所有節點同步。

練習結束若確定此為全新的單節點且無其他服務，可用 `docker swarm leave --force` 離開；既有叢集 manager 不應套用此清理動作。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [建立 Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/)
- [Service update](https://docs.docker.com/reference/cli/docker/service/update/)
- [Swarm secrets](https://docs.docker.com/engine/swarm/secrets/)
