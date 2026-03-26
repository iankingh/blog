---
title: "Vue 教學 28 - Vite 工具"
date: 2026-03-22T20:28:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vite"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 第9章 Vite 工具 完整原始檔

## 原始檔：src/router/router.js

```js
import todo from '../views/todo.vue' // 待辦事項頁面
import recycle from '../views/recycle.vue' // 回收站頁面
import {createRouter,createWebHashHistory} from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
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

## 原始檔：src/store/store.js

```js

import Vuex from 'vuex'
import dataUtils from '../utils/dataUtils'
const myPlugin = (store) => {
  store.subscribe((mutation, state) => {
    // 每次呼叫 mutation，在這裡持久化資料
    dataUtils.setItem('todoList', state.todoItems)
    dataUtils.setItem('recycleList', state.recycleItems)
  })
}
export default Vuex.createStore({
  plugins: [myPlugin],
  state: {
    todoItems:dataUtils.getItem('todoList') || [],
    recycleItems:dataUtils.getItem('recycleList') || [],
  },
  mutations: {
    /*
    * 新增事項
    */
    addTodo (state, obj) {
      state.todoItems.unshift(obj)
    },
    /*
    * 添加回收站事項
    */
    addRecycle (state, obj) {
      state.recycleItems.unshift(obj)
    },
    /*
    * 刪除回收站事項
    */
    deleteRecycle (state, obj) {
      // 以下邏輯為找到對應 id 的事項，然後刪除
      state.recycleItems = state.recycleItems.filter(item=>{
        return item.id != obj.id
      })
    },
    /*
    * 刪除事項
    */
    deleteTodo (state, obj) {
      // 以下邏輯為找到對應 id 的事項，然後刪除
      state.todoItems = state.todoItems.filter(item=>{
        return item.id != obj.id
      })
    },
    /*
    * 重置事項列表
    */
    resetTodo(state, array){
      state.todoItems = array
    }
  },
  actions: {
    addTodo (context, obj) {
      context.commit('addTodo', obj)
    },
    addRecycle (context, obj) {
      context.commit('addRecycle', obj)
    },
    deleteTodo(context, obj){
      // 先刪除待辦事項
      context.commit('deleteTodo', obj)
      // 後增加回收站事項
      context.commit('addRecycle', obj)
    },
    revertTodo(context, obj){
      // 先刪回收站事項
      context.commit('deleteRecycle', obj)
      // 後增加待辦事項
      context.commit('addTodo', obj)
    }
  }
})
```

