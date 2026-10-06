---
title: "Vue 教學 18：history、hash 與部署基底"
date: 2026-03-22T20:18:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "說明兩種網址模式、子目錄部署與重新整理 404 的修正方式。"
lastmod: 2026-10-07T00:01:00+08:00
---

說明兩種網址模式、子目錄部署與重新整理 404 的修正方式。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 切換模式

第 15 章使用 createWebHashHistory。要改為乾淨網址，在 router.js 替換 import 與 history：

```javascript
import { createRouter, createWebHistory } from 'vue-router'
// 保留既有 routes 與頁面匯入
const history = createWebHistory(import.meta.env.BASE_URL)
```

將 createRouter 的 history 欄位設為上述 history。若部署在 `/demo/`，Vite 設 `base: '/demo/'`，Router 使用 BASE_URL，資源路徑與導航基底才能一致。

## Nginx 部署示意

建置後把 dist 放在 `/srv/www/demo/`，Nginx 在對應的 server 區塊設定：

```nginx
location /demo/ {
    root /srv/www;
    try_files $uri $uri/ /demo/index.html;
}
```

修改前用 `nginx -t` 檢查，通過才 reload。以直接開啟 `/demo/about`、重新整理及請求 JS/CSS 檢查，應顯示關於頁且資源回應正確。API 需獨立 location，避免把 API 錯誤回成 index.html。

## 選擇比較

hash 的 `#` 後內容不送給伺服器，通常不需 fallback，適合無 rewrite 控制的靜態空間；history 有較自然的網址但需要主機配合。GitHub Pages 專案頁需額外路由策略，不能只在開發 server 成功就視為部署完成。Memory history 用於 SSR 或測試，不會自行更新瀏覽器網址。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-17-to的兩種寫法.md" >}}) · [下一章]({{< ref "/post/vue/vue-19-命名與巢狀路由.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [History 模式](https://router.vuejs.org/guide/essentials/history-mode.html)
- [Vite public base](https://vite.dev/guide/build.html#public-base-path)
- [Nginx try_files](https://nginx.org/en/docs/http/ngx_http_core_module.html#try_files)
