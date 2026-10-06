---
title: "Vue 教學 00：學習路線與共用練習環境"
date: 2026-03-22T20:00:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "建立可重現的 Vue 3 練習專案，依基礎、元件、路由、狀態管理與工程化循序完成 31 個主題。"
lastmod: 2026-10-07T00:01:00+08:00
---

建立可重現的 Vue 3 練習專案，依基礎、元件、路由、狀態管理與工程化循序完成 31 個主題。

<!--more-->

適用：Vue 3 課程總覽。以下環境供全系列共用；不需要先有後端服務。

## 版本與先備知識

原筆記混合 Vue 3、Vuex 4、Options API 與 Composition API，這次保留各主題，統一練習使用 Vue 3.5。需先了解 JavaScript 陣列、模組、Promise 與 HTML 表單。Vue 2 已結束官方維護，Vuex 章保留作為既有系統維護對照，新專案先學 Pinia。

共用環境選 Node.js 22.12 以上的 22.x、npm、Vue 3.5、Vite 7、Vue Router 4、Pinia 3。這是明確的練習版本組合，不代表所有套件的最新版本；以 lockfile 固定實際安裝版本。

## 建立專案

在獨立的空資料夾建立以下檔案。

`package.json`：

```json
{
  "name": "vue-note-labs",
  "private": true,
  "type": "module",
  "scripts": {"dev": "vite", "build": "vite build", "preview": "vite preview"},
  "dependencies": {"vue": "~3.5.0", "vue-router": "^4.5.0", "pinia": "^3.0.0", "vuex": "^4.1.0"},
  "devDependencies": {"vite": "^7.0.0", "@vitejs/plugin-vue": "^6.0.0"}
}
```

`index.html`：

```html
<!doctype html>
<html lang="zh-Hant">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Vue 筆記練習</title></head>
<body><div id="app"></div><script type="module" src="/src/main.js"></script></body>
</html>
```

`vite.config.js`：

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig({ plugins: [vue()] })
```

`src/main.js`：

```javascript
import { createApp } from 'vue'
import App from './App.vue'
createApp(App).mount('#app')
```

先使用第 01 章的 `src/App.vue`，然後執行：

```bash
npm install
npm run dev
npm run build
```

瀏覽終端顯示的本機網址，應看到可點選的計數器；建置成功後產生 `dist/`。第一次安裝保留 `package-lock.json`，往後用 `npm ci` 重現。每次換章先移除上一章的特定檔案或使用不同資料夾，避免路由與 store 設定互相干擾。

## 閱讀順序

01–08 練模板與響應式；09–13 練元件邊界；14–25 練路由；26–27 比較 Pinia / Vuex；28–31 處理建置、動畫、SSR 與電影目錄。

- [01-Vue概述]({{< ref "/post/vue/vue-01-Vue概述.md" >}})
- [02-Vue-js基礎]({{< ref "/post/vue/vue-02-Vue-js基礎.md" >}})
- [03-列表渲染]({{< ref "/post/vue/vue-03-列表渲染.md" >}})
- [04-ref與reactive]({{< ref "/post/vue/vue-04-ref與reactive.md" >}})
- [05-watch監視屬性]({{< ref "/post/vue/vue-05-watch監視屬性.md" >}})
- [06-生命週期]({{< ref "/post/vue/vue-06-生命週期.md" >}})
- [07-自定義hooks]({{< ref "/post/vue/vue-07-自定義hooks.md" >}})
- [08-響應式進階整理]({{< ref "/post/vue/vue-08-響應式進階整理.md" >}})
- [09-元件化]({{< ref "/post/vue/vue-09-元件化.md" >}})
- [10-Composition-API]({{< ref "/post/vue/vue-10-Composition-API.md" >}})
- [11-元件通訊與Pinia]({{< ref "/post/vue/vue-11-元件通訊與Pinia.md" >}})
- [12-元件通訊進階]({{< ref "/post/vue/vue-12-元件通訊進階.md" >}})
- [13-Vue3進階實務整理]({{< ref "/post/vue/vue-13-Vue3進階實務整理.md" >}})
- [14-路由核心概念]({{< ref "/post/vue/vue-14-路由核心概念.md" >}})
- [15-路由基本接線]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})
- [16-Vue-Router基礎]({{< ref "/post/vue/vue-16-Vue-Router基礎.md" >}})
- [17-to的兩種寫法]({{< ref "/post/vue/vue-17-to的兩種寫法.md" >}})
- [18-history與hash模式]({{< ref "/post/vue/vue-18-history與hash模式.md" >}})
- [19-命名與巢狀路由]({{< ref "/post/vue/vue-19-命名與巢狀路由.md" >}})
- [20-路由元件生命週期]({{< ref "/post/vue/vue-20-路由元件生命週期.md" >}})
- [21-路由傳參query與params]({{< ref "/post/vue/vue-21-路由傳參query與params.md" >}})
- [22-路由props配置]({{< ref "/post/vue/vue-22-路由props配置.md" >}})
- [23-replace屬性]({{< ref "/post/vue/vue-23-replace屬性.md" >}})
- [24-程式設計式導航]({{< ref "/post/vue/vue-24-程式設計式導航.md" >}})
- [25-Vue-Router進階]({{< ref "/post/vue/vue-25-Vue-Router進階.md" >}})
- [26-Pinia集中式狀態管理]({{< ref "/post/vue/vue-26-Pinia集中式狀態管理.md" >}})
- [27-Vuex狀態管理]({{< ref "/post/vue/vue-27-Vuex狀態管理.md" >}})
- [28-Vite工具]({{< ref "/post/vue/vue-28-Vite工具.md" >}})
- [29-Vue動畫]({{< ref "/post/vue/vue-29-Vue動畫.md" >}})
- [30-SSR服務端渲染]({{< ref "/post/vue/vue-30-SSR服務端渲染.md" >}})
- [31-實戰doubanmovie]({{< ref "/post/vue/vue-31-實戰doubanmovie.md" >}})

## 如何判斷學會了

每章先執行範例，再修改一個輸入觀察結果，最後故意移除一個必要設定並說明錯誤原因。`npm run build` 只證明能產生資源，不代表 API、授權或正式站路由正確，部署後仍需測試直接開啟子路徑。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [下一章]({{< ref "/post/vue/vue-01-Vue概述.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Vue 快速開始](https://vuejs.org/guide/quick-start.html)
- [Vite 環境需求](https://vite.dev/guide/)
- [Vuex 與 Pinia 的關係](https://vuex.vuejs.org/)
