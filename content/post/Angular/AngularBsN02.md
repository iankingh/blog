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

# 從 0 開始的 Angular 生活 第2天-認識 Angular CLI 建立的專案架構

<!--more-->

## angular.json

Angular CLI 的設定檔 ，Angular CLI v6 之前檔名 angular-cli.json為。

## .editorconfig

 編輯器設定檔，設定處理 tab 符號、換行等等。

[官網](https://editorconfig.org/)。

## .gitignore

 設定git 忽略那些檔案不要加入版本控管。

## karma.conf.js

 karma.conf.js: 是一個單元測試工具。

[官網](https://karma-runner.github.io/latest/index.html)

## protractor.conf.js

E2E 測試，主要是測試使用者操作與想要的結果是否符合規格。

## tsconfig.json

TypeScript 編譯設定。

## tslint.json

TypeScript 程式碼風格檢查器。

## package.json

 npm 的設定檔， `scripts` 區塊定義了在開發 Angular 時用到的命令 。

## node_modeles 資料夾

存放`npm install` 後所有被下載下來所有的套件。

## e2e 資料夾

存放 End-To-End Testing 所有測試的指定檔都被放在這裡。

## src 資料夾(重要)

根據 Angular 官網的 Style Guide 建立而成Angular 應用程式主要的原始碼。

### app 資料夾(重要)

存放app.module 的地方

### index.html

angular 應用程式地進入點。

### style.css

在這裡它是 「global styles」也就是整個應用程式都會套用到的 CSS 定義，全部都可以寫在這裡。

### main.ts

main.ts 是 Angular 中 JavaScript 程式的進入點。(.ts 代表 TypeScript)

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

`bootstrapModule`  表示以引入` AppModule` 啟動

### app.module.ts 

根目錄的TS module

```typescript

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

### app.component.ts

```typescript
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

根目錄的TS controller

### assets(資產) 資料夾

放置所有的靜態檔案的資料夾，如額外的 JavaScript、JQery、CSS、圖片.........等等。

### .gitkeep 

Git 無法添加完全空目錄 ，希望跟蹤Git中空目錄的人就創建了將名為"gitkeep "的文件，把它放在這些目錄中的慣例，該文件可以被稱為任何東西;Git對此名稱沒有特殊意義。

### environments 資料夾

這個資料夾裡面所定義的是 Angular 專案內的環境變數，透過 TypeScript 定義一些環境變數。

這個資料夾內有兩個檔案，分別是 environment.ts 與 environment.prod.ts ，差別在於 environment.prod.ts 是只有當 build 出 production 版的應用程式時才用得上，否則在開發時期都是使用另一個設定檔。

### favicon.ico

瀏覽器業籤上面的圖示。

### polyfills.ts

當你的 Angular 應用程式同時要符合 IE 或舊版瀏覽器時，會用 [Polyfill](https://en.wikipedia.org/wiki/Polyfill_(programming)) 來填充缺少的 HTML5/JS APIs

### test.ts

測試 - Angular 的檔案

### tsconfig.app.json

Typescripe編譯成Javascript時的編譯設定

### tsconfig.spec.json

Typescripe編譯成Javascript時的編譯設定



# 參考

Angular CLI 7.3 使用 ES2015 的 nomodule 屬性載入 Polyfills 函式庫 | The Will Will Web
https://blog.miniasp.com/post/2019/02/03/Angular-CLI-73-Use-ES2015-nomodule-load-polyfills

[DAY-19] Angular架構與學習資源介紹 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天
https://ithelp.ithome.com.tw/articles/10225044

[從 0 開始的 Angular 生活]No.2 檔案架構 | pvt5r486's Blog
https://pvt5r486.github.io/f2e/20190520/3222844657/

