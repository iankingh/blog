---
title: "Vue 教學 06：生命週期與資源釋放"
date: 2026-03-22T20:06:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "以計時器示範掛載、更新與解除安裝，確保元件移除後不留下背景工作。"
lastmod: 2026-10-07T20:50:40+08:00
---

以計時器示範掛載、更新與解除安裝，確保元件移除後不留下背景工作。

<!--more-->

適用：Vue 3.5 的單檔元件與 Composition API。先依[第 00 章]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}})建立 Vite 專案；除另有指定，範例取代 `src/App.vue`。

## 計時元件

建立 `src/components/Clock.vue`：

```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
const seconds = ref(0)
let timer
onMounted(() => { timer = setInterval(() => seconds.value++, 1000) })
onUnmounted(() => clearInterval(timer))
</script>
<template><p>此元件已存活 {{ seconds }} 秒</p></template>
```

`src/App.vue`：

```vue
<script setup>
import { ref } from 'vue'
import Clock from './components/Clock.vue'
const visible = ref(true)
</script>
<template>
  <button @click="visible = !visible">切換計時器</button>
  <Clock v-if="visible" />
</template>
```

等兩秒後關閉再開啟，計數應從 0 重來。`v-if` 會解除安裝元件，`v-show` 只隱藏，因此換成 v-show 時計時器會持續執行。

## Hook 的執行位置

`onMounted` 適合需要 DOM 的初始化，`onUnmounted` 清除 timer、事件監聽與訂閱。Hook 應在 setup 同步執行時註冊，不要等任意非同步回呼再註冊。資料改變後 DOM 不是立即同步，需等 `nextTick`；不要在 `onUpdated` 無條件修改會導致重渲染的狀態。

Vue 2 的 `beforeDestroy` / `destroyed` 在 Vue 3 Options API 對應 `beforeUnmount` / `unmounted`。SSR 不會執行 mounted，因此 browser-only 初始化放在 mounted，避免伺服器存取 `window`。


## 其他生命週期與版本對照

| Hook | 可觀察時機與用途 |
| --- | --- |
| `onBeforeMount`／`onMounted` | 初次渲染前／掛載後；需要實際 DOM 的程式放 mounted |
| `onBeforeUpdate`／`onUpdated` | 響應狀態造成 DOM 更新前／後；不要在 updated 無條件再改狀態形成循環 |
| `onBeforeUnmount`／`onUnmounted` | 卸載前／後；清理自行建立的 timer、監聽與外部資源 |
| `onActivated`／`onDeactivated` | KeepAlive 快取元件啟用／停用，停用不等於 unmount，背景工作應按需求暫停 |
| `onErrorCaptured` | 處理子元件錯誤，回傳 false 可停止繼續向上傳播，需保留可診斷資訊 |
| `onServerPrefetch` | SSR 取得本次請求所需資料；不把不同使用者資料放全域共享狀態 |

原 Vue 2 的 beforeDestroy／destroyed 在 Vue 3 改名為 beforeUnmount／unmounted；Composition API hooks 要在 setup 的同步執行期註冊，不能等任意 await 結束後才建立。SSR 不執行 mounted，瀏覽器專屬功能仍需分開處理。上表的全部 hook 未逐項以瀏覽器實機測試，本篇實際測試範圍仍以下方紀錄為準。

## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-05-watch監視屬性.md" >}}) · [下一章]({{< ref "/post/vue/vue-07-自定義hooks.md" >}})

## 參考資料

- [生命週期](https://vuejs.org/guide/essentials/lifecycle.html)
- [生命週期 API](https://vuejs.org/api/composition-api-lifecycle.html)
- [範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
