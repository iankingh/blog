---
title: "Vue 教學 03：列表渲染與穩定的 key"
date: 2026-03-22T20:03:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "以排序與刪除任務示範 v-for，避免用索引作為可變動清單的識別值。"
lastmod: 2026-10-07T00:01:00+08:00
---

以排序與刪除任務示範 v-for，避免用索引作為可變動清單的識別值。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 可排序的任務列表

```vue
<script setup>
import { ref } from 'vue'
const tasks = ref([
  { id: 'a', title: '讀文件', done: false },
  { id: 'b', title: '寫範例', done: true }
])
function remove(id) {
  tasks.value = tasks.value.filter(task => task.id !== id)
}
</script>
<template>
  <button @click="tasks.reverse()">反轉順序</button>
  <ul>
    <li v-for="task in tasks" :key="task.id">
      <label><input type="checkbox" v-model="task.done">{{ task.title }}</label>
      <button @click="remove(task.id)">刪除</button>
    </li>
  </ul>
  <p>剩下 {{ tasks.length }} 筆</p>
</template>
```

初始有兩筆，寫範例已勾選。反轉順序後仍只有寫範例勾選；刪除讀檔案後剩一筆。穩定的 `id` 讓 Vue 能對應節點與專案，當內容會排序、插入或含表單狀態時，陣列索引不能表達同一筆資料。

## 篩選與更新

`filter` 回傳新陣列，賦值給 `ref.value` 會觸發更新。`reverse` 改動原陣列，若只是展示排序結果應用 `computed(() => [...tasks.value].sort(...))`，避免不小心改動資料來源。`v-if` 與 `v-for` 不要放在同一個節點，先用 computed 篩選或包一層 `<template>`。

舊 Vue 2 對新增物件屬性與陣列索引賦值有偵測限制，Vue 3 使用 Proxy 後行為不同；維護舊系統時需依實際版本查檔案。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-02-Vue-js基礎.md" >}}) · [下一章]({{< ref "/post/vue/vue-04-ref與reactive.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [列表渲染](https://vuejs.org/guide/essentials/list.html)
