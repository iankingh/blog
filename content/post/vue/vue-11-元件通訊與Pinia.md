---
title: "Vue 教學 11：元件通訊與 Pinia 的分工"
date: 2026-03-22T20:11:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "依狀態的使用範圍選擇 props、事件、provide 或 Pinia，並練習 storeToRefs。"
lastmod: 2026-10-07T00:01:00+08:00
---

依狀態的使用範圍選擇 props、事件、provide 或 Pinia，並練習 storeToRefs。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 先判斷資料屬於誰

單一輸入欄的展開狀態留在元件；父子共同使用資料採 props / emit；同一子樹的主題或表單服務採 provide / inject；跨頁面的購物車與登入資訊採 Pinia。並非所有狀態都需要全域化，資料生命週期應先於工具選擇。

## 最小共享狀態

在第 00 章的 `src/main.js` 加入 Pinia：

```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
createApp(App).use(createPinia()).mount('#app')
```

建立 `src/stores/counter.js`：

```javascript
import { defineStore } from 'pinia'
export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  getters: { doubled: state => state.count * 2 },
  actions: { increment() { this.count++ } }
})
```

`src/App.vue`：

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useCounterStore } from './stores/counter.js'
const store = useCounterStore()
const { count, doubled } = storeToRefs(store)
</script>
<template>
  <p>{{ count }} / {{ doubled }}</p><button @click="store.increment">共享計數加一</button>
</template>
```

按兩次顯示 2 / 4。另一個元件呼叫相同 store 會拿到同一份狀態。state/getter 直接解構會失去連動，使用 storeToRefs；action 可以直接解構。

## 訂閱與儲存

`$subscribe` 適合監看 store 修改，但 localStorage 可能被停用、容量不足或 JSON 損壞，持久化須有 try/catch 與版本遷移。不要儲存 access token 等敏感資料來示範便利性。非同步 action 要處理 loading、錯誤和重複呼叫，第 26 章給出本地資料示例。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-10-Composition-API.md" >}}) · [下一章]({{< ref "/post/vue/vue-12-元件通訊進階.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Pinia 核心觀念](https://pinia.vuejs.org/core-concepts/)
- [Pinia State](https://pinia.vuejs.org/core-concepts/state.html)
- [Vue 元件通訊](https://vuejs.org/guide/components/events.html)
