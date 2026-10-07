---
title: "Vue 教學 30：SSR 的伺服器邊界與最小範例"
date: 2026-03-22T20:30:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
toc: true
draft: false
description: "使用 Node 與 Vue server-renderer 回傳 HTML，釐清 SSR、hydration 與跨請求狀態。"
lastmod: 2026-10-07T20:50:40+08:00
---

使用 Node 與 Vue server-renderer 回傳 HTML，釐清 SSR、hydration 與跨請求狀態。

<!--more-->

適用：Vue 3.5、Node 22 的原生 ES module。原課程為手動組裝 SSR，本章保留此架構作最小示範，並明確區分正式 SSR 所需的其他工作。

## 最小 HTTP SSR

此章使用 Node 22 與 Vue 3.5，不沿用 SPA 入口。先安裝同版本 server renderer：

```bash
npm install @vue/server-renderer@~3.5.0
```

在專案根目錄建立 `server.mjs`：

```javascript
import { createServer } from 'node:http'
import { createSSRApp, h } from 'vue'
import { renderToString } from '@vue/server-renderer'
export function createPage(title) {
  return createSSRApp({ render: () => h('main', [h('h1', title), h('p', '由伺服器產生 HTML')]) })
}
const server = createServer(async (request, response) => {
  try {
    if (request.url !== '/') {
      response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' })
      response.end('Not found')
      return
    }
    const html = await renderToString(createPage('SSR 練習'))
    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' })
    response.end(`<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>SSR</title><body>${html}</body></html>`)
  } catch {
    response.writeHead(500, { 'Content-Type': 'text/plain' })
    response.end('Internal server error')
  }
})
server.listen(3000, '127.0.0.1', () => console.log('http://127.0.0.1:3000'))
```

執行 `node server.mjs`，開首頁或用 curl 取得 HTML，應包含 SSR 練習及伺服器產生的段落；不存在路徑為 404。Ctrl+C 停止。每次請求建立新 app，避免 module singleton 儲存使用者資料。

## 本例與完整 SSR 的差距

此例只產生 HTML，沒有客戶端互動與 hydration。完整 SSR 還需 client entry 以 createSSRApp.mount 接管相同 DOM、伺服器與客戶端一致的初始資料、資源清單、路由 isReady 及錯誤碼處理。建議專案採成熟 SSR 框架再依需求擴充，不把上述示範直接當 production server。

伺服器不能直接使用 window、document 或 localStorage；瀏覽器 API 放 mounted。隨機值、時區或不同資料來源容易造成 hydration mismatch。使用 render 函式將 title 當文位元組點可進行轉義；序列化 JSON 到 HTML 則需額外防止 script 注入。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-29-Vue動畫.md" >}}) · [下一章]({{< ref "/post/vue/vue-31-實戰doubanmovie.md" >}})

## 參考資料

- [Vue SSR 指南](https://vuejs.org/guide/scaling-up/ssr.html)
- [Server renderer API](https://vuejs.org/api/ssr.html)
- [Node HTTP](https://nodejs.org/api/http.html)
