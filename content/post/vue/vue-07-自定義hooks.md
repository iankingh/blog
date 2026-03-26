---
title: "Vue 教學 07 - 自定義 hooks"
date: 2026-03-22T20:07:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "hooks"
- "Composition API"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 這是範本的使用(標題)

## 前言(各章節)

import {ref, reactive} from 'vue'
import axios from'axios'

// 資料
let sum = ref(0)
let doglist = reactive([

'https://images.dog.ceo/breeds/pembroke/ne2113023_4373.jpg' ])

// 方法

function add()5.

hooks ??.js / ??.tsasync function getDog() {⋯
}
</script>

<style scoped〉…
</style>

useDog useOrder

useTeacher


```
import {reactive} from 'vue'

import axios from 'axios'

export default function (){
// 資料

let doglist = reactive([
'https://images.dog.ceo/breeds/pembroke/n@2113023_4373.jpg'

)

/ 方法

async function getDog(){

try{

let result = await axios.get('https://dog.ceo/api/breed/pembroke/images/ndogList.push(result.data.message)

} catch (error){
alert(error)
}

給外部提供東西
return {doglist, getDog}

}
```

```
import { ref }from 'vue'
export default function (){
// 資料
let sum = ref(0)

11 方法
function add(){

sum.value += 1

}

// 給外部提供東西
return [sum,addj
```

```
<template〉

<div class="penson">
<h2>目前求和為:{{ sum }}</h2>
<button @click="add">點我sum+1</button>
<hr>
<img v-for="(dog,index) in dogList" :src="dog" :key="index"><br>
<button @click="getDog">再來一隻小狗</button>
</div>

</template>

<script lang="ts" setup name="Person">
import useSum from'@/hooks/useSum'

import useDog from '@/hooks/useDog'

const {sum, add} = useSum()
const {dogList, getDog} = useDog()

</script>

I

<style scoped〉…
</style>
```

```
<template〉
<div class="penson">
＜h2>目前求和為:{{ sum }},放大10倍後: {{ bigsum }}</h2>

<button @click="add">點我sum+1</button〉 <hr>
<img v-for="(dog, index) ) in dogList" :src="dog" :key="index">

<br>
<button @click="getDog">再來一隻小狗</button></div>
</template〉

<script lang="ts" setup name="Person">
import useSum from '@/hooks/useSum'
import useDog from'@/hooks/useDog'

const {sum,add, bigsum} = useSum()
const {dogList,getDog} = useDog ()
</script>

<style scoped>…
</style〉
```




## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
