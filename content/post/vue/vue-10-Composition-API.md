---
title: "Vue 教學 10：Composition API 的組織方式"
date: 2026-03-22T20:10:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "用可搜尋的待辦列表組合 ref、computed 與函式，理解 setup 的責任與 Options API 的對照。"
lastmod: 2026-10-07T00:01:00+08:00
---

用可搜尋的待辦列表組合 ref、computed 與函式，理解 setup 的責任與 Options API 的對照。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 依功能組織狀態

```vue
<script setup>
import { ref, computed } from 'vue'
const keyword = ref('')
const tasks = ref(['讀 Vue 文件', '練習 Java', '整理 Vue 元件'])
const filtered = computed(() => tasks.value.filter(
  title => title.toLowerCase().includes(keyword.value.toLowerCase())
))
function clear() { keyword.value = '' }
</script>
<template>
  <label>搜尋 <input v-model="keyword"></label><button @click="clear">清除</button>
  <ul><li v-for="title in filtered" :key="title">{{ title }}</li></ul>
  <p>顯示 {{ filtered.length }} / {{ tasks.length }} 筆</p>
</template>
```

輸入 vue 後顯示兩筆，清除後三筆。computed 的 getter 不應發請求或更改 tasks，這樣才容易推導輸入與輸出的關係。

## 與 Options API 比較

Options API 按 data、computed、methods 分組，Composition API 可把同一功能的資料與操作放一起並抽成 composable。兩者都可用於 Vue 3，Composition API 不等於效能必然更好。`<script setup>` 頂層宣告可直接在模板使用；普通 `setup()` 必須 return 模板要使用的內容。

setup 不以 `this` 存取元件，從 Vue 2 搬過來的 `this.tasks` 需改為 ref/reactive。方法解構後保留 ref，避免把 `.value` 的快照當成會自動更新的資料。原始課程的待辦／回收桶邏輯可分成 `useTasks`，但跨頁共用的單例狀態應交給 store。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-09-元件化.md" >}}) · [下一章]({{< ref "/post/vue/vue-11-元件通訊與Pinia.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Composition API 常見問題](https://vuejs.org/guide/extras/composition-api-faq.html)
- [script setup](https://vuejs.org/api/sfc-script-setup.html)
