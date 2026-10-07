---
title: "Linux 網路工具：ss、systemctl 與 firewalld"
date: 2021-04-07T09:54:34+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Linux"
toc: true
description: "補齊網路與防火牆診斷，修正 firewalld state 和 zone 的混淆。"
lastmod: 2026-10-07T20:50:40+08:00
---

補齊網路與防火牆診斷，修正 firewalld state 和 zone 的混淆。

<!--more-->

適用：使用 systemd 的 Linux；firewalld 是否安裝與啟用依發行版而異。

## 先檢查，不先安裝

```bash
ss -lnt
ss -lun
systemctl status firewalld
```

ss -lnt 看監聽 TCP，ss -lun 看 UDP。顯示程式名稱可用 `sudo ss -lntp`，許可權不足不表示服務不存在。舊筆記 netstat 由 net-tools 提供，目前通常可先使用 iproute2 的 ss。

## firewalld 查詢

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
```

--state 的預期為 running，不是 public；public 是可能的 zone 名稱。實際網絡卡所屬 zone 與 default zone 不必相同，要先查 active zones。

## 調整的確認方式

遠端 SSH 操作前先確認 ssh service 在正確 zone 放行，另開第二連線保留恢復入口。要新增服務用指定 zone 的 `--add-service=...`，runtime 與 `--permanent` 分開，必要時在確認runtime有效後儲存；reload 會以永久規則重新建立狀態，不能盲目執行。

服務無法連線依序看監聽位址（127.0.0.1／0.0.0.0）、port、zone規則、主機上游防火牆與實際客戶端。不要以停止防火牆當長期解法。本篇只示範查詢，不代替實際主機的變更核准與回復流程。

## 參考資料

- [firewalld CLI](https://firewalld.org/documentation/man-pages/firewall-cmd.html)
- [ss 手冊](https://man7.org/linux/man-pages/man8/ss.8.html)
- [How To Set Up a Firewall Using firewalld on CentOS 8 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-8)
- [原始參考入口 1](https://www.itzgeek.com/how-tos/linux/centos-how-tos/netstat-command-not-found-on-centos-8-rhel-8-quick-fix.html)
