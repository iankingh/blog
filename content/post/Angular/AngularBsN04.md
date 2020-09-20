---
title: "AngularBsN04"
date: 2020-07-06T05:29:11+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# 從 0 開始的 Angular 生活 第4天-了解 Angular基本架構與啟動流程
<!--more-->



## Angular 應用程式的啟動過程

## npm start

首先開啟一個之前就建立好的 Angular 專案範本，接著在 VSCode 的終端機執行 `npm start` 。

當執行 `npm start` 時，其實是呼叫執行 Angular CLI 的命令 `ng serve` ，這個過程會啟動一個開發伺服器，而這個開發伺服器在啟動之前，背後透過 Webpack 將目前的 Source Code 內所有的 TypeScript 進行編譯。



main.ts   >>>>>  AppModule >>>>>>   bootstrap: [AppComponent]  >>>>> templateUrl:'./app.component.html', styleUrls: ['./app.component.scss']  >>>>>>  動態插入  app-root 底下

## main.ts

 Angular 應用程式的進入點：

```typescript
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

### AppModule 內

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

> 這支檔案可以說是在 Angular 應用程式裡面最重要的一支程式，而程式碼結構不難看出它是一個 `class` 而且被 export 出來，神奇的是裡面沒有任何的程式碼。

在大部分的情況，我們寫 Angular 應用程式時確實是不需要寫程式在裡面的。

我們只需要套用一個 `declarator` ，而這個 `declarator` 要設定成 `NgModule` ，去宣告這個類別它是一個 Angular 的 Module ，然後我們在這個 Module 裡面又有好幾個 Property (屬性) 需要宣告：

- declarations - 用來宣告一些跟 view 有關的元件
- imports - 用來匯入一些跟這個模組會用到的其他模組，而模組說穿了就是多個元件封裝後的東西
  - 而 `BrowserModule` 就是把 `BrowserModule` 內所有的元件一起匯入進來的意思
- providers - 註冊服務的提供者
- bootstrap - 啟動根元件 `AppComponent` ，也就是 Angular 最上層的元件 (預設名稱為 `AppComponent`)

**接著我們使用剛才介紹的追蹤方式，繼續追蹤 `AppComponent`**

### AppComponent 內

```javascript
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

AppComponent 元件的程式碼結構也一樣是個被 export 的 `class` ，然後這個範例程式預設有一個屬性 `title` 。

這個元件一樣有使用到 `declarator` ，叫做 `Component` ，這個 `Component` 在 Angular 內有特殊的涵義，這是用來宣告這個 `class` 代表的是一個 Component 。

而這個 Component 同樣有一些屬性如：

- selector - 如果寫過 JQuery 肯定不會陌生，就是一個選取器，如同範例的

   


  標籤，並且把這個標籤的內容，修改為這個元件執行的結果。
  
  - 同理，如果改寫成 `.app-root` 則是選取具有 `.app-root` 的 className

舉例來說可以這麼做，我們修改 AppComponent 與 index.html 如下：

```html
import { Component } from '@angular/core';

@Component({
  selector: '.app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
}
```

```html
<body>
  <!-- <app-root class="app-root"></app-root> -->
  <div class="app-root"></div>
</body>
```

之後回到瀏覽器觀察，發現仍然是可以運行的。

而 HTML 中不管是直接在元件寫上 className 或者是新建一個具有 `app-root` className 的 div 標籤都是有效果的。

在我們把 `selector` 修改成 `.app-root` 後，下方突然多出綠色的蚯蚓，這是因為我使用了 TSLint ，而 TSLint 這個套件是遵照 Angular 官方發布的 Style Guide 規範，這當中就包含了 Component 的 selector 最好都以 element 的 selector 為主。

[![img](https://i.imgur.com/mGbaM2T.png)](https://i.imgur.com/mGbaM2T.png)

- templateUrl - 指這個 AppComponent 的 HTML Template 的所在之處，而這堆內容就是我們在瀏覽器上看到的 HTML 內容

[![img](https://i.imgur.com/z22zGRb.png)](https://i.imgur.com/z22zGRb.png)

**所以我們的每一個 Component 都會有一個相對應的 HTML Template 做搭配，一個負責程式的邏輯、另一個負責呈現於瀏覽器。**

- styleUrls - 指 AppComponent 的 HTML Template 有用到的 CSS 樣式，需要注意的是這裡的樣式預設只針對這個 Component ，並不會與其他 Component 互相衝突，當然這個預設值也是可以調整的。



