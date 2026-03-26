---
title: "Vue 教學 15 - 路由基本接線"
date: 2026-03-22T20:15:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue Router"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Vue3 路由基本接線

## 目標

完成可切換首頁、新聞頁、關於頁的最小路由專案。

## 步驟 1：安裝套件

```bash
npm i vue-router
```

## 步驟 2：建立路由器

`src/router/index.ts`

```ts
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import News from '@/pages/News.vue'
import About from '@/pages/About.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/home', component: Home },
    { path: '/news', component: News },
    { path: '/about', component: About }
  ]
})

export default router
```

## 步驟 3：在入口掛載 router

`src/main.ts`

```ts
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

## 步驟 4：在殼層頁面加入導航與展示區

`src/App.vue`

```vue
<template>
  <div>
    <nav>
      <RouterLink to="/home">首頁</RouterLink>
      <RouterLink to="/news">新聞</RouterLink>
      <RouterLink to="/about">關於</RouterLink>
    </nav>

    <RouterView />
  </div>
</template>
```

## 常見問題

1. 切換成功但外層沒變：因為只更換展示區元件。
2. 刷新出現 404：history 模式需要伺服器 fallback。

## 檢核

- 是否有 `app.use(router)`
- 是否有 `<RouterView />`
- routes 每筆是否有 path 與 component
