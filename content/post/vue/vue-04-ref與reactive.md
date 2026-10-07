---
title: "Vue 教學 04：ref、reactive 與模板引用"
date: 2026-03-22T20:04:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "區分響應式資料與 DOM 引用，修正原始筆記中的 TypeScript 與模板語法。"
lastmod: 2026-10-07T20:50:40+08:00
---

區分響應式資料與 DOM 引用，修正原始筆記中的 TypeScript 與模板語法。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 同時操作資料與輸入欄

```vue
<script setup>
import { ref, reactive, nextTick } from 'vue'
const count = ref(0)
const person = reactive({ name: 'Ian', age: 18 })
const input = ref(null)
async function focusInput() {
  count.value++
  person.age++
  await nextTick()
  input.value?.focus()
}
</script>
<template>
  <label>名稱 <input ref="input" v-model="person.name"></label>
  <p>{{ person.name }}：{{ person.age }} 歲，操作 {{ count }} 次</p>
  <button @click="focusInput">加一並聚焦</button>
</template>
```

初始為 Ian、18 歲、0 次；按一次後 19 歲、1 次，遊標進入輸入欄。`ref="input"` 是模板引用，掛載前為 `null`；`ref(0)` 是狀態容器。兩者同名 API，但用途不同。

## 選擇原則

原始值或需要整體替換的資料通常用 `ref`；以屬性更新的物件可用 `reactive`。不要以 `person = {...}` 取代 const proxy；改用 `Object.assign(person, newData)`，或一開始就選 `ref`。解構 `const { age } = person` 會取出當下的值，需維持連動可使用 `toRefs(person)`。

TypeScript 可將引用寫為 `ref<HTMLInputElement | null>(null)`，並把 script 改為 `lang="ts"`、安裝 TypeScript。元件引用只能取得子元件公開的 API，不能把它當作任意讀寫子元件狀態的入口；第 12 章示範 `defineExpose`。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-03-列表渲染.md" >}}) · [下一章]({{< ref "/post/vue/vue-05-watch監視屬性.md" >}})

## 參考資料

- [響應式基礎](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
- [模板引用](https://vuejs.org/guide/essentials/template-refs.html)
- [響應式工具](https://vuejs.org/api/reactivity-utilities.html)
- [範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
