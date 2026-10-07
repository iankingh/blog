---
title: "Vue 教學 21：query 與 params 的接收及驗證"
date: 2026-03-22T20:21:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "用任務編號與頁碼比較路徑引數、查詢引數，避免直接把網址值當成可信數字。"
lastmod: 2026-10-07T20:50:40+08:00
---

用任務編號與頁碼比較路徑引數、查詢引數，避免直接把網址值當成可信數字。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。使用[第 15 章路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})；涉及 task 路由時，先加入第 17 章的 `/tasks/:id` 與 Task.vue。

## 傳送引數

在 App.vue 的 nav 加入：

```html
<RouterLink :to="{ name: 'task', params: { id: '7' }, query: { page: '2', q: 'Vue 筆記' } }">任務查詢</RouterLink>
```

Task.vue 替換為：

```vue
<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const id = computed(() => String(route.params.id ?? ''))
const page = computed(() => {
  const raw = route.query.page
  const number = typeof raw === 'string' ? Number(raw) : NaN
  return Number.isSafeInteger(number) && number >= 1 ? number : 1
})
const keyword = computed(() => typeof route.query.q === 'string' ? route.query.q : '')
</script>
<template><p>任務 {{ id }}，第 {{ page }} 頁，關鍵字 {{ keyword }}</p></template>
```

點連結後顯示 7／2／Vue 筆記。手動把 page 改成 -1、abc 或重複 query 應回到第 1 頁。query 值可能是字串、null 或陣列，不應直接執行 trim。

## 選擇與限制

params 在 routes 中必須有對應的動態片段；路徑缺少必填 id 會導致命名導航失敗。query 用於可分享的篩選條件；密碼、token 不放網址，網址會進入歷史、記錄與分享連結。

`router.push({ path: '/tasks', params: { id: '7' } })` 不會自動變成 `/tasks/7`。使用 name 並讓 Router 編碼，避免手動串接帶斜線或空白的識別值。後端還是要檢查使用者能否讀取對應任務。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-20-路由元件生命週期.md" >}}) · [下一章]({{< ref "/post/vue/vue-22-路由props配置.md" >}})

## 參考資料

- [動態路由](https://router.vuejs.org/guide/essentials/dynamic-matching.html)
- [導航參數](https://router.vuejs.org/guide/essentials/navigation.html)
