---
title: "Redis 指令：鍵值、到期與資料結構"
date: 2021-04-06T10:15:58+08:00
draft: false
categories:
 - "筆記"
tags:
 - "redis"
toc: true
description: "補齊原本空白的 SET/GET，提供可核對結果的本地練習及 SCAN 注意事項。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊原本空白的 SET/GET，提供可核對結果的本地練習及 SCAN 注意事項。

<!--more-->

適用：Redis 7.4，先依安裝篇建立 note-redis。以下在容器內 redis-cli 互動終端操作。

## 開啟與基本鍵值

執行 `docker exec -it note-redis redis-cli`，再輸入：

```text
SET note:name Ian
GET note:name
SET note:session active EX 60
TTL note:session
SET note:name other NX
INCR note:count
INCR note:count
```

SET 應為 OK、GET 為 Ian；TTL 是剩餘秒數（0 到 60 間，過期為 -2），NX 因鍵存在回 nil。全新 note:count 兩次 INCR 為1、2；已有資料時先用 GET 確認，不假設一定從零開始。

## Hash、List 與掃描

```text
HSET note:hero name Ian level 1
HGET note:hero name
LPUSH note:tasks read test
LRANGE note:tasks 0 -1
SCAN 0 MATCH note:* COUNT 20
TYPE note:hero
DEL note:session
```

HGET 應為 Ian；LPUSH 從左加入，列表順序 test、read。SCAN 回 cursor 與部分鍵，持續以上次 cursor 查詢直到 0 才算遍歷完成；COUNT 是提示，回傳不保證20筆，過程可能重複看到鍵。TYPE 為 hash，DEL 回被刪除數量。

## 排錯與限制

WRONGTYPE 先用 TYPE 看資料結構，不能對 hash 用 GET。INCR 只接受可解析整數；`KEYS *` 會掃描全部鍵，大資料量避免在正式系統使用，使用 SCAN 並考慮增刪中並非快照。INFO可能含配置和主機資訊，分享前節錄相關欄位。

只以 note: 字首練習，不用 FLUSHALL 清除其他資料；TTL=-1 表示沒有到期，-2 表示不存在。練習完成可逐一 DEL 本文鍵，並用 GET/HGET 確認。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [SET](https://redis.io/docs/latest/commands/set/)
- [SCAN](https://redis.io/docs/latest/commands/scan/)
- [資料型別](https://redis.io/docs/latest/develop/data-types/)
