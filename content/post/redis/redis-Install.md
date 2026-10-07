---
title: "Redis 安裝：本機 Docker 與平臺選擇"
date: 2020-05-20T10:11:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "redis"
toc: true
description: "修正 Redis port 對映及舊 Windows 移植版資訊，提供 localhost 測試與停止流程。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 Redis port 對映及舊 Windows 移植版資訊，提供 localhost 測試與停止流程。

<!--more-->

適用：Redis 7.4 的獨立測試 instance。舊 Redis 6 與 microsoftarchive Windows 版本只作為歷史背景。

## 以 Docker 建立隔離測試

先完成 Docker 安裝並確認 daemon，使用限定 loopback 的 port：

```bash
docker run -d --name note-redis -p 127.0.0.1:6379:6379 redis:7.4-alpine
docker exec note-redis redis-cli PING
docker exec note-redis redis-cli SET note:hello campfire
docker exec note-redis redis-cli GET note:hello
```

依序應為 PONG、OK、campfire。原 `6379:6369` 右側寫錯，Redis 預設監聽6379。若只在容器內操作，可以省略 -p；不需要為練習公開到所有網絡卡。

## 平臺差異

原 microsoftarchive/redis 是已封存的舊 Windows port，不當目前官方版本。Windows可依官方 WSL/Docker 路線；Linux選擇官方支援的repo或固定版本原始碼、核對checksum；不要以舊 `http://...redis-6.0.3` 當「最新版」。發行版的 systemd 服務名稱與配置位置要用套件檔案確認。

Redis 是記憶體資料結構伺服器，持久化為可選設計；主命令處理模型、IO執行緒與背景任務不應全數概括為只有一條執行緒。可當快取、資料儲存或訊息元件，但可靠性、驅逐策略與一致性要求不同。

## 停止與資料

```bash
docker stop note-redis
docker rm note-redis
```

這個無 volume 的練習刪除容器後資料不保留。若要儲存參考[Redis 設定]({{< ref "/post/redis/redis-config.md" >}})與 Docker volume。正式環境另設 ACL、網路隔離、備份與復原測試，不能拿測試 instance 當 production。

## 參考資料

- [Redis 安裝](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
- [Windows 路線](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/)
- [Redis - 維基百科，自由的百科全書 (wikipedia.org)](https://zh.wikipedia.org/wiki/Redis)
- [Redis系列 - 環境建置篇 - Jed's blog (jed1978.github.io)](https://jed1978.github.io/2018/05/02/Redis-Environment-Installation-Configuration.html)
- [How to Install Redis Server on CentOS 8 / RHEL 8 (linuxtechi.com)](https://www.linuxtechi.com/install-redis-server-on-centos-8-rhel-8/)
- [Redis - 在 Windows 上建立高可用性的 Redis :: 天空的垃圾場 v3 (skychang.github.io)](https://skychang.github.io/2017/04/09/Redis-Create_Redis_HA/)
- [原始參考入口 1](https://github.com/microsoftarchive/redis/releases)
