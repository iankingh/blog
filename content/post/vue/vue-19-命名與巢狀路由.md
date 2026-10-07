---
title: "Vue 教學 19：命名與巢狀路由"
date: 2026-03-22T20:19:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "建立帶子頁的任務殼層，理解相對 children path 與第二層 RouterView。"
lastmod: 2026-10-07T20:50:40+08:00
---

建立帶子頁的任務殼層，理解相對 children path 與第二層 RouterView。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 任務殼層

建立 `src/views/TasksLayout.vue`：

```vue
<template>
  <h1>任務大廳</h1>
  <RouterLink :to="{ name: 'task-list' }">列表</RouterLink> |
  <RouterLink :to="{ name: 'task-detail', params: { id: '7' } }">任務 7</RouterLink>
  <RouterView />
</template>
```

`src/views/TaskList.vue`：

```vue
<template><p>目前有一個練習任務</p></template>
```

`src/views/TaskDetail.vue`：

```vue
<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>
<template><p>詳細資料：{{ route.params.id }}</p></template>
```

在 router.js 匯入三個元件，新增這筆紀錄：

```javascript
const taskRoute = {
  path: '/tasks', component: TasksLayout,
  children: [
    { path: '', name: 'task-list', component: TaskList },
    { path: ':id', name: 'task-detail', component: TaskDetail }
  ]
}
```

將 taskRoute 加入 routes。開 `#/tasks` 顯示殼層和列表，開 `#/tasks/7` 殼層保留、下方顯示詳細資料 7。

## 常見問題

children path 不以 `/` 開頭才會接在父 path 後面；以 `/` 開頭會成為絕對網址，但仍有元件巢狀關係。子頁空白先檢查父頁有 RouterView。name 在同一 router 需唯一，否則後註冊的紀錄可能取代前者，應使用具領域意義的名稱。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-18-history與hash模式.md" >}}) · [下一章]({{< ref "/post/vue/vue-20-路由元件生命週期.md" >}})

## 參考資料

- [巢狀路由](https://router.vuejs.org/guide/essentials/nested-routes.html)
- [命名路由](https://router.vuejs.org/guide/essentials/named-routes.html)
