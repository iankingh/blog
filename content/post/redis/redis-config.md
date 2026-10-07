---
title: "Redis 設定：監聽、記憶體與持久化"
date: 2021-04-06T10:22:06+08:00
draft: false
categories:
 - "筆記"
tags:
 - "redis"
toc: true
description: "移除不能直接使用的編號設定片段，補上有效 redis.conf 與核對方式。"
lastmod: 2026-10-07T20:50:40+08:00
---

移除不能直接使用的編號設定片段，補上有效 redis.conf 與核對方式。

<!--more-->

適用：Redis 7.4 的 localhost 練習；Redis Cluster 不支援用 SELECT 做多資料庫隔離。

## 最小本機設定

在獨立目錄先建立 data，儲存 redis.conf：

```conf
bind 127.0.0.1
protected-mode yes
port 6379
daemonize no
logfile ""
dir ./data
dbfilename dump.rdb
save 60 100
appendonly yes
appendfsync everysec
maxmemory 128mb
maxmemory-policy allkeys-lru
```

以原生 Redis 執行 `redis-server ./redis.conf`。另開終端執行 `redis-cli PING`，應 PONG；`redis-cli CONFIG GET maxmemory` 應128MiB對應的134217728。配置不能混入條列編號或中文說明，註釋以 # 開頭。

## 持久化與限制

RDB 依時間與修改數量產生快照，AOF 記錄寫操作；everysec 不是每次寫入都同步落盤，故障可能丟失近期資料。Redis 7 使用多段 AOF，備份不能只找舊版單一 appendonly.aof。兩者都不是自動跨機器備份，需要驗證複製與恢復。

allkeys-lru 可驅逐任何鍵，適合練習快取，不適合把資料當不可丟失記錄。noeviction 達上限會拒絕部分寫入，應用要處理錯誤。maxmemory不等於整個程式RSS上限，複製、緩衝與allocator也佔記憶體。

## 平臺與確認

容器內若使用此 bind127.0.0.1，其他容器不能連到它；容器網路配置需另選監聽地址並以網路／ACL限制，不單純複製本機檔。systemd／container通常前景執行，不需daemonize yes。logfile空字串表示stdout，不寫成 `logfile stdout`。

CONFIG SET 的變更不保證重啟後儲存，需維護真正的配置或依授權使用 CONFIG REWRITE。修改後確認啟動日誌、CONFIG GET、讀寫及重啟資料，再測備份還原。密碼與ACL從部署秘密來源提供，文章不使用預設弱密碼。

## 參考資料

- [Redis configuration](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
- [Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [Eviction](https://redis.io/docs/latest/develop/reference/eviction/)
