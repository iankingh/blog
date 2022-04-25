---
title: "Angular_NullInjectorError"
date: 2020-10-27T21:28:57+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

<!--more-->

### 前言

NullInjectorError: No provider for Pipe!

如果遇到 NullInjectorError 表示 沒有注入提供者

這邊是沒有註冊 Pipe

需註冊在 module 或是 component

<<<<<<< HEAD
需註冊

```
=======
```tsx
>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6
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

[Angular依赖注入的一个常见错误NullInjectorError,No provider for XXX - 云+社区 - 腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1700456)