---
title: "Vue 教學 12：attrs、公開方法與依賴注入"
date: 2026-03-22T20:12:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "完成可聚焦的輸入元件，示範屬性透傳、defineExpose 與跨層 provide / inject。"
lastmod: 2026-10-07T20:50:40+08:00
---

完成可聚焦的輸入元件，示範屬性透傳、defineExpose 與跨層 provide / inject。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 將屬性傳到正確的 DOM

`src/components/Field.vue`：

```vue
<script setup>
import { ref, inject } from 'vue'
defineOptions({ inheritAttrs: false })
const input = ref(null)
const label = inject('fieldLabel', '名稱')
function focus() { input.value?.focus() }
defineExpose({ focus })
</script>
<template>
  <label>{{ label }} <input ref="input" v-bind="$attrs"></label>
</template>
```

`src/App.vue`：

```vue
<script setup>
import { ref, provide } from 'vue'
import Field from './components/Field.vue'
const field = ref(null)
provide('fieldLabel', '冒險者名稱')
</script>
<template>
  <Field ref="field" placeholder="請輸入名稱" aria-label="冒險者名稱" />
  <button @click="field?.focus()">聚焦欄位</button>
</template>
```

畫面應出現注入的名稱及 placeholder；按鈕將遊標移入 input。多根節點元件不會自動知道 attrs 應套用到哪個根，需明確 `v-bind="$attrs"`。attrs 包含未宣告為 props / emits 的屬性與監聽器，不是完全響應式的資料來源。

## API 邊界

`<script setup>` 元件預設不向父元件公開內部變數，defineExpose 只公開必要方法。用 `$parent` 沿 DOM／元件層級找資料會讓結構重整破壞程式，優先 props 或 inject。大型專案提供 Symbol 作為 injection key 避免名稱衝突，並讓 provider 持有修改狀態的方法。

`defineOptions` 需要 Vue 3.3 以上；更早版本在普通 script 的元件選項設定 inheritAttrs。此例按鈕要等 Field 已掛載才取得 ref，因此使用可選鏈處理 null。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-11-元件通訊與Pinia.md" >}}) · [下一章]({{< ref "/post/vue/vue-13-Vue3進階實務整理.md" >}})

## 參考資料

- [屬性透傳](https://vuejs.org/guide/components/attrs.html)
- [依賴注入](https://vuejs.org/guide/components/provide-inject.html)
- [元件模板引用](https://vuejs.org/guide/essentials/template-refs.html)
