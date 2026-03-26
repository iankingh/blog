---
title: "Vue 教學 18 - history 與 hash 模式"
date: 2026-03-22T20:18:00+08:00
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

# history 與 hash 模式

## 兩種模式

### history 模式

```ts
history: createWebHistory()
```

特性：

- URL 漂亮（沒有 #）
- 接近傳統網站路徑
- 需伺服器做 fallback

### hash 模式

```ts
history: createWebHashHistory()
```

特性：

- URL 會帶 #
- 部署通常更簡單
- SEO 相對較弱

## 怎麼選

- 快速部署、內網系統：可先用 hash
- 對 URL 與 SEO 有要求：用 history 並配置伺服器

## history 重新整理 404 的原因

當你在 `/news` 重新整理時，瀏覽器會向伺服器直接請求 `/news`。若伺服器沒有轉回 `index.html`，就會 404。

## 檢核

- 能說出兩種模式 URL 差異
- 能解釋 history 404 根因在伺服器端
