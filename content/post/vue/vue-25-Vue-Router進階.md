---
title: "Vue 教學 25：守衛、延遲載入與導航測試"
date: 2026-03-22T20:25:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "完成本機模擬登入守衛，理解前端攔截的限制與 lazy route 的建置行為。"
lastmod: 2026-10-07T00:01:00+08:00
---

完成本機模擬登入守衛，理解前端攔截的限制與 lazy route 的建置行為。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。使用[第 15 章路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})；涉及 task 路由時，先加入第 17 章的 `/tasks/:id` 與 Task.vue。

## 模擬授權狀態

建立 `src/auth.js`，只供練習，並非正式登入：

```javascript
import { ref } from 'vue'
export const signedIn = ref(false)
```

router.js 使用下列完整設定：

```javascript
import { createRouter, createWebHashHistory } from 'vue-router'
import { signedIn } from './auth.js'
import Home from './views/Home.vue'
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/about', name: 'about', component: () => import('./views/About.vue'), meta: { requiresAuth: true } }
  ]
})
router.beforeEach(to => {
  if (to.meta.requiresAuth && !signedIn.value) return { name: 'home', query: { denied: '1' } }
})
export default router
```

App.vue：

```vue
<script setup>
import { signedIn } from './auth.js'
</script>
<template>
  <label><input type="checkbox" v-model="signedIn">模擬已登入</label>
  <RouterLink to="/about">開啟受限頁</RouterLink>
  <RouterView />
</template>
```

未勾選時點關於，應回首頁且 query 為 denied=1；勾選後能進入。lazy import 讓建置拆出頁面資源，並非減少 API 的授權需求。

## 設計限制

守衛可回傳 false 取消、路由位置導向或不回傳繼續；使用傳統 next 時容易多次呼叫，這裡採回傳值。不要把每個導航都導到同一個受限頁而形成迴圈。正式許可權由伺服器驗證，這個布林值可由使用者修改，不能當安全機制。

測試可用 createMemoryHistory 建立獨立 router，分別 push 首頁與受限頁，檢查 currentRoute；DOM 與返回鍵另在瀏覽器確認。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-24-程式設計式導航.md" >}}) · [下一章]({{< ref "/post/vue/vue-26-Pinia集中式狀態管理.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；memory history實測命名參數、query、resolve與守衛導向。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [導航守衛](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- [延遲載入](https://router.vuejs.org/guide/advanced/lazy-loading.html)
