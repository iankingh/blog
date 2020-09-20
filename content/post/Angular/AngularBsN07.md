---
title: "AngularBsN07"
date: 2020-07-21T11:17:25+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# 從 0 開始的 Angular 生活 第7天-Angular 指令 (Directives)
<!--more-->

## 三種 Angular 指令 ( Directives )

- 元件型指令
  - 預設的元件就是一個含有樣板的指令
- 屬性型指令
  - 這種指令會修改元素的外觀或行為
  - 如 ngStyle 、 ngClass 指令可以自由的調整樣式
- 結構型指令
  - 這種指令會透過新增或者刪除 DOM 元素改變 DOM 結構
  - 例如 ngIf 、 ngFor 、 ngSwitch 就可以控制 DOM 結構
    - 特別注意 ngSwitch 前面不要加上星號
    - ngIf 、 ngFor 、 ngSwitchDefault 、 ngSwitchCase 前面要加上 * 號

# 元件型指令

之前建立的 HeaderComponent 就是屬於元件型指令，它是 Component 同時也是 Directives 。

接下來再次新建一個 Component 練習吧，輸入 `ng g c footer` ，這次我們建立 FooterComponent 。

- 同先前建立 HeaderComponent 步驟，在此不贅述，把程式碼搬運到對應檔案即可

最後別忘了在 AppComponent 內輸入 FooterComponent 的元件型指令，也就是

```html
<app-footer></app-footer>
```

##  footer.component.ts

觀察 FooterComponent 的 `class` ，可以發現只要這是一個 Conponent ，那麼就一定會有一個 裝飾器 ( decorater ) 宣告在上方，如：

**FooterComponent**

```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
}
```



### 裝飾器 ( decorater )

- 裝飾器的語法為

  ```
  @decoraterName
  ```

  - 所有的 Conponent 都會有一個名為 Conponent 的 decorater

- 然後傳入一個物件，這個物件用來描述 Conponent 有哪些特性，如

  - `selector` 選取器
  - `templateUrl` - 指出 template 路徑在哪裡，如果不輸入路徑也可以使用 `template` 屬性，直接輸入該 template 內容即可
  - `styleUrl` - 與 `templateUrl` 不同，後面接的是一個陣列的型態，意思也就是可以輸入多個不同的 CSS 檔

#### template 的例子，如果不想把 template 獨立成一個檔案，可以這麼

可以發現這麼做之後，網頁的 footer 仍然是正常的。



**事實上裝飾器內可以使用的屬性還有非常多，用到時再查文件就可以了。**

#### styleUrl 的例子，來寫一點 CSS

這個檔案是由 Angular CLI 自動幫我們產生的，因此預設是空白的，讓我們隨意寫一點樣式吧。

- 把 footer 底下的 copyright 字樣改成黃色

  複製

  ```
  <p class="text-muted credit">
    Copyright © 2016 by <a href="https://www.facebook.com/will.fans" target="_blank">XCVGYU</a>
    @ <a href="http://www.miniasp.com/" target="_blank">XCVGYUXCVGYU</a> -
    Powered by <a href="http://dotnetblogengine.net/" target="_blank">BlogEngine.NET</a> 3.2.0.3 -
    Design by <a href="http://seyfolahi.net/" target="_blank"
      title="Farzin Seyfolahi - UI/UX Designer at BlogEngine.NET">FS</a>
  </p>
  ```

調整 `credit` ，這邊為了方便示範所以直接使用 `!important` 強制覆蓋。

複製

```
.credit{
  color: yellow !important;
}
```



接著執行開發伺服器查看效果：
[![img](https://i.imgur.com/KAhwMgt.png)](https://i.imgur.com/KAhwMgt.png)

## 元件內的 CSS 不會影響到其他元件？

之前有提到，在這裡設定的 CSS 只會套用到該元件，不會影響到其他元件，超出 FooterComponent 範圍外的通通不會吃到這裡設定的 CSS 樣式。

這可以透過開發者工具觀察 Angular 是如何辦到的！

[![img](https://i.imgur.com/acBHG8e.png)](https://i.imgur.com/acBHG8e.png)

Angular 在這些動態產生的 diretive 下所有的標籤全都被加上了一個底線開頭的 attribute 屬性，而且有一定的規律可循。

**像是根元件上的 `_nghost-tij-c0` ， 0 是個編號，只要遇到不重複的 Component 就會有一個唯一的、不重複的編號。**

> .credit 類別被動態注入到頁面上時，它的選取器並不是單純的 .credit ，而是 .credit 後面加上中括號包覆 attribute 的選取器。

而這個 attribute 剛才說過是個**唯一**的值，這也是為什麼寫在元件內的 CSS 不會影響到其他元件的原因。

[![img](https://i.imgur.com/XEsLNeF.png)](https://i.imgur.com/XEsLNeF.png)

## 讓元件內的 CSS 會影響到其他元件

可以在裝飾器內新增一個屬性 `encapsulation` ，要把這部分的封裝調整成 `none` ，具體設定如下：

複製

```
@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss'],
  encapsulation: ViewEncapsulation.
})
```



[![img](https://i.imgur.com/pt2v0H9.png)](https://i.imgur.com/pt2v0H9.png)

- 預設是

   

  ```
  Emulated
  ```

   

  ，也就是模擬的意思，就是指 CSS Style 的封裝，

  - 在此要把它改成 `none` ，意思是不需要進行 CSS Style 的封裝。

**如此一來，這個 .credit 就會渲染到整個網頁了。**

[![Image](https://i.imgur.com/bDBRwp7.png)](https://i.imgur.com/bDBRwp7.png)

[Image](https://i.imgur.com/bDBRwp7.png)



> 設定後，現在當 .credit 類別被動態注入到頁面上時，它的選取器已經是單純的 .credit 了，也就是說這個網頁所有用到 .credit 這個 class 都會吃到字體顏色變成黃色的設定。

**以上就是元件型指令在使用上可能會用到的一些設定與注意事項，接下來要介紹的是屬性型指令。**

 

#  屬性型指令 (Attribute Directives)

這種 Directives 有個特性，就是本身不會有自己的 Template ，但是套用這個 Directives 的地方，會修改那一個元素或者是那一個標籤的外觀或者是行為。

在 Angular 內建的屬性型指令內有三種：

- ngModule - 雙向繫結
- ngStyle - 動態設置 CSS 的 Style
- ngClass - 動態設置 CSS 的 className

> 透過第二與第三個 Directives 可以很容易地去修改現有 HTML 的外觀、 CSS 的 Style 、 或動態的套用一些 class 。

## 如何使用 ngStyle

現在我們替 HeaderComponent 內加入一個新功能，當點擊網站 LOGO 時，計算被點了幾下。

### 前置作業

- 首先我們在 HeaderComponent 的 `class` 內做調整，加入 `counter` 屬性並補上點擊時 counter++ ：

```typescript
export class HeaderComponent implements OnInit {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  counter = 0;
  constructor() { }

  ngOnInit() {
  }
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
    this.counter++;
  }
}
```

- 並且修改 HeaderComponent 的 Template 使用內嵌繫結

```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3>Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```

### 動態調整 h3 標籤內的字體大小

**修改 HeaderComponent 的 Template**

```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [ngStyle]="{'font-size': (12 + counter) + 'px'}">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```

這邊做了一個 ngStyle 的屬性繫結，但是 ngStyle 並不是 h3 標籤的 Property 也不是 Attribute 。

**ngStyle 本身就是一個 Diretive ，這個 Diretive 可以透過 [] 繫結一個物件，然後這個物件的屬性就是要套用的 CSS 的 Style ，而值就是我們希望套用的值。**



### 進階用法

值得注意的是， ngStyle 後面跟著的是一個物件，這代表其實可以傳入多組 CSS 的 Style ，但是通通寫在 HTML 內會顯得很難看，所以我們也可以這麼處理：

**在 `class` 內撰寫方法並回傳**

```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [ngStyle]="getStyle()">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```

```typescript
export class HeaderComponent implements OnInit {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  counter = 0;
  constructor() { }

  ngOnInit() {
  }
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
    this.counter++;
  }
  getStyle() {
    return {'font-size': (12 + this.counter) + 'px'};
  }
}
```

這麼處理的結果會跟剛才的結果一模一樣。

**或者是直接透過屬性**

```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [ngStyle]="getStyle">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```



```typescript
export class HeaderComponent implements OnInit {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  counter = 0;
  getStyle = {
    'font-size': 20 + 'px'
  };
  constructor() { }

  ngOnInit() {
  }
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
    this.counter++;
  }
}
```



### ngStyle 的簡單用法

ngStyle 還有更簡單的使用方式，像是：



```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [style.font-size]="(12+counter) + 'px'">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```

直接在中括號內輸入 `style` 後面接上 `.` 直接加上想要套用的樣式即可，而等號後面則與剛才設定相同。

而如果你想要同時套用多種，可以這麼做：



```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [style.font-size]="(12+counter) + 'px'"
  [style.color]="'red'">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```



**而這個方法也可以使用 class 內的屬性或方法使其更易讀**



```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [style.font-size]="fontSize" [style.color]="fontColor">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```



```
export class HeaderComponent implements OnInit {
  title = 'firstAngular';
  link = 'http://www.google.com';
  imgUrl = '/assets/images/logo.png';
  counter = 0;
  fontSize = 16 + 'px';
  fontColor = 'red';
  constructor() { }

  ngOnInit() {
  }
  changeTitle(altKey: boolean) {
    if (altKey) {
      this.title = 'changeTitle';
    }
    this.counter++;
  }
}
```

執行結果如下

[![img](https://i.imgur.com/Mx54siL.png)](https://i.imgur.com/Mx54siL.png)

**這些方式可以選擇一種使用即可，看哪個順手就用哪個吧。**

## 如何使用 ngClass

如果已經知道如何使用 ngStyle ，那麼 ngClass 肯定難不倒我們，兩者的用法幾乎是一樣的。

我們將剛才設定過 ngStyle 的地方全部刪除，並且加上 ngClass ：



```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [ngClass]="{cssClass: expression}">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```



可以看到整體結構上基本同於 ngStyle ，等號後方一樣是接收一個物件，因此**剛才介紹的簡化方法 (寫在 class 的屬性、方法內) 同樣適用於 ngClass 。**

**於是可以修改成這樣**



```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [ngClass]="{'highlight': counter % 2 == 0}">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```



**物件屬性就是要設定的 className ， 而不同於 ngStyle 的是，這個地方的值要輸入布林值。**

- 當值為 True 時套用這個 className ，反之則不套用

> 接著新增 highlight 這個 className 吧

header.component.scss



```css
.highlight{
  background-color: red;
}
```





### ngClass 的簡單用法

聰明如你，想必已經猜到了如何使用，不囉嗦直接看範例！

複製

```html
<div class="pull-left">
  <h1><a [href]="link" id="title">{{title}}</a></h1>
  <h3 [class.highlight]="counter % 2 == 0">Lorem ipsum dolor sit amet. {{counter}}</h3>
</div>
```

**等號後方直接給布林值就可以了，這樣是不是更簡單了呢？**

> 也就是說等號後方可以直接寫一個布林值、或者透過 class 內的屬性、方法回傳布林值，這些都是合法的。只要是 `True` 就套用這個 className ，反之則不套用。

## 小結

終於介紹完屬性型指令了，整理這些東西的時候不禁讓我回想起 Vue 裡面的 `:class` 、 `:style` 這些東西，而新學會的這些東西也是相當的好記，語法本身也是蠻簡單的。

接下來就是 Angular 的第三種指令 - 結構型指令囉！

#  結構型指令 (Structural Directives)

這種結構型的指令會透過新增或刪除 DOM 的元素動態改變 DOM 的結構，內建有三種語法：

- ngIf
- ngSwitch
- ngFor

## ngIf

ngIf 的用法相當簡單，可以透過這個指令動態的新增或者是刪除一整段 HTML 的內容。

假設這個 ICON 區塊會根據 Counter 的數字動態的顯示或隱藏，那該怎麼做呢？
[![img](https://i.imgur.com/75oo2zQ.png)](https://i.imgur.com/75oo2zQ.png)

首先找到 Template 內對應的 HTML 區塊，並進行修改

複製

```html
<div id="social-icons" class="pull-right social-icon" *ngIf="counter % 2 == 0">
  <a href="https://www.google.com" target="_blank">
    <img src="/assets/images/facebook.png">
  </a>
  <a href="https://www.google.com" target="_blank">
    <img src="/assets/images/twitter.png">
  </a>
  <a href="https://www.google.com" target="_blank">
    <img src="/assets/images/googleplus.png">
  </a>
  <a href="https://www.google.com" target="_blank">
    <img src="/assets/images/plurk.png">
  </a>
  <a href="https://www.google.com" target="_blank">
    <img src="/assets/images/weibo.png">
  </a>
  <a href="https://www.google.com" title="RSS 訂閱" target="_blank">
    <img src="/assets/images/rss.png">
  </a>
</div>
```



特別的是 ngIf 前面必須加上一個 * 號，這個星號是結構型指令專屬的語法，算是語法糖的一種。

**只要是結構型指令，記得加上 \* 號就對了。**，不過我們也不需要真的死背，可以善用 code snippet 來輔助。

而 `*ngIf` 的等號後方同樣也是接布林值，因此在這裡我們填入 `counter % 2 == 0` 這樣就可以了。

- 只要回傳 True ，那麼就新增這個 HTML 區塊，反之則刪除

> 測試看看吧！

[![新增](https://i.imgur.com/xW7JaSG.png)](https://i.imgur.com/xW7JaSG.png)

[新增](https://i.imgur.com/xW7JaSG.png)



[![刪除](https://i.imgur.com/7L0XvQy.png)](https://i.imgur.com/7L0XvQy.png)

[刪除](https://i.imgur.com/7L0XvQy.png)



**這邊要強調的是 ngIf 是真的操作 DOM 元素動態改變結構進行新增或是刪除，也就是當回傳 False 時該區塊是完全不存在網頁中的，並非單純的隱藏。**

### 需要注意的地方

使用 ngif 時，雖然語法相當的簡單，可是有生命週期的細節需要注意。

使用 ngif 新增或刪除某個區塊的 HTML 時，那些區塊可能含有其他的 Component

- 當 `*ngif = false` 時 Component 會一起被刪除
- 當 `*ngif = True` 時 Component 被新增回來

也就是說這樣的情況下會影響到 Component 的生命週期，當 Component 被刪除時生命週期也就跟著結束了。

**因此下一次新增回來的 Component 狀態肯定會跟之前的不同，這點需要特別注意**

> 這個 Component 狀態好比 HeaderComponent 內的 counter ，假如目前 `counter = 5` 當元件被刪除又新增後，這個時候的 `counter` 已經被重置了。

## ngSwitch

ngSwitch 也是個結構型指令，假設我們有個需求是這樣：

- 根據 ngSwitch 去切換前三個 ICON 與後三個 ICON 的內容
- 切換的條件根據 `counter % 2` 產生的不同的餘數來切換

首先找到 Template 內對應的 HTML 區塊，並進行修改

複製

```html
<div id="social-icons" class="pull-right social-icon">
  <div [ngSwitch]="counter % 2">
    <div *ngSwitchCase="0">
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/facebook.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/twitter.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/googleplus.png">
      </a>
    </div>
    <div *ngSwitchCase="1">
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/plurk.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/weibo.png">
      </a>
      <a href="https://www.google.com" title="RSS 訂閱" target="_blank">
        <img src="/assets/images/rss.png">
      </a>
    </div>
    <div *ngSwitchDefault>N / A</div>
  </div>
</div>
```



`[ngSwitch]` 後面接的是條件，在這裡我們的條件設定為 `counter % 2` ，而 `*ngSwitchCase` 後面接的是「當遇到 0 或 1 時要顯示哪些東西」，那如果都不符合的話的則顯示 `*ngSwitchDefault` 的結果。

> 存檔測試看看吧！

[![img](https://i.imgur.com/xYwqq38.png)](https://i.imgur.com/xYwqq38.png)

[![img](https://i.imgur.com/f7LyRPF.png)](https://i.imgur.com/f7LyRPF.png)

**成功是成功了，但這時會發現使用 ngSwitch 導致 HTML 結構不一致。**

[![img](https://i.imgur.com/ERC9ezY.png)](https://i.imgur.com/ERC9ezY.png)

### 使用 ngSwitch 導致 HTML 結構不一致

這該怎麼修正呢？

> 可以使用 `ng-container` 來取代使用 ngSwitch 時產生的 div 標籤

複製

```html
<div id="social-icons" class="pull-right social-icon">
  <ng-container [ngSwitch]="counter % 2">
    <ng-container *ngSwitchCase="0">
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/facebook.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/twitter.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/googleplus.png">
      </a>
    </ng-container>
    <ng-container *ngSwitchCase="1">
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/plurk.png">
      </a>
      <a href="https://www.google.com" target="_blank">
        <img src="/assets/images/weibo.png">
      </a>
      <a href="https://www.google.com" title="RSS 訂閱" target="_blank">
        <img src="/assets/images/rss.png">
      </a>
    </ng-container>
    <ng-container *ngSwitchDefault>N / A</ng-container>
  </ng-container>
</div>
```

> 再次觀察 DOM 結構

[![img](https://i.imgur.com/QS3vLtz.png)](https://i.imgur.com/QS3vLtz.png)

此時就沒有多餘的 DIV 標籤了。

**從這邊我們知道，當使用結構型指令時可以使用 ng-container 標籤，使其不會產生出額外的 HTML 標籤。**

## ngFor

ngFor 的功能相當強大，使用的時機也相當頻繁。

舉例來說，當我們串接 API 的時候，會取得一份資料。此時可能會透過迴圈的方式顯示在畫面上，這時後就有機會用上 ngFor 。

因為目前網頁的文章是寫死的，接下來要透過 ngFor 動態的把文章的資料呈現在網頁上。

### 處理資料部分

先整理好要給 ngFor 跑的陣列資料，可以先寫死一份假資料在 app.component.ts 內。

**app.component.ts**

複製

```html
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
/* tslint:disable */
export class AppComponent {
  inputValue = '';
  atticleData = [
    {
      "id": 1,
      "href": "http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx",
      "title": "從命令提示字元中開啟 Visual Studio Code 如何避免顯示惱人的偵錯訊息",
      "date": "2016/04/30 18:05",
      "author": "GHJKL",
      "category": "Visual Studio",
      "category-link": "http://blog.miniasp.com/category/Visual-Studio.aspx",
      "summary": "<p>由於我的 Visual Studio Code 大部分時候都是在命令提示字元下啟動，所以只要用 <strong><font color='#ff0000' face='Consolas'>code .</font></strong>就可以快速啟動 Visual Studio Code 並自動開啟目前所在資料夾。不過不知道從哪個版本開始，我在啟動 Visual Studio Code 之後，卻開始在原本所在的命令提示字元視窗中出現一堆惱人的偵錯訊息，本篇文章試圖解析這個現象，並提出解決辦法。</p><p>... <a class='more' href='http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx#continue'>繼續閱讀</a>...</p>"
    },
    {
      "id": 2,
      "href": "http://blog.miniasp.com/post/2016/03/22/Does-Certification-Exam-Useful.aspx",
      "title": "考證照真的沒用嗎？一個從業 20 年的 IT 主管告訴你他怎麼看！",
      "date": "2016/03/22 19:28",
      "author": "GHJKL",
      "category": "心得分享",
      "category-link": "http://blog.miniasp.com/category/%E5%BF%83%E5%BE%97%E5%88%86%E4%BA%AB.aspx",
      "summary": "<p>其實無論在哪個國家都有推行證照制度，且行之有年，台灣當然也不例外，這件事一開始的立意都是好的，就是希望透過一套公平的考試制度，評估一個人的技術能力是否達到一定程度水準，不但能當成一個人的能力指標，也可以讓大家有個明確目標朝專業之路邁進。其他的行業我不清楚，但就我本身熟悉的 IT 產業來說，不知何年何月開始，大家開始對證照制度嗤之以鼻、不屑一顧，甚至覺得是一個人能力的<strong>負指標</strong> (也就是能力不好的人才需要靠證照證明自己)。你說這現象是何等的詭異？是什麼樣的天時、地利、人和，可以讓一個原本立意良善的制度，變成人人喊打的落水狗，可能連有張證照都還不敢承認的地步。今天，就來談談我的個人見解。</p><p>... <a class='more' href='http://blog.miniasp.com/post/2016/03/22/Does-Certification-Exam-Useful.aspx#continue'>繼續閱讀</a>...</p>"
    },
    {
      "id": 3,
      "href": "http://blog.miniasp.com/post/2016/03/14/ASPNET-MVC-Developer-Note-Part-28-Understanding-ModelState.aspx",
      "title": "ASP.NET MVC 開發心得分享 (28)：深入瞭解 ModelState 內部細節",
      "date": "2016/03/14 12:14",
      "author": "GHJKL",
      "category": "ASP.NET MVC",
      "category-link": "http://blog.miniasp.com/category/ASPNET-MVC.aspx",
      "summary": "<p>在 ASP.NET MVC 的 <strong>模型繫結</strong> (Model Binding) 完成之後，我們可以在 Controller / Action 中取得 <span style='font-family: Consolas;'>ModelState</span>                  物件，一般來說我們都會用 <span style='font-family: Consolas;'><strong>ModelState.IsValid</strong></span> 來檢查在「模型繫結」的過程中所做的<strong>輸入驗證</strong> (Input Validation) 與 <strong>模型驗證</strong> (Model Validation) 是否成功。不過，這個 <span style='font-family: Consolas;'>ModelState</span>物件的用途很廣，裡面存有非常多模型繫結過程的狀態資訊，不但在 Controller 中能用，在 View 裡面也能使用，用的好的話，可以讓你的 Controller 更輕、View 也更乾淨，本篇文章將分享幾個 ModelState 的使用技巧。</p><p>... <a class='more' href='http://blog.miniasp.com/post/2016/03/14/ASPNET-MVC-Developer-Note-Part-28-Understanding-ModelState.aspx#continue'>繼續閱讀</a>...</p>"
    }
  ]

  cleanInput() {
    this.inputValue = '';
  }
}
```



在這邊因為 tslint 要求我把所有的雙引號改成單引號，為了開發方便，我先暫時把 tslint 給關閉。

就這樣我們新增了一個 `atticleData` 屬性，裡面是一個陣列，陣列內又有一個個物件，而每一個物件又有相關的屬性。

**接著我們透過 ngFor 這個結構型指令來把這些通通顯示在畫面上吧！**

### 處理 Template 的 HTML 部分

回過頭來處理 HTML 部分，同樣我們使用 code snippet 幫助撰寫程式碼

複製

```html
<!-- Article START-->
<article class="post" id="post0" *ngFor="let item of atticleData">
  <header class="post-header">
    <h2 class="post-title">
      <a [href]="item.href">{{ item.title }}</a>
    </h2>
    <div class="post-info clearfix">
      <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date}}</span>
      <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
          href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
      <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
          [href]="item['category-link']">{{item.category}}</a></span>
    </div>
  </header>
  <section class="post-body text">
    {{item.summary}}
  </section>
</article>
<!-- Article END-->
```

這裡的 `*ngFor` 後面接的語法有點像是 JavaScript 中 ForEach() 的感覺， `item` 代表當前陣列的元素而 `atticleData` 則是要遍歷的目標陣列。

蠻像 Vue 中的 `v-for` 指令的，如果有學習過 Vue 肯定對這個部分不陌生。

> 運行開發伺服器，觀察結果吧！

[![img](https://i.imgur.com/bJU48Re.png)](https://i.imgur.com/bJU48Re.png)

[![img](https://i.imgur.com/TwIZCvw.png)](https://i.imgur.com/TwIZCvw.png)

至此，我們已經成功地透過 ngFor 快速的把資料轉換成網頁的內容，而且程式碼相當的簡潔。

**不過還需要修正最後一個小地方，那就是文章 summary 部分的 HTML 標籤居然直接被輸出了，這該怎麼辦呢？**

### 透過屬性繫結的方式

先把 HTML 中的 ``這段內嵌繫結刪除，並且套用屬性繫結

複製

```html
<!-- Article START-->
<article class="post" id="post0" *ngFor="let item of atticleData">
  <header class="post-header">
    <h2 class="post-title">
      <a [href]="item.href">{{ item.title }}</a>
    </h2>
    <div class="post-info clearfix">
      <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date}}</span>
      <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
          href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
      <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
          [href]="item['category-link']">{{item.category}}</a></span>
    </div>
  </header>
  <section class="post-body text" [innerHTML]="item.summary">
  </section>
</article>
<!-- Article END-->
```

**這一段的作法是將屬性繫結在 section 標籤的 DOM 物件內的 innerHTML 屬性上，這麼一來 HTML 的標籤就會直接寫入 innerHTML 這個屬性內。**

[![img](https://i.imgur.com/mKprMp1.png)](https://i.imgur.com/mKprMp1.png)

> 如此一來就全部搞定啦～

值得注意的是這個作法是有風險的，因為這些 HTML 可能含有一些惡意的內容，可能會導致 **Cross-Site Script** 的攻擊。

不過 Angular 有幫我們做到一些很基本的防護，例如在資料的部分偷偷的加一些料：

複製

```json
atticleData = [
  {
    "id": 1,
    "href": "http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx",
    "title": "從命令提示字元中開啟 Visual Studio Code 如何避免顯示惱人的偵錯訊息",
    "date": "2016/04/30 18:05",
    "author": "GHJKL",
    "category": "Visual Studio",
    "category-link": "http://blog.miniasp.com/category/Visual-Studio.aspx",
    "summary": "<script>alert('XSS!!!')</script><p>由於我的 Visual Studio Code 大部分時候都是在命令提示字元下啟動，所以只要用 <strong><font color='#ff0000' face='Consolas'>code .</font></strong>就可以快速啟動 Visual Studio Code 並自動開啟目前所在資料夾。不過不知道從哪個版本開始，我在啟動 Visual Studio Code 之後，卻開始在原本所在的命令提示字元視窗中出現一堆惱人的偵錯訊息，本篇文章試圖解析這個現象，並提出解決辦法。</p><p>... <a class='more' href='http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx#continue'>繼續閱讀</a>...</p>"
  },
  ...
]
```

**回到網頁上會發現 Angular 自動的把 script 標籤過濾掉了，所以什麼都事情都沒發生，而且還很智慧的顯示這一段提示**

[![img](https://i.imgur.com/sLhRAtb.png)](https://i.imgur.com/sLhRAtb.png)

> 意思是 Angular 幫我們從 HTML內了清除了一些有害的內容，而後面的連結則是關於 XSS 的資安文件。

### 替 ngFor 加上索引值

最後我們要替每一篇文章的 id 補上索引值，而 ngFor 裡面提供了一個好用的方法。

複製

```html
<!-- Article START-->
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <header class="post-header">
    <h2 class="post-title">
      <a [href]="item.href">{{ item.title }}</a>
    </h2>
    <div class="post-info clearfix">
      <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date}}</span>
      <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
          href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
      <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
          [href]="item['category-link']">{{item.category}}</a></span>
    </div>
  </header>
  <section class="post-body text" [innerHTML]="item.summary">
  </section>
</article>
<!-- Article END-->
```

**只有在 ngFor 指令下才可以使用，能自行宣告一個變數 `idx` ，並且賦值為 `index` ，如此一來就能取得目前的索引值。**

這時的文章 id 就會按照索引值增加了。

[![img](https://i.imgur.com/C9y8wIn.png)](https://i.imgur.com/C9y8wIn.png)

> 當然這邊也可以直接使用屬性繫結把資料內的 id 綁上去即可，只是這邊要介紹索引值的用法。

## 小結

總算是介紹完 Angular 的三種類型的指令了，有沒有覺得這些指令都似曾相似呢？就我來說的話肯定是有的，而大部分的用法都蠻接近的，只是細節上有不同之處。

希望能早日把 Angular 給掌握起來！

 

 