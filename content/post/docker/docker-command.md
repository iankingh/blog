---
title: "Docker 常用指令：映像、容器與排錯"
date: 2020-05-31T17:40:46+08:00
toc: true
draft: false
categories:
  - "筆記"
tags:
 - "docker"
description: "整理容器生命週期、日誌、資源與空間檢查，改用正確引數並限制操作到練習容器。"
lastmod: 2026-10-07T00:01:00+08:00
---

整理容器生命週期、日誌、資源與空間檢查，改用正確引數並限制操作到練習容器。

<!--more-->

適用：Docker Engine 與 Compose v2 的 Linux 容器練習。先確認 Docker daemon 已啟動，以獨立測試專案操作，避免和既有服務同名。

## 啟動與檢查

```bash
docker version
docker info
docker pull nginx:1.28-alpine
docker run -d --name note-web -p 127.0.0.1:8080:80 nginx:1.28-alpine
docker ps --filter name=note-web
curl http://127.0.0.1:8080/
```

curl 應取得 Nginx 歡迎 HTML。主機 8080 對應容器 80；EXPOSE 不會自行公開連線埠。若 8080 已使用改為其他主機 port，不修改容器內服務 port。

## 診斷與操作

```bash
docker logs --tail 50 note-web
docker inspect --format '{{.State.Status}}' note-web
docker exec note-web nginx -t
docker stats --no-stream note-web
docker stop note-web
docker ps -a --filter name=note-web
docker start note-web
docker stop note-web
docker rm note-web
```

停止後應為 exited；start 使用同一容器，run 建立新容器。Alpine 未必有 bash，互動式 shell 優先用 `docker exec -it note-web sh`。inspect 可能含環境秘密，不將完整輸出貼到公開紀錄。

## 映像與空間

`docker image ls` 看映像，`docker build -t note-app:1 .` 由目前 context 建置，`docker system df -v` 看佔用。移除練習映像使用 `docker image rm note-app:1`，前提是沒有依賴容器。prune 會影響多個資源，不能把它當無條件清理；先列出對象與備份資料。docker commit 不包含 volume，且不如 Dockerfile 可重現。

本例的 tag 是練習版本；正式維運應確認支援與修補、必要時固定 digest。原筆記的 `docker ps -f id(ContainerId)` 應改為 `--filter id=實際ID`，sell 拼字已修正為 bash。

## 原指令小抄的補充

| 工作 | 指令或限制 |
| --- | --- |
| 只取 container ID | `docker ps -q`；`-a` 含停止的容器，`-l` 只列最新建立者 |
| 從映像 registry 搜尋 | `docker search nginx` 是搜尋 Docker Hub，不是列出本機所有映像；私有 registry 依其 API 或介面查詢 |
| 容器內環境 | `docker exec note-web printenv` 會揭露環境變數，只在自己的測試環境使用 |
| 一次與持續日誌 | `docker logs --tail 50 note-web` 與 `docker logs -f note-web`，持續模式以 Ctrl+C 結束查看，不會停止容器 |
| 進入容器 | `docker exec -it note-web sh`，不要假設精簡映像有 bash；exit 離開此次 exec shell |
| 從容器製作映像 | commit 只保存容器檔案系統的變更，不含 mounted volume、完整 build 歷程或可重現安裝步驟 |
| 清理空間 | `docker system df -v` 先查佔用；system prune 會清理停止容器、未用網路、可清理映像／build cache，`-a`／`--volumes` 改變範圍，須先確認資料 |

本篇只操作具名的練習資源；原先 stop／rm 全部 container 的組合指令不作預設做法。移除 volume 是資料生命週期決定，不能只因容器停止就推定資料不需要。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Docker CLI](https://docs.docker.com/reference/cli/docker/)
- [容器生命週期](https://docs.docker.com/engine/containers/run/)

### 原始筆記保留的來源

- [Docker常用命令小記_程式設計師欣宸的部落格-CSDN部落格](https://blog.csdn.net/boling_cavalry/article/details/101145739)
- [docker container ls命令 - Docker教程™](https://www.yiibai.com/docker/container_ls.html)
