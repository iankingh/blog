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

[![img](https://i.imgur.com/yAmjSev.png)](https://i.imgur.com/yAmjSev.png)

透過這張圖可以觀察到，當執行 `npm start` 時，其實是呼叫執行 Angular CLI 的命令 `ng serve` ，這個過程會啟動一個開發伺服器，而這個開發伺服器在啟動之前，背後透過 Webpack 將目前的 Source Code 內所有的 TypeScript 進行編譯。

編譯之後把所有的 JavaScript 檔案合併在一起，而這個過程中產生了幾支檔案：

- es2015-polyfills.js, es2015-polyfills.js.map
- polyfills.js, polyfills.js.map
- runtime.js, runtime.js.map
- styles.js, styles.js.map
- vendor.js, vendor.js.map

**那麼這些檔案會用在什麼地方呢？**

## index.html

在首頁打開的時候，預設會把剛才編譯產生的這些檔案給載入，我們可以透過觀察原始碼來了解。

### 對著 index.html 按右鍵 > 檢視網頁原始碼

標籤事實上就是 Angular 裡面的根元件，也可以稱它為一個 directive ，關於 directive 之後會有更詳細的說明。

然後發現 之前被插入了剛剛編譯出來的 .js 檔，而 Angular 應用程式也在載入這些 .js 檔後正式開始運行。

**然而執行的過程中，也有一個啟動的流程。**

啟動的流程結束後，標籤的內容就會被動態的插入一些 DOM 物件，最後顯示在畫面上。

### 對著 index.html 按右鍵 > 檢查

從 chrome 的開發者工具底下，可以看到標籤包含了一些從剛剛的原始碼內看不到的標籤。



因為這些內容全部都是透過 Angular 應用程式動態運算出來的結果。

### 實際觀察專案內的 index.html 檔案

這支檔案也就是剛才 chrome 瀏覽器開啟的檔案，而裡面確實有個標籤。

可以發現檔案內的

標籤內並沒有插入剛才那些 .js 檔，也就是說那是 **Webpack 幫我們編譯後動態插入的**。



> 也就是說我們在開發 Angular 網頁時，它的 JavaScript 在開發時期是動態被注入的。

## 從哪支 .js 檔開始跑呢？

之前有提過， Angular 應用程式的進入點是 main.ts 檔案，而它的長相如下：

複製

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

前面 5 行主要是引用從某一些模組匯入程式運行時必要的物件進來。
而第 11 行的地方，則是透過 `platformBrowserDynamic().bootstrapModule(AppModule)` 去執行啟動模組這件事，接著會進入到 `AppModule` 裡面執行相關的程式碼，讓我們一起觀察下去吧。

> 小提示：在 VSCode 內可以對著 `AppModule` 點一下接著按 F12 會自動追蹤到該檔案喔

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

   

  ```
  app-root
  ```

   

  就是選取到 HTML 中

   

  ```
  app-root
  ```

   

  標籤，並且把這個標籤的內容，修改為這個元件執行的結果。

  - 同理，如果改寫成 `.app-root` 則是選取具有 `.app-root` 的 className

舉例來說可以這麼做，我們修改 AppComponent 與 index.html 如下：

複製

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



## 透過 Angular CLI 建立 Component

可以使用 VSCode 下方的終端機 (按下 Ctrl + ` 開啟)，

可以輸入以下指令查看它可以幫我們產生哪些 Component 範本：

```
ng generate -h
```

執行後可以得知它還能幫我們產生以下這些 Component 範本，是不是很方便呢？

[![img](https://i.imgur.com/9S8VBbj.png)](https://i.imgur.com/9S8VBbj.png)

如果要透過 Angular CLI 建立 Component ，並且把這個元件加到 AppComponent 下，以下指令擇一即可。

完整指令

```
ng generate component myFirstCompoent
```

簡寫指令

```
ng g c myFirstCompoent
```



執行後得到以下結果：

得知 Angular CLI 幫我們建立了 4 個檔案，並且更新了 app.module.ts 這支檔案。**

並發現於 app 資料夾中多出了剛才輸入的 myFirstCompoent 資料夾 (不一致是因為 Angular CLI 會自動轉換成適合的名稱)

[![img](https://i.imgur.com/CSHd3fy.png)](https://i.imgur.com/CSHd3fy.png)

> 之後當我們使用這個方式來建立 Component 時，都會產生類似的檔案結構來建立 Angular 應用程式。

### 觀察 my-first-component.component.ts

```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-my-first-component',
  templateUrl: './my-first-component.component.html',
  styleUrls: ['./my-first-component.component.scss']
})
export class MyFirstComponentComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
```

剛剛建立的 Component 的 selector 預設就叫做 `app-my-first-component` ，而 `class` 名稱就是 `MyFirstComponentComponent` ，第一個字母自動會變成大寫。

接著還有相對應的 HTML Template 與 SCSS ， SCSS 的內容是空的 、 Template 的預設內容如下：

複製

```html
<p>
  my-first-component works!
</p>
```



而透過 Angular CLI 還有一支 my-first-component.component.spec.ts 檔，這主要是拿來做單元測試用的檔案。

所以**一個 Component 預設會有 4 支檔案被建立**，還記得剛才 Angular CLI 有更新 app.module.ts ，讓我們看看它做了什麼。

### 觀察 app.module.ts

複製

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MyFirstComponentComponent } from './my-first-component/my-first-component.component';

@NgModule({
  declarations: [
    AppComponent,
    MyFirstComponentComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Angular CLI 很智慧地幫在 `declarations` 內註冊了剛才建立的 `MyFirstComponentComponent` 元件，而且也自動的把 `MyFirstComponentComponent` 元件給 import 進 app.module.ts ，相當的便利。

那麼，接下來我們要如何把剛剛建立的 `MyFirstComponentComponent` 呈現在畫面上呢？

## 把新建立的元件加到 AppComponent 下

如果我們直接運行開發伺服器，是看不見剛才建立的元件的。

如果要把 `MyFirstComponentComponent` 加入到 `AppComponent` 下，那麼就要把 `MyFirstComponentComponent` 的 directive 註冊到 `AppComponent` 的 HTML Template 內，像是這樣：

```html
<!--The content below is only a placeholder and can be replaced.-->
<div style="text-align:center">
  <h1>
    Welcome to {{ title }}!
  </h1>
  <!--這邊有一張圖片進行 base64 編碼，太佔空間了所以我把它移除 .-->
</div>
<app-my-first-component></app-my-first-component>
<h2>Here are some links to help you start: </h2>
<ul>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://angular.io/tutorial">Tour of Heroes</a></h2>
  </li>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://angular.io/cli">CLI Documentation</a></h2>
  </li>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://blog.angular.io/">Angular blog</a></h2>
  </li>
</ul>
```

## 調整 MyFirstComponentComponent 元件

來到 `MyFirstComponentComponent` 的 HTML Template 進行如下修改：

```html
<h2>Here are some links to help you start: </h2>
<ul>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://angular.io/tutorial">Tour of Heroes</a></h2>
  </li>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://angular.io/cli">CLI Documentation</a></h2>
  </li>
  <li>
    <h2><a target="_blank" rel="noopener" href="https://blog.angular.io/">Angular blog</a></h2>
  </li>
</ul>
```



而 `AppComponent` 修改如下

```html
<!--The content below is only a placeholder and can be replaced.-->
<div style="text-align:center">
  <h1>
    Welcome to {{ title }}!
  </h1>
  <!--這邊有一張圖片進行 base64 編碼，太佔空間了所以我把它移除 .-->
</div>
<app-my-first-component></app-my-first-component>
```

## 將靜態檔案加入 Angular CLI 建立的專案

將靜態檔案加入 src 資料夾步驟

1.將檔案加入 src 中

首先我有一份靜態網頁的版型叫做 BlogSiteHtml ，解壓縮後的內容有：

- api 資料夾
- assets 資料夾
- blog-index 網頁版型

接著把這些檔案全部貼到 Angular 專案的 src 資料夾內

2.修改angular.json 的設定

因為當我們把這些新的靜態檔案加入到 src 目錄後，還需要設定 angular.json ，告訴這支檔案我們做了什麼異動。

進入到這支檔案後，可以看到非常多密密麻麻的設定，而我們這次要修改的是 `assets` 區塊的內容，而它位於 `architect` 物件下的 `build` 物件下的 `options` 物件內。

修改前

複製

```json
"assets": [
  "src/favicon.ico",
  "src/assets"
],
```



**修改的目的就是要告訴這支檔案我們在 src 資料夾內增加了什麼東西，希望它一起編譯。**

修改如下：

複製

```json
"assets": [
  "src/favicon.ico",
  "src/assets",
  "src/api",
  "src/blog-index.html"
],
```

3.

接著再度重啟開發伺服器，並且重新輸入對應網址觀察。

這次就成功地看到一個漂亮的部落格版型囉。

```
http://localhost:4200/blog-index.html
```



## Angular CLI 發行與部屬

可以透過 Angular CLI 的指令辦到這件事情，叫出 VS Code 的終端機，並輸入以下指令：

複製

```
ng build
```



這麼做 Angular CLI 會透過 webpack 幫我們把專案的內容通通打包並且輸出到 dist 資料夾內，而且是沒有進行 minify 的版本。

而如果是正式發布的產品版，則應該額外加入 `--prod` 參數，進行 minify 優化，如：

複製

```
ng build --prod
```



