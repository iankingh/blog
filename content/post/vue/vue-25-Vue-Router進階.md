---
title: "Vue 教學 25 - Vue Router 進階"
date: 2026-03-22T20:25:00+08:00
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

# 第7章 Vue Router 路由管理 完整原始檔

## 原始檔：src/router/router.js

```js
import todo from '../views/todo.vue' // 待辦事項頁面
import recycle from '../views/recycle.vue' // 回收站頁面
import {createRouter,createWebHistory} from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
      { path: '/', redirect: '/todo' },// 配置預設路由，重新導向到/todo
      { path: '/todo', component: todo },
      { path: '/recycle', component: recycle },
    ]
})

export default router

```

## 原始檔：src/main.js

```js
import { createApp } from 'vue';
import App from './App.vue'
import store from './store/store.js'
import router from './router/router.js'

const app = createApp(App)

app.use(store)
app.use(router)
app.mount('#app')

```

## 原始檔：src/App.vue

```vue
<template>

  <div class="container">
      <div class="app-content animated bounce">
        <navheader></navheader>
        <router-view v-slot="{ Component }">
            <transition enter-active-class="fadeIn animated faster" leave-active-class="fadeOut animated faster">
                <component :is="Component"></component>
            </transition>
        </router-view>

      </div>
    </div>

</template>
<script>
  import navheader from './components/navheader.vue'

  /**
   * 待辦事項頁面元件
   */
  export default {
    name: 'App',// 元件的名稱，盡量和檔名一致
    components: {
      navheader,
    },
  }
</script>
<style>
  body {
    margin: 0; /* 清除頁面預設邊距 */
  }
  #app {
    color: #2c3e50;/* 設定預設字型顏色 */
    background: linear-gradient(180deg, #2ebf91, #8360c3);/* 設定線性漸層：從藍色到紫色 */
    height: 100vh;/* 設定容器高度為撐滿容器 */
    display: flex;/* 設定容器為彈性佈局 */
    align-items: center/* 設定文字置中 */
  }
  .container {
    padding: 0 10px;/* 設定內邊距 */
    flex-grow: 1;/* 設定彈性值為了撐滿寬度 */
    margin: 0 auto;/* 設定置中 */
    position: relative;
  }
  .app-content {
    background: #ededed;/* 設定背景顏色 */
    padding: 16px;/* 設定內邊距 */
    padding-top: 0;/* 設定內上邊距為 0 */
    border-radius: 5px;/* 設定圓角屬性 */
    box-shadow: 0 0 30px -5px #2c3e50;/* 設定邊框陰影 */
    margin: 16px auto;/* 設定上下邊距並左右置中 */
    min-height: 400px;/* 設定最小高度 */
  }
  /* 美化捲軸樣式 */
  ::-webkit-scrollbar {
    background: 0 0;
    width: 6px;
    height: 6px;
  }
  ::-webkit-scrollbar-thumb {
    background: #d7d7d7;
    border-radius: 6px;
    width: 6px;
    height: 6px;
  }
</style>

```

