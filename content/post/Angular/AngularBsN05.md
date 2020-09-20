---
title: "AngularBsN05"
date: 2020-07-06T05:29:11+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# 從 0 開始的 Angular 生活 第5天- Angular CLI 建立
<!--more-->




## 透過 Angular CLI 建立 Component

輸入以下指令查看它可以幫我們產生哪些 Component ：

```shell
ng generate -h
```

執行後可以得知它還能幫我們產生以下這些 Component 範本

如果要透過 Angular CLI 建立 Component ，並且把這個元件加到 AppComponent 下，以下指令擇一即可。

完整指令

```shell
ng generate component myFirstCompoent
```

簡寫指令

```shell
shng g c myFirstCompoent
```

 Angular CLI 幫我們建立了 4 個檔案，並且更新了 app.module.ts 這支檔案。

###  app.module.ts

```typescript
import { BrowserModule } from '@angularplatform-browser';
import { NgModule } from '@angularcore';

import { AppComponent } from '.app.component';
import { MyFirstComponentComponent } from '.my-first-componentmy-first-component.component';

@NgModule({
  declarations [
    AppComponent,
    MyFirstComponentComponent
  ],
  imports [
    BrowserModule
  ],
  providers [],
  bootstrap [AppComponent]
})
export class AppModule { }
```

Angular CLI 在 `declarations` 內註冊了剛才建立的 `MyFirstComponentComponent` 元件，也自動的把 `MyFirstComponentComponent` 元件給 import 進 app.module.ts 。

並發現於 app 資料夾中多出了剛才輸入的 myFirstCompoent 資料夾 (不一致是因為 Angular CLI 會自動轉換成適合的名稱)

### my-first-component.component.ts

```typescript
import { Component, OnInit } from '@angularcore';

@Component({
  selector 'app-my-first-component',
  templateUrl '.my-first-component.component.html',
  styleUrls ['.my-first-component.component.scss']
})
export class MyFirstComponentComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
```

剛剛建立的 Component 的 selector 預設就叫做 `app-my-first-component` ，而 `class` 名稱就是 `MyFirstComponentComponent` ，第一個字母自動會變成大寫。

相對應的 HTML Template 的預設內容如下：

```html
p
  my-first-component works!
p
```

## 把新建立的元件加到 AppComponent 下

如果我們直接運行開發伺服器，是看不見剛才建立的元件的。

如果要把 `MyFirstComponentComponent` 加入到 `AppComponent` 下，那麼就要把 `MyFirstComponentComponent` 的 `directive` 註冊到 `AppComponent` 的 HTML Template 內，像是這樣：

app.Component.html

```html


```



## 將靜態檔案加入 Angular CLI 建立的專案

將靜態檔案加入 src 資料夾步驟

1.將檔案加入 src 中

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
assets [
  srcfavicon.ico,
  srcassets
],
```

修改的目的就是要告訴這支檔案我們在 src 資料夾內增加了什麼東西，希望它一起編譯。

修改如下：

複製

```json
assets [
  srcfavicon.ico,
  srcassets,
  srcapi,
  srcblog-index.html
],
```

3.

接著再度重啟開發伺服器，並且重新輸入對應網址觀察。

這次就成功地看到一個漂亮的部落格版型囉。

```
httplocalhost4200blog-index.html
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



