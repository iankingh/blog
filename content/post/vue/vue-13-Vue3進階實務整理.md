---
title: "Vue 教學 13 - Vue3 進階實務整理"
date: 2026-03-22T20:13:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "進階"
- "TypeScript"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Vue3 進階實務整理

> 整理日期：2026-03-22  
> 資料來源：本資料夾 46 張截圖（B 站教學畫面、VS Code 程式碼畫面、瀏覽器結果畫面）

## 一、這批圖片主要在講什麼

這批截圖主軸是 Vue3 + TypeScript 的實作與原理，重點集中在：

- 元件通訊：`props`、`emit`、Event Bus
- `v-model` 在元件上的用法（含 Vue3 命名規則）
- 自定義指令（directive）與生命週期鉤子
- `computed`、`watch` 的實務寫法
- Vue3 原始碼閱讀（`reactivity`、`runtime-core`）

---

## 二、重點筆記（可直接當複習提綱）

### 1. 元件通訊（A/B 元件示例）

- 子元件透過 `defineEmits` 觸發事件，父元件接收後更新狀態。
- 另一種方式是 Event Bus：
  - 建立 `Bus.ts`，提供 `on` 與 `emit`。
  - A 元件 `emit`，B 元件 `on` 訂閱。
- 這兩種方式差異：
  - 父子單向資料流，優先用 `props + emit`。
  - 跨層或非父子時，Bus 可快速打通，但大型專案建議改 Pinia。

### 2. Vue3 的 v-model（破壞性更新重點）

- Vue2：預設 `value` + `input`。
- Vue3：預設 `modelValue` + `update:modelValue`。
- 元件要支援 `v-model`，本質是：
  - `defineProps` 接收 `modelValue`
  - `defineEmits(['update:modelValue'])` 回傳變更
- 可擴充套件多個 `v-model` 與修飾詞（modifiers）。

### 3. 自定義指令（directive）

- Vue3 指令週期常見：`created`、`beforeMount`、`mounted`、`beforeUpdate`、`updated`、`beforeUnmount`、`unmounted`。
- 圖中範例包含：
  - 區域指令命名（`vNameOfDirective`）
  - 函式簡寫（只處理 `mounted/updated` 行為時可用）
  - 圖片懶載入（`IntersectionObserver`）
  - 許可權按鈕顯示/隱藏（`v-has-show` 型別邏輯）

### 4. 生命週期與 DOM 取得時機

- `onBeforeMount` 通常拿不到最終 DOM。
- `onMounted` 後可安全讀取 DOM。
- 更新期可對比：
  - `onBeforeUpdate`：更新前狀態
  - `onUpdated`：更新後狀態
- 解除安裝期：`onBeforeUnmount` / `onUnmounted`。
- 進階追蹤：`onRenderTracked`、`onRenderTriggered`（用於依賴收集與觸發除錯）。

### 5. computed 實作與使用

- `computed` 可用 `getter` 單向衍生。
- 也可使用 `get/set` 雙向處理（例如拆分與組合姓名）。
- 截圖中的實務案例：
  - 購物車總價 `total`
  - 關鍵字篩選 `searchData`

### 6. watch 的常用選項

- 常見引數：`deep`、`immediate`、`flush`。
- `flush` 時機：`pre` / `post` / `sync`。
- 深層物件監聽與 `v-model` 聯動在截圖中有示範。

### 7. Vue3 原始碼閱讀路徑（截圖對照）

- `packages/reactivity/src/computed.ts`
- `packages/reactivity/src/ref.ts`
- `packages/runtime-core/src/apiLifecycle.ts`
- `KeepAlive` 相關程式碼畫面

建議閱讀順序：

1. 先懂 API 怎麼用（computed/watch/lifecycle）
2. 再看對應實作檔案
3. 最後對照實際專案行為（Console + DOM）

---

## 三、可直接練習的題目

1. 做一個可重用 Dialog 元件，完整支援 `v-model`（開關 + 內容同步）。
2. 寫一個 `v-permission` 指令，依角色控制按鈕顯示。
3. 寫一個 `v-lazy` 指令，滾動到可視區才載入圖片。
4. 用 `computed` 完成購物車總價、搜尋、分類統計。
5. 用 `watch` 比較 `flush: pre/post/sync` 的更新差異。

---

## 四、速讀總結（章節精簡版）

- 元件通訊：父子關係優先使用 `props + emit`；跨層通訊可用 Bus，但中大型專案建議採 Pinia。
- `v-model`：Vue3 改為 `modelValue` + `update:modelValue`，本質是 `props + emits`。
- 自定義指令：常見於許可權控制、懶載入、DOM 行為封裝；需掌握指令生命週期。
- 生命週期：DOM 安全讀取時機在 `onMounted` 與 `onUpdated`，更新前後行為可用 before/after 鉤子觀察。
- `computed`：適合衍生資料與快取，若有反向寫入需求可用 `get/set`。
- `watch`：用於副作用與監聽流程控制，常用 `deep`、`immediate`、`flush`。
- 原始碼學習路徑：先 API 實作，再對照 `reactivity` 與 `runtime-core` 關鍵檔案。

---

## 五、複習順序建議

1. 先做元件通訊與 `v-model` 小練習，確認資料流方向。
2. 補上 directive（許可權與懶載入）建立可重用能力。
3. 用 `computed` + `watch` 完成一個小型資料互動頁。
4. 最後閱讀對應原始碼，加深對響應式與生命週期機制的理解。

---

## 六、後續可加值

- 若要逐圖教學，可再補每張圖的「看圖重點」一行註解。
- 若要面試用途，可再濃縮成 1 頁「Vue3 常考速記」。
