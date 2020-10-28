---
title: "Angular_NullInjectorError"
date: 2020-10-27T21:28:57+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angular NullInjectorError 
<!--more-->

NullInjectorError: No provider for  Pipe!
如果遇到 NullInjectorError 表示 沒有註冊

這邊是沒有註冊 Pipe

## 圖待補



需註冊

```
@NgModule({
  imports:      [ .. ],
  declarations: [ CustomPipe ],
  exports:    [ CustomPipe ],
  providers:    [ CustomPipe ]
})
export class SharedModule { }

```
參考
https://stackoverflow.com/questions/46299952/no-provider-for-custompipe-angular-4
