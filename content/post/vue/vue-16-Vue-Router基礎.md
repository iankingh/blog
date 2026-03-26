---
title: "Vue 教學 16 - Vue Router 基礎"
date: 2026-03-22T20:16:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue Router"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# Vue Router 基礎

1.路由就是一組 key-Value 對應關係。
2.多個路由，需要經過路由器的管理。

router 路由器

keyl+ value1 => => 路由 route
key2+ value2 => 路由 route
key3+ value3 => => 路由route
key4+ value4 => 路由route



1.導航區、展示區 2.請來路由器
3.制定路由的具體規則 4.形成一個一個的路由。

```
<template〉
<div class="app">

<h2>Vue路由測試</h2>

<!-- 導航區 -->

<div class="navigate">
<a href="#”>首頁</a>
<a href="#”>新聞</a>
<a href="#”>關於</a〉
</div>

<!-- 展示區--＞
<div class="main-content">
此處以後可能要展示各種元件,到底展示哪個元件,需要看路徑

</div>

</div>
</template>

<script lang="ts" setup name="App">

</script>
```

```
11 建立一個路由器,並暴露出去

// 第一步:引入 createRouter
import {createRouter, createwebHistory}from 'vue-router' // 引入一個一個可能要呈現元件
import Home from '@/components/Home.vue'
import News from '@/components/News.vue'
impont About from '@/components/About.vue'

// 第二步:建立路由器
const router = createRouter({
history:createWebHistory(),//路由器的工作模式(稍後講解) routes:[ //一個一個的路由規則⋯

]

}

// 暴露出去 router
export default router
```

main.ts
```
// 引入 createApp 用於建立應用 import {createApp}from from 'vue' // 引入 App 根元件
import App from'./App.vue' // 引入路由器
import router from'./router' // 建立一個應用
const app = createApp(App) // 使用路由器

app.use (router)
/1 掛載整個應用到 app 容器中app.mount ('#app')
```

```
<template>
<div class="app">

<h2 class="title">Vue路由測試</h2>

<!-- 導航區 -->
<div class="navigate">
<RouterLink to="/home" active-class="active">首頁</RouterLink><RouterLink to="/news" active-class="active">新聞</RouterLink><RouterLink to="/about" active-class="active">關於</RouterLink>

≤/div>

<!--展示區 -->

<div class="main-content">

<RouterView></RouterView>

</div>
```


## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
