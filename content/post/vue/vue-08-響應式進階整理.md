---
title: "Vue 教學 08：進階響應式、唯讀資料與插槽"
date: 2026-03-22T20:08:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "比較 shallowRef、readonly 和 toRaw，並用插槽把資料邏輯與呈現分開。"
lastmod: 2026-10-07T00:01:00+08:00
---

比較 shallowRef、readonly 和 toRaw，並用插槽把資料邏輯與呈現分開。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 淺層狀態的更新方式

```vue
<script setup>
import { shallowRef, readonly } from 'vue'
const state = shallowRef({ score: 0 })
const view = readonly(state)
function replace() { state.value = { score: state.value.score + 1 } }
</script>
<template>
  <p>分數 {{ view.score }}</p>
  <button @click="replace">替換物件</button>
</template>
```

每次按鈕分數加一。shallowRef 只追蹤 `.value` 的替換；直接改 `state.value.score++` 不會由此觸發更新。必要時可用 `triggerRef(state)`，但優先保持清楚的替換策略。

## API 比較

| API | 用途 | 限制 |
| --- | --- | --- |
| shallowReactive | 只代理根層屬性 | 巢狀物件不是自動響應式 |
| readonly | 對外提供唯讀檢視 | 原來源更新仍會反映，不是複製快照 |
| shallowReadonly | 僅禁止根層賦值 | 巢狀屬性仍可能可修改 |
| toRaw | 暫時取得 proxy 的原始物件 | 不應長期儲存後繞過追蹤修改 |
| markRaw | 排除第三方物件的代理轉換 | 留意原物件與代理物件的識別差異 |

## 插槽是呈現邊界

建立 `src/components/Frame.vue`：

```vue
<template>
  <section><header><slot name="title">預設標題</slot></header><slot /></section>
</template>
```

父元件匯入 Frame 後使用：

```vue
<script setup>
import Frame from './components/Frame.vue'
</script>
<template>
  <Frame><template #title>技能紀錄</template><p>今天完成兩次練習</p></Frame>
</template>
```

標題應是技能紀錄而非預設標題。插槽內容在父元件作用域求值；若要使用子元件資料，由子元件傳 slot props，不能直接存取子元件內部變數。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-07-自定義hooks.md" >}}) · [下一章]({{< ref "/post/vue/vue-09-元件化.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [進階響應式 API](https://vuejs.org/api/reactivity-advanced.html)
- [插槽](https://vuejs.org/guide/components/slots.html)
