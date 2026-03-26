---
title: "Vue 教學 29 - Vue 動畫"
date: 2026-03-22T20:29:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "動畫"
- "transition"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 第5章 Vue.js 動畫 完整原始檔

## 原始檔：src/views/todo.vue

```vue
<template>
  <div class="todo">
    <div class="title">
      事項列表<span class="shuffle-btn" @click="shuffleList"></span>
    </div>
    <div class="add-new">
      <input v-model.trim="state.newTodoContent" class="input" type="text" name="new_todo" placeholder="請輸入內容" enterkeyhint="send"
        @keyup.enter.prevent="saveTodo">
    </div>
    <div class="s-wrap">
        <transition-group name="list-complete" tag="div">
            <div v-for="item in state.todoItems" class="list-complete-item"  :key="item.id">
                <titem :item="item" @delete="deleteItem" @complete="completeItem"></titem>
            </div>
        </transition-group>
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
    setup(){
      const state = reactive({
        newTodoContent: '',// 輸入框 input 的內容
        todoItems: []// 待辦事項的列表
      })

      function fetchData() {
        state.todoItems = dataUtils.getItem('todoList') || []
      }
      /**
       * 建立事項
       */
      function saveTodo() {

        // 如果沒有輸入內容，直接返回
        if (!state.newTodoContent) return
        // 將事項存入列表
        state.todoItems.unshift({
          id: Math.random().toString(36).substr(2, 5),// 取得隨機 ID 值
          content: state.newTodoContent// 設定內容
        })
        // 建立完成後清空輸入框內容
        state.newTodoContent = ''
      }
      /**
       * 儲存事項列表
       */
      function storeItems(array) {

        dataUtils.setItem('todoList', array)
      }
      /**
       * 刪除事項
       */
      function deleteItem(obj) {
        // 以下邏輯為找到對應 id 的事項，然後刪除
        state.todoItems = state.todoItems.filter(item=>{
            return item.id != obj.id
        })

        // 修改已刪除事項頁面資料，更新已刪除資料
        let recycleList = dataUtils.getItem('recycleList') || []
        recycleList.unshift(obj)
        dataUtils.setItem('recycleList', recycleList)

      }

      /**
       * 修改事項
       */
      function completeItem(obj) {
        // 找到對應 id 的事項，然後替換
        for (let i = 0 ; i < state.todoItems.length ; i++) {
          if (state.todoItems[i].id == obj.id) {
            state.todoItems[i] = obj
            break
          }
        }
      }
      /**
       * 打亂順序
       */
      function shuffleList() {
        state.todoItems = _.shuffle(state.todoItems)
      }

      watch(
        () => JSON.parse(JSON.stringify(state.todoItems)),
        (val, oldVal) => {
          storeItems(val)// 一旦有改動立刻呼叫更新儲存
        },{deep: true}
      )

      onMounted(()=>{

        fetchData()
      })


      return {
        state,
        deleteItem,
        completeItem,
        shuffleList,
        saveTodo
      }
    }
  }
</script>
<style scoped>
  .todo {
    position: absolute;/* 絕對定位 */
    background: #ededed;/* 設定背景顏色 */
    left: 16px;/* 設定位置 */
    right: 16px;
    top:90px;
  }
  .s-wrap {
    overflow-y:auto;/* 設定可縱向捲動 */
    height: 208px;
  }
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
  
  .list-complete-item {
    transition: all 0.8s ease;/* 全狀態新增過渡 */
  }
  /* 動畫進入和離開時套用 CSS 樣式 */
  .list-complete-enter-from,
  .list-complete-leave-to {
    opacity: 0;/* 漸隱效果 */
    transform: translateY(20px);/* 向下移動 */
  }
  .shuffle-btn {
    cursor: pointer;
    width: 30px;
    height: 30px;
    background-image: url('../assets/shuffle.png');/* 設定背景圖片 */
    background-size: 60% 60%;/* 設定背景尺寸 */
    background-repeat: no-repeat;/* 設定背景不重複 */
    background-position: center;/* 設定背景位置 */
    border-radius: 50%;/* 設定 div 為圓形 */
    display: inline-block;/* 橫向排列 */
    vertical-align: -8px;
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
    <div class="no-data" v-if="state.recycleItems.length == 0">暫無已刪除的事項</div>
    <div class="s-wrap">
      <ritem v-for="item in state.recycleItems" :key="item.id" :item="item" @revert="revertItem"></ritem>
    </div>
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

    setup(){
      const state = reactive({
        recycleItems: []// 已刪除事項的列表
      })

      /**
       * 從儲存中取得已刪除事項資料
       */
      function fetchData() {
        state.recycleItems = dataUtils.getItem('recycleList') || []
      }
      /**
       * 恢復事項
       */
      function revertItem(obj) {
        // 將需要恢復的事項從已刪除事項列表中剔除
        state.recycleItems = state.recycleItems.filter(item=>{
            return item.id != obj.id
        })


        // 修改待辦事項頁面資料，恢復待辦資料
        let todoList = dataUtils.getItem('todoList') || []
        todoList.unshift(obj)
        dataUtils.setItem('todoList', todoList)
      }
      /**
       * 儲存已刪除事項列表
       */
      function storeItems(array) {
        dataUtils.setItem('recycleList', array)
      }

      watch(
        () => JSON.parse(JSON.stringify(state.recycleItems)),
        (val, oldVal) => {
          storeItems(val)// 一旦有改動立刻呼叫更新儲存
        },{deep:true}
      )

      onMounted(()=>{
        fetchData()
      })

      return {
        state,
        revertItem
      }

    }

  }
</script>
<style scoped>
  .recycle {
    position: absolute;
    background: #ededed;
    left: 16px;
    right: 16px;
    top: 90px;
  }
  .s-wrap {
    overflow-y:auto;
    height: 208px;
  }
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

