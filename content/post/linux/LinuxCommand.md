---
title: "Linux 基礎指令：路徑、檔案與許可權"
date: 2020-06-22T19:01:50+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Linux"
toc: true
description: "修正 HOME 變數與 chmod 範例，以明確檔案展示讀寫及執行許可權。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正 HOME 變數與 chmod 範例，以明確檔案展示讀寫及執行許可權。

<!--more-->

適用：Linux 的 Bash 與 GNU coreutils；以下在可丟棄資料夾練習。

## 路徑與檔案

```bash
mkdir linux-note-lab
cd linux-note-lab
pwd
printf 'hello\n' > note.txt
ls -la
cat note.txt
cp note.txt backup.txt
mv backup.txt copied.txt
```

應得到兩個內容為 hello 的文字檔。`pwd` 是目前目錄，`cd "$HOME"` 回家目錄；Linux 環境變數區分大小寫，`$home` 一般不是 HOME。

## 許可權

```bash
chmod 644 note.txt
ls -l note.txt
printf '#!/bin/sh\nprintf "ready\\n"\n' > run.sh
chmod 755 run.sh
./run.sh
```

644 表示 owner 可讀寫、group/others 可讀；755 的執行檔 owner 可讀寫執行，其他人讀與執行。目錄的 x 表示可穿越，不等於檔案執行。ACL、SELinux、掛載選項仍可能影響訪問，不只看這九個 bit。

不要把 chmod -R 777 當許可權修復，先確認 `id`、檔案擁有者、群組與目的。sudo 只在需要時對特定操作使用。檢視磁碟用 `df -h`、目錄大小用 `du -sh 目錄`，兩者統計不同。

確認後只清除自己建立的練習資料，rm 不經回收桶；不在不明目前目錄執行遞迴刪除。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [GNU chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)
- [GNU 檔案操作](https://www.gnu.org/software/coreutils/manual/html_node/Basic-operations.html)
