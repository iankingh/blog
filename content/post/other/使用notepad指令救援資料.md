---
title: "Windows 修復環境複製資料：Notepad 與磁碟辨識"
date: 2021-03-15T09:50:02+08:00
categories:
 - "筆記"
tags:
 - "windows"
 - "other"
toc: true
draft: false
description: "保留 WinRE 檔案對話方塊的操作情境，區分一般檔案複製與真正故障磁碟救援。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 WinRE 檔案對話方塊的操作情境，區分一般檔案複製與真正故障磁碟救援。

<!--more-->

適用：可進WinRE／安裝媒體命令提示字元且磁碟仍可讀取的Windows；本次未操作故障磁碟。

## 適用範圍

Notepad的開啟檔案對話方塊可作簡單檔案瀏覽與複製，不會修復壞軌或保證恢復已刪資料。磁碟持續異響、頻繁讀取錯誤或重要唯一資料時，應避免反覆讀寫，先制定映像／專業恢復策略。

## 確認磁碟

從Windows復原環境的疑難排解→進階選項→命令提示字元進入；舊F8快捷鍵不保證在現代快速啟動系統有效。WinRE磁碟代號可能不同於平常，先確認來源與外接目的磁碟，不用格式化／clean操作。

```cmd
notepad
```

選檔案→開啟，檔案型別切所有檔案，瀏覽來源的使用者資料；複製需要的檔案到外接磁碟。不要按儲存覆蓋來原始檔。如果磁碟使用BitLocker，需持有合法復原金鑰才能解鎖，Notepad不能繞過加密。

## 確認結果

外接磁碟需足夠容量與支援檔案大小；FAT32單檔4GB上限可能阻礙大型檔案。複製後在另一臺正常電腦開啟代表檔案、核對數量／大小，重要檔案比對checksum；對話方塊顯示完成不代表全部內容無損。

來源讀取失敗先記錄檔名與錯誤，不反覆執行chkdsk /f或其他會寫入磁碟的修復當資料備份第一步。這篇操作只涵蓋可讀檔案搬移，不能宣稱為通用壞軌資料救援工具。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Windows RE](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference)
- [BitLocker recovery](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/recovery-overview)
