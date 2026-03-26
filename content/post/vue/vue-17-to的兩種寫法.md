---
title: "Vue 教學 17 - to 的兩種寫法"
date: 2026-03-22T20:17:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "Vue Router"
- "RouterLink"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# to 的兩種寫法

RouterLink 的 `to` 常見兩種寫法。

## 寫法 1：字串

```vue
<RouterLink to="/home">首頁</RouterLink>
```

適合：

- 單純跳轉
- 不帶複雜引數

## 寫法 2：物件

```vue
<RouterLink
  :to="{
    name: 'news',
    query: { page: 1 }
  }"
>
  新聞
</RouterLink>
```

適合：

- 需要 query 或 params
- 想用 name 增加可維護性

## 選擇建議

- 路徑固定且簡單：字串
- 有引數、可讀性需求高：物件

## 常見錯誤

1. 傳 params 卻沒搭配 name。
2. query 傳遞不可序列化資料。

## 建議

團隊開發時，優先用 name 導航，路徑調整時改動更小。
