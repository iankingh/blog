---
title: "Vue Turtorial 01"
date: 2024-08-26T21:02:25+08:00
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

# Vue 學習 

## ref vs reactive 用的地方

ref : 基本类型数据、对象类型数据

reactive 用来定义：对象类型数据。

## ref vs reactive 區別

ref 创建的变量必须使用。value（可以使用voLar 擂件自动添加•value）

reactive 重新分配一个新对象，会失去响应式（可以使用 Object.assign 去整体替换）。

• 使用原则：
1. 若需要一个基本类型的响应式数据，必须使用 ref。
2. 若需要一个响应式对象，层级不深，ref、reactive 都可以。
3. 若需要一个响应式对象，且层级较深，推荐使用 reactive。


3.7. [toRefs 5 toRef)
•作用：将一个响应式对象中的每一个属性，转换为 ref 对象。
•备注：toRefs 与toRef 功能一致，但 toRefs 可以批量转换。

```
/数据
let car = reactive({brand: ' 79t'
，price:100｝）
let sum = ref(0)
// 方法
function changeBrand(){
car.brand ='宝马'
｝
function changePrice(){
car-price += 10
｝
function changeCar (){
// car = （｛brana：'奥拓'，price:1｝）
// car = reactive({brand: 'Fu#F', price: 1})
Object. assign(car, {brand: 'B#F', price:1})
function changeSum (){
sum.value += 1
```


## watch

作用：监视数据的变化（和Vue2 中的watch 作用一致）

特点：
Vue3 中的watch 只能监视以下四种数据：
1.ref 定义的数据。
2.reactive 定义的数据。
3. 函数返回一个值。
4．一个包含上述内容的数组。


我们在Vue3中使用watch的时候，通常会遇到以下几种情况：

### 情况一
监视 ref 定义的【基本类型】数据：直接写数据名即可，监视的是其 value 值的改变。

```
< template>
‹div class="person">
<h2>watch情况一：监视【ref】定义的【基本类型】数据，默认监视的就是value值。</h2>
chr>
<h3>当前求和：｛｛sum｝｝</h3>
‹button @click="changeSum" >sum+1</button>
</div>
</ template>


< script lang="ts" setup name="Person" > import {ref,watch} from
'vue'
/ 数据
let sum = ref（0）
// 方法
function changeSum){
sum.value += 1
｝
// 监视
watch (sum, (newValue, oldValue) =>{
console.1og（'sum变化了*
, newValue, oldValue)
｝）
</script>

```


```
‹template >
‹div class="person" >
＜h1>情况一：监视【ref定义的基本类型数据</h1>
<h2>当前求和为：｛｛sum｝｝</h2>
‹button @click="changeSum"> #Fsum+1</button>
</div›
‹/template>
«script lang="ts" setup name="Person">
import {ref,watch) from 'vue'
//数据
let sum = ref(0)
1/ 方法
function changeSum (){
sum.value += 1
｝
//监视
watch (sum, (newValue, oldValue)=>{
console. 1og（'sum変化了'， newvalue, oldvalue）
｝）
</script>

```
### 情况二
监视 ref 定义的【对象类型】数据：直接写数据名，监视的是对象的【地址值】，若想监视对象内部的数据，要手动开启深度监视

注意：
• 若修改的是 ref 定义的对象中的属性，
• 若修改整个 ref 定义的对象，newValue 是新值，
newValue 和 oldValue 都是新值，因为它们是同一个对象。
oldvalue 是旧值，因为不是同一个对象了。

```
‹ template>
‹div class="person">
<h2>watch情况二：监视【ref】定义的【对象类型】数据。</h2>
chr>
<h3>人员信息：｛｛person.name｝｝，今年｛｛person.age｝｝岁</h3>
<button @click="changeName">修改名字</button><button @click="changeAge">修改年龄</button><button @click="changePerson">修改整个人</button>
</ div>
</ template>
«script setup lang="ts" name="person">
import (ref,watch) from 'vue'
let person = ref({
name：'张三：，
age: 18 )

function changeName ({
person.value.name += '~
› ‹style scoped ›
watch callback
function changeAge({
person.value.age += 1
function changePerson (){
person. value = {name: '#', age:90}


//监视
watch (person, (newValue, oldValue)=>{
console. log(' personskT', newvalue, oldValue)|
log(...data: any[]): void
｝）
```

监视，情况一：监视 【ref】定义的【对象类型】数据，监视的是对象的地址值，若想监视对象内部属性的变化，需要手动
watch的第一个参数是：被监视的数据
watch的第二个参数是：监视的回调
watch的第三个参数是：配置対象（deep、immediate等等....)



watch(person, (newValue, oldValue)=>{
console. log( 'personk]', newValue, oldValue)
}, {deep: truel})

### 情况三

监视reactive定义的对象类型数据，且默认开启了深度监视。

```
< template>
‹div class="person">
<h2>watch情况三：监视【reactive】定义的【响应式对象】。</h2>
shr>
<h2>当前人的信息：</h2>
<h3>姓名：｛｛person.name｝｝</h3>
<h3>/F#: {{person.age})</h3>
<button @click="changeName">改姓名</button><button @click="changeForeignAge">改对外年龄</button>
</div›
</ template>
«script setup lang="ts" name="Person"> import {reactive,watch} from 'vue'
// 数据
let person = reactive({
name：'张三’，
age: {
foreignAge :18, realAge :38, 

})

```

```
//监视，情况三：监视
reactive】 定义的【对象类型】数据，
watch(person, (newValue, oldValue)=>{
console. log('persong1k', newValue, oldValue)

｝）
watch(obj, (newValue,oldValue)=>{

console.1og（'obj変化了'， newvalue,oldvalue）
｝）


### 情况四

监视 ref 或 reactive 定义的【对象类型】数据中的某个属性，注意点如下：
1．若该属性值不是【对象类型】，需要写成函数形式。
2. 若该属性值是依然是【对象类型】，可直接编，也可写成函数，不过建议写成函数。
```
<template>
<div class="person">
<h2>watch情况三：监视ref或reactive定义的【响应式对象】中的某个数据。</h2>chr>

<h2>当前人的信息：</h2>
<h3>姓名：｛｛person.name｝｝</h3>
<h3>年龄：</h3>

≤ul>

<11>对外：｛｛person.age.foreignAge｝｝</11>
<li>真实：｛｛person.age.realAge｝｝</11>

≤/u1>
sbutton @click="changeName">改姓名</button>
<button @click="changeforeignAge">改对外年龄</button>

</div>

</template>

<script setup lang="ts" name="Person">
import ｛reactive,watch｝from 'vue"

let person = reactive（｛

```


```
function changeAge（）｛

person.age += 1

｝

function changeC1（）｛

person.car.c1 ='奥迪'

function changeC2（）｛

person.car.c2 ='大众'

｝

function changeCar（）｛

person.car = ｛c1：'雅迪' ，c2：'爱玛'｝

｝

11 监视，情况四：监视响应式对象中的某个属性，且该属性时基本类型的，要写成函数式watch（（）=> person.name， （newValue, oldValue）=>｛

console.1og（ person.name变化了' ，newalue, oldVvalue）

｝

</script>
```

｝

function changeC2（）｛

person.car.c2 ='大众'

｝

function changeCar（｛

person.car = ｛c1：'雅迪’，c2：'爱玛"｝

// 监视，情况四：监视响应式对象中的某个属性，且该属性是基本类型的，要写成函数式

/* watch（（）=> person.name， （newValue, OldValue）=>｛
console.log（'person.name变化了'，newValue,oldValue）

｝）*/

1/监视，情况四：监视响应式对象中的某个属性，且该属性是对象类型的，可以直接写，也能写函数，更推荐写函数
watch（（）=>person.car，（newvalue, oldValue）=>｛
console.log（'person.car变化了'，newValue, oldvalue）

｝，fdeep:true｝）

</script>


## watchEffect

官网：立即运行一个函数，同时响应式地追踪其依赖，并在依赖更改时重新执行该函数。
• watch 对比 watchEffect
1.都能监听响应式数据的变化，不同的是监听数据变化的方式不同
2
watch：要明确指出监视的数据
3. watchEffect： 不用明确指出监视的数据（函数中用到哪些属性，那就监视哪些属性）。
• 示例代码：
‹ template>
‹div class="person" >
<h1>需求：水温达到50°C，或水位达到20cm，则联系服务器</h1>
<h2 id="demo">*ill: {{temp}}</h2>
<h2>水位：｛｛height｝｝</h2>
‹button @click="changePrice">ki#+1‹/button>
‹ button @click="changeSum">*/+10</button>
</div>
</template>
< script lang="ts" setup name="Person"›
import {ref, watch, watchEffect)


<template>
<div class="person">

<h1>中国</h1>

充

<h2 ref="title2">北京</h2>
<h3>尚硅谷</h3>
<button @click="showLog">点我输出h2这个元素</button>
</div>

-SK
</template>

-SK

-SK <script lang="ts" setup name="Person">

谷
import ｛ref｝ from 'vue'

11 创建一个title2，用于存储ref标记的内容

let title2 = ref（）

-S

Sp
function showLog（）a


console.log（title2.value）

</script>

<style scope>


</div>
</template〉

<script lang="ts" setup name="Person">import ｛ref, defineExpose｝ from 'vue'
11 创建一个title2，用于存储ref标记的内容let title2 = ref（）
let a = ref（0）
let b = ref（1）
let c = ref（2）

function showLog（）｛

console.log（title2.value）

｝

defineExpose（｛a, b,C｝）

</script>



## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
