---
title: "Vue 教學 12 - 元件通訊進階"
date: 2026-03-22T20:12:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "元件通訊"
- "$attrs"
- "provide/inject"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 元件通訊進階整理

## 目的
這份整理承接上一份筆記，專門對應你新提供的截圖主題：
1. $attrs
2. $refs 與 defineExpose（含 $parent 概念）
3. provide / inject
4. slot（預設插槽、具名插槽）

## A. $attrs（父到子到孫）

### A1. 核心觀念
1. $attrs 會收集父元件傳給子元件、但沒有被子元件 props 宣告的屬性。
2. 子元件可用 v-bind="$attrs" 一次轉交給更下層（祖 -> 孫）。
3. 已在 defineProps 中宣告過的欄位，不會出現在 $attrs 內。

### A2. 你圖中的流程
1. Father 傳入 a、b、c、d 與額外 x、y。
2. Child 只宣告 a。
3. Child 內其餘資料在 $attrs，並透過 v-bind="$attrs" 傳給 GrandChild。
4. GrandChild 可直接看到 b、c、d、x、y 等屬性。

### A3. 最小示意
```vue
<!-- Father.vue -->
<Child :a="a" :b="b" :c="c" :d="d" v-bind="{ x: 100, y: 200 }" />

<!-- Child.vue -->
<template>
  <GrandChild v-bind="$attrs" />
</template>
<script setup lang="ts">
defineProps(['a'])
</script>
```

## B. $refs、defineExpose、$parent

### B1. 核心觀念
1. 在 Vue3 script setup 裡，父元件要透過 ref 拿到子元件公開資料，子元件必須用 defineExpose。
2. 子元件不 expose 的內容，父元件無法直接存取。
3. 教學裡常把它和 $parent 一起講：
- $refs：父找子（推薦）
- $parent：子找父（耦合高，通常不建議作主流程）

### B2. 你圖中的流程
1. Father 用 c1、c2 繫結 Child1、Child2 的 ref。
2. Child1、Child2 分別 defineExpose 自己要給外部用的資料（如 toy、book、computer）。
3. Father 透過 c1.value / c2.value 直接修改子元件公開狀態。

### B3. 最小示意
```vue
<!-- Father.vue -->
<Child1 ref="c1" />
<Child2 ref="c2" />

<script setup lang="ts">
import { ref } from 'vue'
let c1 = ref()
let c2 = ref()

function changeToy() {
  c1.value.toy = '小豬佩奇'
}
</script>

<!-- Child1.vue -->
<script setup lang="ts">
import { ref } from 'vue'
let toy = ref('奧特曼')
let book = ref(3)
defineExpose({ toy, book })
</script>
```

## C. provide / inject（跨層直達）

### C1. 核心觀念
1. provide 由祖先元件提供資料。
2. inject 由後代元件接收資料，不用一層一層 props 傳遞。
3. 建議注入 key 名稱一致、語義清楚（例如 money、car、moneyContext）。

### C2. 你圖中的流程
1. Father 提供 money（ref）與 car（reactive）。
2. GrandChild 注入後直接顯示資料。
3. 進一步版本：把資料與函式一起包成 context 注入（例如 { money, updateMoney }）。
4. GrandChild 點按鈕呼叫 updateMoney，直接回寫祖先狀態。

### C3. 最小示意
```vue
<!-- Father.vue -->
<script setup lang="ts">
import { ref, reactive, provide } from 'vue'

let money = ref(100)
let car = reactive({ brand: '賓士', price: 100 })

function updateMoney(value: number) {
  money.value -= value
}

provide('moneyContext', { money, updateMoney })
provide('car', car)
</script>

<!-- GrandChild.vue -->
<script setup lang="ts">
import { inject } from 'vue'

let { money, updateMoney } = inject('moneyContext') as any
let car = inject('car', { brand: '未知', price: 0 })
</script>
```

## D. slot（內容分發）

### D1. 預設插槽
1. 子元件用 <slot>預設內容</slot>。
2. 父元件在元件標籤內放內容，即可替換預設內容。

### D2. 具名插槽
1. 子元件宣告多個 slot name（例如 s1、s2）。
2. 父元件透過 template v-slot:s1 / template v-slot:s2 指定填入位置。
3. 縮寫可用 #s1、#s2。

### D3. 你圖中的典型結構
1. Category.vue 負責容器外觀。
2. Father.vue 針對不同分類（遊戲、美食、影片）塞入不同內容。
3. 同一個 Category 元件可重複使用，靠 slot 變化內容。

### D4. 最小示意
```vue
<!-- Category.vue -->
<template>
  <div class="category">
    <slot name="s1">預設內容1</slot>
    <slot name="s2">預設內容2</slot>
  </div>
</template>

<!-- Father.vue -->
<Category>
  <template #s1>
    <h2>熱門遊戲列表</h2>
  </template>
  <template #s2>
    <ul>
      <li v-for="g in games" :key="g.id">{{ g.name }}</li>
    </ul>
  </template>
</Category>
```

## E. 選型速記
1. 父傳子：props
2. 子傳父：emit
3. 跨層共享資料：provide/inject 或 Pinia
4. 父主動操作子公開能力：ref + defineExpose
5. 元件內容客製化：slot
6. 屬性透傳：$attrs

## F. 這批圖片的一頁結論
1. $attrs 是「未宣告 props 的剩餘屬性」，適合多層透傳。
2. ref 在 script setup 要搭配 defineExpose 才能讓父元件安全存取。
3. provide/inject 能解決祖孫傳資料，不必層層轉手。
4. slot 讓同一個元件殼可承載不同內容，提高重用性。
