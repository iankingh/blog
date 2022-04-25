---
title: "AngularUseJavaScript"
date: 2021-01-22T13:38:06+08:00
draft: false
categories:
- "筆記"
tags:
- "Angular"
- "FrontEnd"
---
## **Angular引入**JavaScript

## 前言

在實務上我們可以在npm上面找到要用的 JavaScript 來引用 , 有時可能找不到 , 也有時可能要匯入自己寫的JavaScript ,如果功能不複雜 ,可以轉成TypeScript
<!--more-->

## 方法一

如果JavaScript  不複雜可以轉成 TypeScript

## 方法 二 引入第三方的JavaScript

### 第一步 安裝下載JavaScript

準備一個 JavaScript 

****ex.**** 

```javascript
function Hello(){
	alert("Hello")
}
```

**把js文件放到 /assets目錄下**

****ex.****
```
 /assets/Hello.js
```

## 第二步 設置**compilerOptions**的**allowJs**屬性為true

打開 tsconfig.json，找到**compilerOptions**  ，並設置**compilerOptions**的**allowJs**屬性為true;，添加 "**allowJs**": true,

ex. 添加 **"allowJs": true,**

```
 /assets/js/Hello.js
```

### 第二步 設置**compilerOptions**的**allowJs**屬性為true

打開 tsconfig.json，找到**compilerOptions**  ，並設置**compilerOptions**的**allowJs**屬性為true;，添加 "**allowJs**": true,

**ex.** 添加 **"allowJs": true,**
>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6

```json
 "compilerOptions": {
    .....................
    "allowJs": true,
	  .....................
  }
```

完整如下
tsconfig.json完整如下

```json
{
  "compileOnSave": false,
  "compilerOptions": {
    "baseUrl": "./",
    "outDir": "./dist/out-tsc",
    "sourceMap": true,
    "declaration": false,
    "downlevelIteration": true,
    "experimentalDecorators": true,
    "module": "esnext",
    "moduleResolution": "node",
    "allowJs": true,
    "importHelpers": true,
    "target": "es5",
    "lib": [
      "es2018",
      "dom"
    ]
  },
  "angularCompilerOptions": {
    "fullTemplateTypeCheck": true,
    "strictInjectionParameters": true,
    "enableIvy": false
  }
}

```

### 第三步 : 引入JS
### 第三步 : 引入javaScript

### 在 angular.json，scripts區塊配置js文件路径

```json
"scripts": [
              "src/assets/js/Hello.js",
            ]
```

### 第四步，在當前组件.ts中使用函数添加js
### 在 index.html 引入

<!-- Hello js -->

<script src="assets/js/Hello.js" type="text/javascript"></script>

**index.html**

```html
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>Hello</title>
  <base href="/">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,IE=11">
  <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <script src="assets/js/Hello.js" type="text/javascript"></script>

</head>

<body class="mat-typography">
  <app-root></app-root>
</body>

</html>
```

### 第四步 : 在當前组件.ts中使用函数添加js

`import 'src/assets/js/Hello.js';`
>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6

## 參考

[angular在ts中使用第三方js_weixin_43182222的博客-CSDN博客](https://blog.csdn.net/weixin_43182222/article/details/105205283?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control)

[How to call JavaScript functions from Typescript in Angular 5? - Stack Overflow](https://stackoverflow.com/questions/49526681/how-to-call-javascript-functions-from-typescript-in-angular-5)

[Angular引入自己写的js或者其他_qq_43205711的博客-程序员宅基地_angular引用自己的js - 程序员宅基地 (cxyzjd.com)](https://www.cxyzjd.com/article/qq_43205711/84139445)