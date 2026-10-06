---
title: "Windows MongoDB：免安裝配置與 mongosh 確認"
date: 2023-07-30T22:37:01+08:00
categories:
- "筆記"
tags:
- "MongoDB"
- "NoSQL"
toc: true
draft: false
description: "保留 ZIP 安裝情境，補上有效 YAML、資料目錄、localhost 與 shell 測試。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 ZIP 安裝情境，補上有效 YAML、資料目錄、localhost 與 shell 測試。

<!--more-->

適用：MongoDB Community 8.x的Windows本地練習；使用前查所選版本支援的Windows與CPU，原舊版安裝路徑僅作對照。

## 下載與配置

從官方下載ZIP，解壓到獨立目錄，另安裝mongosh；mongod是伺服器，mongosh是client，不一定在同一安裝包。建立C:\mongo-note\data與logs，儲存C:\mongo-note\mongod.cfg：

```yaml
storage:
  dbPath: C:\mongo-note\data
systemLog:
  destination: file
  path: C:\mongo-note\logs\mongod.log
  logAppend: true
net:
  bindIp: 127.0.0.1
  port: 27017
```

以實際mongod.exe完整路徑執行：

```powershell
& 'C:\mongodb\bin\mongod.exe' --config 'C:\mongo-note\mongod.cfg'
mongosh 'mongodb://127.0.0.1:27017'
```

第一個終端保持伺服器執行，第二個開shell。若路徑不同先改成實際位置；原配置勿混用舊版本過時storage選項。

## Shell 練習

```javascript
use note_lab
db.runCommand({ ping: 1 })
db.tasks.insertOne({ title: '整理筆記', done: false })
db.tasks.find({ done: false })
```

ping回ok:1，insert回acknowledged:true，find可見任務。`use note_lab`是mongosh命令，不是一般Node程式；資料庫會在實際寫入後建立。

## 排錯與範圍

瀏覽器開27017不是有效資料庫操作驗證，改用mongosh。啟動失敗先查log、dbPath存在和許可權、port衝突，不能任意刪除data。新版升級需按官方upgrade path，資料目錄不能直接拿舊binary降版使用。

此設定只有loopback、本地無認證練習；正式網路服務必須按官方設身分驗證、許可權與備份，不能只把bindIp改0.0.0.0。Ctrl+C停本地foreground程式，資料目錄保留，不宣稱已建立Windows service。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [MongoDB Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
- [Configuration options](https://www.mongodb.com/docs/manual/reference/configuration-options/)
- [mongosh](https://www.mongodb.com/docs/mongodb-shell/)

### 原始筆記保留的來源

- [MongoDB Community Downloads | MongoDB](https://www.mongodb.com/download-center/community/releases)
- [MongoDB免安裝版安裝_java後端指南的部落格-CSDN部落格](https://blog.csdn.net/Ting1king/article/details/124757490)
- [windowns免安裝MongoDB_windows免安裝mongodb_花哥碼天下的部落格-CSDN部落格](https://blog.csdn.net/qq_39940205/article/details/120434224)
- [Day17 - MongoDB 安裝設定 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天 (ithome.com.tw)](https://ithelp.ithome.com.tw/articles/10186324)
