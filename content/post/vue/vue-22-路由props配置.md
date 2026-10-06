---
title: "Vue 教學 22：路由 props 與解耦的頁面"
date: 2026-03-22T20:22:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "將 route 轉成元件 props，讓任務頁可獨立使用與測試。"
lastmod: 2026-10-07T00:01:00+08:00
---

將 route 轉成元件 props，讓任務頁可獨立使用與測試。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。使用[第 15 章路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})；涉及 task 路由時，先加入第 17 章的 `/tasks/:id` 與 Task.vue。

## 讓頁面只接收資料

Task.vue 改為：

```vue
<script setup>
defineProps({ id: { type: String, required: true }, mode: { type: String, default: 'read' } })
</script>
<template><p>任務 {{ id }}，模式 {{ mode }}</p></template>
```

router.js 的任務紀錄可選以下其中一種設定，勿重複加入相同 path：

```javascript
// 布林：把 params 直接傳入
const byParams = { path: '/tasks/:id', name: 'task', component: Task, props: true }
// 物件：適合固定頁面參數
const fixed = { path: '/sample', component: Task, props: { id: '7', mode: 'demo' } }
// 函式：做轉換與預設值，保持無副作用
const converted = {
  path: '/tasks/:id', name: 'task', component: Task,
  props: route => ({ id: String(route.params.id), mode: route.query.edit === '1' ? 'edit' : 'read' })
}
```

使用 converted 並開啟 `#/tasks/7?edit=1` 應顯示任務 7、模式 edit。元件也能被直接寫成 `<Task id="7" mode="demo" />`，不需要建立 router 測試頁面顯示。

## 限制

props:true 只傳 params，不會自動傳 query。命名檢視需對每個 view 指定 props。若把 id 轉成數字，先檢查格式與範圍，避免 `Number('')` 變成 0。props 函式負責對映資料，不應在其中發請求或更改 store。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-21-路由傳參query與params.md" >}}) · [下一章]({{< ref "/post/vue/vue-23-replace屬性.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [傳遞 props](https://router.vuejs.org/guide/essentials/passing-props.html)
