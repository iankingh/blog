---
title: "AngularBsN05"
date: 2020-07-06T05:33:29+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# 從 0 開始的 Angular 生活 第5天-資料繫結的四種方法
<!--more-->

在 Angular 內總共有四種資料繫結的方法，分別是

- 內嵌繫結 ( interpolation )

  ```
  {{property}}
  ```

- 屬性繫結 ( Property Binding )

  ```
  [property] = statemant
  ```

- 事件繫結 ( Event Binding )

  ```html
  (event) = someMethod($event)
  ```

- 雙向繫結 ( Two-way Binding )

  ```
  [(ngModel)] = property
  ```



## 內嵌繫結 ( interpolation )

之前把靜態網頁版型加到 Angular 專案內以 Component 方式管理後就沒有再動過了，這回我們從 `app.component.ts` 這裡開始。

**`app.component.ts` 內容**

複製

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

可以看到這個元件裡面除了一些必要的程式碼之外，沒有其他的東西了，相當的單純。而 `class` 裡面有一個 `title` 的屬性，這是一開始我們建立專案時 Angular CLI 自動幫我們添加的。

接著來到 `app.component.html` ，可將 `` 標籤處使用內嵌繫結 ( interpolation ) 的語法，替換成 `class` 內的 `title` 的屬性。

複製

```html
<div class="pull-left">
  <h1><a href="http://blog.miniasp.com/">{{title}}</a></h1>
  <h3>Lorem ipsum dolor sit amet.</h3>
</div>
```



打開 Angular 開發伺服器，可以觀察到  標籤內容的確是 title的屬性值。



內嵌繫結是屬於單向的繫結，也就是說畫面上呈現的 `title` 資料，只會從 Component 內把值傳送給 template 顯示。

## 把內嵌繫結用於屬性上

**內嵌繫結的語法除了放在標籤內，也可以使用在 HTML 標籤的屬性上。**

舉個例子，我們在 `app.component.ts` 內的屬性上新增一個 `link` 屬性：

複製

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
}
```

接著回到 `app.component.html` 將某一段 `a` 標籤的 `href` 內容給替換掉：

```html
<div class="pull-left">
  <h1><a href="{{link}}">{{title}}</a></h1>
  <h3>Lorem ipsum dolor sit amet.</h3>
</div>
```



## 屬性繫結 ( Property Binding )

> 值得注意的是屬性繫結 ( Property Binding ) 的屬性英文單字是 Property ，而 Attribute 的中文翻譯也叫做屬性。因此很有可能跟上一篇介紹到的內嵌繫結也可以應用在 HTML 標籤的屬性 ( Attribute ) 上搞混。

**實際看個例子，這次我們不使用內嵌繫結來改變 `a` 標籤上的 `href` 屬性：**

**component**

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
}
```

**templat**

```html
<div class="pull-left">
  <h1><a [href]="link">{{title}}</a></h1>
  <h3>Lorem ipsum dolor sit amet.</h3>
</div>
```

****

**component**

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
}
```

**template**

```html
<img [title]="title" [src]="imgUrl" class="pull-left logo">
```



## Property 與 Attribute 的差異

接下來透過一些範例，釐清 Property 與 Attribute 的差異。

### Attribute

一般而言，要擴充 HTML 標籤上的 Attribute 會使用 `data-*` 自由的擴充 HTML 標籤上的 Attribute ，例如：

**template**

```
<img [title]="title" [src]="imgUrl"　data-title="" class="pull-left logo">
```



接著我們可以實驗看看自訂的 HTML Attribute 可不可以使用屬性繫結。

**template**

```html
<img [title]="title" [src]="imgUrl"　[data-title]="title" class="pull-left logo">
```

運行開發伺服器，可以發現錯誤訊息

> 這段訊息大意上是說，綁定 Property 的時候， Angular 發現 `img` 底下並沒有 `data-title` 這個 Property ，因為 `data-title` 是我們自訂的 Attribute ，因此不能任意的使用屬性繫結，儘管它們中文翻譯都是**屬性**。

### Property

運行開發伺服器，並且使用開發工具觀察 `img` 標籤，可以看到非常多的 attribute。

這個標籤裡面 `class` 、 `title` 、 `src` 都是 Attribute

然而什麼是 Property 呢？

> 如果想知道 `img` 標籤的 Property ，可以查詢 `img` 的 DOM 物件所有的 Property 。

**透過開發者工具查詢**
可以點選 Properties 頁籤，切換過去後就可以看到 `img` 標籤下所有的 Property 了。

而在這裡面可以發現如 `class` 、 `title` 、 `src` 的 Property 。

### 什麼叫做 屬性繫結 ( Property Binding )

**屬性繫結 ( Property Binding ) 真正的對象，其實是 HTML 標籤下 DOM 的 Property ，而不是指 HTML 標籤上的 Attribute 。**

> 套用在剛才的範例上就是 `img` 標籤，這一個 DOM 的 Property。

### 透過標準的作法讓剛才自訂的 Attribute 也能使用屬性繫結

其實方法也不困難，只需要在前面補上 `attr.` ，如：

**template**

複製

```html
<img [title]="title" [src]="imgUrl"　[attr.data-title]="title" class="pull-left logo">
```

這樣子就可以成功設定 data Attribute 的自動綁定。

這時我們可以再次回到網頁上觀察情況。

可以發現 data-title 這個 Attribute 被綁定，而且也可以使用屬性繫結方法了。

## 事件繫結 ( Event Binding )

### 事件繫結語法 (一)

在事件中間加上 「-」，代表這是 Angular 的語法，並且在雙引號內放入 function ，但是在 **Angular 內並沒有 function 只有類別**，而**類別內只有屬性以及方法**。

**template**

```html
<img on-click="changeTitle()" [title]="title" [src]="imgUrl" [attr.data-title]="title" class="pull-left logo">
```

讓我們宣告一個方法叫做 `changeTitle` 。

**component**

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  changeTitle() {
    this.title = 'changeTitle';
  }
}
```



### 事件繫結語法 (二)

除了上述的作法外，也可以使用這種方式添加事件繫結。

**template**

```html
<img (click)="changeTitle()" [title]="title" [src]="imgUrl" [attr.data-title]="title" class="pull-left logo">
```

這樣的方式跟上一篇提到的屬性繫結是不是有點相似呢？

**差別在於屬性繫結是使用中括號 [] 表示，而事件繫結是使用小括號 () 表示。**

而大部分的 Angular 開發者都是使用第二種方法來進行事件綁定，較少使用第一種方法。

### 接著運行開發伺服器，測試看看結果。

[![點擊 LOGO 後](https://i.imgur.com/5shPMfI.png)](https://i.imgur.com/5shPMfI.png)

[點擊 LOGO 後](https://i.imgur.com/5shPMfI.png)



標題的確被更新了，但這是怎麼辦到的呢？

### 事件繫結的背後

我們在 LOGO 上執行了 Click 動作，然後註冊 Angular 的事件繫結，而這個事件繫結到了 `changeTitle` 方法，因此當有人點了 LOGO 時，就會跳到 AppComponent 內去執行 `changeTitle` 方法。

而這個方法會藉由執行 `this.title = 'changeTitle';` 來變更 class 內的 `title` 屬性，又因為先前我們對網站標題使用了內嵌繫結，所以當 class 內的 `title` 屬性有異動時， Angular 就會管理頁面 DOM 的狀態，也就是所有頁面中有繫結 `title` 屬性的地方一起改變。

## 事件繫結 - 使用 $event 參數

當撰寫事件繫結時必須要傳入一個方法，預設可以不用傳入任何參數，但是在這裡確實可以傳入一個很特別的參數 `$event` ，讓我們觀察看看。

**這個 `$event` 可以幫助我們取得事件的詳細資訊**

**template**

```html
<img (click)="changeTitle($event)" [title]="title" [src]="imgUrl" [attr.data-title]="title" class="pull-left logo">
```

**component**

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  changeTitle($event) {
    this.title = 'changeTitle';
    console.log($event);
  }
}
```



接著運行開發伺服器，按下 F12 開啟開發者工具並點擊 LOGO 圖案。

> 可以看到跑出了很多東西，而這個 MouseEvent 其實就是 DOM 的 MouseEvent ，因此這一次觸發的滑鼠事件內可以找到相當多的屬性。

### $event 參數內 - target

`target` 屬性代表的是剛剛點下去的那個 DOM 物件，例如說剛剛我們是點擊 img 觸發的，也就是說它的 `target` 屬性會是：

[![img 標籤的 DOM](https://i.imgur.com/xWBHVGL.png)](https://i.imgur.com/xWBHVGL.png)

[img 標籤的 DOM](https://i.imgur.com/xWBHVGL.png)



### $event 參數內 - altkey

`altkey` 屬性代表的是點擊時有沒有按下 「alt」 這個按鍵，因此我們可以替剛剛那個範例加上一個新的需求，必須要按下 「alt」 這個按鍵才可以更改標題。

**component**

複製

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  changeTitle($event) {
    if ($event.altKey) {
      this.title = 'changeTitle';
    }
    console.log($event);
  }
}
```



我在這邊踩到了一的雷，那就是 altKey 的 K 是大寫，因此這部分要特別注意英文的大小寫部分。

> 搞定！運行開發伺服器測試看看

[![img](https://i.imgur.com/vz5vUD6.png)](https://i.imgur.com/vz5vUD6.png)

**但是這個部分可以有更好的寫法，那就是使用具有型別的 $event 參數**

## 事件繫結 - 使用具有型別 $event 參數

在上一個範例裡，因為英文的大小寫導致程式沒有按我們預期的跑，但我們現在是使用 TypeScript 進行開發，所以我們可以利用 TypeScript 帶來的好處，利用型別來標註參數的型別，具體來說我們可以這麼做:

- 由剛才範例可知

   

  ```
  $event
  ```

   

  的內容其實是 MouseEvent

  - 也就是說傳入方法的參數其實是 MouseEvent 的型別

因此可以在 **Component** 內這麼寫：

複製

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  changeTitle($event: MouseEvent) {
    if ($event.altKey) {
      this.title = 'changeTitle';
    }
    console.log($event);
  }
}
```



接著神奇的事情發生了，當我們輸入 `$event` 並按下 `.` 時，VS Code 會列出所有 MouseEvent 內所有可以選擇的屬性。

[![img](https://i.imgur.com/KcPe3tN.png)](https://i.imgur.com/KcPe3tN.png)

### 巧妙的利用型別重構

我們知道可以在事件繫結中傳入 `$event` 參數，但其實這個部分可以更進一步的改寫，並且結合剛才的提到的型別，例如：

**template**

```
<img (click)="changeTitle($event.altKey)" [title]="title" [src]="imgUrl" [attr.data-title]="title" class="pull-left logo">
```

> 可以直接在這個地方就傳入 `$event.altKey` 。

**component**

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
  }
}
```



然而因為 `$event.altKey` 的值是 true 或 false ，因此型別是布林。

接著可以再次確認運作是否正常。



## 雙向繫結 ( Two-way Binding )

到目前為止介紹了三種資料繫結的方法，分別是內嵌繫結、屬性繫結、事件繫結，這三種的前兩種都是屬於從 Component 單向將資料傳送到 Template 的繫結方式。而事件繫結也算是單向的繫結方式，這是從 Template 內透過瀏覽器的事件觸發之後呼叫 Component 內的方法。

而我們這次要介紹的繫結方式就是雙向的繫結方式，這種繫結方式會自動的做到屬性繫結與事件繫結，也因此我們寫的程式碼會更少、更精簡。

### 拿上一篇的練習改寫，使其具有雙向繫結效果

我們將之前的練習改寫，見識見識雙向繫結的威力。

**template**

複製

```
<div class="widget-content">
  <div id="searchbox">
    <input type="text" placeholder="請輸入搜尋關鍵字" accesskey="s"
      [(ngModel)]="inputValue"
      (input)="calcLength($event.target.value)"
      (keydown.escape)="cleanInput($event.target)">
    <input type="button" value="搜尋" id="searchbutton">
  </div>
  目前字數 <span>{{inputStrLen}}</span>
</div>
```



> 要使用雙向繫結的話辦法相當簡單，使用 `[(ngModel)]` 語法後面接一個想要雙向繫結並且在 component 內的屬性即可。

**component**

複製

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  inputValue = '';
  inputStrLen = 0;
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
  }
  calcLength(str: string) {
    this.inputStrLen = str.length;
  }
  cleanInput(inputEl: HTMLInputElement) {
    this.inputStrLen = 0;
    inputEl.value = '';
  }
}
```



> 當運行開發伺服器後會發現， Angular 又掛掉了。



**意思就是 Angular 看不懂 ngModel 這個屬性是什麼。**

也就是說如果我們想要使用雙向繫結，還有一個步驟要做，那就是把 Angular 表單的模組匯入到 AppModule 內。

**於是打開 AppModule 這支檔案進行修改**

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

> 修改完成後，再次運行開發伺服器，發現可以成功運行網頁了，但我們還需要調整程式碼的部分。

可以透過內嵌繫結，測試一下剛才設置的雙向繫結 `inputValue` 有沒有成功

**template**

```
<div class="widget-content">
  <div id="searchbox">
    <input type="text" placeholder="請輸入搜尋關鍵字" accesskey="s"
      [(ngModel)]="inputValue"
      (input)="calcLength($event.target.value)"
      (keydown.escape)="cleanInput($event.target)">
    <input type="button" value="搜尋" id="searchbutton">
  </div>
  輸入文字：{{inputValue}} 目前字數 <span>{{inputStrLen}}</span>
</div>
```



**藉由這個測試知道，目前這個 input 的輸入框跟 component 內的 `inputValue` 已經建立了雙向繫結。**

## 完成這個練習

我們已經成功地建立了雙向繫結，接著把其他地方的程式碼也修改一下吧。

**template**

```html
<div class="widget-content">
  <div id="searchbox">
    <input type="text" placeholder="請輸入搜尋關鍵字" accesskey="s"
      [(ngModel)]="inputValue"
      (keydown.escape)="cleanInput()">
    <input type="button" value="搜尋" id="searchbutton">
  </div>
  輸入文字：{{inputValue}} 目前字數 <span>{{inputValue.length}}</span>
</div>
```

**component**

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  inputValue = '';
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
  }
  cleanInput() {
    this.inputValue = '';
  }
}
```

## 雙向繫結不是萬靈丹

雙向繫結既然這麼好用，我們是不是應該不管怎麼樣都使用雙向繫結呢？

事實上，過度濫用雙向繫結也會給網頁效能造成一些負擔，可能導致網頁的反應會變慢，但具體來說還是得看實際狀況而定就是了。



 