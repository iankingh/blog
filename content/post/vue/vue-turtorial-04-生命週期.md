---
title: "Vue Turtorial 04 生命週期"
date: 2024-08-27T07:40:09+08:00
categories:
- "筆記"
tags:
- "tag1"
- "tag2"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 這是範本的使用(標題)

## 前言(各章節)

绝件的生命週期:

【時刻】【調用特定的函數】
創建 created

掛載 mounted

更新
销毁

生命週期、生命週期函數、生命週期鉤子

創建 (創建前,創建完毕)


掛載 (掛載前,掛載完毕)


更新 (更新前,更新完毕)


销毁 (销毁前,销毁完毕)



概心: Vue組件實例住創建时要經歷一系外的制始化步球,在此過程中 Vue 会仕合適的 商健港特感開,1
数,从而让開發者有機會在特定階段運行自己的程式碼,这些特定的函數統稱为:生命週期鉤子
 · 规律:

生命週期整体分为四个階段,分别是:創建、掛載、更新、销毁,每个階段都有两个鉤子,一前一后.

 · Vue2 的生命週期

創建階段: beforeCreate、 created

掛載階段: beforeMount、 mounted

更新階段: beforeUpdate、 updated

销毁階段 beforeDestroy、 destroyed

 · Vue3 的生命週期

創建階段: setup

掛載階段: onBeforeMount、 onMounted

更新階段: onBeforeUpdate、 onupdated

销毁階段: onBeforeUnmount onUnmounted

 · 常用的鉤子: onMounted(掛載完毕)、 onupdated (更新完毕)、 onBeforeUnmount (卸载之前)

 · 示例程式碼:

 尚硅谷 創建階段: beforeCreate、 created

14:3Z 掛載階段: beforeMount、 mounted

更新階段: beforeUpdate、 updated

销毁階段: beforeDestroy、 destroyed

Vue3 的生命週期

創建階段: setup

掛載階段: onBeforeMount、 onMounted

更新階段: onBeforeUpdate、 onUpdated

卸载階段: onBeforeUnmount onUnmounted

常用的鉤子: onMountea( 掛載完毕)、 onUpdated (更新完毕)、 onBeforeUnmount(卸载之前) 示例程式碼:

<template〉

＜h2>當前求和为:{{ sum }}/h2>
<button @click="changeSum">点我sum+1</button></div>

</template>

```
<template〉

<div class="person">
<h2>當前求和为:{{ sum }}</h2>
<button @click="add">点我sum+1</button>
<hr>
<img v-for="(dog,index)in dogList" :src="dog" :key="index">

</div>

</templatex

I

<script lang="ts" setup name="Person">

import {ref, reactive} from 'vue'
import axios from 'axios'

// 数据

let sum = ref(0)
let doglist = reactive([
'https://images.dog.ceo/breeds/pembroke/n2113023_4373.jpg' ])

1/ 方法

function add(){

sum.value += 1
```


```
</aIV>
</template>

<script lang="ts" setup name="Person">

import {ref, reactive} from 'vue'
import axios from 'axios'

// 数据

let sum = ref(0)
let doglist = reactive([

'https://images.dog.ceo/breeds/pembroke/n92113023 4373.jpg'

])

1/ 方法

function add(){

sum.value += 1

async function getDog(){

let result = await axios.get('https://dog.ceo/api/breed/pembroke/images/ doglist.push(result.data.message)

}

</script>
```

## CSS
```
<style scoped>
person {

background-color: skyblue; box-shadow: 0 0 10px; border-radius: 10px; padding: 20px; }

button
margin: 5px; }

1i {

font-size: 20px; }

img {

height: 100px; margin-right: 10px; }
```

```
<script>
export default [ /* eslint-disable */ name: 'Person',

// 数据

 · .. data(){

// 方法

methods:{…
}, I

// 創建前的鉤子
beforeCreate(){ console.1og('創建前') },


```

```
methods:{…
},

// 創建前的鉤子beforeCreate(){… },

// 創建完毕的鉤子
created(){…

},

// 掛載前

beforeMount(){
console.1og('掛載前'DF},

// 掛載完毕
mounted(){

console.1og('掛載完毕') }s
```

```
created(){…

/ 掛載前beforeMount(){ console.1og('掛載前') },
掛載完毕
mounted(){

console.1og('掛載完毕') / 更新前beforeUpdate(){ console.1og('更新前') },

/ 更新完毕
updated(){
console.1og(更新完毕:) }

[
}
```

創建(創建前 i beforeCreate,創建完毕 created)
掛載(掛載前,掛載完毕)

更新(更新前,更新完毕)

销毁(销毁前,销毁完毕)

```
beforeMount(){
console.1og('掛載前') },

// 掛載完毕

mounted(){

console.1og('掛載完毕') // 更新前

IbeforeUpdate(){
console.1og('更新前') // 更新完毕
updated({
console.log('更新完毕') },

// 销毁前

beforeDestroy(){
console.1og('销毁前') },

// 销毁完毕

destroyed(){
```


```
<button @click="add">点我sum+1</button>
</div>
</template>

<script 1ang="ts" setup name="Person">
import {ref} from 'vue'

// 数据

let sum = ref(0)

// 方法

function add(){

sum.value += 1

一> setup }
// 創建 beforeCreate created

</script>

 · <style scoped>
</style>
```
```
}

// 創建

console.1og('創建') // 掛載前

onBeforeMount(()=>{ console.log('掛載前') })

掛載完毕onMounted(()=>{ console.1og('掛載完毕') })

// 更新前onBeforeUpdate(()=>{ console.log('更新前') })

// 更新完毕onUpdated(C)=>{ console.1og('D
```

```
})
// 更新前

onBeforeUpdate(()=>{ console.1og('更新前') })
// 更新完毕

onUpdated(()=>{
console.log('更新完毕') })
// 卸载前

onBeforeUnmount(()=>{ console.log('卸载前') })
// 卸载完毕

onUnmounted(()=>{ console.log('卸载完毕') })
```

```
<template>
<Person v-if="isshow"/>
</template>

<script lang="ts" setup name="App">
import Person from'./components/Person.vue' import {ref, onMounted} from 'vue'

let isShow = ref(true)

// 掛載完毕

onMounted(()=>{

console.1og('父---掛載完毕"】

}

</script>
```

```
<template》
<div class-"penson"

<h2>當前冰和为:{ sum }s/h2>
《button @click-"add">点我sum+1</button>

</div>
</template>

《script lang-"ts" setup name-"Person">
import (ref, onBeforeMount, onMlounted, onBeforelpdate, onlpdated, onBeforeUnmount, onlnmounted} from 'vue'
// 效瓶
1et sum - ref(0)
1/ 方法
function addC)f

sum.value +- 1

1/ 創建
console.1og('創建:)

1/ 掛載前

onBeforeMlount(()-x{

// console.1og('挂前")

// 掛載完毕
onMounted(()-2/

console.1og(' - -挂 完毕”)

1! 更新前
onBeforelpdate(()-y

1/ console.1og('更新前")

})
1/ 更新完毕
onlpdated(()-y

console.1og('更新完毕”)

})
1/ 卸载前
onBeforeUnmount(()

 · 1/ console.1og('卸或前")

})

// 卸或完毕

onUnmounted(C)-2{

1/ console.1og('卸或完毕")

</scPipt>
```


## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
