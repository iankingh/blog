---
title: "Vue 教學 04 - ref 與 reactive"
date: 2026-03-22T20:04:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "ref"
- "reactive"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Vue 學習

標籤的 ref 屬性

作用：用於註冊模板引用。
• 用在普通DOM 標籤上,獲取的是DOM節點.
• 用在元件標籤上,獲取的是元件例項物件.
用在普通DOM 標籤上:
<template>
‹div class="person" ›
<h1 ref="title1">尚矽谷</h1>
<h2 ref="title2">前端</h2>
<h3 ref="title3" >Vue</h3>
<input type="text" ref="inpt"> <bry<bry
<button @click="showLog">點我列印內容</button>
‹/div›
‹/template>
< script lang="ts" setup name="Person">
import (ref) from 'vue'
let titlel = ref()
let title2 = ref()

```
// 定義一個介面，用於限制 person 物件的具體屬性
export interface PersonInter {
id:string,

name:string,
age:number

}

// 一個自定義型別
// export type Persons = Array<PersonInter>
export type Persons = PersonInten[]
```

```
<template>
<div class="person">

???

</div>
</template>

<script lang="ts" setup name="Person">
import {type PersonInter, type Persons} from '@/types'

1/ let person: PersonInter = {id:'asyud7asfdo1', name:'張三',age:60} let personList:Persons = [

{id:'asyud7asfdo1', name:'張三',age:60}, {id:'asyud7asfdo2',name:'李四',age:18}, {id:'asyud7asfde3', name:'王五',age:5}

]

</script>

<style scoped>…
```

父
```
<template〉
<Person a="哈哈" List="personList"/>

</template〉

<script lang="ts" setup name="App">
import Person from'./components/Person.vue' import {reactive} from 'vue'
import {type Persons} from '@/types'

let personList = reactive<Persons>([
{id:'asudfysafde1', name:'張三',age:18}, {id:'asudfysafdo2'
'李四',age:20},

{id:'asudfysaf)de3', name:'王五',age:22} ])

</script>
```

Person.vue
```
<template〉
<div class="person"

<h2>{{a}}</h2>
<h2>{{list}}</h2>

</div>
</template〉

<script Lang="ts" setup name="Person"〉 impoft {defineProps} from 'vue' // 接收a

// 只接收list

// defineProps(['list'])

// 接收 list + 限制型別
// defineProps<{list:Persons}>()

// 接收 list + 限制型別 + 限制必要性 + 指定預設
defineProps<{list?:Persons}>()

// 接收 list + 限制型別
// defineProps<{list: Persons}>()

// 接收 list + 限制型別 + 限制必要性 + 指定預設值

withDefaults(defineProps<(list?)Persons}>(),{

list:()=> [{id:'ausydgyuon ,hame:'康師傅 王麻子 特侖蘇',age:19}] }

接收 a，同時將 props 儲存起來
/* let x = defineProps(['a'])
console.1og(x.a)*/

</script>
```


## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
