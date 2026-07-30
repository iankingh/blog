---
title: "AngularBsN02"
date: 2020-07-05T19:02:31+08:00
draft: false
categories:
- "筆記"
tags:
- "Angular"
- "FrontEnd"
toc: true
---

## **從 0 開始的 Angular 生活 第2天- Angular CLI 建立的專案架構**

<!--more-->

### **angular.json**

Angular CLI 的設定檔 ，可以在這邊看到專案的一些設定 ,EX: 輸出目錄 , bulid 之類的。

### **.editorconfig**

編輯器設定檔，設定處理 tab 符號、換行等等。[EditorConfig](https://editorconfig.org/)

### **.gitignore**

設定git 忽略那些檔案不要加入版本控管。

### **karma.conf.js**

karma.conf.js: Angular 單元測試的工具。

[Karma - Spectacular Test Runner for Javascript (karma-runner.github.io)](https://karma-runner.github.io/latest/index.html)

### **tsconfig.json**

TypeScript 編譯設定。

### **tslint.json**

TypeScript 程式碼風格檢查器。

### **package.json**

npm 的設定檔， `scripts` 區塊定義了在開發 Angular 時用到的命令 EX: ng serve  。

### **node_modeles  Folder**

存放`npm install` 後所有被下載下來所有的套件。

### **src Folder(重要)**

根據 Angular 官網的 Style Guide 建立而成Angular 應用程式主要的原始碼。

### **app Folder(重要)**

app.module 在這一個資料夾中 作為啟動的 module 

### **index.html**

SPA 的html , build 好的js 都會放到這邊 ,也可以當作一個入口。

### **style.css**

在這裡它是 「global styles」也就是整個應用程式都會套用到的 CSS 定義，全部都可以寫在這裡。

### **main.ts**

main.ts 是 Angular 中 JavaScript 程式的進入點。(.ts 代表 TypeScript)

**bootstrapModule**  表示以引入**AppModule** 啟動

```tsx
import { enableProdMode } from '@angular/core';

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';

import { environment } from './environments/environment';

if (environment.production) {

enableProdMode();

}

platformBrowserDynamic().bootstrapModule(AppModule)

.catch(err => console.error(err));
```

### **app.module.ts**

根目錄的TS module

```tsx
import { BrowserModule } from '@angular/platform-browser';

import { NgModule } from '@angular/core';

import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';

@NgModule({

declarations: [

AppComponent

],

imports: [

BrowserModule,

AppRoutingModule,

FormsModule

],

providers: [],

bootstrap: [AppComponent]

})

export class AppModule { }
```

### **app.component.ts**

根目錄的 component  ,進入的第一支 component 

```tsx
import { Component } from '@angular/core';

@Component({

selector: 'app-root',

templateUrl: './app.component.html',

styleUrls: ['./app.component.scss']

})

export class AppComponent {

title = 'firstAngular';

}
```

### **assets(資產) folder**

放置所有的靜態檔案的資料夾，如額外的 JavaScript、JQery、CSS、圖片.........等等。

### **environments folder**

透過 TypeScript 定義一些環境變數。

這個資料夾內有預設有兩個檔案，分別是 environment.ts 與 environment.prod.ts 。

一般來說會有開發 ,sit ,uat ,prod 4種

1. environment.ts
2. environment.sit.ts
3. environment.uat.ts
4. environment.prod.ts

### **favicon.ico**

瀏覽器業籤上面的圖示。

### **polyfills.ts**

當你的 Angular 應用程式同時要符合 IE 或舊版瀏覽器時。

### **test.ts**

測試設定檔決定是否要跑甚麼測試檔案

### **tsconfig.app.json**

Typescripe編譯成Javascript時的編譯設定

## **參考**

[[從 0 開始的 Angular 生活]No.2 檔案架構 | pvt5r486's Blog](https://pvt5r486.github.io/f2e/20190520/3222844657/)

[Angular CLI 7.3 使用 ES2015 的 nomodule 屬性載入 Polyfills 函式庫 | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2019/02/03/Angular-CLI-73-Use-ES2015-nomodule-load-polyfills)

[[DAY-19] Angular架構與學習資源介紹 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天 (ithome.com.tw)](https://ithelp.ithome.com.tw/articles/10225044)