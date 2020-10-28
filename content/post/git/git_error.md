---
title: "Git_error"
date: 2020-10-06T21:45:42+08:00
draft: true
categories:
 - "筆記"
tags:
 - "git"
toc: true
---
# git error筆記
<!--more-->

當 git pull  出現

```
error: Your local changes to the following files would be overwritten by merge:
```

意思是本地新修改的程式碼檔案，將會被git伺服器上的程式碼覆蓋

解決發法如下：

**方法1**：如果你想保留剛才本地修改的程式碼，並把git伺服器上的程式碼pull到本地（本地剛才修改的程式碼將會被暫時封存起來）

```
git stash 
git pull origin master
git stash pop
```

1. 使用 `pop` 指令，可以把某個 Stash 拿出來並套用在目前的分支上。套用成功之後，那個套用過的 Stash 就會被刪除。

**方法2**、如果你想完全地覆蓋本地的程式碼，只保留伺服器端程式碼，則直接回退到上一個版本，再進行pull：

git reset --hard
git pull origin master

注：其中origin master表示git的主分支。

**方法3** 




參考

git pull遇到錯誤：error: Your local changes to the following files would be overwritten by merge:解決方法

https://www.itread01.com/content/1545046022.html

【狀況題】手邊的工作做到一半，臨時要切換到別的任務 - 為你自己學 Git | 高見龍

https://gitbook.tw/chapters/faq/stash.html