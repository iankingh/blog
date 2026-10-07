---
title: "Vue 教學 07：自訂 composable 與可重用狀態"
date: 2026-03-22T20:07:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "把計數器邏輯抽成 useCounter，辨識每次呼叫獨立的狀態與共用單例。"
lastmod: 2026-10-07T20:50:40+08:00
---

把計數器邏輯抽成 useCounter，辨識每次呼叫獨立的狀態與共用單例。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 抽出邏輯

`src/composables/useCounter.js`：

```javascript
import { ref, computed } from 'vue'
export function useCounter(initial = 0) {
  const count = ref(initial)
  const doubled = computed(() => count.value * 2)
  function increment() { count.value++ }
  function reset() { count.value = initial }
  return { count, doubled, increment, reset }
}
```

`src/App.vue`：

```vue
<script setup>
import { useCounter } from './composables/useCounter.js'
const { count, doubled, increment, reset } = useCounter(2)
</script>
<template>
  <p>{{ count }} / {{ doubled }}</p>
  <button @click="increment">加一</button>
  <button @click="reset">重設</button>
</template>
```

初始 2 / 4，加一後 3 / 6，重設回 2 / 4。回傳 ref 的物件能安全解構；若回傳 reactive 物件，直接解構其原始值屬性會失去連動。

## 邊界與常見問題

此例每次呼叫建立新的 count，兩個元件互不影響；把 count 移到函式外會變成共用狀態，SSR 還可能讓不同使用者共用資料。全域應用狀態可用 Pinia 管理。

Composable 若註冊事件或 timer，需一併在解除安裝時清除。命名以 `use` 開頭是慣例，不是編譯器要求；與 React Hooks 的規則不同，不應照搬 React 的依賴陣列。原筆記的圖片、hook 名稱與未完成片段已改成以上可執行範例。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-06-生命週期.md" >}}) · [下一章]({{< ref "/post/vue/vue-08-響應式進階整理.md" >}})

## 參考資料

- [Composable 設計](https://vuejs.org/guide/reusability/composables.html)
- [範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
