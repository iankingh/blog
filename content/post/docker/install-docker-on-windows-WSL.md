---
title: "Windows WSL 2 與 Docker：安裝前檢查及錯誤排除"
date: 2021-06-16T17:10:10+08:00
categories:
 - "筆記"
tags:
 - "windows"
 - "docker"
toc: true
draft: false
description: "保留 0x80370102 與 0xc03a001a 情境，補上虛擬化、WSL 狀態與 Docker 整合的診斷順序。"
lastmod: 2026-10-07T20:50:40+08:00
---

保留 0x80370102 與 0xc03a001a 情境，補上虛擬化、WSL 狀態與 Docker 整合的診斷順序。

<!--more-->

適用：Windows 的 WSL 2 與 Docker Desktop。原錯誤記錄屬於舊版 WSL，以下使用狀態檢查與官方排錯路線；本次 macOS 未實機重現。

## 安裝前確認

使用支援 WSL 2 的 Windows 10/11 與目前 Docker Desktop 支援的版本。以系統管理員 PowerShell 檢查：

```powershell
wsl --status
wsl --version
wsl --list --verbose
```

舊 WSL 可能不認識 --version，先按官方更新路線確認，不表示 Linux distribution 壞掉。首次安裝依 Microsoft 檔案執行 `wsl --install`，完成後可能需重新啟動。Docker Desktop 選 WSL 2 backend 並啟用指定 distribution 的 integration。

## 錯誤診斷

`0x80370102` 先檢查 UEFI/BIOS 虛擬化、Windows Virtual Machine Platform 與重新啟動；若 Windows 本身在 VM，主機還需允許 nested virtualization。不要看到錯誤就先 unregister distribution，該動作會刪資料。

`0xc03a001a` 常與虛擬磁碟檔案被壓縮／加密或所在磁碟屬性有關。原筆記以取消 AppData 目錄壓縮處理，但不同 Store/WSL 版本的資料位置不同；先依實際錯誤和官方排錯查出 VHD 位置，備份後調整相關屬性，不修改整個使用者目錄。

## 確認 Docker

在已啟用整合的 Linux shell 執行：

```bash
docker version
docker run --rm hello-world
```

應有 Server 資訊與 Hello from Docker。若只有 Windows 終端正常、WSL 不正常，檢查 integration 與 PATH。檔案大量 IO 的專案可放在 Linux 檔案系統，再從 VS Code Remote WSL 操作，避免把差異誤判為容器效能。

## 參考資料

- [WSL 安裝](https://learn.microsoft.com/en-us/windows/wsl/install)
- [WSL 排錯](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Docker WSL backend](https://docs.docker.com/desktop/features/wsl/)
- [wsl2的Error 0x80370102 解決方案 - 知乎](https://zhuanlan.zhihu.com/p/147233604)
- [安裝WSL2子系統出現 0xc03a001a錯誤 - 清晨小農夫](https://rdfarm.net/wsl2-error-0xc03a001a/)
- [使用 WSL 2 打造優質的多重 Linux 開發環境 | The Will Will Web](https://blog.miniasp.com/post/2020/07/26/Multiple-Linux-Dev-Environment-build-on-WSL-2)
