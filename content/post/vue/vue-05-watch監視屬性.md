---
title: "Vue 教學 05 - watch 監視屬性"
date: 2026-03-22T20:05:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "watch"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 09-監視屬性-watch 資料夾整理

## 核心程式碼

### 1) 基本 watch（天氣切換）

```html
<div id="root">
	<h2>今天天氣很{{info}}</h2>
	<button @click="changeWeather">切換天氣</button>
</div>

<script>
new Vue({
	el: '#root',
	data() {
		return { isHot: true }
	},
	computed: {
		info() {
			return this.isHot ? '炎熱' : '涼爽'
		}
	},
	methods: {
		changeWeather() {
			this.isHot = !this.isHot
		}
	},
	watch: {
		isHot(newVal, oldVal) {
			console.log('isHot 被監視到', newVal, oldVal)
		}
	}
})
</script>
```

### 2) 深度監聽（物件）

```html
<script>
new Vue({
	el: '#root',
	data() {
		return {
			numbers: { a: 1, b: 2 }
		}
	},
	watch: {
		numbers: {
			deep: true,
			handler(newVal, oldVal) {
				console.log('numbers 被監視到', newVal, oldVal)
			}
		}
	}
})
</script>
```

## 重點

1. 監聽單一欄位可直接寫函式。
2. 監聽物件內層變化要加 `deep: true`。
3. watch 很適合做副作用邏輯（例如存檔、呼叫 API）。

