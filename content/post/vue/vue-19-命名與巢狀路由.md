---
title: "Vue 教學 19 - 命名與巢狀路由"
date: 2026-03-22T20:19:00+08:00
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

# 命名路由與巢狀路由

## 命名路由

路由規則加上 name：

```ts
{ name: 'news', path: '/news', component: News }
```

導航時可用：

```vue
<RouterLink :to="{ name: 'news' }">新聞</RouterLink>
```

好處：

- path 變更時，導覽程式可少改
- 程式語意更清楚

## 巢狀路由

```ts
{
  path: '/news',
  component: News,
  children: [
    {
      path: 'detail',
      component: Detail
    }
  ]
}
```

重點：

- 子路由通常使用相對 path（不加前導 /）
- 父元件必須包含第二層 `<RouterView />`

## 常見坑

1. 子路由寫成 `/detail` 導致不在父路由底下。
2. 父頁忘記放 `<RouterView />` 看不到子頁。

## 結構建議

- 路由頁：`pages` 或 `views`
- 可重用 UI：`components`
