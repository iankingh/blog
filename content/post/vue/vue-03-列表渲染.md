---
title: "Vue 教學 03 - 列表渲染"
date: 2026-03-22T20:03:00+08:00
categories:
- "筆記"
tags:
- "Vue"
- "v-for"
- "列表"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# 11-列表渲染 資料夾整理

## 核心程式碼

```html
<div id="root">
	<h2>人員列表(List)</h2>
	<ul>
		<li v-for="person in persons" :key="person.id">
			<span>{{person.id}}</span>
			<span>{{person.name}}</span>
			<span>{{person.age}}</span>
		</li>
	</ul>

	<h2>汽車訊息(Object)</h2>
	<ul>
		<li v-for="(value,key,index) in car" :key="index">
			{{key}}-{{value}}
		</li>
	</ul>
</div>

<script>
new Vue({
	el:'#root',
	data:{
		persons:[
			{id:1,name:'小明',age:18},
			{id:2,name:'小花',age:19}
		],
		car:{
			brand:'BMW',
			price:1000000,
			color:'red'
		}
	}
})
</script>
```

## 重點

1. 陣列用 `v-for="item in list"`。
2. 物件可同時取 `value/key/index`。
3. `:key` 建議使用穩定唯一值。

