---
title: "Vue 教學 02：模板語法、表單與條件渲染"
date: 2026-03-22T20:02:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "完成可新增留言的表單，練習 v-model、事件、屬性繫結與條件顯示。"
lastmod: 2026-10-07T00:01:00+08:00
---

完成可新增留言的表單，練習 v-model、事件、屬性繫結與條件顯示。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 留言練習

```vue
<script setup>
import { ref } from 'vue'
const text = ref('')
const messages = ref([])
let nextId = 1
function submit() {
  const value = text.value.trim()
  if (!value) return
  messages.value.unshift({ id: nextId++, text: value })
  text.value = ''
}
</script>
<template>
  <form @submit.prevent="submit">
    <label>留言 <input v-model="text"></label>
    <button :disabled="!text.trim()">新增留言</button>
  </form>
  <p v-if="messages.length === 0">目前沒有留言</p>
  <ul v-else>
    <li v-for="message in messages" :key="message.id">{{ message.text }}</li>
  </ul>
</template>
```

輸入「第一則」送出，再輸入「第二則」，列表應由上到下顯示第二則、第一則，輸入欄清空。`.prevent` 阻止原生表單導頁，`:disabled` 是 `v-bind` 簡寫，`@submit` 是 `v-on` 簡寫。

## 容易混淆的地方

`v-if` 會建立或移除節點；`v-show` 使用 CSS 控制可見性，頻繁切換時可考慮後者。`{{ text }}` 會把輸入當文字，適合使用者留言；不要用 `v-html` 顯示未清理的輸入。此例只存在記憶體，重新整理資料會消失；需要儲存時另設 API 或有錯誤處理的本機儲存流程。

Vue 2 與 Vue 3 的模板概念相近，但 Vue 3 可使用多個根節點。表單有 IME 中文輸入需求時應測試組字過程，不要假設每次按鍵都代表完整文字。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-01-Vue概述.md" >}}) · [下一章]({{< ref "/post/vue/vue-03-列表渲染.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [模板語法](https://vuejs.org/guide/essentials/template-syntax.html)
- [表單輸入綁定](https://vuejs.org/guide/essentials/forms.html)
- [條件渲染](https://vuejs.org/guide/essentials/conditional.html)
