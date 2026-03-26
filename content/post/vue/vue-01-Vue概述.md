---
title: "Vue 教學 01 - Vue 概述"
date: 2026-03-22T20:01:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "基礎"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 01-Vue概述 資料夾整理

## 核心程式碼

```html
<div id="app">
	<div><img src="./imgs/logo.png" /></div>
	<div>{{msg}}</div>
	<div><input v-model="msg" /></div>
</div>

<script>
Vue.createApp({
	data() {
		return {
			msg: 'Hello Vue 3'
		}
	}
}).mount('#app')
</script>
```

## 重點

1. 這是最小可運作的 Vue 3 範例。
2. `v-model` 讓輸入和 `msg` 雙向繫結。
3. 畫面上的 `{{msg}}` 會即時反映輸入值。

