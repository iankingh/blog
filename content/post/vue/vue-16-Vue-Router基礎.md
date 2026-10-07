---
title: "Vue 教學 16：匹配、重新導向與找不到頁面"
date: 2026-03-22T20:16:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "在共用骨架加入任務頁、重新導向與 404，檢查路由匹配的完整行為。"
lastmod: 2026-10-07T20:50:40+08:00
---

在共用骨架加入任務頁、重新導向與 404，檢查路由匹配的完整行為。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 擴充 routes

建立 `src/views/NotFound.vue`：

```vue
<template><h1>找不到這個任務</h1><RouterLink to="/">回首頁</RouterLink></template>
```

在第 15 章 router.js 匯入 NotFound，將 routes 改為：

```javascript
const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/about', name: 'about', component: About },
  { path: '/start', redirect: { name: 'home' } },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound }
]
```

將 createRouter 裡的 `routes: [...]` 改為 `routes`。開啟 `#/start` 應轉到首頁；開 `#/missing` 應顯示找不到任務。catch-all 是 Router 4 寫法，不能使用 Router 3 的單獨 `*` 路徑。

## active class 與導向

RouterLink 會為符合紀錄的連結加入 active class，巢狀頁面可能使父連結也 active；只要完全相符用 exact-active-class。redirect 改變目的地，alias 則讓不同網址對應同一紀錄且保留使用者輸入的網址。

SPA 顯示 404 元件不代表伺服器回應 HTTP 404，SEO 或 SSR 需要後端配合。這份入門骨架使用 hash，只展示前端狀態；部署回應碼另行驗證。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-15-路由基本接線.md" >}}) · [下一章]({{< ref "/post/vue/vue-17-to的兩種寫法.md" >}})

## 參考資料

- [重新導向與別名](https://router.vuejs.org/guide/essentials/redirect-and-alias.html)
- [路由匹配](https://router.vuejs.org/guide/essentials/route-matching-syntax.html)
- [Active links](https://router.vuejs.org/guide/essentials/active-links.html)
- [範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
