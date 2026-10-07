---
title: "AI 工具清單：聊天、搜尋與翻譯"
description: "依用途比較聊天、搜尋與翻譯工具，說明來源查核、資料範圍與使用限制。"
date: 2024-07-02T20:47:15+08:00
lastmod: 2026-10-07T20:50:40+08:00
categories:
- "筆記"
tags:
- "AI"
- "Tools"
toc: true
draft: false
---

依用途比較聊天、搜尋與翻譯工具，說明來源查核、資料範圍與使用限制。

<!--more-->

適用：原2024工具清單在2026的內容整理；產品功能、可用模型與額度會變，依官方入口確認，不列未查證價格或保證效果。

## 工具入口與用途

| 工具 | 本篇保留的用途 | 使用時確認 |
| --- | --- | --- |
| [Monica](https://monica.im/) | 聊天、寫作與瀏覽器助理 | 擴充許可權、資料來源與帳號設定 |
| [Poe](https://poe.com/) | 透過平臺使用不同bot | bot建立者、模型來源與限額 |
| [Phind](https://www.phind.com/) | 原 2024 筆記中的技術搜尋工具 | 本次入口回傳 404，保留歷史參考 |
| [Felo](https://felo.ai/) | 搜尋與資料整理 | 原始來源、地域／語言與可用功能 |
| [沉浸式翻譯](https://immersivetranslate.com/) | 雙語閱讀與檔案翻譯 | 翻譯引擎、原文與上傳範圍 |

2026-10-06 查核 Phind 官方首頁時回傳 HTTP 404；本篇保留原始來源，無法確認現行服務是否可用，也不以搜尋快取推定營運狀態。其他工具未登入測試帳號功能。

原Sage／Claude+等模型名反映當時平臺，不當現行可用清單；產品入口能開啟也不表示每個功能都無帳號／免費可用。

## 同一問題如何比較

用一個不含秘密的技術問題，例如「Vue Router4 history模式部署到子路徑後重新整理404」，要求列出具體原因、適用版本與官方來源。逐個開啟來源核對，自己在本地測最小例子，不只比較回答流暢度。

搜尋工具的引用也可能過期／誤解；翻譯保持原文對照，API名稱、not／should等關鍵限制要回原文檢查。程式碼建議必須經過build與行為測試，不能將平臺的自信語氣當結果。

## 清單與專案的分工

這篇是工具索引，不叫外掛集也不收納可執行skill／agent。未來AI-tools repository可分別記錄安裝、許可權、輸入輸出與驗證；取得確認的真實repository地址後再加blog連結，不虛構尚未建立的專案URL。

## 資料與限制

需要帳號／外部服務的操作本次未登入或提交資料。先檢查擴充會讀取哪些頁面、檔案如何處理，再決定是否用於工作資料；使用自製假資料作比較，保留prompt與日期讓結果可追溯。

## 參考資料

- [Monica官方](https://monica.im/)
- [Poe官方](https://poe.com/)
- [Phind官方](https://www.phind.com/)
- [Felo官方](https://felo.ai/)
- [沉浸式翻譯官方](https://immersivetranslate.com/)
- [原始參考入口 1](https://monica.im/home)
- [原始參考入口 2](https://poe.com/ChatGPT)
- [原始參考入口 3](https://www.phind.com/search?home=true)
- [原始參考入口 4](https://felo.ai/search)
