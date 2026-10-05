---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
description: ""
# 實際修訂後再加入 lastmod，保留原始 date。
# lastmod: 2026-10-05T21:00:00+08:00
# 精選文章可加入正整數，數字越小越靠前；一般筆記不需此欄位。
# featuredOrder: 1
categories:
- "筆記"
tags:
- "tag1"
- "tag2"
toc: true
draft: true
---



# 這是範本的使用（標題）

<!-- 簡介 -->
<!--more-->
## 前言（各章節）

### 環境

- java版本:
- 後端框架：Spring Boot
- 前端框架：Angular
- 資料庫  ：MySQL
- 專案管理：Maven
- 開發工具：Visual Studio Code
- 開發環境：Windows

## 用 H2 作為各章節的標題

### 用 H3作為各章節的分段

## 標題2

### 標題2-2-2

## 程式碼

### 程式碼的部分

****ex.****

```javascript
const s = "範本應用"
alert(s);
```

## Summary

## 參考

[範本 (notion.so)](https://www.notion.so/98b881454a694080a84fb7988c2b3d8a)
