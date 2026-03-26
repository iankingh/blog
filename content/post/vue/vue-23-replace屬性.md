---
title: "Vue 教學 23 - replace 屬性"
date: 2026-03-22T20:23:00+08:00
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

# replace 屬性

## push 與 replace 差異

- push：新增一筆瀏覽器歷史紀錄（預設）
- replace：覆蓋目前這筆歷史紀錄

## 在 RouterLink 使用 replace

```vue
<RouterLink to="/news" replace>新聞</RouterLink>
```

## 在程式碼中使用 replace

```ts
router.replace({ name: 'news' })
```

## 什麼情境用 replace

1. 登入成功後跳轉，不希望返回到登入頁。
2. 導引流程頁，不希望堆積過多中間頁歷史。

## 注意

replace 不會阻止使用者回上一頁「更早的歷史」，它只是不新增當前這一步。
