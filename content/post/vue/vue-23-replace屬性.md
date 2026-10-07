---
title: "Vue 教學 23：replace 與瀏覽器歷史"
date: 2026-03-22T20:23:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "透過返回鍵實驗 push 與 replace，選擇適合登入導向與篩選更新的行為。"
lastmod: 2026-10-07T20:50:40+08:00
---

透過返回鍵實驗 push 與 replace，選擇適合登入導向與篩選更新的行為。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。使用[第 15 章路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})；涉及 task 路由時，先加入第 17 章的 `/tasks/:id` 與 Task.vue。

## 導航的兩種歷史行為

第 15 章 App.vue 可改成：

```vue
<template>
  <nav>
    <RouterLink to="/">首頁</RouterLink> |
    <RouterLink to="/about">push 關於</RouterLink> |
    <RouterLink to="/about" replace>replace 關於</RouterLink>
  </nav>
  <RouterView />
</template>
```

先從首頁點 push 關於，再按返回，應回到首頁。另開本機首頁，再點 replace 關於，這次目前的首頁紀錄會被取代，返回可能回到上一個網站或沒有可返回紀錄。測試時要分開兩次起始狀態，避免前一次導航汙染判斷。

## 程式寫法與使用場合

```javascript
await router.push({ name: 'about' })
await router.replace({ name: 'about' })
```

這段使用第 24 章取得的 router。push 新增歷史，replace 替換目前紀錄；replace 不會清除全部歷史，也不是整頁重新整理。登入成功後取代登入頁、頻繁更新同一頁的排序條件適合 replace；讀者探索不同文章一般保留 push。

從路由返回不等於 HTTP redirect 或許可權控制；即使登入頁不在返回鏈中，API 仍必須驗證身分。無變化的重複導航可能回傳 navigation failure，需按第 24 章的方式檢查。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-22-路由props配置.md" >}}) · [下一章]({{< ref "/post/vue/vue-24-程式設計式導航.md" >}})

## 參考資料

- [替換目前位置](https://router.vuejs.org/guide/essentials/navigation.html#replace-current-location)
