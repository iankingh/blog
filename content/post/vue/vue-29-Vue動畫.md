---
title: "Vue 教學 29：Transition 與列表動畫"
date: 2026-03-22T20:29:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "完成進出場與排序動畫，讓 key、CSS class 與降低動態偏好互相配合。"
lastmod: 2026-10-07T20:50:40+08:00
---

完成進出場與排序動畫，讓 key、CSS class 與降低動態偏好互相配合。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 可增減的列表

```vue
<script setup>
import { ref } from 'vue'
const visible = ref(true)
const items = ref([{ id: 1, title: '讀文件' }])
let nextId = 2
function add() { items.value.push({ id: nextId++, title: '新練習' }) }
</script>
<template>
  <button @click="visible = !visible">切換提示</button>
  <Transition name="fade"><p v-if="visible">準備開始</p></Transition>
  <button @click="add">新增</button><button @click="items.reverse()">反轉</button>
  <TransitionGroup tag="ul" name="list">
    <li v-for="item in items" :key="item.id">{{ item.title }} <button @click="items = items.filter(x => x.id !== item.id)">刪除</button></li>
  </TransitionGroup>
</template>
<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity .2s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.list-enter-active, .list-leave-active, .list-move { transition: opacity .2s, transform .2s; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateX(12px); }
@media (prefers-reduced-motion: reduce) {
  .fade-enter-active, .fade-leave-active, .list-enter-active, .list-leave-active, .list-move { transition: none; }
}
</style>
```

切換提示有淡入淡出；新增、刪除有位移與透明度變化，排序使用穩定 id。Transition 處理單一元素／元件，TransitionGroup 處理帶 key 的多個元素。

## 舊版本差異與限制

Vue 3 用 `*-enter-from`，Vue 2 常見的是 `*-enter`。原筆記的 Vuex 待辦頁動畫可套用這組 class，但先確認列表 key 唯一，不能靠索引固定節點。leave 元素若要脫離排列以產生較完整的 FLIP 效果，需依容器位置設 absolute 並測試尺寸，不能無條件套全站。

降低動態偏好停用動畫；視覺過場不能成為理解內容的唯一方式。動態尺寸、遠端圖片載入與長列表仍需實機檢查，編譯成功不代表動畫時序正確。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-28-Vite工具.md" >}}) · [下一章]({{< ref "/post/vue/vue-30-SSR服務端渲染.md" >}})

## 參考資料

- [Transition](https://vuejs.org/guide/built-ins/transition.html)
- [TransitionGroup](https://vuejs.org/guide/built-ins/transition-group.html)
