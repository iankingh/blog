---
title: "AngularUseJS"
date: 2021-01-22T13:38:06+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angular 使用 JavaScript

在實務上我們可以在npm 上面找到要用的 js 來引用 , 有時可能找不到 , 有時可能要匯入自己寫的js ,如果功能不複雜 ,可以轉成ts
<!--more-->

## 方法一

如果JS 不複雜可以轉成 ts 


##  方法 二 引入第三方的JS
##  第一步 安裝下載js 

把js文件放到 /assets目錄下

```
eX: /assets/Hello.js
```


##  第二步 設定 "allowJs": true

在tsconfig.json，属性compilerOptions，添加 "allowJs": true,
    "allowJs": true,

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

##  第三步 : 引入JS 


1. 可以在 angular.json文件，在scripts中配置js文件路径
2. 或是在 index.html 引入


第四步，在當前组件.ts中使用函数添加js


```

## 參考


[angular在ts中使用第三方js_weixin_43182222的博客-CSDN博客](https://blog.csdn.net/weixin_43182222/article/details/105205283?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control)


[How to call JavaScript functions from Typescript in Angular 5? - Stack Overflow](https://stackoverflow.com/questions/49526681/how-to-call-javascript-functions-from-typescript-in-angular-5)
