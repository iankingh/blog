---
title: "技術提問：重現步驟、預期結果與診斷證據"
date: 2023-06-30T07:38:52+08:00
categories:
- "筆記"
tags:
- "問問題"
toc: true
draft: false
description: "保留原提問與除錯主題，整理成可複製模板，移除難以辨識來源的個人經驗敘事。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留原提問與除錯主題，整理成可複製模板，移除難以辨識來源的個人經驗敘事。

<!--more-->

適用：向團隊、issue tracker與技術社群提問；先依對方的issue模板填寫。

## 提問模板

```text
目的：我想完成的操作／結果
環境：OS、框架與工具版本、最小依賴
重現步驟：從乾淨環境開始的可重做順序
預期：具體應看到的輸出
實際：實際輸出、完整錯誤與關鍵堆疊
已查資料：來源與我理解的結論
已試方法：每次只改什麼、結果如何
目前假設：認為失敗在哪一層、希望釐清的問題
```

不要只貼「不能動」，也不要把整個公司專案含秘密丟上網。以最小程式、去識別化資料與可複製文字提供證據，截圖用來顯示佈局，不取代錯誤文字。

## 一個具體例子

「本機Vue Router4使用history，點/about正常，但直接重新整理Tomcat上的/task-app/about回404。base-href為/task-app/，JS首頁200；已確認後端API不走這條路徑。應如何設此應用的fallback？」比「Angular/Vue部署壞了」更能讓他人診斷。

## 搜尋與溝通

搜尋使用完整錯誤、實際版本和產品名稱，先讀官方文件與issue的日期，避免套用不同major。保留自己的猜測但不把它當已證實事實，對方能先檢查前提。

問設計理由可用「目前理解是X，這裡採Y是為了哪些限制」，不需要先稱讚來交換回答。回報修復方法、驗證結果與適用版本，讓後續讀者受益。原筆記中的training故事無法辨識是否作者或轉貼，改為一般實踐，不新增個人經歷。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [How to Ask Questions 原文](http://www.catb.org/~esr/faqs/smart-questions.html)
- [Stack Overflow minimal example](https://stackoverflow.com/help/minimal-reproducible-example)

### 原始筆記保留的來源

- [如何用 ORID 提問框架，記錄心得、回顧發現、內化學習｜ALPHA Camp Blog](https://tw.alphacamp.co/blog/orid-objective-reflective-interpretive-decisional)
- [ryanhanwu/How-To-Ask-Questions-The-Smart-Way: 本文原文由知名 Hacker Eric S. Raymond 所撰寫，教你如何正確的提出技術問題並獲得你滿意的答案。 (github.com)](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)
