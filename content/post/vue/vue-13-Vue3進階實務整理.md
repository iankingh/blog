---
title: "Vue 教學 13：v-model、自訂指令與衍生資料"
date: 2026-03-22T20:13:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "完成可雙向繫結的輸入元件，對照 Vue 3 的 modelValue 協定與 defineModel。"
lastmod: 2026-10-07T00:01:00+08:00
---

完成可雙向繫結的輸入元件，對照 Vue 3 的 modelValue 協定與 defineModel。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 明確的 v-model 協定

`src/components/NameInput.vue`：

```vue
<script setup>
defineProps({ modelValue: { type: String, default: '' } })
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <label>名稱 <input :value="modelValue" @input="emit('update:modelValue', $event.target.value)"></label>
</template>
```

`src/App.vue`：

```vue
<script setup>
import { ref, computed } from 'vue'
import NameInput from './components/NameInput.vue'
const name = ref('Ian')
const length = computed(() => name.value.trim().length)
const vFocus = { mounted: element => element.focus() }
</script>
<template>
  <NameInput v-model="name" />
  <p>有效長度 {{ length }}</p>
  <label>練習指令 <input v-focus></label>
</template>
```

初始有效長度 3，改為空白字串後為 0；載入後第二個輸入欄獲得焦點。自訂指令處理底層 DOM 行為，資料推導用 computed，跨元件資料則透過 props / emit。

## 新舊版本對照

Vue 2 預設使用 `value` / `input`，Vue 3 改為 `modelValue` / `update:modelValue`，不能只更改事件名稱而保留舊 prop。Vue 3.4 以上可在子元件用 `const model = defineModel()` 簡化協定，但不要以子元件 default 掩蓋父元件未提供值造成的狀態不同步。

directive 使用於元件時可能套在根節點，遇到多根元件要改在明確 DOM 上使用。computed getter 維持無副作用；非同步搜尋用第 05 章的 watch 清理模式。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-12-元件通訊進階.md" >}}) · [下一章]({{< ref "/post/vue/vue-14-路由核心概念.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [元件 v-model](https://vuejs.org/guide/components/v-model.html)
- [自訂指令](https://vuejs.org/guide/reusability/custom-directives.html)
- [計算屬性](https://vuejs.org/guide/essentials/computed.html)
