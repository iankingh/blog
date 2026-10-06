---
title: "Vue 教學 20：路由元件重用與資料重新整理"
date: 2026-03-22T20:20:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "以任務識別碼變動示範元件重用，避免只在 mounted 讀取一次 params。"
lastmod: 2026-10-07T00:01:00+08:00
---

以任務識別碼變動示範元件重用，避免只在 mounted 讀取一次 params。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 重用時監看需要的引數

先依第 17 章建立 task 路由，再把 Task.vue 改成：

```vue
<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const task = ref(null)
const data = { '7': { title: '讀文件' }, '8': { title: '寫測試' } }
watch(() => route.params.id, id => { task.value = data[String(id)] ?? null }, { immediate: true })
onMounted(() => console.log('Task 元件掛載'))
</script>
<template>
  <RouterLink to="/tasks/7">7</RouterLink> | <RouterLink to="/tasks/8">8</RouterLink>
  <p>{{ task?.title ?? '找不到任務' }}</p>
</template>
```

在任務頁 7、8 間切換應依序顯示讀檔案、寫測試；Console 的 mounted 不會每次都執行，因為同一個路由元件被重用。開任務 9 應顯示找不到任務。

## 如何載入真實資料

可在 watch 或 `onBeforeRouteUpdate` 發請求；前者也能用 immediate 處理首次載入，後者能取消導航。請求需取消過期回應，處理 loading、404 與網路錯誤。不要監看整個 route 物件而為無關 query 更動重抓資料。

給 RouterView 元件綁 `:key="route.fullPath"` 可強迫重建，但可能失去輸入內容與捲動狀態，不應用它掩蓋重新整理設計。KeepAlive 另有 activated / deactivated，快取與重用是不同機制。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-19-命名與巢狀路由.md" >}}) · [下一章]({{< ref "/post/vue/vue-21-路由傳參query與params.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [動態路由重用](https://router.vuejs.org/guide/essentials/dynamic-matching.html)
- [Composition API 路由](https://router.vuejs.org/guide/advanced/composition-api.html)
