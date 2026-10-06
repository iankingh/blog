---
title: "CentOS Linux 8 安裝紀錄：VM 流程與 EOL 說明"
date: 2020-06-29T08:51:38+08:00
categories:
 - "筆記"
tags:
 - "Linux"
 - "CentOS"
toc: true
draft: false
description: "補齊原本空白的安裝章節，採 VM 說明磁碟、網路與帳號設定，標示替代發行版。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊原本空白的安裝章節，採 VM 說明磁碟、網路與帳號設定，標示替代發行版。

<!--more-->

適用：CentOS Linux 8 的歷史安裝情境。該版本已結束維護；本篇用於理解舊系統，不建議新服務繼續部署。

## 準備與版本選擇

CentOS Linux 8 的 EOL 日期為 2021-12-31。新環境可評估 CentOS Stream、Rocky Linux 或 AlmaLinux，但它們不是原 CentOS Linux 8 的相同發布模式，需依硬體、套件相容性與供應商支援選擇。

在隔離 VM 準備專用虛擬磁碟、ISO、網路與足夠記憶體／磁碟。ISO 從發行版官方來源取得，核對其 SHA-256 與簽章。原筆記的 dd USB 操作易選錯實體磁碟，本篇以掛載 ISO 的 VM 流程取代，不涉及主機磁碟覆寫。

## 安裝順序

1. 由 ISO 開機，選 Install，設定語言與鍵盤。
2. 在 Installation Summary 選目的磁碟，確認只選 VM 的專用磁碟；初學採自動分割，手動分割先規劃 `/`、boot 與所需 swap。
3. 選時區、同步時間、設定 hostname 與網絡卡；確認 DHCP 或靜態地址符合所在網段。
4. 選擇軟體組合，如 Minimal Install。建立具管理許可權的一般帳號，設定強密碼。
5. 開始安裝，完成後解除安裝 ISO 並重開，避免又進安裝畫面。

## 開機確認

```bash
cat /etc/os-release
lsblk
ip address
ip route
 timedatectl
systemctl --failed
```

應從硬碟進系統，根目錄掛在預期虛擬磁碟、網路地址／default route正確、沒有意外失敗服務。若無網路先看網絡卡狀態與VM NAT/bridge，再檢查DNS，不先換掉所有repo。

Cockpit 若實際需要，依受支援系統的套件檔案安裝並只向管理網段開放；不要因筆記有一個命令就在歷史系統上公開9090。舊系統遷移先備份、另建新VM還原與測試，保留回復路線。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [CentOS Linux EOL](https://www.centos.org/centos-linux-eol/)
- [CentOS Stream](https://www.centos.org/centos-stream/)
- [Rocky 文件](https://docs.rockylinux.org/)
- [AlmaLinux 文件](https://wiki.almalinux.org/)

### 原始筆記保留的來源

- [參考 Red Hat swap 建議](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_storage_devices/getting-started-with-swap_managing-storage-devices#recommended-system-swap-space_getting-started-with-swap)
- [Cockpit](https://cockpit-project.org/)

### 原始筆記的其他連結

- [原始參考入口 1](https://iter01.com/443455.html)
- [原始參考入口 2](https://linoxide.com/distros/how-to-install-centos/)
- [原始參考入口 3](https://www.footmark.info/linux/centos/centos8-installation/)
