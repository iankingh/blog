---
title: "Vue 教學 14：路由的角色與網址對映"
date: 2026-03-22T20:14:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue 3"
- "Vue Router"
toc: true
draft: false
description: "釐清 Router、RouterLink、RouterView 與頁面元件的分工，建立 SPA 路由的操作流程。"
lastmod: 2026-10-07T00:01:00+08:00
---

釐清 Router、RouterLink、RouterView 與頁面元件的分工，建立 SPA 路由的操作流程。

<!--more-->

適用：Vue 3.5 與 Vue Router 4。先完成第 00 章環境與[第 15 章的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})，後續範例依指定檔案替換。

## 一次導航經過什麼

1. RouterLink 或 router.push 提出目標網址。
2. Router 根據 routes 與網址比對紀錄，執行必要的守衛。
3. 成功後更新目前 route 與瀏覽器歷史。
4. RouterView 根據匹配紀錄顯示頁面元件。

RouterLink 是導航控制，並不承載目標頁面內容；RouterView 是展示位置，巢狀路由需要巢狀 RouterView。

## 網址與頁面的關係

| 網址 | 配對規則 | 可用資料 |
| --- | --- | --- |
| `/` | `/` | 首頁 |
| `/tasks/7` | `/tasks/:id` | params.id 是字串 7 |
| `/tasks?done=1` | `/tasks` | query.done 是字串 1 |

先使用第 15 章的首頁／關於頁例子，點導航後網址變動而整頁不過載，再直接輸入網址確認展示結果。若改用 hash 模式，畫面仍能切換，但網址含 `#`。

## 路由與後端的邊界

前端守衛只能改善操作流程，不能保護 API。伺服器仍要驗證身分及許可權。History 模式下重新整理子路徑會直接請求伺服器，需設定 SPA fallback；API、資源及真正不存在的路徑不應全數偽裝成成功頁面。

Vue Router 3 配合 Vue 2 使用，Router 4 以 createRouter 建立例項；舊 `new VueRouter()` 不應複製到本系列。


## 章節導覽

[系列目錄]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) · [上一章]({{< ref "/post/vue/vue-13-Vue3進階實務整理.md" >}}) · [下一章]({{< ref "/post/vue/vue-15-路由基本接線.md" >}})

## 查核範圍

Vue Router API文件查核；memory history實測命名參數、query、resolve與守衛導向。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Vue Router 概述](https://router.vuejs.org/guide/)
- [路由匹配](https://router.vuejs.org/guide/essentials/dynamic-matching.html)
