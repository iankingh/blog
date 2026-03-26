---
title: "Vue 教學 22 - 路由 props 配置"
date: 2026-03-22T20:22:00+08:00
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

# 路由 props 配置

## 為什麼需要 props

讓路由元件直接透過 props 收到引數，降低元件對 `useRoute()` 的耦合。

## 三種寫法

### 寫法 1：布林

```ts
{
  path: '/detail/:id',
  component: Detail,
  props: true
}
```

效果：把 `params` 全部對映成元件 props。

### 寫法 2：物件

```ts
{
  path: '/detail',
  component: Detail,
  props: { source: 'router' }
}
```

效果：傳固定值給元件。

### 寫法 3：函式

```ts
{
  path: '/detail',
  component: Detail,
  props: (route) => ({
    id: route.query.id,
    title: route.query.title
  })
}
```

效果：自行決定如何把 route 轉成 props。

## 元件端接收

```ts
const props = defineProps<{ id?: string; title?: string }>()
```

## 何時用哪種

- 純 params 轉 props：`props: true`
- 固定設定值：物件
- 需要轉換與合併：函式
