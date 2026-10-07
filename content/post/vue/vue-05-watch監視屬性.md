---
title: "Vue 教學 05：watch 與副作用清理"
date: 2026-03-22T20:05:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "監看特定資料並取消過期操作，區分 computed、watch 與 watchEffect 的責任。"
lastmod: 2026-10-07T20:50:40+08:00
---

監看特定資料並取消過期操作，區分 computed、watch 與 watchEffect 的責任。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 防止過期的搜尋結果

```vue
<script setup>
import { ref, watch } from 'vue'
const query = ref('')
const result = ref('請輸入關鍵字')
watch(query, (value, oldValue, onCleanup) => {
  result.value = '等待搜尋'
  const timer = setTimeout(() => {
    result.value = value.trim() ? `找到：${value.trim()}` : '請輸入關鍵字'
  }, 300)
  onCleanup(() => clearTimeout(timer))
})
</script>
<template>
  <label>關鍵字 <input v-model="query"></label>
  <p>{{ result }}</p>
</template>
```

快速輸入 A 再改成 B，等待 300ms 後只應顯示 B。這是本地模擬，沒有發出 HTTP 請求。若改成 fetch，除了清除計時器還需以 `AbortController` 中止請求，並處理 HTTP 非成功狀態。

## 正確選擇監看來源

監看 reactive 的單一屬性寫 `watch(() => person.age, ...)`，不能傳 `person.age` 的當下數字。`watch` 預設不會立刻執行，初始化需要 `{ immediate: true }`。深度監看物件時新舊值可能是同一個 proxy，不能當作完整快照比較。

只要推導畫面資料先用 computed；需發請求、記錄或同步外部系統才用 watch。`watchEffect` 自動收集同步讀取的依賴，非同步函式在 await 後讀取的資料不會因此自動成為依賴。Vue 3.5 另有 `onWatcherCleanup`，需於同步階段註冊；此例採回呼提供的 onCleanup 以相容較早的 Vue 3。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-04-ref與reactive.md" >}}) · [下一章]({{< ref "/post/vue/vue-06-生命週期.md" >}})

## 參考資料

- [監看器](https://vuejs.org/guide/essentials/watchers.html)
