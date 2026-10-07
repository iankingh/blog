---
title: "Vue 教學 17：to 的字串與物件寫法"
date: 2026-03-22T20:17:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "比較固定網址與命名路由導航，避免以 path 搭配 params 造成引數遺失。"
lastmod: 2026-10-07T20:50:40+08:00
---

比較固定網址與命名路由導航，避免以 path 搭配 params 造成引數遺失。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 加入任務頁

建立 `src/views/Task.vue`：

```vue
<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>
<template><p>任務 {{ route.params.id }}，來源 {{ route.query.from }}</p></template>
```

router.js 匯入 Task，加入 `{ path: '/tasks/:id', name: 'task', component: Task }`。App.vue 的 nav 可加入：

```html
<RouterLink to="/tasks/7?from=home">固定網址</RouterLink>
<RouterLink :to="{ name: 'task', params: { id: '8' }, query: { from: 'menu' } }">命名導航</RouterLink>
```

第一個顯示任務 7／home，第二個任務 8／menu。`to="..."` 是字串；`:to="..."` 是 JavaScript 物件表示式，少了冒號會把內容當字面文字。

## 使用命名路由的理由

具名方式會編碼引數，調整 path 時呼叫端不必跟著改字串。傳 `{ path: '/tasks', params: { id: '8' } }` 不會補上 id；使用 name 搭 params 或直接提供完整 path。query 適合篩選與來源，params 適合必填的資源識別值。

在程式測試可用 `router.resolve({ name: 'task', params: { id: '8' } }).href` 確認結果含 `/tasks/8`，不需真的導頁。網址中的資料不可信，接收後仍要驗證型別與授權。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-16-Vue-Router基礎.md" >}}) · [下一章]({{< ref "/post/vue/vue-18-history與hash模式.md" >}})

## 參考資料

- [具名路由](https://router.vuejs.org/guide/essentials/named-routes.html)
- [程式導航](https://router.vuejs.org/guide/essentials/navigation.html)
