---
title: "Dockerfile：建立靜態網頁映像"
date: 2020-09-20T19:45:16+08:00
categories:
  - "筆記"
tags:
 - "docker"
toc: true
draft: false
description: "從完整 Dockerfile 與 HTML 建置映像，補上 context、快取、COPY 及執行結果。"
lastmod: 2026-10-07T00:01:00+08:00
---

從完整 Dockerfile 與 HTML 建置映像，補上 context、快取、COPY 及執行結果。

<!--more-->

適用：Docker Engine 與 Compose v2 的 Linux 容器練習。先確認 Docker daemon 已啟動，以獨立測試專案操作，避免和既有服務同名。

## 完整範例

在空資料夾建立 index.html：

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>Docker</title><h1>營火已啟動</h1></html>
```

Dockerfile：

```dockerfile
FROM nginx:1.28-alpine
LABEL org.opencontainers.image.title="note-web"
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

.dockerignore：

```text
.git
.env
node_modules
```

```bash
docker build -t note-web:1 .
docker run --rm -d --name note-file-demo -p 127.0.0.1:8081:80 note-web:1
curl http://127.0.0.1:8081/
docker stop note-file-demo
```

回應應包含營火已啟動，stop 後 `--rm` 會移除容器。這裡沿用基底映像的啟動指令，不需再定義 CMD。

## 指令與快取

FROM 選基底、WORKDIR 設後續工作目錄、COPY 帶入檔案、RUN 在建置時執行、CMD 提供啟動預設、ENTRYPOINT 設定主要執行檔。`RUN cd /tmp` 不會持續到下一個 RUN，用 WORKDIR。

`-f` 選 Dockerfile，命令末尾的 `.` 是 context，COPY 不能任意讀取 context 外檔案。MAINTAINER 已是舊寫法，改 LABEL。不是每個指令都會建立有內容的檔案系統層，現行 BuildKit 快取也不能簡化成每步 commit；改檔會使相關 COPY 與後續步驟重建。

不要在 ARG/ENV、COPY 或 RUN 中放秘密，以免留在映像或快取。若需下載依賴，優先先 COPY lockfile 安裝，再 COPY 來源，以改善可重現性與快取。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Dockerfile 語法](https://docs.docker.com/reference/dockerfile/)
- [建置快取](https://docs.docker.com/build/cache/)
- [建置 context](https://docs.docker.com/build/concepts/context/)

### 原始筆記保留的來源

- [Dockerfile **使用介紹 -** **純潔的微笑部落格**](http://www.ityouknow.com/docker/2018/03/12/docker-use-dockerfile.html)
