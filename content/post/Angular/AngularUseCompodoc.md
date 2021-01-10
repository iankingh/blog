---
title: "AngularUseCompodoc"
date: 2020-07-20T16:17:45+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angularg use compodoc 
compodoc是一個用於產生 Angular 靜態網頁的工具

Angular 使用 compodoc 產生說明文件

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

```sh
compodoc -p src\tsconfig.app.json -s -r 8888


compodoc -p tsconfig.app.json src -s -r 8888

npx compodoc -p tsconfig.json -s -r 8888

npx compodoc -p tsconfig.base.json -s -r 8888
```

### 啟用本地文件網站

```shell
compodoc -p tsconfig.json -s
```

### jsDoc Tags 

```typescript


@Injectab()
export class HelloService{
    
    constructor(){
        
    }
    
    /**
    * Represents a hellWord.
    * @param {string} UserName - The UserName of the hellWord.
    * @param {string} age - The age of the hellWord.
    */
     hellWord(UserName: string, age : string) {
    }
}
```

 

## 參考

Angular 工具篇之文档管理 | 前端修仙之路

https://semlinker.com/ng-compodoc-intro/

Angular #10 Angular Documentation

https://tpu.thinkpower.com.tw/tpu/articleDetails/864

Javascript文檔註解規則使用方式@use JSDoc | ucamc

https://www.ucamc.com/e-learning/javascript/250-javascript-use-jsdoc


你寫的文件別人看得懂嗎？：compodoc | Jonny Huang 的學習筆記

https://jonny-huang.github.io/angular/training/23_compodoc/