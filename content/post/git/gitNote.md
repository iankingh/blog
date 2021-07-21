---
title: "GitNote"
date: 2021-07-13T22:07:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
toc: true
---

## git 實戰用法
<!-- 簡介 -->

紀錄一些 git 用法

<!--more-->



### git status

看目前訊息
取得目前 Git 工作目錄的狀態用這個指令可以取得當前目錄的版控狀態，例如有檔案被變更、刪除、新增或其他。

### 把檔案push 到遠端儲存庫

1. git remote add origin 遠端儲存庫URL  新增遠端儲存庫到本地
2. git push --set-upstream origin master  建立連結
3. git push -u origin master(分支)  發布分支(簡寫)


git reset -p 修改索引---用途:避免本地設定檔上傳

git push --tags ....> 推送tag

### 回復到上一個（或更前的）版本

git reset --hard HEAD 回復到最新提交版本
git reset --hard HEAD~ // 等於 ~1 回復到上一個提交版本
git reset --hard HEAD~n // n 等於往上第幾個提交版本 回復之前指定的提交版本



## 參考
