---
title: "Chrome DevTools Overrides：本地模擬回應與保留修改"
date: 2021-04-11T19:11:37+08:00
categories:
 - "筆記"
tags:
 - "net"
 - "chrome"
toc: true
draft: false
description: "補上建立 override、確認生效和停用流程，區分 DOM 修改與真正來源檔案。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上建立 override、確認生效和停用流程，區分 DOM 修改與真正來源檔案。

<!--more-->

適用：Chrome DevTools近期版本的Local Overrides；不同版本選單名稱可能略有差異。本次以檔案核對流程，未修改外部服務。

## 操作步驟

開啟一個可測的本地頁面，DevTools → Network選回應，右鍵Override content／headers。首次選擇本機資料夾並允許DevTools存取；也可從Sources → Overrides配置。修改內容並儲存，再重新載入。

對JSON回應可把任務清單改為空陣列，核對UI空狀態；對CSS可改間距，確認重新整理仍保留。Network的override標記表示回應被替換，應記錄原內容與改動用於復原。

## 與其他功能的區別

Elements臨時改DOM通常不會被Overrides儲存；由HTML內嵌CSS的Styles修改也有不同限制，應編輯對應來源內容。Workspaces是對映實際原始來源並儲存，Overrides是取代瀏覽器讀到的網路回應，不會改伺服器。

開啟Overrides時DevTools會停用cache，效能測試要記錄此影響。source-mapped資源可能需操作實際network原始檔，不直接在對映後的來源點選就認為伺服器內容改變。

## 確認與清理

關閉Enable Local Overrides後重新整理，確認回到原回應；測試結論明確標註模擬資料與真實服務差異。不要用修改Authorization／CORS回應頭的本地模擬宣稱後端許可權已修復，實際伺服器仍需正確設定。

可用於介面尚未完成時測試UI，但變更只影響自己的瀏覽器；要團隊重現需將假資料與測試server存專案，而非只交截圖。override資料夾可能存實際響應，注意不包含秘密或個人資料。

## 參考資料

- [Chrome Overrides](https://developer.chrome.com/docs/devtools/overrides/)
- [Chrome Workspaces](https://developer.chrome.com/docs/devtools/workspaces/)
- [Chrome Dev Tool 的好用功能 - overrides](https://pvencs.blogspot.com/2019/01/chrome-dev-tool-overrides.html)
- [原始參考入口 1](https://developer.chrome.com/blog/new-in-devtools-65/#overrides)
