---
title: "Vue 教學 09 - 元件化"
date: 2026-03-22T20:09:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "元件"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 第3章 Vue.js 元件 完整原始檔

## 原始檔：src/main.js

```js
import { createApp } from 'vue';
import App from './App.vue'
import mitt from 'mitt'

let app = createApp(App)


window.mitt = mitt()


app.mount('#app')

```

## 原始檔：src/views/todo.vue

```vue
<template>
  <div class="todo">
    <div class="title">
      事項列表
    </div>
    <div class="add-new">
      <input v-model.trim="newTodoContent" class="input" type="text" name="new_todo" placeholder="請輸入內容" enterkeyhint="send"
        @keyup.enter.prevent="saveTodo">
    </div>
    <div>
      <titem v-for="item in todoItems" :key="item.id" :item="item" @delete="deleteItem" @complete="completeItem"></titem>
    </div>
  </div>
</template>

<script>
  import titem from '../components/titem.vue'
  import {onMounted,reactive,watch} from 'vue'
  
  import dataUtils from '../utils/dataUtils'
  /**
   * 待辦事項頁面元件
   */
  export default {
    name: 'todo',// 元件的名稱，盡量和檔名一致
    components: {
      titem
    },
    data(){
      return {
        newTodoContent: '',// 輸入框 input 的內容
        todoItems: []// 待辦事項的列表
      }
    },
    mounted(){
      window.mitt.on('addRevert', (obj) =>{
        this.todoItems.push(obj)
      })
      this.fetchData()
    },
    watch:{
      // 一旦有改動立刻呼叫更新儲存
      todoItems:{
          handler(val){
            this.storeItems(val)
          },
          deep:true
      }
    },
    methods:{
      fetchData(){
        this.todoItems = dataUtils.getItem('todoList') || []
      },
      /**
       * 建立事項
       */
      saveTodo(){
        // 如果沒有輸入內容，直接返回
        if (!this.newTodoContent) return
        // 將事項存入列表
        this.todoItems.push({
          id: Math.random().toString(36).substr(2, 5),// 取得隨機 ID 值
          content: this.newTodoContent// 設定內容
        })
        // 建立完成後清空輸入框內容
        this.newTodoContent = ''
      },
       /**
       * 儲存事項列表
       */
      storeItems(array){
        dataUtils.setItem('todoList', array)
      },
      deleteItem(obj){

        // 以下邏輯為找到對應 id 的事項，然後過濾並刪除
        this.todoItems = this.todoItems.filter(item=>{
          return item.id != obj.id
        })
        // 通知已刪除事項頁面，即時更新已刪除資料
        window.mitt.emit('addDelete', obj)
      },
       /**
       * 修改事項
       */
      completeItem(obj){
        // 找到對應 id 的事項，然後替換
        for (let i = 0 ; i < this.todoItems.length ; i++) {
          if (this.todoItems[i].id == obj.id) {
            this.todoItems[i] = obj
            break
          }
        }
      }
    },
  }
</script>
<style scoped>
  .todo .title {
    font-size: 24px;
    font-weight: 600;
    line-height: 27px;
    margin-bottom: 24px;
    text-align: center;
  }

  .todo .add-new {
    margin-bottom: 10px;
  }

  .todo .add-new input {
    box-shadow: inset 0 0.0625em 0.125em rgba(10, 10, 10, .05);/* 新增陰影效果 */
    width: 100%;/* 設定寬度 */
    height: 40px;/* 設定高度 */
    padding: 4px;/* 設定內邊距 */
    font-size: 16px;/* 設定字型大小 */
    color: #363636;/* 設定字型顏色 */
    background-color: #fff;/* 設定背景顏色 */
    border-color: transparent;/* 去除預設背景邊框 */
    border-radius: 4px;/* 設定圓角 */
    box-sizing: border-box;/* 設定內邊距不佔據寬高 */
  }


</style>

```

## 原始檔：src/views/recycle.vue

```vue
<template>
  <div class="recycle">
    <div class="title">
      回收站
    </div>
    <div class="no-data" v-if="recycleItems.length == 0">暫無已刪除的事項</div>
    <ritem v-for="item in recycleItems" :key="item.id" :item="item" @revert="revertItem"></ritem>

  </div>
</template>

<script>
  import ritem from '../components/ritem.vue'
  import dataUtils from '../utils/dataUtils'
  import {onMounted,reactive,watch} from 'vue'
  /**
   *  回收站頁面元件
   */
  export default {
    name: 'recycle',// 元件的名稱，盡量和檔名一致
    components: {
      ritem
    },
    data(){
      return {
        recycleItems: []// 已刪除事項的列表
      }
    },
    watch:{
      // 一旦有改動立刻呼叫更新儲存
      recycleItems:{
          handler(val){
            this.storeItems(val)
          },
          deep:true
      }
    },
    mounted(){
      window.mitt.on('addDelete', (obj) =>{
        this.recycleItems.push(obj)
      })
      this.fetchData()
    },
    methods:{
       /**
       * 從儲存中取得已刪除事項資料
       */
      fetchData(){
        this.recycleItems = dataUtils.getItem('recycleList') || []
      },
      /**
       * 恢復事項
       */
      revertItem(obj){
        // 將需要恢復的事項從已刪除事項列表中剔除
        this.recycleItems = this.recycleItems.filter(item=>{
          return item.id != obj.id
        })

        window.mitt.emit('addRevert', obj)
      },
      /**
       * 儲存已刪除事項列表
       */
      storeItems(array){
        dataUtils.setItem('recycleList', array)
      }
    }
  }
</script>
<style scoped>
  .recycle .title {
    font-size: 24px;
    font-weight: 600;
    line-height: 27px;
    margin-bottom: 24px;
    text-align: center;
  }

  .recycle .no-data {
    text-align: center;
  }
</style>

```

