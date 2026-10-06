---
title: "Windows 開發工具清單：用途與安裝後檢查"
date: 2021-10-06T09:12:56+08:00
draft: false
categories:
 - "筆記"
tags:
 - "windows"
toc: true
description: "將原裝機名單分類，補上重複功能取捨、來源與版本記錄。"
lastmod: 2026-10-07T00:01:00+08:00
---

將原裝機名單分類，補上重複功能取捨、來源與版本記錄。

<!--more-->

適用：受支援Windows開發環境的工具規劃；不代表每個產品都必裝或目前都免費。

## 按任務選工具

| 任務 | 原清單中的工具 | 安裝後檢查 |
| --- | --- | --- |
| 編輯與版控 | VS Code、Git、Fork | git version、editor與credential設定 |
| API除錯 | Postman | 本地測試API與環境秘密分離 |
| VM／開發環境 | Vagrant、VMware、VirtualBox | provider、CPU架構與虛擬化相容 |
| 網路診斷 | Wireshark | 驅動、capture許可權與合法測試介面 |
| 壓縮與文字 | 7-Zip、Notepad++ | 支援格式與UTF-8檔案 |
| 圖片／規劃 | Flameshot、XMind | 截圖快捷鍵與匯出能力 |
| 行動與語言 | Android Studio、Go | SDK與PATH按專案設定 |

Zoom、Notion、輸入法與CrystalDiskInfo屬於協作／習慣或硬體檢查，不和編譯工具混作Java專案依賴。Windows本身的截圖工具可能已經滿足需求，先確認需求再加軟體。

## 來源與固定版本

從原廠取得安裝包並核對簽章／校驗。使用winget等管理器先查packageId與來源，例如 `winget search --id Git.Git --exact`，確認後再安裝；可用`winget list`記錄環境。不要複製一串未核對的全域性安裝指令碼。

編輯器plugin與app分開維護，避免匯入陌生設定執行任意任務。JDK、Node和SDK按專案版本固定，不能靠裝「最新版所有工具」保證舊專案執行。安裝完記錄版本、完成一個本地build與復原步驟。

## 更新與取捨

原2021清單有拼字與產品命名變化，已修正Notepad++、Postman、VMware等名稱。價格、授權和OS支援會變，購買／部署前讀原廠當前條款。本篇提供用途清單，不聲稱所有軟體現時可直接無授權商用。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [VSCode](https://code.visualstudio.com/docs/setup/windows)
- [Git Windows](https://gitforwindows.org/)
- [Wireshark](https://www.wireshark.org/docs/)

### 原始筆記的其他連結

- [原始參考入口 1](https://github.com/flameshot-org/flameshot)
