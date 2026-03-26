---
title: "Vue 教學 14 - 路由核心概念"
date: 2026-03-22T20:14:00+08:00
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

# 路由核心概念

## 你要先知道的事

在 SPA（單頁應用）裡，頁面看起來像在換頁，其實多數時候是：

- URL 改變
- 路由規則比對
- 指定元件被渲染到展示區

也就是：路徑（path）對應到元件（component）。

## 基本角色分工

- Router（路由器）：管理所有路由規則
- Route（路由規則）：單筆對應關係
- RouterLink：做導覽跳轉
- RouterView：顯示目前路由對應元件

## 最小心智模型

把 Router 想像成總機：

1. 接收你要去哪（URL）
2. 在 routes 清單找到對應規則
3. 把對應元件渲染到 RouterView

## 常見誤解

### 誤解 1：RouterLink 會直接把元件插進畫面
不是。RouterLink 只負責導航，真正顯示元件的是 RouterView。

### 誤解 2：路由切換就等於整頁重整
不是。大多是前端路由切換，不會像傳統多頁網站整頁重新整理。

## 練習檢核

- 你能口頭解釋 path 到 component 的關係嗎？
- 你知道 RouterLink 與 RouterView 的職責差異嗎？
- 你知道為何 SPA 體感更流暢嗎？
