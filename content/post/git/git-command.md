---
title: "GitCommand"
date: 2021-07-14T09:21:29+08:00
draft: true
categories:
 - "筆記"
tags:
 - "git"
toc: true
---

## git command
<!-- 簡介 -->

紀錄 git command

<!--more-->

### git status  看目前訊息

取得目前 Git 工作目錄的狀態用這個指令可以取得當前目錄的版控狀態，例如有檔案被變更、刪除、新增或其他。

### git add   新增索引

( 將尚未被 Git 追蹤的新增檔案加進去 )來告知 git，哪些是我們將要 commit 的檔案
git add . : 把所有新增檔案與更新檔案加入編舞

git add若加上一個小數點 ( . ) 代表目前目錄，它會自動把所有尚未版控的檔案(Untracked files) 加入到 Git 的追蹤清單中，也代表這些檔案才會經由 Git 進行版本控管。

git add 檔案名.副檔名 : 

如果你只想把未控管 (Untracked) 的檔案加入，則必須指定檔名來加入。




## 參考
