---
title: "AngularUseCompodoc"
date: 2020-07-20T16:17:45+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angularg use compodoc
compodoc是一個用於產生 Angular 靜態網頁的工具

<!--more-->

## 安裝compodoc

### 以 local 模式安裝

```shell
$ npm install --save-dev @compodoc/compodoc
```

### 以global(全域) 模式安裝

```shell
$ npm install -g @compodoc/compodoc
```

### 產生文件

```sh
$ compodoc -p tsconfig.json
```

### 啟用本地文件網站

```shell
compodoc -p tsconfig.json -s
```

### jsDoc Tags 

```typescript
@retruns returnsvalue 返回值
@param  paramkey 定義傳入參數
@example  範例
```

 

## 參考

Angular 工具篇之文档管理 | 前端修仙之路

https://semlinker.com/ng-compodoc-intro/

Angular #10 Angular Documentation

https://tpu.thinkpower.com.tw/tpu/articleDetails/864

