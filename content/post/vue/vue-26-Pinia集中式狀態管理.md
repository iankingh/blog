---
title: "Vue 教學 26 - Pinia 集中式狀態管理"
date: 2026-03-22T20:26:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Pinia"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Pinia 集中式狀態管理

## 為什麼需要 Pinia

當資料要在多個元件共享時，靠一層層 props 傳遞會變複雜。Pinia 可集中管理狀態，讓資料流更清楚。

## 安裝與掛載

### 安裝

```bash
npm i pinia
```

### main.ts 掛載

```ts
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
app.use(createPinia())
app.mount('#app')
```

## 建立第一個 store

`src/stores/counter.ts`

```ts
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    sum: 1
  }),
  getters: {
    double: (state) => state.sum * 2
  },
  actions: {
    increment(n: number) {
      this.sum += n
    },
    decrement(n: number) {
      this.sum -= n
    }
  }
})
```

## 元件中使用

```ts
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
counter.increment(1)
console.log(counter.sum)
console.log(counter.double)
```

## storeToRefs 使用時機

當你要解構 store 裡的 state 或 getters，又要保持響應式，使用 `storeToRefs`：

```ts
import { storeToRefs } from 'pinia'

const counter = useCounterStore()
const { sum, double } = storeToRefs(counter)
```

## 非同步 action 範例

```ts
actions: {
  async fetchQuote() {
    const res = await fetch('https://api.uomg.com/api/rand.qinghua?format=json')
    const data = await res.json()
    this.quoteList.unshift({ id: crypto.randomUUID(), title: data.content })
  }
}
```

## 實務建議

1. 按功能切 store，不要做超大單一 store。
2. 非同步請求放在 action，不放元件模板邏輯。
3. 把商業邏輯集中在 store，元件專注畫面互動。

## 常見錯誤

1. 直接解構 store 導致失去響應式（要用 storeToRefs）。
2. 在 action 內使用 `this` 時誤用箭頭函式。
3. 把一次性 UI 狀態與全域狀態混在一起，造成維護困難。
