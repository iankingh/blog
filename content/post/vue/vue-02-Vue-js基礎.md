---
title: "Vue 教學 02 - Vue.js 基礎"
date: 2026-03-22T20:02:00+08:00
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

# 第2章 Vue.js 基礎 資料夾整理

## 核心程式碼

```html
<button @click="submit">評論</button>
<textarea @keyup.enter="submit" v-model="msg"></textarea>

<ul>
	<li v-for="(item,index) in list" :key="item.time">
		<div>{{item.text}}</div>
		<div>{{formatDate(item.time)}}</div>
	</li>
</ul>

<script>
Vue.createApp({
	data() {
		return {
			msg: null,
			list: []
		}
	},
	computed: {
		newdate() {
			if (this.list.length == 0) return null
			return this.formatDate(this.list[this.list.length - 1].time)
		}
	},
	methods: {
		submit() {
			if (this.msg) {
				this.list.push({ text: this.msg, time: Date.now() })
				this.msg = null
			}
		},
		formatDate(value) {
			let date = new Date(value)
			let year = date.getFullYear()
			let month = String(date.getMonth() + 1).padStart(2, '0')
			let day = String(date.getDate()).padStart(2, '0')
			let hour = String(date.getHours()).padStart(2, '0')
			let minute = String(date.getMinutes()).padStart(2, '0')
			let second = String(date.getSeconds()).padStart(2, '0')
			return `${year}-${month}-${day} ${hour}:${minute}:${second}`
		}
	}
}).mount('#app')
</script>
```

### 變體：最新留言排前面

也可以用 `unshift` 把新留言插到陣列最前面，搭配簡化的日期格式：

```html
<script>
Vue.createApp({
	data() {
		return {
			msg: null,
			list: []
		}
	},
	methods: {
		submit() {
			if (this.msg) {
				this.list.unshift({ text: this.msg, time: Date.now() })
				this.msg = null
			}
		},
		formatDate(time) {
			const date = new Date(time)
			return `${date.getFullYear()}年${date.getMonth()+1}月${date.getDate()}日`
		}
	}
}).mount('#app')
</script>
```

## 重點

1. `submit` 會把留言與時間寫入 `list`（`push` 新增到尾端，`unshift` 新增到前端）。
2. `computed` 用來衍生顯示最新回覆時間。
3. `formatDate` 將 timestamp 轉成可讀字串。

