---
title: "Vue 教學 28：Vite 建置、環境變數與資源路徑"
date: 2026-03-22T20:28:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "補齊 Vite 專案設定，區分開發服務、正式建置與公開環境變數。"
lastmod: 2026-10-07T20:50:40+08:00
---

補齊 Vite 專案設定，區分開發服務、正式建置與公開環境變數。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 建置流程

沿用第 00 章專案。`npm run dev` 提供開發轉換與 HMR；`npm run build` 產生 dist；`npm run preview` 僅用於本機檢查建置成果，不是正式維運服務。

建立 `.env.development`：

```dotenv
VITE_API_BASE=/mock
```

App.vue 可檢查環境：

```vue
<script setup>
const base = import.meta.env.VITE_API_BASE ?? '/api'
const mode = import.meta.env.MODE
</script>
<template><p>環境 {{ mode }}，API {{ base }}</p></template>
```

開發顯示 development／mock；沒有 `.env.production` 的 production 建置使用 `/api`。變更 env 後重啟開發 server。`VITE_` 字首會進入客戶端 bundle，不能存放密碼或私鑰。

## Proxy 與資源

若本機後端在 8080，vite.config.js 的 defineConfig 內可加入：

```javascript
const server = {
  proxy: { '/api': { target: 'http://127.0.0.1:8080', changeOrigin: true } }
}
```

再把 server 加入設定物件；只在開發服務生效，正式站臺需反向代理或 API 的 CORS 設定。此片段不是會自動啟動後端的設定。

`src/assets` 的匯入資源可參與雜湊與打包；public 下檔案保持名稱直接複製。部署到子路徑時設 base，模板中處理 public 路徑可用 `import.meta.env.BASE_URL`。Vite 7 練習環境使用 Node 22.12 以上；舊筆記使用其他 Vite major 時先核對 engine，而非直接升級 Node/外掛全部套件。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-27-Vuex狀態管理.md" >}}) · [下一章]({{< ref "/post/vue/vue-29-Vue動畫.md" >}})

## 參考資料

- [Vite 入門](https://vite.dev/guide/)
- [環境變數](https://vite.dev/guide/env-and-mode.html)
- [正式建置](https://vite.dev/guide/build.html)
- [開發 proxy](https://vite.dev/config/server-options.html#server-proxy)
