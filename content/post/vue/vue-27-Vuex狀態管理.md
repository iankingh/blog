---
title: "Vue 教學 27 - Vuex 狀態管理"
date: 2026-03-22T20:27:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vuex"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 第6章 Vuex 狀態管理 完整原始檔

## 原始檔：src/store/store.js

```js

import {createStore} from 'vuex'
import dataUtils from '../utils/dataUtils'
const myPlugin = (store) => {
  store.subscribe((mutation, state) => {
    // 每次呼叫 mutation，在這裡持久化資料
    dataUtils.setItem('todoList', state.todoItems)
    dataUtils.setItem('recycleList', state.recycleItems)
  })
}
export default createStore({
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

## 原始檔：src/views/todo.vue

```vue
<template>
  <div class="todo">
    <div class="title">
      事項列表<span class="shuffle-btn" @click="shuffleList"></span>
    </div>
    <div class="add-new">
      <input v-model.trim="newTodoContent" class="input" type="text" name="new_todo" placeholder="請輸入內容" enterkeyhint="send"
        @keyup.enter.prevent="saveTodo">
    </div>
    <div class="s-wrap">
        <transition-group name="list-complete" tag="div">
          <div v-for="item in todoItems" class="list-complete-item"  :key="item.id">
            <titem :item="item" @delete="deleteItem" @complete="completeItem"></titem>
          </div>
        </transition-group>
    </div>
  </div>
</template>

<script>
  import titem from '../components/titem.vue'
  import {ref,computed,toRaw} from 'vue'
  
  import dataUtils from '../utils/dataUtils'
  import Vuex from 'vuex'
  /**
   * 待辦事項頁面元件
   */
  export default {
    name: 'todo',// 元件的名稱，盡量和檔名一致
    components: {
      titem
    },
    setup(){
      const store = Vuex.useStore()
      let todoItems = computed(() => store.state.todoItems)

      let newTodoContent = ref('')// 輸入框 input 的內容
      
      /**
       * 建立事項
       */
      function saveTodo() {

        // 如果沒有輸入內容，直接返回
        if (!newTodoContent.value) return
        // 將事項存入列表
        store.dispatch('addTodo',{
          id: Math.random().toString(36).substr(2, 5),// 取得隨機 ID 值
          content: newTodoContent.value// 設定內容
        })
        // 建立完成後清空輸入框內容
        newTodoContent.value = ''
      }
      /**
       * 刪除事項
       */

      const deleteItem = (obj)=>store.dispatch('deleteTodo',obj)

      /**
       * 修改事項
       */
      function completeItem(obj) {
        let arr = []
        // 找到對應 id 的事項，然後替換
        for (let i = 0 ; i < todoItems.value.length ; i++) {
          if (todoItems.value[i].id == obj.id) {
            arr.push(obj)
          } else {
            arr.push(todoItems.value[i])
          }
        }

        store.commit('resetTodo',arr)
      }
      /**
       * 打亂順序
       */
      let shuffleList = ()=> {
          store.commit('resetTodo',_.shuffle(toRaw(todoItems.value)))
      }

      return {
        newTodoContent,
        deleteItem,
        todoItems,
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
    <div class="no-data" v-if="recycleItems.length == 0">暫無已刪除的事項</div>
    <div class="s-wrap">
      <ritem v-for="item in recycleItems" :key="item.id" :item="item" @revert="revertItem"></ritem>
    </div>
  </div>
</template>

<script>
  import ritem from '../components/ritem.vue'
  import dataUtils from '../utils/dataUtils'
  import {computed} from 'vue'
  import Vuex from 'vuex'
  /**
   *  回收站頁面元件
   */
  export default {
    name: 'recycle',// 元件的名稱，盡量和檔名一致
    components: {
      ritem
    },

    setup(){

      const store = Vuex.useStore()
      let recycleItems = computed(() => store.state.recycleItems)
      /**
       * 恢復事項
       */
      const revertItem = (obj)=>store.dispatch('revertTodo',obj)

      return {
        recycleItems,
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

