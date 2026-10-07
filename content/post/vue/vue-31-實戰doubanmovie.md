---
title: "Vue 教學 31：電影目錄實作與本地模擬資料"
date: 2026-03-22T20:31:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "保留豆瓣電影專案的搜尋與列表情境，以本地 JSON 完成可重現的載入、錯誤與篩選流程。"
lastmod: 2026-10-07T20:50:40+08:00
---

保留豆瓣電影專案的搜尋與列表情境，以本地 JSON 完成可重現的載入、錯誤與篩選流程。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 專案邊界

原筆記引用豆瓣外部服務與多個缺漏頁面，無法保證 API 存在、允許跨域或有使用授權。練習改用自己建立的虛構電影資料，沒有抓取豆瓣內容；正式整合應另確認 API 文件、授權、速率限制與 CORS。

建立 `public/movies.json`：

```json
[
  {"id": 1, "title": "星際營火", "year": 2024, "genre": "科幻"},
  {"id": 2, "title": "山城日記", "year": 2025, "genre": "劇情"},
  {"id": 3, "title": "營火之後", "year": 2026, "genre": "劇情"}
]
```

回到第 00 章無 Router 的 main.js，App.vue：

```vue
<script setup>
import { ref, computed, onMounted } from 'vue'
const movies = ref([])
const query = ref('')
const loading = ref(false)
const error = ref('')
const filtered = computed(() => movies.value.filter(movie => movie.title.includes(query.value.trim())))
async function load() {
  loading.value = true
  error.value = ''
  try {
    const response = await fetch(`${import.meta.env.BASE_URL}movies.json`)
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    const data = await response.json()
    if (!Array.isArray(data) || !data.every(x => Number.isInteger(x.id) && typeof x.title === 'string' && Number.isInteger(x.year) && typeof x.genre === 'string')) {
      throw new Error('電影資料格式不正確')
    }
    movies.value = data
  } catch (cause) { error.value = cause.message }
  finally { loading.value = false }
}
onMounted(load)
</script>
<template>
  <h1>電影目錄</h1>
  <label>片名 <input v-model="query"></label>
  <p v-if="loading" role="status">讀取中</p>
  <p v-else-if="error" role="alert">{{ error }} <button @click="load">重試</button></p>
  <template v-else>
    <p>顯示 {{ filtered.length }} / {{ movies.length }} 部</p>
    <ul><li v-for="movie in filtered" :key="movie.id">{{ movie.title }}（{{ movie.year }}）／{{ movie.genre }}</li></ul>
    <p v-if="filtered.length === 0">沒有符合的電影</p>
  </template>
</template>
```

## 操作與確認

啟動後三部電影；輸入營火剩兩部，輸入不存在片名顯示空結果。暫時改名 movies.json 並重新整理，應出現 HTTP 錯誤，改回後按重試可恢復。改 JSON 為物件應顯示格式錯誤。

此練習是 CSR、本地載入與前端搜尋，沒有 SSR、後端分頁或登入。要增加詳情頁先依第 17／22 章傳入 id；要跨頁共享改用第 26 章 store。資料量大時應改 API 搜尋與分頁，不把所有資料永久下載到前端。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-30-SSR服務端渲染.md" >}})

## 參考資料

- [Vue 非同步與生命週期](https://vuejs.org/guide/essentials/lifecycle.html)
- [Vite 靜態資源](https://vite.dev/guide/assets.html)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
