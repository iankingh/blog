---
title: "Docker Volume：持久化、掛載與備份"
date: 2020-09-20T20:29:24+08:00
categories:
  - "筆記"
tags:
 - "docker"
toc: true
draft: false
description: "重整 volume、bind mount 與唯讀掛載範例，補上實際寫入確認、備份還原與多主機限制。"
lastmod: 2026-10-07T00:01:00+08:00
---

重整 volume、bind mount 與唯讀掛載範例，補上實際寫入確認、備份還原與多主機限制。

<!--more-->

適用：Docker Engine 與 Compose v2 的 Linux 容器練習。先確認 Docker daemon 已啟動，以獨立測試專案操作，避免和既有服務同名。

## 選擇儲存方式

| 方式 | 資料位置 | 適合情境 |
| --- | --- | --- |
| named volume | 由 Docker 管理 | 資料庫與容器更換後仍保留的資料 |
| bind mount | 指定主機路徑 | 開發來源、外部提供的設定 |
| tmpfs | 記憶體 | 不需保留的暫存內容，僅 Linux 支援 |

Volume 的生命週期不依附容器，但不是自動備份或跨主機複寫。Docker Desktop 的 volume 位於 VM 裡，不應直接依照 Linux 的 /var/lib/docker 路徑修改。

## 寫入與讀取

```bash
docker volume create note-data
docker run --rm --mount type=volume,src=note-data,dst=/data alpine:3.21 sh -c 'printf "campfire\n" > /data/note.txt'
docker run --rm --mount type=volume,src=note-data,dst=/data,readonly alpine:3.21 cat /data/note.txt
docker volume inspect note-data
```

第二個容器應讀到 campfire，證明刪除第一個容器沒有刪掉 volume。read-only 掛載仍可讀，但不能寫入。`--mount` 欄位較清楚；`-v note-data:/data:ro` 為簡寫。

## 本地備份與還原

在空的備份資料夾執行，使用目前目錄放檔案：

```bash
docker run --rm --mount type=volume,src=note-data,dst=/data,readonly --mount type=bind,src="$PWD",dst=/backup alpine:3.21 tar -czf /backup/note-data.tgz -C /data .
docker volume create note-restored
docker run --rm --mount type=volume,src=note-restored,dst=/data --mount type=bind,src="$PWD",dst=/backup,readonly alpine:3.21 tar -xzf /backup/note-data.tgz -C /data
docker run --rm --mount type=volume,src=note-restored,dst=/data,readonly alpine:3.21 cat /data/note.txt
```

還原後同樣應讀到 campfire。這是靜態檔案練習；運作中的資料庫需要停寫、快照或資料庫專用備份，不能假設 tar 一定一致。還原要驗證內容與許可權，不只看壓縮檔存在。

## 常見問題

掛載到已有內容的容器目錄會遮住原內容；空 volume 可能由映像目錄預填，`volume-nocopy` 可停用該行為。Bind mount 的 `--mount` 在來源不存在時報錯，`-v` 可能建立目錄，容易掩蓋拼錯路徑。SELinux 主機另需核對標籤，不能直接把整個主機目錄改成開放許可權。

多容器共用 volume 仍需應用程式處理併發；NFS 或第三方 driver 需獨立驗證認證、延遲與故障。練習完成再用 `docker volume rm note-data note-restored`，只刪本文建立的 volume；全域 prune 前先確認沒有其他待保留資料。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
- [儲存方式](https://docs.docker.com/engine/storage/)

### 原始筆記保留的來源

- [**Understanding Volumes in Docker**](http://container-solutions.com/2014/12/understanding-volumes-docker/)
- [**https://docs.docker.com/userguide/dockervolumes/**](https://docs.docker.com/userguide/dockervolumes/)
- [docker學習筆記18：Dockerfile 指令 VOLUME 介紹](https://www.cnblogs.com/51kata/p/5266626.html)
- [Docker 實戰系列（二）：在 DockerHub 上分享自己的 image](https://larrylu.blog/share-image-on-dockerhub-ccb7d9b26fa8)
- [官方文件](https://docs.docker.com/storage/volumes/)

### 原始筆記的其他連結

- [原始參考入口 1](https://www.itread01.com/content/1548752791.html)
- [原始參考入口 2](https://julianchu.net/2016/04/19-docker.html)
- [原始參考入口 3](http://chenxiaoyu.org/2014/12/26/docker-volume-chown/)
- [原始參考入口 4](https://blog.51cto.com/dengaosky/1854568)
- [原始參考入口 5](https://larrylu.blog/using-volumn-to-persist-data-in-container-a3640cc92ce4)
