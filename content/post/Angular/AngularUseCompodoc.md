---
title: "Angular use compodoc"
date: 2020-07-20T16:17:45+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

## **Angular use compodoc**

compodoc是一個用於產生 Angular 靜態網頁的工具

Angular 使用 compodoc 產生說明文件

<!--more-->

## **安裝compodoc**

### **以 local 模式安裝**

```bash
npm install --save-dev @compodoc/compodoc
```

### **產生檔案**

```bash
./node_modules/.bin/compodoc -p tsconfig.json
```

### **RUN server**

```bash
./node_modules/.bin/compodoc -s
```

### **以global(全域) 模式安裝**

```bash
npm install -g @compodoc/compodoc
```

### **產生文件**

```bash
compodoc -p tsconfig.json
```

### **啟用本地文件網站**

```bash
compodoc -p tsconfig.json -s
```

### **使用 npx(推薦)**

```bash
npx compodoc -p tsconfig.json -s -r 8888
```

**指令**

- p : 表示 產生文件
- s : 啟用文件網站

### **jsDoc Tags**

```tsx
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

## **參考**

[Angular 工具篇之文档管理 | 前端修仙之路](https://semlinker.com/ng-compodoc-intro/) 

[Angular #10 Angular Documentation](https://tpu.thinkpower.com.tw/tpu/articleDetails/864)

[Javascript文檔註解規則使用方式@use JSDoc - ucamc](https://www.ucamc.com/e-learning/javascript/250-javascript-use-jsdoc)

[你寫的文件別人看得懂嗎？：compodoc | Jonny Huang 的學習筆記 (jonny-huang.github.io)](https://jonny-huang.github.io/angular/training/23_compodoc/)