---
title: "Vue 教學 08 - 響應式進階整理"
date: 2026-03-22T20:08:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "響應式"
- "shallowRef"
- "shallowReactive"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Vue3 響應式進階整理筆記

整理日期：2026-03-22

## 1. Slot（插槽）核心觀念

### 圖片重點
- 子元件 `Game.vue` 透過 `<slot :youxi="games" x="哈哈" y="你好"></slot>` 把資料丟給父元件。
- 父元件 `Father.vue` 可用多種語法接收：
  - `v-slot="params"`，再用 `params.youxi`
  - `#default="{ youxi }"` 解構接收
- 口訣：**資料在子元件，結構在父元件決定**。

### 一句話記憶
- 你可以把插槽想成：子元件提供「內容材料」，父元件決定「排版樣式」。

---

## 2. shallowRef 與 shallowReactive

### shallowRef
- 用途：建立淺層 ref，只追蹤 `.value` 本身的替換。
- 重點：
  - `person.value = 新物件` 會觸發更新。
  - `person.value.name = '李四'` 這種深層修改通常**不會**觸發（因為內層不是深度代理）。

### shallowReactive
- 用途：建立淺層 reactive 物件。
- 重點：
  - 只追蹤第一層屬性。
  - 巢狀物件（如 `options.color`）不是深度響應。

### 什麼時候用
- 物件很大、深層資料很多、你只在乎頂層替換時。
- 想減少深度代理的效能成本。

### 常見誤區
- 看到 `shallowRef` 就以為跟 `ref` 一樣深度追蹤。
- 在 `shallowReactive` 裡直接改深層欄位，卻期待畫面更新。

---

## 3. readonly 與 shallowReadonly（從截圖脈絡延伸）

### readonly
- 提供深層只讀保護。
- 任何層級都不該直接改值。

### shallowReadonly
- 只有第一層只讀。
- 深層屬性仍可能可變（需特別注意）。

### 實務建議
- 對外暴露狀態（例如給別的模組）時，優先考慮 `readonly`。
- 若只想限制頂層 API 變動，可用 `shallowReadonly`。

---

## 4. toRaw 與 markRaw

### toRaw
- 用途：取出 reactive 代理物件背後的原始物件。
- 重點：
  - 拿到的是原始資料參考。
  - 適合短暫讀取、與非 Vue 函式庫互通。
  - 不建議長期持有並到處修改，避免狀態混亂。

### markRaw
- 用途：標記某個物件「永遠不要被轉成響應式」。
- 適用場景：
  - 第三方例項（地圖、圖表、播放器、SDK 例項）
  - 大型靜態資料

### 常見組合
- `markRaw(obj)` 後再 `reactive(obj)`，通常仍維持非響應式核心行為。

---

## 5. 這批圖片的學習路線（重排後）

1. 先懂 Slot：資料來源與結構控制權分離。
2. 再懂淺層響應：`shallowRef` / `shallowReactive` 的更新邏輯。
3. 補只讀控制：`readonly` / `shallowReadonly` 的邊界。
4. 再掌握原始物件：`toRaw` / `markRaw` 的使用時機。
5. 最後學 `customRef`：自己控制追蹤與觸發時機（例如防抖）。

---

## 6. 快速對照表

| 主題 | 核心作用 | 會追蹤深層嗎 | 常見用途 |
|---|---|---|---|
| slot（作用域插槽） | 子給資料，父定結構 | 不適用 | 元件內容客製化 |
| ref | 單值/物件響應式容器 | 物件內部會被深度代理（一般情況） | 一般狀態管理 |
| shallowRef | 只追蹤 `.value` 替換 | 否 | 大物件、效能最佳化 |
| reactive | 物件深度響應式 | 是 | 一般物件狀態 |
| shallowReactive | 只追蹤第一層 | 否 | 控制代理成本 |
| readonly | 深層只讀保護 | 不可改 | 對外唯讀暴露 |
| shallowReadonly | 第一層只讀 | 深層可能可改 | 限制 API 入口 |
| toRaw | 取原始物件 | 不適用 | 與外部系統互通 |
| markRaw | 永不轉響應式 | 不適用 | 第三方例項/大型靜態資料 |
| customRef | 自訂 ref 的追蹤與觸發 | 由你決定 | 防抖輸入、節流、延遲更新 |

---

## 7. customRef（這批新圖重點）

### 一句話
- `customRef` 是「可程式化的 ref」：你可以自己決定何時 `track()`、何時 `trigger()`。

### 從截圖可看到的推導流程
1. 先用普通 `ref` + `v-model` 繫結輸入框（基準版）。
2. 改成 `customRef(() => ({ get, set }))` 的骨架。
3. 在 `get()` 裡回傳值；在 `set(value)` 裡接收新值。
4. 補上 `initValue` 暫存真實資料。
5. 改成 `customRef((track, trigger) => ({ ... }))`。
6. 在 `get()` 呼叫 `track()`：讓 Vue 建立依賴追蹤。
7. 在 `set()` 更新資料後呼叫 `trigger()`：通知 Vue 重新渲染。
8. 最後加上 `setTimeout` + `clearTimeout`，完成防抖輸入。

### 精簡範例（防抖 1000ms）

```ts
import { customRef } from 'vue'

function useDebouncedRef(initialValue: string, delay = 1000) {
  let value = initialValue
  let timer: number | undefined

  return customRef<string>((track, trigger) => ({
    get() {
      track()
      return value
    },
    set(newValue: string) {
      window.clearTimeout(timer)
      timer = window.setTimeout(() => {
        value = newValue
        trigger()
      }, delay)
    }
  }))
}
```

### 為什麼一定要 `track()` / `trigger()`
- 沒有 `track()`：模板讀到值時不會被追蹤，後續更新可能不重渲染。
- 沒有 `trigger()`：即使值改了，Vue 也不知道要更新畫面。

### 這批圖中的常見坑
- 只寫 `get` / `set` 但沒接 `(track, trigger)` 引數。
- `set()` 有改 `initValue`，卻忘了呼叫 `trigger()`。
- 防抖場景沒先 `clearTimeout`，造成多次延遲更新疊加。

### 與 `ref` 的關係
- `ref`：Vue 幫你固定好追蹤規則，開箱即用。
- `customRef`：你接管規則，換取更高彈性。

---

## 8. 你這組截圖最重要的一句總結

**Vue3 的高階 API 本質是在「控制響應式的深度、邊界與觸發時機」；插槽是結構控制，`customRef` 是更新時機控制。**

---

## 9. 本次上傳圖片逐張整理（customRef 實作線）

### 9.1 流程總覽
- 先回顧 `markRaw` 定位：某些資料不該被響應式化。
- 進入 `customRef` 主題：用來自訂 `ref` 的依賴追蹤與更新觸發。
- 在 `App.vue` 先用 `ref + v-model` 建立基準行為。
- 改寫成 `customRef`，逐步補齊 `get` / `set`。
- 再補 `track()` 與 `trigger()` 讓畫面可正確追蹤與更新。
- 最後加上 `timer + clearTimeout + setTimeout`，完成防抖。
- 抽離成 `useMsgRef.ts`，變成可重用的組合式函式。

### 9.2 逐張重點（依你提供順序）
1. `markRaw` 回顧畫面
- 強調：被 `markRaw` 標記的物件，不會再被 `reactive` 深入轉換。

2. `7.4 customRef` 章節開場
- 定義出現：可手動控制何時追蹤、何時觸發更新。

3. `App.vue` 的基準版
- `h2` 顯示 `msg`，`input` 用 `v-model="msg"`。
- 腦中基準：先確認普通 `ref` 的行為。

4. 改成 `customRef` 骨架
- 開始寫 `customRef(() => { return { get(){}, set(){} } })`。

5. 補上「何時呼叫」註解
- `get` 對應讀取時機。
- `set` 對應寫入時機。

6. `get` / `set` 先有基本內容
- `get` 先回傳字串。
- `set` 先印 log，驗證有接到 `value`。

7. 匯入 `initValue`
- 改成由 `initValue` 統一儲存狀態。
- `get` 回傳 `initValue`，`set` 改寫 `initValue = value`。

8. 補上 `(track, trigger)`
- 寫成 `customRef((track, trigger) => ({ ... }))`。
- 進入 customRef 核心：手動宣告依賴與通知更新。

9. 補齊 `track()` / `trigger()`
- `get` 內 `track()`：讀取時建立依賴。
- `set` 末 `trigger()`：寫入後通知渲染。

10. 加入防抖計時器
- 宣告 `timer:number`。
- `set` 內先 `clearTimeout(timer)` 再 `setTimeout(...)`。
- 延遲後才更新 `initValue` 並 `trigger()`。

11. 抽離到 `useMsgRef.ts`
- 把邏輯從 `App.vue` 移到 composable，提升可讀性與重用性。

12. 引數化 composable
- 介面改成 `function(initValue:string, delay:number)`。
- 讓初始值與延遲時間可由外部傳入。

13. 保留空骨架 + `return {msg}`
- 教學畫面短暫收斂成骨架，凸顯最終輸出介面。

14. 在 `App.vue` 使用 `useMsgRef`
- `let {msg} = useMsgRef('你好', 2000)`。
- 結果：UI 維持 `v-model` 用法，但更新行為改為「延遲觸發」。

### 9.3 你可以用來複習的口訣
- `get` 要 `track`：讀取時納入依賴。
- `set` 要 `trigger`：寫入後通知更新。
- 防抖三件事：`clear`、`delay`、`trigger`。

### 9.4 一眼看懂版本演進
- v1：`ref('你好')`。
- v2：`customRef` 空骨架。
- v3：`initValue` 資料落地。
- v4：`track/trigger` 響應式接通。
- v5：`timer` 防抖。
- v6：抽離 `useMsgRef`，元件只保留使用端程式。

---

## 10. 本次上傳圖片逐張整理（Vue3 新元件與 API 遷移）

### 10.1 章節地圖
- 8.1 `Teleport`
- 8.2 `Suspense`
- 8.3 全域性 API 轉移到應用物件（app instance）
- 8.4 其他破壞性/行為變更

### 10.2 Teleport（彈窗案例）

#### 圖片重點
1. 教材先示範一般彈窗：`Modal.vue` 裡用 `v-show` 控制顯示。
2. `App.vue` 與 `Modal.vue` 各自有樣式；彈窗嘗試 `position: fixed` 置中。
3. 畫面特別框出父層 `.outer` 的 `filter: saturate(200%)`。
4. 同時把 `Modal` 的 fixed 相關定位框起來打叉，暗示「定位出問題」。
5. 之後改為：

```vue
<teleport to="body">
  <div class="modal" v-show="isShow">...</div>
</teleport>
```

#### 這段教學真正想說的事
- `Teleport` 會把元件的渲染結果「搬移」到指定 DOM（例如 `body`）。
- 當父層存在某些屬性（像 `transform/filter/perspective` 等）可能影響定位上下文時，彈窗 UI 容易跑位。
- 把彈窗 Teleport 到 `body`，可以避免受原本父層佈局影響，特別適合 Modal/Drawer/Tooltip。

#### Teleport 口訣
- **邏輯留在元件，DOM 掛到外層。**

### 10.3 Suspense（等待非同步元件）

#### 圖片重點
1. 章節頁先給標準結構：`default` 與 `fallback` 兩個插槽。
2. `App.vue` 使用：

```vue
<Suspense>
  <template v-slot:default>
    <Child/>
  </template>
  <template v-slot:fallback>
    <h2>載入中.......</h2>
  </template>
</Suspense>
```

3. `Child.vue` 內有 `await axios.get(...)`（在 `script setup` 中非同步取資料）。
4. 圖上先打叉只寫 `default` 的版本，再補齊 `fallback`。

#### 實務重點
- 只要子樹有 async 依賴（例如 async setup、非同步元件），`Suspense` 能統一顯示等待畫面。
- `default` 放「真正內容」，`fallback` 放「載入佔位內容」。
- 好處是不用在每個子元件各自硬寫一套 loading UI。

#### Suspense 口訣
- **內容慢慢來，先給 fallback。**

### 10.4 8.3 全域性 API 轉移到 app 例項

#### 圖片重點
- 清單圈出：
  - `app.component`
  - `app.config`
  - `app.directive`
  - `app.mount`
  - `app.unmount`
  - `app.use`
- 程式碼示範在 `main.ts`：
  - `const app = createApp(App)`
  - `app.component('Hello', Hello)`
  - `app.config.globalProperties.x = 99`
  - `app.directive('beauty', ...)`

#### 觀念整理
- Vue2 多數全域能力掛在 `Vue` 全域物件；Vue3 改為掛在「應用例項」`app`。
- 核心目的：不同 app 互不汙染，測試與多應用掛載更清楚。
- TypeScript 場景要配合擴充型別（例如 `ComponentCustomProperties`）才能安全使用 `this.x`。

### 10.5 8.4 其他（圖上條列彙整）

#### 截圖列到的變更
- 過渡 class 名稱：`v-enter` 改為 `v-enter-from`、`v-leave` 改為 `v-leave-from`。
- `keyCode` 作為 `v-on` 修飾符的支援移除。
- 元件上的 `v-model` 語法重設計，取代舊的 `v-bind.sync` 思維。
- `v-if` 與 `v-for` 同元素使用時的優先順序有調整。
- 移除 `$on`、`$off`、`$once` 例項方法。
- 移除過濾器 `filter`。
- 移除 `$children`。

#### 這區塊的學習策略
- 先記「哪些 API 不在了」，再找對應替代方案。
- 若在維護舊專案，這一段是 migration check-list 的高風險區。

### 10.6 一頁速記（這批圖最重要）
- `Teleport`：解決彈窗等浮層的 DOM 掛載位置問題。
- `Suspense`：解決非同步內容顯示節奏問題。
- `app.*`：解決 Vue2 全域汙染問題，改成 app 級管理。
- `8.4 其他`：解決舊語法相容問題，屬於升級必查清單。
