---
title: "Vue Turtorial 05 自定義的hooks"
date: 2024-08-27T07:52:23+08:00
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

# 這是範本的使用（標題）

## 前言（各章節）

import ｛ref, reactive｝ from 'vue'
import axios from'axios'

11 数据
let sum = ref（0）
let doglist = reactive（［

'https://images.dog.ceo/breeds/pembroke/ne2113023_4373.jpg' ］）

// 方法

function add（）5.

hooks ？？.js / ？？.tsasync function getDog（） ｛⋯
｝
</script>

<style scoped〉…
</style>

useDog useOrder

useTeacher


```
import ｛reactive｝ from 'vue'

import axios from 'axios'

export default function （）｛
7/数据

let doglist = reactive（［
'https://images.dog.ceo/breeds/pembroke/n@2113023_4373.jpg'

）

/ 方法

async function getDog（）｛

try｛

let result = await axios.get（'https://dog.ceo/api/breed/pembroke/images/ndogList.push（result.data.message）

｝ catch （error）｛
alert（error）
｝

回外部提供东西
return ｛doglist, getDog｝

｝
```

```
import ｛ ref ｝from 'vue'
export default function （）｛
/ 数据
let sum = ref（0）

11 方法
function add（）｛

sum.value += 1

｝

// 给外部提供东西
return ［sum,addj
```

```
<template〉

<div class="penson">
<h2>当前求和为：｛｛ sum ｝｝</h2>
<button @click="add">点我sum+1</button>
<hr>
<img v-for="（dog,index） in dogList" ：src="dog" ：key="index"><br>
<button @click="getDog">再来一只小狗</button>
</div>

</template>

<script lang="ts" setup name="Person">
import useSum from'@/hooks/useSum'

import useDog from '@/hooks/useDog'

const ｛sum, add｝ = useSum（）
const ｛dogList, getDog｝ = useDog（）

</script>

I

<style scoped〉…
</style>
```

```
<template〉
<div class="penson">
＜h2>当前求和为：｛｛ sum ｝｝，放大10倍后： ｛｛ bigsum ｝｝</h2>

<button @click="add">点我sum+1</button〉 <hr>
<img v-for="（dog, index） ） in dogList" ：src="dog" ：key="index">

<br>
<button @click="getDog">再来一只小狗</button></div>
</template〉

<script lang="ts" setup name="Person">
import useSum from '@/hooks/useSum'
import useDog from'@/hooks/useDog'

const ｛sum,add, bigsum｝ = useSum（）
const ｛dogList,getDog｝ = useDog （）
</script>

<style scoped>…
</style〉
```


## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
