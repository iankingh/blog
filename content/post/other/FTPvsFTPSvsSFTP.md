---
title: "FTP、FTPS 與 SFTP：協定和連線埠差異"
date: 2023-07-27T18:55:20Z
categories:
- "筆記"
tags:
- "FTP"
- "FTPS"
- "SFTP"
toc: true
draft: false
description: "修正主動／被動模式的方向及 FTPS 分類，提供連線選擇與診斷依據。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正主動／被動模式的方向及 FTPS 分類，提供連線選擇與診斷依據。

<!--more-->

適用：檔案傳輸協定比較；實際port由服務端配置，不以預設值代替檢查。

## 比較

| 協定 | 保護機制 | 常見控制連線 | 額外資料連線 |
| --- | --- | --- | --- |
| FTP | 預設明文 | TCP21 | 主動或被動模式 |
| FTPS explicit | FTP升級TLS（AUTH TLS） | TCP21 | 仍有FTP資料通道 |
| FTPS implicit | 連線即TLS | 通常TCP990 | 仍需配置資料通道 |
| SFTP | SSH | 通常TCP22 | 一般使用同一SSH連線 |

SFTP不是「FTP加SSL」，和FTPS不能互換client設定。FTPS區分explicit／implicit，不是安全／明文模式；資料通道是否TLS還需正確PROT等設定。

## 主動與被動

FTP控制由client連server21。主動模式資料連線由server（通常來源20）連到client宣告的port；被動模式server提供一個資料port，由client去連。原文把方向寫反已修正。NAT與防火牆下常用被動模式，server需設定可達地址與被動port範圍。

只放行21不保證能傳檔，列目錄也可能使用資料通道；自訂50000–50010不是FTPS固定協定port。應同時核對server、防火牆與client模式。

## 選擇與確認

SSH生態中的檔案交換可採SFTP，企業既有FTP流程可依需求支援FTPS。首次連線核對SSH host key或TLS憑證，不能接受未知fingerprint或關掉驗證作永久方案。

測試登入、列目錄、上傳小檔、下載並核對checksum及許可權。SFTP的`put`/`get`與遠端shell命令不同，使用受控測試目錄而非覆蓋正式資料。傳輸加密不等於儲存加密、備份或檔案內容可信。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [FTP RFC959](https://www.rfc-editor.org/rfc/rfc959)
- [FTP over TLS RFC4217](https://www.rfc-editor.org/rfc/rfc4217)
- [OpenSSH sftp](https://man.openbsd.org/sftp)

### 原始筆記保留的來源

- [SFTP, FTP與FTPS - HackMD](https://hackmd.io/tBJORR5_R7mNTMnijUlOfw?both)
