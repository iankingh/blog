---
title: "Vue 教學 11 - 元件通訊與 Pinia"
date: 2026-03-22T20:11:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "元件通訊"
- "Pinia"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 元件通訊與 Pinia 整理

## 目的
這份筆記是依照你提供的截圖順序整理，重點放在：
1. Pinia 基礎到進階用法
2. Vue3 元件通訊常見方式
3. v-model 在元件上的本質與細節

## A. Pinia 流程整理

### A1. 安裝與掛載
在 main.ts 先建立 app，再建立 pinia，最後安裝到 app。

重點流程：
1. import createPinia
2. const pinia = createPinia()
3. app.use(pinia)

### A2. 建立 store 與 state
用 defineStore 建立倉庫，state 是真正存資料的地方。

範例概念：
- count store：sum、school、address
- talk store：talkList

### A3. 修改資料三種方式
你的圖片中示範了三種：
1. 直接改：store.sum += 1
2. patch：store.$patch({ sum: 888, school: 'xxx' })
3. action：store.increment(value)

建議：
- 小型變更可直接改
- 批次更新可用 $patch
- 具商業邏輯一律放 action

### A4. 非同步 action（talkList）
使用 axios 取得內容，再組成物件 push 或 unshift 到 talkList。

圖片裡的核心做法：
1. await axios.get(...)
2. 解構出 content 並改名為 title
3. 用 nanoid 建立 id
4. this.talkList.unshift(obj)

### A5. storeToRefs
元件中若要解構 store 內資料，為了保留響應式要用 storeToRefs。

關鍵觀念：
- 直接解構會失去響應式
- storeToRefs(store) 解構後仍是 ref

### A6. getters
適合放需要二次計算的資料。

圖片示範：
- bigSum: state.sum * 10
- upperSchool(): this.school.toUpperCase()

### A7. 持久化與訂閱
你提供的流程有用到：
- state 初始值從 localStorage 讀取
- 透過 store.$subscribe 監聽變化
- 變化時 JSON.stringify 後回寫 localStorage

這種寫法可在不重整 store plugin 的情況下快速做本地持久化。

### A8. setup 風格 store
除了 options 寫法，也能用 defineStore('talk', () => {})。

在 setup 風格中：
1. 狀態可用 ref 或 reactive
2. action 用一般 function
3. 最後 return 要暴露的狀態與方法

## B. 元件通訊整理

### B1. props（父傳子）
父元件把資料與函式傳給子元件：
- :car="car"
- :sendToy="getToy"

子元件透過 defineProps 接收後可直接使用。

### B2. 自訂事件（子傳父）
標準流程：
1. 子元件 defineEmits([...])
2. 子元件 emit('event-name', payload)
3. 父元件以 @event-name 繫結處理函式

事件命名建議：
- 使用 kebab-case，例如 send-toy
- 避免在模板監聽端用駝峰事件名

### B3. mitt（兄弟或跨層元件）
你圖片中的模式：
1. 建立 utils/emitter.ts 並 export default mitt()
2. 需要傳送的元件 emitter.emit('send-toy', toy)
3. 需要接收的元件 emitter.on('send-toy', handler)
4. 元件解除安裝前解除監聽：off 或 all.clear()

重點：
- 接收者先繫結，傳送者再 emit
- 記得解除監聽，避免記憶體洩漏

## C. v-model 細節整理

### C1. 原生元素上的 v-model
本質等同於：
1. :value="狀態"
2. @input="狀態 = $event.target.value"

此時 $event 是原生 DOM Event，所以有 target。

### C2. 元件上的 v-model（預設）
父元件：
- <CustomInput v-model="username" />

等價於：
1. :modelValue="username"
2. @update:modelValue="username = $event"

子元件需配合：
1. defineProps(['modelValue'])
2. defineEmits(['update:modelValue'])
3. 輸入時 emit('update:modelValue', 新值)

### C3. 多個 v-model 與自訂引數
可改用具名引數：
- v-model:ming="username"
- v-model:mima="password"

對應子元件：
1. props: ming, mima
2. emits: update:ming, update:mima

### C4. $event 何時有 target
你截圖裡提到的結論非常重要：
1. 原生事件：$event 是 Event，可用 target
2. 自訂事件：$event 是 emit 傳出的 payload，通常沒有 target

## D. 圖片內容對照索引

### D1. Pinia 章節
1. Pinia 接線（main.ts）
2. count 與 talk store 的 state
3. 在元件讀取 talkList
4. 三種修改狀態方式
5. talk store 非同步 action
6. storeToRefs 與 getters
7. $subscribe + localStorage
8. setup 風格 defineStore

### D2. 元件通訊章節
1. props 父子傳值與傳函式
2. defineEmits 子傳父
3. 事件名稱建議 kebab-case
4. mitt 實作、emit/on/off
5. v-model 原生元素
6. v-model 元件 modelValue 規則
7. 自訂引數 v-model:abc
8. 多重 v-model

## E. 一頁結論
1. Pinia 負責跨元件狀態，action 放邏輯，getter 放衍生值。
2. 元件通訊由近到遠可選 props/emit、mitt、Pinia。
3. v-model 在元件上是語法糖，核心永遠是 prop + update 事件。
4. 看到 $event 先分辨是原生事件還是自訂事件，再決定能不能用 target。
