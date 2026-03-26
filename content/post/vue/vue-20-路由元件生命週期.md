---
title: "Vue 教學 20 - 路由元件生命週期"
date: 2026-03-22T20:20:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue Router"
- "生命週期"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 路由元件生命週期

## 核心觀念

路由切換時，舊路由元件通常會被解除安裝，新路由元件會被掛載。

## 實務影響

- 表單輸入可能消失
- local state 會重置
- 計時器、訂閱若未清理會造成資源洩漏

## 建議做法

1. 在 `onUnmounted` 清理副作用。
2. 重要狀態放到 Pinia 或其他持久層。
3. 需要保留切換狀態時再評估 `keep-alive`。

## 範例

```ts
import { onMounted, onUnmounted } from 'vue'

let timer: number | undefined

onMounted(() => {
  timer = window.setInterval(() => {
    // periodic work
  }, 1000)
})

onUnmounted(() => {
  if (timer) window.clearInterval(timer)
})
```

## 檢核

- 是否有清理副作用
- 是否理解切換路由可能重建元件
