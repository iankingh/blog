---
title: "Vue 教學 27：Vuex 4 與既有狀態管理維護"
date: 2026-03-22T20:27:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "保留 Vuex 的 state、getter、mutation、action 流程，並對照新專案的 Pinia 路線。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 Vuex 的 state、getter、mutation、action 流程，並對照新專案的 Pinia 路線。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 歷史版本定位

Vuex 4 支援 Vue 3，Vuex 3 常見於 Vue 2。此章使用 Vuex 4.1，是維護舊專案的對照；新專案先參考第 26 章 Pinia。不要直接將 Vuex 的 mapState 套到 Pinia store。

`src/store.js`：

```javascript
import { createStore } from 'vuex'
export default createStore({
  state: () => ({ tasks: [] }),
  getters: { count: state => state.tasks.length },
  mutations: { setTasks(state, tasks) { state.tasks = tasks } },
  actions: {
    async load({ commit }) {
      const tasks = await Promise.resolve([{ id: 1, title: 'Vuex 維護練習' }])
      commit('setTasks', tasks)
    }
  }
})
```

`src/main.js`：

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import store from './store.js'
createApp(App).use(store).mount('#app')
```

App.vue：

```vue
<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const tasks = computed(() => store.state.tasks)
const count = computed(() => store.getters.count)
</script>
<template>
  <button @click="store.dispatch('load')">讀取</button>
  <ul><li v-for="task in tasks" :key="task.id">{{ task.title }}</li></ul>
  <p>{{ count }} 筆</p>
</template>
```

讀取後顯示一筆。mutation 保持同步，非同步操作放 action，再以 commit 改資料。此例 Promise 模擬成功回應，正式請求仍需 error/loading。

## 遷移時比較

Pinia 不要求 mutation，action 可直接改 state；Vuex 的 namespaced modules 對應到多個 Pinia store 時要重看依賴與迴圈引用，而不是只換函式名。先列出每個 action 的輸入、狀態變化與副作用，再逐步切換呼叫端並保留測試。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-26-Pinia集中式狀態管理.md" >}}) · [下一章]({{< ref "/post/vue/vue-28-Vite工具.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Vuex 4 入門](https://vuex.vuejs.org/guide/)
- [Vuex Actions](https://vuex.vuejs.org/guide/actions.html)
- [Pinia 遷移](https://pinia.vuejs.org/cookbook/migration-vuex.html)
