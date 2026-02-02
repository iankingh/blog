---
title: "Vue Turtorial 06 Route"
date: 2024-08-27T07:55:55+08:00
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

1.路由就是一组key-Value 對應關係.
2.多个路由,需要经过培出器的管理.

router 路由器

keyl+ value1 => => 路由 route
key2+ value2 => 路由 route
key3+ value3 => => 路由route
key4+ value4 => 路由route



1.导航区、展示区2.请来路由器
3.制定路由的具體規則(什4.形成一个一个的【???.

```
<template〉
<div class="app">

<h2>Vue路由测试</h2>

<!-- 导航区 -->

<div class="navigate">
<a href="#”>首页</a>
<a href="#”>新闻</a>
<a href="#”>关于</a〉
</div>

<!-- 展示区--＞
<div class="main-content">
此处以后可能要展示各种組件,到底展示哪个組件,需要看路径

</div>

</div>
</template>

<script lang="ts" setup name="App">

</script>
```

```
11 創建一个路由器,并暴露出去

// 第一步:引入createRouter
import {createRouter, createwebHistory}from 'vue-router' // 引入一个一个可能要呈现組件
import Home from '@/components/Home.vue'
import News from '@/components/News.vue'
impont About from '@/components/About.vue'

// 第二步:創建路由器
const router = createRouter({
history:createWebHistory(),//路由器的工作模式(稍后讲解) routes:[ //一个一个的路由規則⋯

]

}

// 暴露出去router
export default router
```

main.ts
```
// 引入createApp用於創建應用import {createApp}from from 'vue' // 引入App根組件
import App from'./App.vue' // 引入路由器
import router from'./router' // 創建一个應用
const app = createApp(App) // 使用路由器

app.use (router)
/1 掛載整個應用到app容器中app.mount ('#app')
```

```
<template>
<div class="app">

<h2 class="title">Vue路由测试</h2>

<!-- 导航区 -->
<div class="navigate">
<RouterLink to="/home" active-class="active">i页</RouterLink><RouterLink to="/news" active-class="active">新闻</RouterLink><RouterLink to="/about" active-class="active">关子</RouterLink>

≤/div>

<!--展示区 -->

<div class="main-content">

<RouterView></RouterView>

</div>
```



## 前言(各章節)

## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
