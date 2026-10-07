---
title: "CentOS 8 的 Docker 安裝紀錄與替代路線"
date: 2021-03-25T10:21:24+08:00
categories:
 - "筆記"
tags:
 - "linux"
 - "docker"
toc: true
draft: false
description: "標示 CentOS Linux 8 結束維護，區分歷史套件操作與目前受支援系統的安裝確認。"
lastmod: 2026-10-07T20:50:40+08:00
---

標示 CentOS Linux 8 結束維護，區分歷史套件操作與目前受支援系統的安裝確認。

<!--more-->

適用：原筆記的 CentOS Linux 8 歷史情境；新部署依實際受支援發行版選官方流程。本次未執行 OS 安裝或遷移。

## 歷史環境

CentOS Linux 8 已於 2021-12-31 結束維護。原筆記的 yum/dnf repo 安裝步驟保留為情境說明，不建議為新服務改用 vault 後繼續長期運作。CentOS Stream 與 CentOS Linux 不同發行方式，不能直接視為相同版本的修補升級。

先讀 `/etc/os-release` 與 `uname -m`，確認發行版、major 與架構，再按 Docker 官方對該系統的支援矩陣安裝。不要混用 RHEL、CentOS、Rocky、AlmaLinux 的套件來源；若官方未列出就以供應商檔案或受支援 VM 作替代。

## 安裝後檢查

受支援系統完成官方 repo 與套件安裝後，檢查：

```bash
sudo systemctl enable --now docker
sudo docker version
sudo docker info
sudo docker run --rm hello-world
sudo docker compose version
```

version 應同時有 Client / Server，hello-world 應輸出 Hello from Docker。daemon 未啟動先讀 `journalctl -u docker --since '10 minutes ago'`，不是重灌所有套件。

## 許可權與遷移

docker 群組等同可控制主機的重要許可權，開發帳號加入前先評估，不能以 chmod 666 socket 解決。Rootless mode 是不同部署路線，需要核對限制。舊 CentOS 8 移轉前備份 volume、Compose 檔、設定與映像來源，在新 VM 重建並做還原與連線驗證。

原先指定 docker-ce 的精確版本可能已不在 repo；應先列出可用版本、選擇相容修補版並保留記錄，而非加 `--allowerasing` 無條件移除其他套件。

## 參考資料

- [CentOS EOL](https://www.centos.org/centos-linux-eol/)
- [Docker CentOS 安裝](https://docs.docker.com/engine/install/centos/)
- [安裝後權限](https://docs.docker.com/engine/install/linux-postinstall/)
- [linux-docker.sock](https://stackoverflow.com/questions/48568172/docker-sock-permission-denied)
- [CentOS 8 install Docker - Pocket Admin](https://pocketadmin.tech/en/centos-8-install-docker/)
- [Docker - 第十三章 | 安裝Apache Server | J.J.'s Blogs](https://morosedog.gitlab.io/docker-20190601-docker13/)
