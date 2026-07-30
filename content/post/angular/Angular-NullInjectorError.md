---
title: "Angular_NullInjectorError"
date: 2020-10-27T21:28:57+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
---

<!--more-->

## 前言

NullInjectorError: No provider for Pipe!

如果遇到 NullInjectorError 表示 沒有注入提供者

這邊是沒有註冊 Pipe

需註冊在 module 或是 component

```
@NgModule({

imports: [ .. ],

declarations: [ CustomPipe ],

exports: [ CustomPipe ],

providers: [ CustomPipe ]

})

export class SharedModule { }
```

## 參考

[No Provider for CustomPipe - angular 4 - Stack Overflow](https://stackoverflow.com/questions/46299952/no-provider-for-custompipe-angular-4)

[Angular依賴注入的一個常見錯誤NullInjectorError,No provider for XXX - 雲+社群 - 騰訊雲 (tencent.com)](https://cloud.tencent.com/developer/article/1700456)