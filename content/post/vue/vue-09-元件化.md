---
title: "Vue 教學 09：元件拆分、props 與事件"
date: 2026-03-22T20:09:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "完成可刪除的待辦元件，讓父元件持有資料、子元件回報操作。"
lastmod: 2026-10-07T20:50:40+08:00
---

完成可刪除的待辦元件，讓父元件持有資料、子元件回報操作。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 子元件

建立 `src/components/TaskItem.vue`：

```vue
<script setup>
defineProps({ task: { type: Object, required: true } })
const emit = defineEmits(['remove'])
</script>
<template>
  <li>{{ task.title }} <button @click="emit('remove', task.id)">刪除</button></li>
</template>
```

父元件 `src/App.vue`：

```vue
<script setup>
import { ref } from 'vue'
import TaskItem from './components/TaskItem.vue'
const tasks = ref([{ id: 1, title: '練習元件' }, { id: 2, title: '整理筆記' }])
function remove(id) { tasks.value = tasks.value.filter(task => task.id !== id) }
</script>
<template>
  <ul><TaskItem v-for="task in tasks" :key="task.id" :task="task" @remove="remove" /></ul>
  <p>共 {{ tasks.length }} 筆</p>
</template>
```

初始兩筆，刪除任一筆後剩一筆。props 是父到子的資料流，emit 是子回報意圖；不要在子元件刪除父陣列或修改 task.title。巢狀物件 props 技術上仍可被子元件修改，唯讀規則需要設計與檢查維持。

## 拆分判斷

有獨立責任、重複使用或需單獨測試的 UI 適合抽元件；不要只因檔案很長就把資料流切得難以追蹤。`defineProps` / `defineEmits` 是編譯巨集，不必 import。原範例中待辦與回收桶頁面缺少關聯檔案，此例先完成同一頁的完整資料流；跨頁共享在第 26 章處理。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-08-響應式進階整理.md" >}}) · [下一章]({{< ref "/post/vue/vue-10-Composition-API.md" >}})

## 參考資料

- [元件基礎](https://vuejs.org/guide/essentials/component-basics.html)
- [元件 Props](https://vuejs.org/guide/components/props.html)
- [元件事件](https://vuejs.org/guide/components/events.html)
