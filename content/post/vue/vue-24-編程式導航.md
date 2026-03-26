---
title: "Vue 教學 24 - 程式設計式導航"
date: 2026-03-22T20:24:00+08:00
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

# 程式設計式導航

## 什麼是程式設計式導航

不是點 RouterLink，而是在程式邏輯內用程式碼決定何時跳頁。

## 常用 API

```ts
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
```

- `router`：主動導航（push、replace、back）
- `route`：讀取目前路由資訊

## push 範例

```ts
router.push({
  name: 'newsDetail',
  query: { id: '001' }
})
```

## replace 範例

```ts
router.replace({ path: '/home' })
```

## 搭配按鈕

```vue
<button @click="goDetail(item)">檢視詳情</button>
```

```ts
function goDetail(item: { id: string; title: string }) {
  router.push({
    name: 'newsDetail',
    query: {
      id: item.id,
      title: item.title
    }
  })
}
```

## 常見錯誤

1. 誤把 `useRoute` 當成導航工具。
2. name 拼錯，導致找不到目標路由。
