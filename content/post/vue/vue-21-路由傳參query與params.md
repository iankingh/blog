---
title: "Vue 教學 21 - 路由傳參 query 與 params"
date: 2026-03-22T20:21:00+08:00
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

# 路由傳參：query 與 params

## query 引數

### 傳遞

```vue
<RouterLink :to="{ path: '/news/detail', query: { id: 1, title: '標題' } }">
  檢視
</RouterLink>
```

### 接收

```ts
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.query.id)
```

特性：

- 顯示在 URL 的 `?` 後
- 可選填、彈性高

## params 引數

### 路由規則

```ts
{ path: '/news/detail/:id/:title', name: 'newsDetail', component: Detail }
```

### 傳遞

```vue
<RouterLink :to="{ name: 'newsDetail', params: { id: 1, title: '標題' } }">
  檢視
</RouterLink>
```

### 接收

```ts
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.params.id)
```

特性：

- 引數是 URL 路徑的一部分
- 通常搭配命名路由最穩定

## 如何選

- URL 可讀且非必要欄位：query
- 資源識別、語意路徑：params

## 常見錯誤

1. 傳 params 但路由沒宣告對應佔位。
2. 傳 params 時未使用 name，導致行為不如預期。
