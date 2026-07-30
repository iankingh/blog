---
title: "Vue 教學 31 - 實戰 doubanmovie"
date: 2026-03-22T20:31:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "實戰"
- "SSR"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 第12章 實戰專案 完整原始檔

## 原始檔：src/main.js

```js

import App from './App.vue'
import { createSSRApp } from 'vue'
import { createRouter } from './router/router.js'
import { createStore } from './store/store.js'

export function createApp() {
  // 如果使用服務端渲染需要將createApp替換為createSSRApp方法
  const app = createSSRApp(App)
  // 路由
  const router = createRouter()
  // store
  const store = createStore()
  app.use(router)
  app.use(store)
  // 將根例項以及路由暴露給呼叫者
  return { app, router, store } 
}
```

## 原始檔：src/entry-client.js

```js
import { createApp } from './main'

const { app, router,store } = createApp()
// 針對有懶載入路由元件的情況，需等待路由解析完
router.isReady().then(() => {
  app.mount('#app')
})
if(window.__INIT_STATE__) {
  // 當使用 template 時，context.state 將作為 window.__INIT_STATE__ 狀態自動嵌入到最終的 HTML
  // 在客戶端掛載到應用程式之前，store 就應該取得狀態：

  store.replaceState(window.__INIT_STATE__._state.data)
}
```

## 原始檔：src/entry-server.js

```js
import { createApp } from './main'
import { renderToString } from 'vue/server-renderer'
import { getAsyncData } from './store/getAsyncData';  // 非同步處理資料的時候使用

export async function render(url, manifest) {
  const { app, router, store } = createApp()

  // 設定預設的路由，/ 預設走 home 路由
  router.push(url)
  // 等待路由載入完成
  await router.isReady()
  // 取得首屏需要的非同步資料store
  await getAsyncData(router,store, true)
  
  // store中已經存放了資料 提供渲染出 HTML 字串
  const ctx = {}
  ctx.state = store.state
  const html = await renderToString(app, ctx)

  // 處理需要預載入的連結
  const preloadLinks = renderPreloadLinks(ctx.modules, manifest)
  return [html, preloadLinks, store]
}

// 取得需要 preload 的資源
function renderPreloadLinks(modules, manifest) {

  let links = ''
  const seen = new Set()
  modules.forEach((id) => {
    const files = manifest[id]
    if (files) {
      files.forEach((file) => {
        if (!seen.has(file)) {
          seen.add(file)
          links += renderPreloadLink(file)
        }
      })
    }
  })

  return links
}

function renderPreloadLink(file) {
  if (file.endsWith('.js')) {
    return `<link rel="modulepreload" crossorigin href="${file}">`
  } else if (file.endsWith('.css')) {
    return `<link rel="stylesheet" href="${file}">`
  } else if (file.endsWith('.woff')) {
    return ` <link rel="preload" href="${file}" as="font" type="font/woff" crossorigin>`
  } else if (file.endsWith('.woff2')) {
    return ` <link rel="preload" href="${file}" as="font" type="font/woff2" crossorigin>`
  } else if (file.endsWith('.gif')) {
    return ` <link rel="preload" href="${file}" as="image" type="image/gif">`
  } else if (file.endsWith('.jpg') || file.endsWith('.jpeg')) {
    return ` <link rel="preload" href="${file}" as="image" type="image/jpeg">`
  } else if (file.endsWith('.png')) {
    return ` <link rel="preload" href="${file}" as="image" type="image/png">`
  } else {
    // TODO
    return ''
  }
}

```

## 原始檔：src/router/router.js

```js

import home from '../views/home/home.vue'

import {
  createMemoryHistory,
  createRouter as _createRouter,
  createWebHistory,
  // createWebHashHistory
} from 'vue-router'

export function createRouter() {
  return _createRouter({
    // use appropriate history implementation for server/client
    // import.meta.env.SSR is injected by Vite.
    history: import.meta.env.SSR ? createMemoryHistory('/') : createWebHistory('/'),
    routes:[
      { path: '/', redirect: '/home' },// 配置預設路由，重新導向到/home
      { path: '/home', component: home },
      { path: '/detail', component:() => import('../views/detail/detail.vue') },
      { path: '/publish', component:() => import('../views/publish/publish.vue') },
      { path: '/login', component:() => import('../views/login/login.vue') },
      { path: '/search', component:() => import('../views/search/search.vue') }
    ]
  })
}
```

## 原始檔：src/utils/service.js

```js
import axios from 'axios'


const baseURL = import.meta.env.SSR ? 'http://localhost:8887' : '/'// 此處和 webpack 的 publicPath 保持一致
// 機密金鑰只保留在 SSR／後端環境，不要提交到版本控制或送到瀏覽器。
const apiKey = import.meta.env.SSR ? process.env.DOUBAN_API_KEY : undefined

// 建立 axios 例項
let service = axios.create({
  baseURL: baseURL,
  withCredentials: true,// 跨域訪問帶上cookie
  timeout: 30000, // 請求超時時間,
})

// 新增request攔截器
service.interceptors.request.use(config => {
  if (apiKey && config.params) {
    config.params = {
      apiKey:apiKey,
      ...config.params
    }
  }
  if (apiKey && config.data) {
    config.data = {
      apiKey:apiKey,
      ...config.data
    }
  }
  return config
}, error => {
  Promise.reject(error)
})
// 新增respone攔截器
service.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    return Promise.reject(error.response)
  }
)

const get = (url, params = {}) =>{
  return service({
    url: url,
    method: 'get',
    params,
  })
}

// 封裝 post 請求
const post = (url, data = {}) =>{
  // 預設配置
  let sendObject = {
    url: url,
    method: 'post',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8'
    },
    data: data
  }
  return service(sendObject)
}


// 不要忘記 export
export default {
  get,
  post,
  baseURL
}
```
