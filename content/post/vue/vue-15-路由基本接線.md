---
title: "Vue 教學 15：建立可運作的路由骨架"
date: 2026-03-22T20:15:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "提供入口、路由器、兩個頁面與展示區的完整檔案，作為後續路由章節的基礎。"
lastmod: 2026-10-07T20:50:40+08:00
---

提供入口、路由器、兩個頁面與展示區的完整檔案，作為後續路由章節的基礎。

<!--more-->

適用：Vue 3 與 Vue Router 4。先建立第 00 章練習專案，以下檔案取代其入口與 App.vue。

## 建立必要檔案

`src/views/Home.vue`：

```vue
<template><h1>首頁任務</h1></template>
```

`src/views/About.vue`：

```vue
<template><h1>關於冒險者</h1></template>
```

`src/router.js`：

```javascript
import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/about', name: 'about', component: About }
  ]
})
```

`src/main.js`：

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
createApp(App).use(router).mount('#app')
```

`src/App.vue`：

```vue
<template>
  <nav><RouterLink to="/">首頁</RouterLink> | <RouterLink to="/about">關於</RouterLink></nav>
  <RouterView />
</template>
```

## 確認結果

啟動 Vite 後首頁顯示「首頁任務」，點關於顯示「關於冒險者」，網址結尾變成 `#/about`。返回鍵回到首頁。這裡先用 hash，避免初學時同時處理伺服器 rewrite。

`Failed to resolve component: RouterLink` 通常是沒有 app.use(router)；導航有效但內容空白先看 RouterView 與 component 匯入路徑。檔名在 Linux 區分大小寫，本機能運作的 Home/home 差異可能在部署時失敗。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-14-路由核心概念.md" >}}) · [下一章]({{< ref "/post/vue/vue-16-Vue-Router基礎.md" >}})

## 參考資料

- [路由快速開始](https://router.vuejs.org/guide/)
- [Router 安裝](https://router.vuejs.org/installation.html)
