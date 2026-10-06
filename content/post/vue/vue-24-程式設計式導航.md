---
title: "Vue 教學 24：程式導航與失敗處理"
date: 2026-03-22T20:24:00+08:00
aliases:
- "/post/vue/vue-24-編程式導航/"
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "按操作結果導航，使用 useRouter、push、replace 與 navigation failure 判斷完成狀態。"
lastmod: 2026-10-07T00:01:00+08:00
---

按操作結果導航，使用 useRouter、push、replace 與 navigation failure 判斷完成狀態。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。使用[第 15 章路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})；涉及 task 路由時，先加入第 17 章的 `/tasks/:id` 與 Task.vue。

## 按鈕導航

替換 App.vue：

```vue
<script setup>
import { ref } from 'vue'
import { useRouter, isNavigationFailure } from 'vue-router'
const router = useRouter()
const status = ref('')
async function openAbout() {
  try {
    const failure = await router.push({ name: 'about' })
    status.value = isNavigationFailure(failure) ? '未切換，可能已在此頁或被守衛攔下' : '導航完成'
  } catch (error) {
    status.value = `導航錯誤：${error.message}`
  }
}
</script>
<template>
  <button @click="openAbout">開啟關於</button>
  <button @click="router.back()">返回</button>
  <p>{{ status }}</p><RouterView />
</template>
```

由首頁按開啟關於，應顯示關於頁與導航完成；再次按可能得到重複導航訊息。router.push 是非同步操作，需 await 後才依結果關閉對話方塊或顯示成功。

## route 與 router 的區分

useRoute 取得目前位置資料；useRouter 取得導航能力。`router.go(-1)` 等同 back，但瀏覽器沒有前一筆時不會保證回到本站首頁；「回任務列表」宜明確 push 到列表。

守衛回 false 的取消通常以 navigation failure 表示，守衛丟出錯誤則可能使 promise reject，兩者分開處理。不要把未驗證的 query redirect 值直接交給 `window.location`，先限制站內目的地，避免開放重新導向。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-23-replace屬性.md" >}}) · [下一章]({{< ref "/post/vue/vue-25-Vue-Router進階.md" >}})

## 查核範圍

SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [程式導航](https://router.vuejs.org/guide/essentials/navigation.html)
- [導航失敗](https://router.vuejs.org/guide/advanced/navigation-failures.html)
