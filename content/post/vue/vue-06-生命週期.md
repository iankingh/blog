---
title: "Vue 教學 06 - 生命週期"
date: 2026-03-22T20:06:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "生命週期"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 元件的生命週期

## 前言

元件的生命週期:

【時刻】【呼叫特定的函式】
建立 created

掛載 mounted

更新
銷毀

生命週期、生命週期函式、生命週期鉤子

建立 (建立前,建立完畢)


掛載 (掛載前,掛載完畢)


更新 (更新前,更新完畢)


銷毀 (銷毀前,銷毀完畢)



核心：Vue 元件例項在建立時要經歷一系列的初始化步驟，在此過程中 Vue 會在合適的時機呼叫特定函
數，從而讓開發者有機會在特定階段執行自己的程式碼，這些特定的函式統稱為：生命週期鉤子
 · 規律:

生命週期整體分為四個階段,分別是:建立、掛載、更新、銷毀,每個階段都有兩個鉤子,一前一後.

 · Vue2 的生命週期

建立階段: beforeCreate、 created

掛載階段: beforeMount、 mounted

更新階段: beforeUpdate、 updated

銷毀階段 beforeDestroy、 destroyed

 · Vue3 的生命週期

建立階段: setup

掛載階段: onBeforeMount、 onMounted

更新階段: onBeforeUpdate、 onupdated

銷毀階段: onBeforeUnmount onUnmounted

 · 常用的鉤子: onMounted(掛載完畢)、 onupdated (更新完畢)、 onBeforeUnmount (解除安裝之前)

 · 示例程式碼:

 尚矽谷 建立階段: beforeCreate、 created

14:3Z 掛載階段: beforeMount、 mounted

更新階段: beforeUpdate、 updated

銷毀階段: beforeDestroy、 destroyed

Vue3 的生命週期

建立階段: setup

掛載階段: onBeforeMount、 onMounted

更新階段: onBeforeUpdate、 onUpdated

解除安裝階段: onBeforeUnmount onUnmounted

常用的鉤子: onMountea( 掛載完畢)、 onUpdated (更新完畢)、 onBeforeUnmount(解除安裝之前) 示例程式碼:

<template〉

＜h2>目前求和為:{{ sum }}/h2>
<button @click="changeSum">點我sum+1</button></div>

</template>

```
<template〉

<div class="person">
<h2>目前求和為:{{ sum }}</h2>
<button @click="add">點我sum+1</button>
<hr>
<img v-for="(dog,index)in dogList" :src="dog" :key="index">

</div>

</templatex

I

<script lang="ts" setup name="Person">

import {ref, reactive} from 'vue'
import axios from 'axios'

// 資料

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

// 資料

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

// 資料

 · .. data(){

// 方法

methods:{…
}, I

// 建立前的鉤子
beforeCreate(){ console.1og('建立前') },


```

```
methods:{…
},

// 建立前的鉤子beforeCreate(){… },

// 建立完畢的鉤子
created(){…

},

// 掛載前

beforeMount(){
console.1og('掛載前'DF},

// 掛載完畢
mounted(){

console.1og('掛載完畢') }s
```

```
created(){…

/ 掛載前beforeMount(){ console.1og('掛載前') },
掛載完畢
mounted(){

console.1og('掛載完畢') / 更新前beforeUpdate(){ console.1og('更新前') },

/ 更新完畢
updated(){
console.1og(更新完畢:) }

[
}
```

建立(建立前 i beforeCreate,建立完畢 created)
掛載(掛載前,掛載完畢)

更新(更新前,更新完畢)

銷毀(銷毀前,銷毀完畢)

```
beforeMount(){
console.1og('掛載前') },

// 掛載完畢

mounted(){

console.1og('掛載完畢') // 更新前

IbeforeUpdate(){
console.1og('更新前') // 更新完畢
updated({
console.log('更新完畢') },

// 銷毀前

beforeDestroy(){
console.1og('銷毀前') },

// 銷毀完畢

destroyed(){
```


```
<button @click="add">點我sum+1</button>
</div>
</template>

<script 1ang="ts" setup name="Person">
import {ref} from 'vue'

// 資料

let sum = ref(0)

// 方法

function add(){

sum.value += 1

一> setup }
// 建立 beforeCreate created

</script>

 · <style scoped>
</style>
```
```
}

// 建立

console.1og('建立') // 掛載前

onBeforeMount(()=>{ console.log('掛載前') })

掛載完畢onMounted(()=>{ console.1og('掛載完畢') })

// 更新前onBeforeUpdate(()=>{ console.log('更新前') })

// 更新完畢onUpdated(C)=>{ console.1og('D
```

```
})
// 更新前

onBeforeUpdate(()=>{ console.1og('更新前') })
// 更新完畢

onUpdated(()=>{
console.log('更新完畢') })
// 解除安裝前

onBeforeUnmount(()=>{ console.log('解除安裝前') })
// 解除安裝完畢

onUnmounted(()=>{ console.log('解除安裝完畢') })
```

```
<template>
<Person v-if="isshow"/>
</template>

<script lang="ts" setup name="App">
import Person from'./components/Person.vue' import {ref, onMounted} from 'vue'

let isShow = ref(true)

// 掛載完畢

onMounted(()=>{

console.1og('父---掛載完畢"】

}

</script>
```

```
<template》
<div class-"penson"

<h2>目前求和為:{ sum }s/h2>
《button @click-"add">點我sum+1</button>

</div>
</template>

《script lang-"ts" setup name-"Person">
import (ref, onBeforeMount, onMlounted, onBeforelpdate, onlpdated, onBeforeUnmount, onlnmounted} from 'vue'
// 效瓶
1et sum - ref(0)
1/ 方法
function addC)f

sum.value +- 1

1/ 建立
console.1og('建立:)

1/ 掛載前

onBeforeMlount(()-x{

// console.1og('掛前")

// 掛載完畢
onMounted(()-2/

console.1og(' - -掛載完畢”)

1! 更新前
onBeforelpdate(()-y

1/ console.1og('更新前")

})
1/ 更新完畢
onlpdated(()-y

console.1og('更新完畢”)

})
1/ 解除安裝前
onBeforeUnmount(()

 · 1/ console.1og('解除安裝前")

})

// 解除安裝完畢

onUnmounted(C)-2{

1/ console.1og('解除安裝完畢")

</scPipt>
```


## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
