---
title: "Vue 學習路線總整理"
date: 2026-03-22T20:00:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "學習路線"
toc: true
draft: true
---

<!-- 這份檔案整理了所有 Vue 教學筆記的分類與建議學習順序，檔案已統一命名為 vue-{編號}-{主題}.md -->
<!--more-->

# Vue 學習路線總整理

> 整理日期：2026-03-22
> 共 31 份筆記，統一命名為 `vue-01` ~ `vue-31`，分為 **6 大階段**。

---

## 階段總覽

| 階段 | 主題 | 編號範圍 | 篇數 |
|------|------|---------|------|
| 一 | Vue 基礎與模板語法 | 01 – 03 | 3 篇 |
| 二 | 響應式系統與核心 API | 04 – 08 | 5 篇 |
| 三 | 元件化與元件通訊 | 09 – 13 | 5 篇 |
| 四 | Vue Router 路由 | 14 – 25 | 12 篇 |
| 五 | 狀態管理（Pinia / Vuex） | 26 – 27 | 2 篇 |
| 六 | 工程化、動畫、SSR 與實戰 | 28 – 31 | 4 篇 |

---

## 階段一：Vue 基礎與模板語法

> 目標：理解 Vue 是什麼、怎麼跑起來、基本模板怎麼寫。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 01 | [vue-01-Vue概述](vue-01-Vue概述.md) | 最小可運作範例、v-model 雙向繫結 |
| 02 | [vue-02-Vue-js基礎](vue-02-Vue-js基礎.md) | 事件、v-for、computed、methods |
| 03 | [vue-03-列表渲染](vue-03-列表渲染.md) | v-for 陣列與物件、:key 使用 |

**學完檢核：**
- 能寫出含 v-model、v-for、computed 的小應用
- 理解 data → 模板 → 畫面的單向資料流

---

## 階段二：響應式系統與核心 API

> 目標：掌握 ref / reactive、watch、生命週期、hooks，為元件化做準備。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 04 | [vue-04-ref與reactive](vue-04-ref與reactive.md) | ref、reactive、props 型別、defineProps |
| 05 | [vue-05-watch監視屬性](vue-05-watch監視屬性.md) | watch 基本用法、deep 深度監聽 |
| 06 | [vue-06-生命週期](vue-06-生命週期.md) | Vue2 vs Vue3 生命週期鉤子對照 |
| 07 | [vue-07-自定義hooks](vue-07-自定義hooks.md) | 抽取可重用邏輯（useSum、useDog） |
| 08 | [vue-08-響應式進階整理](vue-08-響應式進階整理.md) | shallowRef/shallowReactive、readonly、toRaw、markRaw、customRef |

**學完檢核：**
- 能分辨 ref 與 reactive 使用時機
- 能自己寫一個 custom hook 抽取邏輯
- 理解生命週期各階段可以做什麼

---

## 階段三：元件化與元件通訊

> 目標：熟悉元件拆分、父子通訊、跨層通訊、v-model 在元件的本質。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 09 | [vue-09-元件化](vue-09-元件化.md) | 元件結構、SFC 寫法、mitt Event Bus |
| 10 | [vue-10-Composition-API](vue-10-Composition-API.md) | Composition API 重構元件 |
| 11 | [vue-11-元件通訊與Pinia](vue-11-元件通訊與Pinia.md) | props、自訂事件、mitt、v-model 元件用法、Pinia 進階 |
| 12 | [vue-12-元件通訊進階](vue-12-元件通訊進階.md) | $attrs、$refs/defineExpose、provide/inject、slot |
| 13 | [vue-13-Vue3進階實務整理](vue-13-Vue3進階實務整理.md) | v-model 破壞性更新、自定義指令、computed/watch 進階 |

**學完檢核：**
- 能說出 5 種以上元件通訊方式與使用時機
- 能正確在元件上使用 v-model（modelValue + update:modelValue）
- 理解 provide/inject 與 $attrs 的跨層傳遞

---

## 階段四：Vue Router 路由

> 目標：從路由概念到巢狀路由、傳參、程式設計式導航，完整掌握前端路由。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 14 | [vue-14-路由核心概念](vue-14-路由核心概念.md) | SPA 路由原理、Router vs Route |
| 15 | [vue-15-路由基本接線](vue-15-路由基本接線.md) | createRouter、RouterLink、RouterView |
| 16 | [vue-16-Vue-Router基礎](vue-16-Vue-Router基礎.md) | 路由器建立、main.ts 掛載、完整接線 |
| 17 | [vue-17-to的兩種寫法](vue-17-to的兩種寫法.md) | 字串 vs 物件 to |
| 18 | [vue-18-history與hash模式](vue-18-history與hash模式.md) | createWebHistory vs createWebHashHistory |
| 19 | [vue-19-命名與巢狀路由](vue-19-命名與巢狀路由.md) | name、children、子 RouterView |
| 20 | [vue-20-路由元件生命週期](vue-20-路由元件生命週期.md) | 路由切換對元件掛載/解除安裝的影響 |
| 21 | [vue-21-路由傳參query與params](vue-21-路由傳參query與params.md) | query vs params 傳參與接收 |
| 22 | [vue-22-路由props配置](vue-22-路由props配置.md) | 三種 props 寫法（布林/物件/函式） |
| 23 | [vue-23-replace屬性](vue-23-replace屬性.md) | push vs replace、歷史紀錄控制 |
| 24 | [vue-24-程式設計式導航](vue-24-程式設計式導航.md) | useRouter / useRoute、程式碼跳轉 |
| 25 | [vue-25-Vue-Router進階](vue-25-Vue-Router進階.md) | 路由搭配 Vuex/Store 的完整架構 |

**學完檢核：**
- 能獨立建立含巢狀路由與傳參的專案
- 能說出 query 與 params 差異
- 能在按鈕事件中用 router.push 做程式跳轉

---

## 階段五：狀態管理（Pinia / Vuex）

> 目標：掌握集中式狀態管理，會用 Pinia（主流）、認識 Vuex（舊專案維護）。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 26 | [vue-26-Pinia集中式狀態管理](vue-26-Pinia集中式狀態管理.md) | defineStore、state/getters/actions、storeToRefs |
| 27 | [vue-27-Vuex狀態管理](vue-27-Vuex狀態管理.md) | Vuex（state/mutations/actions/plugins），瞭解即可 |

> 補充：Pinia 的 $patch、非同步 action、setup 風格 store、localStorage 持久化，在 [vue-11](vue-11-元件通訊與Pinia.md) 的 A 部分也有詳細說明。

**學完檢核：**
- 能用 Pinia 建 store、在元件讀寫資料
- 知道 storeToRefs 為何需要
- 認識 Vuex 與 Pinia 的差異

---

## 階段六：工程化、動畫、SSR 與實戰

> 目標：認識 Vite 工程化、Vue 動畫、SSR 概念，最後走一遍實戰專案。

| 順序 | 檔案 | 重點 |
|------|------|------|
| 28 | [vue-28-Vite工具](vue-28-Vite工具.md) | Vite 專案建置、Hash 模式部署 |
| 29 | [vue-29-Vue動畫](vue-29-Vue動畫.md) | transition、TransitionGroup、CSS 動畫 |
| 30 | [vue-30-SSR服務端渲染](vue-30-SSR服務端渲染.md) | createSSRApp、entry-client/server 分離 |
| 31 | [vue-31-實戰doubanmovie](vue-31-實戰doubanmovie.md) | SSR 實戰專案、axios 封裝、完整架構 |

**學完檢核：**
- 能用 Vite 建立與打包專案
- 理解 SSR 的 client/server 入口拆分
- 能從頭到尾走完一個完整專案

---

## 建議學習節奏

```
第 1 週：階段一 + 階段二（vue-01 ~ vue-08，基礎 → 響應式）
第 2 週：階段三（vue-09 ~ vue-13，元件通訊）
第 3 週：階段四（vue-14 ~ vue-25，路由，份量最多，可拆兩週）
第 4 週：階段五 + 階段六（vue-26 ~ vue-31，狀態管理 → 實戰）
```

---

## 檔案命名對照表

以下列出舊檔名 → 新檔名，方便回溯：

| 新編號 | 新檔名 | 舊檔名 |
|--------|--------|--------|
| 01 | vue-01-Vue概述 | vue-turtorial-01-vue概述 |
| 02 | vue-02-Vue-js基礎 | vue-turtorial-02-vue-js基礎 |
| 03 | vue-03-列表渲染 | vue-turtorial-05-列表渲染 |
| 04 | vue-04-ref與reactive | vue-turtorial-03-ref-reactive |
| 05 | vue-05-watch監視屬性 | vue-turtorial-04-watch監視屬性 |
| 06 | vue-06-生命週期 | vue-turtorial-06-生命週期 |
| 07 | vue-07-自定義hooks | vue-turtorial-07-自定義hooks |
| 08 | vue-08-響應式進階整理 | 圖片整理_Vue3_截圖筆記 |
| 09 | vue-09-元件化 | vue-turtorial-09-元件化 |
| 10 | vue-10-Composition-API | vue-turtorial-10-composition-api |
| 11 | vue-11-元件通訊與Pinia | 12-元件通訊與Pinia圖片整理 |
| 12 | vue-12-元件通訊進階 | 13-元件通訊進階圖片整理 |
| 13 | vue-13-Vue3進階實務整理 | Vue3_圖片教學整理 |
| 14 | vue-14-路由核心概念 | 01-路由核心概念 |
| 15 | vue-15-路由基本接線 | 02-Vue3路由基本接線 |
| 16 | vue-16-Vue-Router基礎 | vue-turtorial-08-vue-router基礎 |
| 17 | vue-17-to的兩種寫法 | 03-to的兩種寫法 |
| 18 | vue-18-history與hash模式 | 04-history與hash模式 |
| 19 | vue-19-命名與巢狀路由 | 05-命名與巢狀路由 |
| 20 | vue-20-路由元件生命週期 | 06-路由元件生命週期 |
| 21 | vue-21-路由傳參query與params | 07-路由傳參-query與params |
| 22 | vue-22-路由props配置 | 08-路由props配置 |
| 23 | vue-23-replace屬性 | 09-replace屬性 |
| 24 | vue-24-程式設計式導航 | 10-程式設計式導航 |
| 25 | vue-25-Vue-Router進階 | vue-turtorial-13-vue-router進階 |
| 26 | vue-26-Pinia集中式狀態管理 | 11-pinia集中式狀態管理 |
| 27 | vue-27-Vuex狀態管理 | vue-turtorial-12-vuex狀態管理 |
| 28 | vue-28-Vite工具 | vue-turtorial-14-vite工具 |
| 29 | vue-29-Vue動畫 | vue-turtorial-11-動畫 |
| 30 | vue-30-SSR服務端渲染 | vue-turtorial-15-ssr |
| 31 | vue-31-實戰doubanmovie | vue-turtorial-16-實戰doubanmovie |

---

## 快速查詢索引

### 按主題查詢

| 想查的主題 | 對應檔案 |
|-----------|---------|
| v-model | vue-02、vue-11、vue-13 |
| ref / reactive | vue-04、vue-08 |
| watch | vue-05、vue-13 |
| props / defineProps | vue-04、vue-11 |
| emit / 自訂事件 | vue-11、vue-13 |
| $attrs / provide-inject | vue-12 |
| slot 插槽 | vue-08、vue-12 |
| 路由基礎 | vue-14、vue-15、vue-16 |
| 路由傳參 | vue-21、vue-22 |
| 程式設計式導航 | vue-24 |
| Pinia | vue-26、vue-11（A 部分） |
| Vuex | vue-27 |
| 生命週期 | vue-06、vue-20 |
| 自定義指令 | vue-13 |
| SSR | vue-30、vue-31 |
| 動畫 | vue-29 |
