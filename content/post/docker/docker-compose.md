---
title: "Docker Compose：Web 與 Redis 的完整練習"
date: 2020-09-28T21:53:46+08:00
categories:
  - "筆記"
tags:
 - "docker"
 - "compose"
toc: true
draft: false
description: "用完整 Node Web 與 Redis 小專案理解 Compose 服務解析、健康檢查及持久化。"
lastmod: 2026-10-07T20:50:40+08:00
---

用完整 Node Web 與 Redis 小專案理解 Compose 服務解析、健康檢查及持久化。

<!--more-->

適用：Docker Engine 與 Compose v2 的 Linux 容器練習。先確認 Docker daemon 已啟動，以獨立測試專案操作，避免和既有服務同名。

## 版本與專案檔案

原筆記使用 docker-compose 1.29，現行練習採 `docker compose` v2。Compose 的頂層 version 已不再決定新格式，不需要寫 `version: '2'`。建立空資料夾，package.json：

```json
{"name":"compose-note","private":true,"type":"module","dependencies":{"redis":"4.7.0"}}
```

app.mjs：

```javascript
import { createServer } from 'node:http'
import { createClient } from 'redis'
const cache = createClient({ url: 'redis://redis:6379' })
cache.on('error', error => console.error(error.message))
await cache.connect()
createServer(async (request, response) => {
  try {
    const count = await cache.incr('note:hits')
    response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' })
    response.end(`瀏覽 ${count} 次\n`)
  } catch {
    response.writeHead(503)
    response.end('Cache unavailable\n')
  }
}).listen(8080, '0.0.0.0')
```

Dockerfile：

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY app.mjs ./
CMD ["node", "app.mjs"]
```

先用 `npm install --package-lock-only` 產生 lockfile，與來源一起保留。compose.yaml：

```yaml
services:
  web:
    build: .
    ports: ["127.0.0.1:8080:8080"]
    depends_on:
      redis:
        condition: service_healthy
  redis:
    image: redis:7.4-alpine
    command: ["redis-server", "--appendonly", "yes"]
    volumes: ["redis-data:/data"]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 2s
      timeout: 1s
      retries: 10
volumes:
  redis-data:
```

## 執行與預期結果

```bash
docker compose config
docker compose up -d --build
docker compose ps
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/
docker compose logs --tail 30 web
docker compose down
```

全新的 volume 下兩次 curl 分別應為瀏覽 1 次、瀏覽 2 次。重新 up 後計數延續；瀏覽器可能多請求 favicon，使數字不只加一，精確測試使用 curl。down 保留 named volume，`down -v` 會刪掉本專案資料，僅在確定不需練習紀錄時使用。

容器內 redis 是服務名稱，不是 localhost；主機不公開 Redis port。healthcheck 可處理初次啟動順序，不能取代執行中故障的重試、連線恢復與正式監控。本篇以本地小服務取代原筆記未提供的 Spring Boot 專案，正式應用仍可依同樣網路原則配置。

## 原 Compose 指令與 v2 對照

原 `docker-compose` 的指令大多可改為 `docker compose`，但安裝方式、頂層格式與工具支援需確認：

| 目的 | 此練習的指令 |
| --- | --- |
| 停止／啟動既有服務 | `docker compose stop web`、`docker compose start web`；start 不會重新建置來源 |
| 映像與執行狀態 | `docker compose images`、`docker compose ps -a` |
| 重新建置／拉映像 | `docker compose build web`、`docker compose pull redis`，然後用 up 套用需要的變更 |
| 服務內執行 | `docker compose exec redis redis-cli ping`，服務已執行時應回 PONG |
| 移除停止者 | `docker compose rm`；與 down 的專案網路移除行為不同 |
| 強制停止 | `docker compose kill` 不提供正常停止的寬限流程，通常先用 stop |
| 複本數 | `docker compose up -d --scale web=2` 的概念可用，但本例固定主機 8080，複本會爭用 port，先改代理或不公開每個複本的固定主機 port |

不要把可支援 scale 等同服務已具備 HA；仍要處理入口、session、資料共享與依賴故障。原未提供的 Spring Boot app 已由本文明確的 Node 小服務取代，兩者的語言和框架不同，網路與持久化觀念相同。

## 參考資料

- [Compose 規格](https://docs.docker.com/reference/compose-file/)
- [服務啟動順序](https://docs.docker.com/compose/how-tos/startup-order/)
- [Compose 網路](https://docs.docker.com/compose/how-tos/networking/)
- [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)
- [使用 docker-compose 替代 docker run - 張志敏的技術專欄](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Angular — Local Development With Docker-Compose | by Bhargav Bachina | Bachina Labs | Medium](https://medium.com/bb-tutorials-and-thoughts/angular-local-development-with-docker-compose-13719b998e42)
- [Docker(四)：Docker 三劍客之 Docker Compose](https://mp.weixin.qq.com/s/DCqjeXtGoHnM7Wfm5Sme6w?)
