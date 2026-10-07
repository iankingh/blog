---
title: "Vue 教學 01：宣告式畫面與第一個元件"
date: 2026-03-22T20:01:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "用計數器理解 Vue 如何把狀態對映成畫面，區分模板、事件與應用程式掛載。"
lastmod: 2026-10-07T20:50:40+08:00
---

用計數器理解 Vue 如何把狀態對映成畫面，區分模板、事件與應用程式掛載。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 最小計數器

```vue
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <main>
    <h1>冒險練習</h1>
    <p>已完成 {{ count }} 次練習</p>
    <button @click="count++">完成一次</button>
  </main>
</template>
```

初始顯示 0，按三次變成 3。`ref` 儲存會影響畫面的狀態；模板讀取時會解開 `.value`，在 JavaScript 函式中則必須寫 `count.value`。`createApp` 建立應用程式、`mount` 指定根 DOM，這兩步位於第 00 章的入口。

## 使用方式與限制

Vue 適合需要根據資料切換介面的頁面，不必為單純文字頁面加入完整 SPA。單檔元件的 `<script setup>` 需要 Vite 編譯，不能直接把 `.vue` 丟給瀏覽器。無建置工具的舊版 CDN 範例可以使用 Vue 的完整瀏覽器版本，但不能混用 Vue 2 的 `new Vue()` 與 Vue 3 的 `createApp()`。

若畫面空白，依序確認 `#app` 存在、入口有匯入 `App.vue`、終端無編譯錯誤，再看瀏覽器 Console。修改狀態後手動操作 DOM 容易被下一次渲染覆蓋，應先修改資料。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [下一章]({{< ref "/post/vue/vue-02-Vue-js基礎.md" >}})

## 參考資料

- [Vue 概述](https://vuejs.org/guide/introduction.html)
- [應用程式 API](https://vuejs.org/api/application.html)
