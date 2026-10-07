---
title: "Vue 教學 26：Pinia 狀態、getter 與非同步 action"
date: 2026-03-22T20:26:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "以本地任務資料完成 loading、錯誤與 storeToRefs 的操作流程。"
lastmod: 2026-10-07T20:50:40+08:00
---

以本地任務資料完成 loading、錯誤與 storeToRefs 的操作流程。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 任務 store

沿用第 11 章的 createPinia 入口，建立 `src/stores/tasks.js`：

```javascript
import { defineStore } from 'pinia'
export const useTasksStore = defineStore('tasks', {
  state: () => ({ items: [], loading: false, error: '' }),
  getters: { completed: state => state.items.filter(item => item.done).length },
  actions: {
    async load(fail = false) {
      if (this.loading) return
      this.loading = true
      this.error = ''
      try {
        const data = await Promise.resolve([{ id: 1, title: '整理筆記', done: false }])
        if (fail) throw new Error('模擬讀取失敗')
        this.items = data
      } catch (error) { this.error = error.message }
      finally { this.loading = false }
    },
    toggle(id) {
      const item = this.items.find(item => item.id === id)
      if (item) item.done = !item.done
    }
  }
})
```

App.vue：

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useTasksStore } from './stores/tasks.js'
const store = useTasksStore()
const { items, loading, error, completed } = storeToRefs(store)
</script>
<template>
  <button :disabled="loading" @click="store.load()">讀取任務</button>
  <button :disabled="loading" @click="store.load(true)">模擬失敗</button>
  <p v-if="error" role="alert">{{ error }}</p>
  <ul><li v-for="item in items" :key="item.id"><button @click="store.toggle(item.id)">{{ item.title }}：{{ item.done }}</button></li></ul>
  <p>完成 {{ completed }} 筆</p>
</template>
```

讀取後一筆且完成 0，點任務變完成 1；模擬失敗顯示錯誤、保留原資料。這裡的 Promise 是模擬資料，沒有真實網路延遲。

## 維護注意

替換成 fetch 時檢查 response.ok、資料結構與取消機制。Option store 可用 `$reset`，setup store 需自行定義 reset。Pinia 允許直接修改 state，但重要商業操作集中 action 更易追蹤。測試與 SSR 每次建立自己的 Pinia 例項，避免跨案例或跨請求汙染。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-25-Vue-Router進階.md" >}}) · [下一章]({{< ref "/post/vue/vue-27-Vuex狀態管理.md" >}})

## 參考資料

- [Pinia Actions](https://pinia.vuejs.org/core-concepts/actions.html)
- [Pinia Getters](https://pinia.vuejs.org/core-concepts/getters.html)
- [Pinia State](https://pinia.vuejs.org/core-concepts/state.html)
