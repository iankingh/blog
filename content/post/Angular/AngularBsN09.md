---
title: "AngularBsN09"
date: 2020-07-22T18:25:12+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angular元件架構與模組
<!--more-->





@input() 透過 Property Binding 傳值到子元件





 





(生命週期的介面)

ngOnInit 跟 ngOnDestroy  跟 ngOnchange介面



@output() 透過 Binding 傳值到父元件





# Angular 元件架構



Angular 是採用元件化模組開發的框架，可以想像就是不同大大小小元件堆砌而成的網頁，這樣的情況下元件架構又是如何呢？



## Angular 元件架構

[![img](https://i.imgur.com/Z3wEIRK.png)](https://i.imgur.com/Z3wEIRK.png)

從這張圖可以看出完整個的 Angular 應用程式，是由不同的元件所組成。

最上層的根元件預設名稱為 AppComponent ，而底下可能包含了 Header 元件與 ArticleList 元件。

- 而 Header 元件裡面可能只有單純的 HTML 或一些互動
- 而元件內可以放入其他元件，如 ArticleList 元件可以在包含其他不同的元件，像是
  - ArticleHeader 元件
  - ArticleBody 元件

**也就是說在 Angular 的世界，網頁是由一層層的元件所組成。**

而元件跟元件之間就有父子的關係，像是

- ArticleList 元件可以說是 ArticleHeader 、 ArticleBody 的父元件
  - 反過來就是 ArticleHeader 、 ArticleBody 元件是 ArticleList 的子元件

## 元件之間的溝通

元件與元件之間是可以互相溝通的，例如：

- 資料存放於 ArticleList 元件上，而需要把資料往下傳送給子元件 ArticleBody
  - 此時會在 ArticleBody 建立一個屬性準備接收資料，因此就能形成屬性繫結的關係

相反的，如果是子元件往父元件溝通呢？

- ArticleHeader 、 ArticleBody 有一個共同的父元件 ArticleList
  - 此時可以透過事件繫結的方式來通知父元件
    - 具體來說就是會在子元件內寫一些屬性、程式來通知父元件

[![img](https://i.imgur.com/F3XGWYO.png)](https://i.imgur.com/F3XGWYO.png)

## 服務元件？

進階的元件與元件的溝通會藉由建立服務元件來達成。

而服務元件有可能會透過一種稱為**相依注入 ( Dependency Injection ) 簡稱 DI** 的技術，把預先設計好的服務元件直接注入到某個特定得元件內。

**舉例來說，可以透過 DI 技術將某個服務元件注入到 ArticleList 元件內，或者是 ArticleHeader 元件等等。**

> 而服務元件內封裝的就是不同元件之間需要共用的資料、方法等等

## 模組化

雖然這個架構看起來相當不錯，當網站越來越大時，通常會將相關的元件像是：

- ArticleList
- ArticleHeader
- ArticleBody
- 服務元件

把這些相關的元件封裝起來，獨立成為一個 Angular 的模組，像這種根據特定功能建立的模組，有時候也被稱為**功能模組 (Feature Module)**。

[![img](https://i.imgur.com/FPb4bnF.png)](https://i.imgur.com/FPb4bnF.png)

## 小結

好的，現在我了解在 Angular 內不同元件間是如何溝通的了，而且也覺得蠻熟悉的，儘管方法可能完全不同，但卻有點類似。

- 像是在 Vue 中 父子元件溝通的方式可以透過 props 傳入 、 emit 傳出，來達成父子元件溝通
- 也可以使用 event bus 或者 Vuex 來管理元件間的溝通

**好了，讓我們繼續探索 Angular 吧。**

 

# 建立功能模組

ng g m article 



## Angular 功能模組

 發表於 2019-05-30 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

當專案的架構越來越龐大時，此時會將一些較相關的元件與服務元件獨立封裝成一個 Angular 的模組，像這種根據特定功能建立的模組，有時候也被稱為**功能模組 (Feature Module)**



## 事前規劃

假使我想要逐步地將目前部落格版型改成這張圖片上畫的那樣，該怎麼做呢？

[![img](https://i.imgur.com/qRLnhnv.png)](https://i.imgur.com/qRLnhnv.png)

> 目前專案內並沒有 Article 相關的三個元件， ArticleModule 也還沒建立，讓我們一一的完成它吧。

## 建立 ArticleModule 模組 (Feature Module)

我要建立一個 Article 的模組，而這個模組在建立完成後，必須匯入到 AppModule 內，如此一來 Angular 才知道有 ArticleModule 的存在。

### 透過 Angular CLI 建立模組並加入根模組

這裡有兩種方式可以建立模組，則一即可：

- `ng generate Module article`
- `ng g m article`

**模組名稱打小寫就可以了，不用特地加上 Module 字樣**

執行成功後 app 資料夾內會產生一個 article 的資料夾

[![img](https://i.imgur.com/jNME8ll.png)](https://i.imgur.com/jNME8ll.png)
[![img](https://i.imgur.com/vDY17aw.png)](https://i.imgur.com/vDY17aw.png)

比較一下 app.module 與 article.module 的內容差異

**app.module**

複製

```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
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



**article.module**

複製

```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ]
})
export class ArticleModule { }
```



app.module 是根模組、 article.module 是功能模組

- article.module 內的 declarations 是空的，因為目前還沒有任何元件

**而下一步則是把 article.module 加入 app.module**，讓 Angular 知道我們新增了功能模組。

調整如下：
[![自動完成](https://i.imgur.com/8I5SEx5.png)](https://i.imgur.com/8I5SEx5.png)

[自動完成](https://i.imgur.com/8I5SEx5.png)



[![不費吹灰之力](https://i.imgur.com/2nhRZAF.png)](https://i.imgur.com/2nhRZAF.png)

[不費吹灰之力](https://i.imgur.com/2nhRZAF.png)



> 這是因為新版的 VS Code 內建 TypeScript 新的版本，而 TypeScript 新版支援 Auto Import 的功能。

存檔後確認有無任何錯誤。

[![img](https://i.imgur.com/4mW7bDU.png)](https://i.imgur.com/4mW7bDU.png)

**非常好，沒有任何問題產生！**

## 其實剛剛做的事情只需要一行就完成

剛才介紹了如何透過 Angular CLI 建立模組，但其實這些指令後面還可以加入一些參數，例如：

- `ng generate Module article -m app`
- `ng g m article -m app`

> `-m` 後面可以接一個模組名稱，像是上面的指令示範。

**這麼做就會使 Angular CLI 建立 article 模組後自動地向 app.module 註冊。**

[![img](https://i.imgur.com/vixBlID.png)](https://i.imgur.com/vixBlID.png)

[![img](https://i.imgur.com/5W8R2ji.png)](https://i.imgur.com/5W8R2ji.png)

> **超棒的功能，不是嗎？**

## 將現有的元件加入功能模組

目前這個功能模組內是空的，因此要開始拆解部落格內關於 Article 的 HTML 並封裝成元件了。

將 Article 的 HTML 拆分為以下三個元件：

- ArticleList
  - ArticleHeader
  - ArticleBody

最後向 ArticleModule 註冊這些元件。

### ArticleList 元件拆解

首先將 AppComponent 底下 Article 的部分，全部拆解成一個新的元件 - ArticleList

- 輸入 `ng g c articleList` 建立 ArticleList 元件。

但此時我們不能直接輸入這道命令，因為預設 Angular CLI 會把元件註冊到 app.module ，但事實上必須將其註冊到 article.module 才正確。

**因此應該先使用 CD 指令，將資料夾切換至 article 資料夾底下**

[![img](https://i.imgur.com/X5HpCAz.png)](https://i.imgur.com/X5HpCAz.png)

接著就可以一如往常地建立元件了～

[![img](https://i.imgur.com/ChJehi5.png)](https://i.imgur.com/ChJehi5.png)

> 而且也會發現元件在 article.module 內被註冊了。

**除了在 app.module 內註冊 article.module 外， article.module 也必須匯出元件才行！**

因此修改 article.module

複製

```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleListComponent } from './article-list/article-list.component';

@NgModule({
  declarations: [ArticleListComponent],
  imports: [
    CommonModule
  ],
  exports: [ArticleListComponent]
})
export class ArticleModule { }
```



**接著開始搬運 AppComponent 底下 Article 的 HTML**

- 在 app.component.html 剪下 HTML ，並補上 ``
- 把剪下的 HTML 貼到 article-list.component.html
- 之前文章的資料存放於 app.component.ts ，因此也必須移轉到 article-list.component.ts

> 搞定！執行看看吧～

[![img](https://i.imgur.com/oHlKsrc.png)](https://i.imgur.com/oHlKsrc.png)

### 把剩餘的兩個元件拆完

跟剛才建立 article-list 元件一樣，必須將目錄切換過去才能開始建立元件，過程就不贅述了。

- 輸入指令建立 article-header 、 article-body

[![img](https://i.imgur.com/0FY1nmC.png)](https://i.imgur.com/0FY1nmC.png)

**這時我們可能會想要把這些元件給匯出，畢竟記取剛才的教訓嘛～**

> 從外部的角度而言，只需要看到 article-list 元件，並不需要看到 article-header 、 article-body 。
> 因為這兩個子元件是被封裝在 article-list 元件內的，所以僅匯出 article-list 元件即可。

接著就繼續搬動 HTML 囉，過程就不贅述了

- 拆分 article-list.component.html 內的 HTML 給
  - article-header.component.html
  - article-body.component.html

最後於 article-list.component.html 內補上對應的元件標籤就完成了。

至此已經將架構大致完成，但細部還需要做調整。

**此時網頁會是壞掉的，因為目前 article 的資料仍停留在 article-list 並未向下傳遞**，

下一篇將介紹如何把資料往子元件傳遞。

[# 學習筆記](https://pvt5r486.github.io/tags/學習筆記/) [# Angular](https://pvt5r486.github.io/tags/Angular/)

 

##  定義 Angular 元件的輸入介面 - @input()

 發表於 2019-05-30 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

承接上一篇文章，目前資料是存放於父元件的，但卻是子元件需要這份資料做輸出，那要如何將父元件的資料傳遞給子元件呢？

[![img](https://images.unsplash.com/photo-1559032806-99a331d600b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1498&q=80)](https://images.unsplash.com/photo-1559032806-99a331d600b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1498&q=80)

## @input()

現在專案內發生的問題就是:

- 兩個子元件 ArticleHeader 與 ArticleBody 的 Template 內有使用到 item 變數
  - 但是 `item` 變數並沒有被傳進來，它仍然存在於 ArticleList 內

**如何把 `item` 變數傳入這兩個子元件呢？**

### 在子元件的 class 內加入 @input() 裝飾器

如同先前提到的，要將父元件的資料傳遞到子元件，必須透過屬性繫結的方式。

> 意味著子元件必須要有一個屬性可以承接，於是在這邊宣告屬性 item ，並且不賦予任何值。

複製

```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  item;
  constructor() { }

  ngOnInit() {
  }

}
```

但這麼做還不夠，因為目前這個 item 只隸屬於 ArticleHeader 元件，在預設的情況下 `item` 是無法被父元件透過屬性繫結注入資料的。

**還必須加入 @input() 這個 declarator 裝飾器**，並且匯入相依模組才可以使用。

而這個步驟同樣也有自動完成可以使用，因此修正後如下：

複製

```
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;
  constructor() { }

  ngOnInit() {
  }

}
```



> 我們必須也在 ArticleBody 的 class 進行相同的操作，就不贅述了。

而經過上述這些步驟可以發現原本的錯誤已經不見了。

原因是我們已經定義了 `item` ，但是這樣還不算完成，先看一下目前網頁的狀態。

[![img](https://i.imgur.com/dHqzlMO.png)](https://i.imgur.com/dHqzlMO.png)

**可以看到目前是沒有資料傳進來的，還需要做一些處理。**

### 透過屬性繫結傳入資料

回到 ArticleList 的 Template 內，並且對兩個子元件加入屬性繫結。

**居然有支援自動完成，太神啦！**

[![img](https://i.imgur.com/JtmlJ7D.png)](https://i.imgur.com/JtmlJ7D.png)

複製

```
<!-- Article START-->
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <app-article-header [item]=item></app-article-header>
  <app-article-body [item]=item></app-article-body>
</article>
<!-- Article END-->
```

> 我們就完成了子元件的屬性繫結，中括號 [] 裡面的 `item` 是剛才在子元件內定義的屬性，而等號後面接的是要傳入的資料也就是區域變數 `item` 。

來測試看看吧！

[![img](https://i.imgur.com/3qkwND0.png)](https://i.imgur.com/3qkwND0.png)

至此，我們就完成了一個功能模組的建立，並且這個功能模組內有三個元件，其中父元件為 ArticleList 與它的兩個子元件 ArticleHeader 、 ArticleBody 。

[![img](https://i.imgur.com/pVrmA9I.png)](https://i.imgur.com/pVrmA9I.png)

## 小結

Angular 應用程式的架構，就是把網頁變成一個個大大小小的元件，這是屬於元件化的架構。

在元件化的架構下只要能妥善規劃，在開發、維護、管理層面上複雜度可以大幅地降低。





ng g m article -m app







# 建立專案

 開啟Cmd Cd到目錄

ng new demo1èèèèè 建立專案

ng serve  èèèèè 啟動專案

將網頁加入Angular

 

Angualr 啟動流程 >>>>>

\1.   main.ts 

\2.   app.module.ts

\3.   app.component.ts

\4.   執行1.component export calss 

\5.   2.selector :’app-root’

\6.   3.app.component.htm

\7.   4.app.component.css

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

1. 

2. 1. class內的變數，可以直接在html利用{{}}輸出

   2. 1. 例如
             export class AppComponent {
              title = 'app works!';
             }
             可以在app.component.html新增div tag，然後寫入{{title}}，這樣就可以把資料顯示出來
             例如
             <div>{{title}}</div>
             這樣就會顯示app works字串

   3. 顯示紅底字是beta11才有的問題

   4. app這個prefix的設定在angular-cli.json的defaults的物件

   5. css !important，會把上層的css蓋掉

   6. 用ng2下的tag都會加上component的專屬ID，這樣可以讓各component的互不影響

   7. 若要使用全域的css有下列作法

   8. 1. 把css放在index.html
      2. 在component.ts設定(通常不這麼做)

   9. 在command line執行ng build -prod可以匯出目前的ng2檔案

   10. 1. 比較重要的檔案會在body內顯示重要的script的js檔案，要複製過去才能使用

   11. *ngIf：會套用template標籤

   12. data是關鍵字不要亂用

   13. 盡量不要再view裡面宣告變數，最好在ts裡面宣告，再到view裡面使用

   14. pipe = 類似ng1的filter

3. 練習01：將靜態頁面變成動態的 Angular 2 模組與範本

4. 1. 搬移index-blog.html的head區塊搬到index.html
   2. 搬移index-blog.html的body區塊搬到app.component.html (view)

5. 練習02：將網頁頁首的部分建立成 HeaderComponent 元件

6. 1. 將header封裝成元件，讓app.component使用

   2. 使用command line執行ng g(general) c(component) header

   3. 將app.component.html的<head>放到header.component.html

   4. 在app.component.html輸入<app-header>

   5. 到app.component.ts，import header.component

   6. 1. import { HeaderComponent } from './header';

   7. 在@Component的物件新增一個屬性directives，值是陣列

   8. directives屬性輸入HeaderComponent(為header.component的ClassName)

   9. @Component({
          selector: 'app-root',
          templateUrl: 'app.component.html',
          styleUrls: ['app.component.css'],
          directives:[HeaderComponent]
          })

7. 練習03：修改     HeaderComponent 的 selector 條件 ( .header ) (     <div class="header"></div> )

8. 1. 在header.component的selector可以指定成class、id，例如selector: '.app-header'
   2. 在app.component的部分只要將<app-header>改成，<div      class="app-header">，也可以正常運作

9. 練習04：練習 Angular 2 資料繫結方法：內嵌繫結 ( interpolation )

10. 1. 在header.component內增加屬性，pageTitle      = “The will will Web Test"

    2. 1. 可以不用加型別，因為typescript會自動型別判定

    3. 到header.component.html把title換成{{pageTitle}}

11. 練習05：練習 Angular 2 資料繫結方法：屬性繫結 ( Property Binding )

12. 1. <a [href]="pageTitleLink">

    2. 1. 將href的屬性加上[]，這樣就不用加上{{}}
       2. pageTitleLink是header.component.ts的變數

13. 練習06：練習 Angular 2 資料繫結方法：屬性繫結 ( Property Binding ) + DOM 屬性繫結 ( innerHTML )

14. 1. 如果要綁在某個tag上，利用innerHtml屬性處理，例如

    2. 1. <h3       [innerHtml]="subTitle"></h3>

       2. subTitle = '記載著       <strong>Will</strong> 在網路世界的學習心得與技術分享';

15. 練習07：了解 Angular 2 元件 CSS 樣式如何套用到頁面上

16. 1. 將class寫到header.component.css，例如.blus {color:blue;}，並將想調整的tag加上class

    2. 因為ng2下的tag都會加上component的專屬ID，這樣可以讓各component的互不影響

    3. 1. 例如app.component.css內的class css不會影響到header.component.html的class

17. 練習08：練習 Angular 2 資料繫結方法：事件繫結 ( Property Binding ) + DOM 屬性繫結 ( Event Binding )

18. 1. 先在html的tag加上(click)="plus($event)"

    2. 1. $event固定

    3. 然後到ts內寫method

    4. plus(event:MouseEvent){
           this.num++;
         }

    5. 1. event後面加上型別，可以讓ts知道event有什麼屬性可用

19. 練習09：練習 Angular 2 資料繫結方法：雙向繫結 ( Two-way Binding )

20. 1. ng2的ng-model寫法如下

    2. 1. <input type="text"       placeholder="請輸入搜尋關鍵字" accesskey="s"       (keyup)="search($event)" [(ngModel)]="keyword”>{{keyword}}

    3. 可以不宣告keyword這個變數在header.ts內

    4. [(ngModel)]由[ngModel] = “keyword”      & (ngModelChange) = “keyword = $event"

21. 練習10：練習 Angular 2 範本參考物件的用法 ( #name )

22. 1. 單向綁定的寫法，透過範本參考變數使用

    2. <input type="text"      placeholder="請輸入搜尋關鍵字" accesskey="s" (keyup)="search($event,keywordInput)" #keywordInput>

    3. 1. \#keywordInput會是一個存在template內的變數，用來存取這個input的屬性

    4. search(event:KeyboardEvent,input:HTMLInputElement){
           this.keyword = input.value;
          }

    5. 1. input的value像是$(input).val()的意思
       2. Keyboard,HTMLInputElement都是告知ts這個變數的可以有什麼屬性

23. 練習11：練習 Angular 2 屬性型指令 (directives)：ngClass

24. 1. 先寫好css classname

    2. <h3 (click)="plus($event)"      [innerHtml]="subTitle" [ngClass]="{blue:      num%2==1,red:num%2==0}"></h3>

    3. 1. 根據物件名稱例如 blue後的條件，決定要不要使用這個class

    4. 另一種寫法<h3 (click)="plus($event)"      [innerHtml]="subTitle" [class.blue]="num%2==1"      [class.red]="num%2==0"></h3>

25. 練習12：練習 Angular 2 結構型指令 (directives)：ngIf

26. 1. <div *ngIf="num%2==1"      id="social-icons" class="pull-right social-icon">

27. 練習13：練習 Angular 2 結構型指令 (directives)：ngFor

28. 1. <article *ngFor="let item of      data" class="post">

    2. <a href=""      [innerHTML]="item.test"></a>

    3. <a href=""      >{{item.test}}</a>

29. 練習14：練習 Angular 2 的元件資料輸入機制 @Input()

30. 1. 在主要的html引用另一個component，例如<app-post [item]="data"></app-post>

    2. 1. item是子層的component的變數，data是父層component的變數

    3. 子層的component，import { Component, OnInit,Input } from      '@angular/core';

    4. 1. Input是關鍵字，傳值的東西

    5. @Input() item:any;

    6. 1. 這個寫法就會將父層的data，指定成父層的data變數

31. 練習15：請將先前 App 元件的 ngFor 迴圈改成 Article 元件 + ngFor 迴圈 + 傳入單一文章物件到 Article 元件裡

32. 1. <app-post      [item]="data"></app-post>

33. 練習16：

34. 1. Output：回傳資料

    2. EventEmitter：送資料回去
           doSearch(event:KeyboardEvent,input:HTMLInputElement){
           if(event.keyCode == 13){
               this.keyword = input.value;
               this.search.emit(this.keyword);
              }
           }

    3. 範例：@Output() search = new EventEmitter();

    4. 父層html寫<app-search      (search)="searchKeyword=$event"></app-search>

    5. 1. search = 子層的變數
       2. searchKeyword = 父層的變數
       3. $event = 回傳值 = 第二點的this.search.emit(this.keyword);

35. 練習17：注入器，共用service

36. 1. 利用@Injectable()，建立相依
    2. 到main.ts新增serviceProvider
    3. 到要共用service的component的import
    4. 在建構子設定
           constructor(private searchSearch: SearchService) {}
    5. 這樣就能共用該service.ts內的function及函式

37. 練習18：利用ajax接值(GET)

38. 1. main.ts加入

    2. 1. import { HTTP_PROVIDERS } from       '@angular/http';
       2. bootstrap(AppComponent, [HTTP_PROVIDERS]);

    3. 到要使用ajax的component加入

    4. 1. import { Http } from '@angular/http';
       2. constructor(private http: Http) {
              http.get('/api/articles.json').subscribe((value) => {
               this.data = this.defaults = value.json();
              });
            }









附錄



Cmd 功能

npm list -g –deth=0 

npm outdated –g

npm install 安裝npm

npm install –g @angular/cli 安裝angular/cli

Ctrl +C 停止指令

ng –v

ng update

ng generate -h 	查可以建立的原件

ng generate component page1 	建立component (四個檔案一個資料夾)

(ng g c page1) (ng generate component page1)

ng g c test1  建立名叫test1的component

ng g c article -list  建立component

ng g m article 建立 ArticleModule

ng build  編譯成js跟html

ng build --prod  編譯成js跟html (壓縮板)



main.ts 	進入點 

.angular-cli.json

設定載入資源

“apps”:

[

{

}

]

 

Index.html 

<head>



<bade href="/"> 設定目錄資源連結位址

</head>

 [從 0 開始的 Angular 生活]No.28 Angular 的生命週期 Hook - ngOnInit 與 ngOnDestroy

 發表於 2019-05-30 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

每一個 Angular 元件都有自己的生命周期，元件隨時會被建立也有可能隨時被註銷，之前介紹到結構性指令的時候也有稍微提到一些。而這一篇文章主要介紹的是，元件被建立的過程中程式碼運行的順序是如何？

[![img](https://images.unsplash.com/photo-1559163206-6615672fad34?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)](https://images.unsplash.com/photo-1559163206-6615672fad34?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)

## 元件的生命週期 Hook

之前在建立元件時，常常會在元件的 class 內看到兩個方法，但是從來沒有使用過。

分別是：

- constructor(){}
- ngOnInit(){}

### 最先執行 - 建構式 constructor()

constructor 是一個建構式，而建構式會在 class 被建立時，第一時間被執行，換句話說在 Angular 的生命週期裡面，這是第一個執行的程式碼。

不過幾乎不會寫任何程式在 constructor 內，因為當 constructor 執行時，元件尚未被初始化，所以是接不到任何資料的。

儘管如此， constructor 還是有特殊的用途，例如拿來做**相依注入 ( DI )**

### 生命週期 Hook - ngOnInit()

從這個名稱來看，應該多少會猜到是 Angular 進行 Init 初始化後會執行的程式碼。

從 ngOnInit() 開始，該元件的初始化、該元件所有必要的屬性繫結都已經完成。

> 也就是說可以對目前這個元件做一些初始化的動作。

舉例來說

- 設定屬性的預設值
- 發出 Ajax 的要求跟伺服器要資料，並把值寫到屬性內，透過屬性繫結呈現在 Template 上

> 所以這個方法算是蠻常用到的。

**當 ngOnInit() 結束後就會正式進入到 Angular 的生命週期，像是進行屬性繫結、事件繫結等等。**

### 生命週期 Hook - ngOnDestroy()

當父元件決定要摧毀目前這個子元件時，這個方法可以讓元件在被摧毀前執行特定的程式碼。

但是這個 Hook 的使用機會比較少，大部分的情況元件裡面的記憶體通常都會自動回收。

所以不需要特別地去寫程式處理這一塊，但是在少數的情況下像是搭配 Rxjs 去做一些非同步事件的訂閱，有些時候確實就必須在這個時間點做處理。

### 小結

關於元件的生命週期還有很多沒有介紹到，同樣也是可以等用到時在了解即可，在撰寫這篇的過程中也找到一些前輩整理好的資料：

- [[Angular 大師之路\] Day 04 - 認識 Angular 的生命週期](https://ithelp.ithome.com.tw/articles/10203203)
- [[功能介紹-3\] Hooks的生命週期](https://ithelp.ithome.com.tw/articles/10194566)

[![Lifecycle Hooks](https://i.imgur.com/eMUPWsS.png)](https://i.imgur.com/eMUPWsS.png)









## [從 0 開始的 Angular 生活]No.29 定義 Angular 元件的輸出介面 - @Output()

 發表於 2019-05-31 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

在物件導向程式的領域，有個稱為 OCP ( Open Closed Principle ) 的原則，中文稱為開放封閉原則。這原則說的是，在進行物件導向程式設計時要能符合開放擴充但封閉修改的要素，這樣子才能把每個不同的物件獨立切開、互不干擾。

這段前言又跟這篇文章有什麼關係呢？

## 截至目前為止的結構

可整理出如下列表

- AppModule - 根模組
  - AppComponent
    - ArticleList
      - ArticleHeader
      - ArticleBody

而元件一層包一層的好處是，一次只要關注一個想要修改的地方就好了，不管應用程式多複雜透過元件化的架構，就可以把一份複雜的網頁切割成多個元件，每個元件只單純負責幾件事情就好。

## 製作刪除文章的功能

假使想要實作出刪除文章的按鈕，想要將這個按鈕放在 ArticleHeader 的 Template 內，點擊後能夠將刪除的資訊傳給父元件 ArticleList ，最後達成刪除文章的效果。

### 添加刪除按鈕

首先在 ArticleHeader 的 Template 內做出一顆按鈕。

複製

```
<header class="post-header">
  <h2 class="post-title">
    <a [href]="item.href">{{ item.subject?.title|lowercase|slice:-20 }}</a>
    <small>{{item.subject?.subtite}}</small>
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span><button>刪除</button></span>
</header>
```

但是這樣是沒辦法刪除的，因為資料是由父元件 ArticleList 傳遞給子元件 ArticleHeader ，子元件本身並不具有這份資料。

**解決辦法是將要刪除哪筆篇文章的資料往上傳遞給父元件，透過父元件刪除該篇文章。**

白話來說，以刪除文章這個功能而言：

- 子元件 ArticleHeader 扮演的角色是：**透過點擊事件通知父元件哪一篇文章的刪除按鈕被點擊了。**
- 接著父元件 ArticleList 接收到訊息後把對應資料刪除，重新透過 ngFor 渲染網頁。

### 註冊 ArticleHeader 內的事件

**從父元件傳值給子元件是透過屬性繫結；從子元件傳值給父元件則必須透過事件繫結。**

在 Angular 元件內要註冊一個事件必須先宣告一個屬性，同時宣告一個 `@Output` 裝飾器，跟之前介紹過的 `@Input` 一樣。

首先來到 ArticleHeader 的 `class` 內進行修改：

複製

```
import { Component, OnInit, Input, Output } from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete;
  constructor() { }

  ngOnInit() {
  }

}
```

> 這樣就完成了 delete 事件的註冊，接著要將這個事件繫結到父元件上。

**事件的名稱可以自由命名。**

### 在父元件上繫結 delete 事件

剛才已經在子元件內註冊了 delete 事件，此時在 ArticleList 內已經可以從自動完成中看到對應的選項。

[![img](https://i.imgur.com/l4Hl1aK.png)](https://i.imgur.com/l4Hl1aK.png)

ArticleList 內的 Template

複製

```
<!-- Article START-->
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <app-article-header [item]="item" (delete)="doDelete($event)"></app-article-header>
  <app-article-body [item]="item"></app-article-body>
</article>
<!-- Article END-->
```



> 當接收到 `delete` 事件發出的通知時，就會觸發 ArticleList 內的 `doDelete()` 方法，而且還要讓它傳入一個 `$event` 參數，這樣才能知道使用者點擊的是哪一篇文章的刪除按鈕。

### 完成 ArticleHeader 內的 delete 事件

剛才雖然已經註冊 `delete` 事件，但還有很多細節尚待處理。

- 例如剛才宣告的

   

  ```
  delete
  ```

   

  屬性需要 new 一個 EventEmitter 物件

  - EventEmitter 是一個事件的發射器。
  - EventEmitter 後面可以接 `` ，代表要傳送的資料可以是任意型別

[![選擇正確的 EventEmitter](https://i.imgur.com/S0vTXFQ.png)](https://i.imgur.com/S0vTXFQ.png)

[選擇正確的 EventEmitter](https://i.imgur.com/S0vTXFQ.png)



複製

```
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();
  constructor() { }

  ngOnInit() {
  }

}
```

**什麼時候發射 delete 的事件？自然是按下刪除按鈕的時候**
回到 ArticleHeader 的 Template :

複製

```
<header class="post-header">
  <h2 class="post-title">
    <a [href]="item.href">{{ item.subject?.title|lowercase|slice:-20 }}</a>
    <small>{{item.subject?.subtite}}</small>
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span><button (click)="deleteArticle()">刪除</button></span>
</header>
```

> 當點擊按鈕時透過點擊事件，觸發 ArticleHeader 內的 `deleteArticle` 方法。
> 因此我們必須實作 `deleteArticle` 方法。

複製

```
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();
  constructor() { }

  ngOnInit() {
  }

  deleteArticle(){
    this.delete.emit(this.item);
  }
}
```

當 `deleteArticle` 方法被觸發時，透過 `delete.emit()` 這個事件發射器，將 `this.item` 向父元件射出。

而父元件上的 `$event` 接收的資料就會是剛才被射出的 `this.item` 。

### 實作 doDelete 方法

回到 ArticleList 的 `class` 內，實作刪除文章。

複製

```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html',
  styleUrls: ['./article-list.component.scss']
})
export class ArticleListComponent implements OnInit {
  atticleData: Array<any>;
  constructor() { }
  ngOnInit() {
    /* tslint:disable */
    this.atticleData = [
      {
        "id": 1,
        "href": "http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx",
        "subject": {
          "title": "從命令提示字元中開啟 Visual Studio Code 如何避免顯示惱人的偵錯訊息",
          "subtite": "Visual Studio Code"
        },
        "date": "2016/04/30 18:05",
        "author": "GHJKL",
        "category": "Visual Studio",
        "category-link": "http://blog.miniasp.com/category/Visual-Studio.aspx",
        "summary": "<p>由於我的 Visual Studio Code 大部分時候都是在命令提示字元下啟動，所以只要用 <strong><font color='#ff0000' face='Consolas'>code .</font></strong>就可以快速啟動 Visual Studio Code 並自動開啟目前所在資料夾。不過不知道從哪個版本開始，我在啟動 Visual Studio Code 之後，卻開始在原本所在的命令提示字元視窗中出現一堆惱人的偵錯訊息，本篇文章試圖解析這個現象，並提出解決辦法。</p><p>... <a class='more' href='http://blog.miniasp.com/post/2016/04/30/Visual-Studio-Code-from-Command-Prompt-notes.aspx#continue'>繼續閱讀</a>...</p>"
      },
      ...
    ];
  }
  doDelete(item){
    this.atticleData = this.atticleData.filter((data)=>{
      return data.id !== item.id;
    })
  }
}
```

因為 `atticleData` 屬性並沒有明確的型別，所以使用自動完成並沒有提示可以使用什麼方法，因此手動補上 `Array` 代表這是一個可以傳入任何資料的陣列。

最後透過 ES6 的 filter 方法篩選被刪除的文章，達成本次需求。

> 搞定～測試看看吧！

[![把文章全刪除了](https://i.imgur.com/Ijsd8NI.png)](https://i.imgur.com/Ijsd8NI.png)

[把文章全刪除了](https://i.imgur.com/Ijsd8NI.png)



## 小結

可以很明顯的看出，從子元件將資料傳遞給父元件是要透過比較多道手續的，但整體而言也不難理解，就花點時間好好地記住吧。



## [從 0 開始的 Angular 生活]No.30 解釋單向資料流與不可變的物件

 發表於 2019-05-31 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

單向資料流與不可變的物件，究竟這是什麼意思呢？

[![img](https://images.unsplash.com/photo-1559157865-4982964542a3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)](https://images.unsplash.com/photo-1559157865-4982964542a3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)

## 目前架構

我們目前的專案結構大致如下：

[![img](https://i.imgur.com/PuCHg6s.png)](https://i.imgur.com/PuCHg6s.png)

- ArticleList 元件 - 擁有所有的資料，並透過屬性繫結把資料傳給子元件
  - ArticleHeader - 擁有屬性 item ，承接來自父元件的物件資料
  - ArticleBody - 擁有屬性 item ，承接來自父元件的物件資料

## 功能需求

假設今天有一個需求是要更改文章標題，最簡單的做法就是直接從 ArticleHeader 動手，修改 item 這個物件的屬性值，這個屬性值只要一改變，父元件 data 下的這些物件值也會跟著改變。

> 而雖然這個改法很簡單，不過建議最好不要這麼做。

盡量不要在子元件內直接對資料進行任何修改，否則元件間的相依性會太重，當有 Bug 產生時也不容易除錯。

最好是透過**單向資料流**的方式來達成。

## 單向資料流

單向資料流的意思就是，**所有資料的變更永遠是從上層元件傳給下層元件。**

換句話說，比較好的做法是：

- ArticleHeader 內提供一個編輯的介面，讓使用者設定新的標題
- 當確定送出時才把要變更的內容透過事件繫結傳遞給父元件，也就是 ArticleList 元件
- ArticleList 元件做實際物件的操作 (變更資料等等)

## 不可變的物件

JavaScript 物件本身是可變的，所以當物件發生改變時如果希望另一個元件也能知道這個物件發生改變，這在 JavaScript 內非常不容易做到。

舉例來說，在 ArticleHeader 內修改了 item 物件，那麼 ArticleBody 如何知道 ArticleHeader 內修改了 item 物件的哪個屬性呢？

要怎麼樣 Angular 這個物件確實發生了改變、讓 ArticleBody 能反映出相對應的資料呢？

**Angular 確實做得到，但是這樣效能會很差。**

像是在 ArticleHeader 新增了一個點擊事件，並且觸發一個 `test` 方法，執行 `item` 物件內 `summary` 屬性值的修改。

複製

```
<header class="post-header" (click)="test()">
  <h2 class="post-title" >
    <a [href]="item.href">{{ item.subject?.title|lowercase|slice:-20 }}</a>
    <small>{{item.subject?.subtite}}</small>
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span><button (click)="deleteArticle()">刪除</button></span>
</header>
```

複製

```
import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();
  constructor() { }

  ngOnInit() {
  }
  deleteArticle() {
    this.delete.emit(this.item);
  }
  test() {
    console.log(this.item);
    this.item.summary = 'aaa';
  }
}
```

[![img](https://i.imgur.com/bU0KI9w.png)](https://i.imgur.com/bU0KI9w.png)

> 點擊後的確影響到 ArticleBody 內的資料了，但是非常不推薦這麼做。

**好的作法**

- 當在 ArticleHeader 修改了 item 物件的內容，應該把修改過的內容往上傳給父元件
- 在父元件內找出是哪一筆資料更動，假設是第一筆
  - 接著重新建立一個全新的物件、連同陣列的部分也產生新的

而這樣就是所謂的**不可變的物件特性**。

只要物件不管哪個屬性發生變更，通通都重新產生物件的話，在 Angular 內很容易就可以辨識出那些物件發生了變化。

舉例來說

- 只要陣列變成新的，那麼 ngFor 就會重新渲染
- 陣列的其中一個元素的物件是新的，Angular 就會知道這個物件在做資料繫結時要把新的資料渲染到畫面上。



## [從 0 開始的 Angular 生活]No.31 實作單向資料流與不可變的物件





## 需求描述

我想要實作一個修改文章標題的功能

- 在 ArticleHeader 內新增一個按鈕叫做編輯標題
  - 按下後標題顯示輸入框供使用者輸入新標題，按下 Enter 確定修改；按下 ESC 則退出

了解需求後立馬動手吧～

## 先從 UI 開始

因為這個需求所以要調整 ArticleHeader 元件下的 Template 以及 class ，順便移除掉一些不相干的東西讓這個範例看起來更單純。

### ArticleHeader Template 的調整

- 新增編輯標題按鈕、取消編輯按鈕並加上點擊事件
- 把之前的 PipeComponent 給取消
- 重新調整一下文章的資料格式，讓範例更簡單易懂
  - 把 `subject` 那一層拿掉、刪除 `subtitle`

複製

```
<header class="post-header">
  <h2 class="post-title" >
    <a [href]="item.href">{{ item.title}}</a>
    <input type="text" size="70" [value]="item.title">
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span>
    <button (click)="deleteArticle()">刪除</button>
    <button (click)="">編輯標題</button>
    <button (click)="">取消編輯</button>
  </span>
</header>
```

現在網頁呈現的畫面是這樣的：

[![img](https://i.imgur.com/XY4RgNv.png)](https://i.imgur.com/XY4RgNv.png)

邏輯是這樣的：

- 使用結構型指令 ngIf 控制標題與輸入框以及編輯與取消按鈕的顯示
- 當使用者點擊編輯標題按鈕時修改 `isEdit` 的值為 `True` 、點擊取消編輯按鈕時 `isEdit` 的值為 `False`

> 為了做到這些事情，所以必須先到 ArticleHeader class 進行調整

### ArticleHeader class 的調整

這裡需要做的調整如下：

- 新增屬性　`isEdit` 用來判斷是不是處於編輯模式，預設為 `False`

複製

```
import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();

  isEdit = false;
  constructor() { }
  ngOnInit() {
  }
}
```

**回到 Template 補上 ngIf**

複製

```
<header class="post-header">
  <h2 class="post-title" >
    <a *ngIf="!isEdit" [href]="item.href">{{ item.title}}</a>
    <input *ngIf="isEdit" type="text" size="70" [value]="item.title">
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span>
    <button (click)="deleteArticle()">刪除</button>
    <button *ngIf="!isEdit" (click)="isEdit=true">編輯標題</button>
    <button *ngIf="isEdit" (click)="isEdit=false">取消編輯</button>
  </span>
</header>
```

**測試一下目前的邏輯是否正確**

[![非編輯模式](https://i.imgur.com/MKSogOE.png)](https://i.imgur.com/MKSogOE.png)

[非編輯模式](https://i.imgur.com/MKSogOE.png)



[![編輯模式](https://i.imgur.com/vRK5l1Q.png)](https://i.imgur.com/vRK5l1Q.png)

[編輯模式](https://i.imgur.com/vRK5l1Q.png)



## 實作編輯文章標題

這邊有個一個簡單但不太建議的做法：

- 直接在 input 上使用雙向繫結綁定 `item.title`

> 這麼做會直接把修改的內容直接寫回去，而需求瞬間就完成了。

**但伴隨而來的缺點是**

- 會讓子元件與父元件間相依性太重
- 因為是雙向繫結，一但修改後是沒辦法透過取消編輯取消的，會直接修改到原始的資料。

> 所以這個做法肯定是不太行的，得換個方式。

**比較好的方式** - 透過單向資料流與不可變的物件方式

- 在 ArticleHeader Template 的 input 上建立二個 Keyup 事件，並傳入參數

   

  ```
  $event
  ```

  - 當使用者按下 Enter 時觸發 `editTitle` 方法
  - 當使用者按下 ESC 時觸發 `exitEdit` 方法

- 在 ArticleHeader class 內建立一個屬性值 `newTitle`

- 進行 `ngOnInit()` 時將 `newTitle` 賦值為 `item.title`

- input 上使用屬性繫結 value 的值改用 `newTitle`

複製

```
<header class="post-header">
  <h2 class="post-title" >
    <a *ngIf="!isEdit" [href]="item.href">{{ item.title}}</a>
    <input *ngIf="isEdit" type="text" size="70" [value]="newTitle"
      (keyup.enter)="editTitle($event)" (keyup.escape)="editExit($event)">
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span>
    <button (click)="deleteArticle()">刪除</button>
    <button *ngIf="!isEdit" (click)="isEdit=true">編輯標題</button>
    <button *ngIf="isEdit" (click)="isEdit=false">取消編輯</button>
  </span>
</header>
```

複製

```
import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();
  isEdit = false;
  newTitle = '';
  constructor() { }

  ngOnInit() {
    this.newTitle = this.item.title;
  }
  deleteArticle() {
    this.delete.emit(this.item);
  }
  editTitle(e) {
    console.log('editTitle', e.target);
    this.newTitle = e.target.value;
  }
  editExit(e) {
    console.log('editExit', e.target);
    e.target.value = this.item.title;
    this.isEdit = false;
  }
}
```

- 當觸發 `editTitle` 方法時，會將 input 內的 value 值取出並賦值給 `newTitle` ，等待傳送給父元件
- 當觸發 `editExit` 方法時，將原始資料塞回 input 內的 value

**前置作業都做完了，剩下就是通知父元件 ArticleList 囉！**

- 建立一個新的 `@Output()` 並宣告一個 `titleChange` 的事件
- 當觸發 `editTitle` 方法時，使用 `emit` 發射要變更的資料給父元件

複製

```
import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();

  @Output()
  changeTitle = new EventEmitter<any>();

  isEdit = false;
  newTitle = '';
  constructor() { }

  ngOnInit() {
    this.newTitle = this.item.title;
  }
  deleteArticle() {
    this.delete.emit(this.item);
  }
  editTitle(e) {
    console.log('editTitle', e.target);
    this.newTitle = e.target.value;
    this.changeTitle.emit({ newTitle: this.newTitle, id: this.item.id });
  }
  editExit(e) {
    console.log('editExit', e.target);
    e.target.value = this.item.title;
    this.isEdit = false;
  }
}
```

> 接下來就是到父元件上設定接收並做出實際的改變啦～

- 事件繫結 `changeTitle` 並且當這個事件被觸發時執行 `doChange()` 方法，使用 `$event` 參數接收子元件送來的資料

**ArticleList Template**

複製

```
<!-- Article START-->
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <app-article-header [item]="item" (delete)="doDelete($event)" (changeTitle)="doChange($event)"></app-article-header>
  <app-article-body [item]="item"></app-article-body>
</article>
<!-- Article END-->
```



> 到了最後這個步驟了，為了讓底下的所有子元件都知道資料物件發生改變，所以 `atticleData` 屬性指向的陣列要重新建立，而陣列裡面的物件如果裡面的屬性有發生修改，也要重新建立。

**ArticleList class**

複製

```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html',
  styleUrls: ['./article-list.component.scss']
})
export class ArticleListComponent implements OnInit {
  atticleData: Array<any>;
  constructor() { }
  ngOnInit() {
    /* tslint:disable */
    this.atticleData = [
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
      ...以下省略
    ];
  }
  doDelete(item){
    this.atticleData = this.atticleData.filter(v => v !== item);
  }
  doChange($event: any){
    this.atticleData = this.atticleData.map((item)=>{
      if($event.id === item.id) {
        // 不要這樣寫 item.title = $event.title;
        // 當屬性被改動時，要建立新的物件
        return Object.assign({}, item, $event);
      }
      return item;
    });
  }
}
```



- 為了讓陣列重新建立，使用 ES6 的陣列方法 map ，它會回傳一個新的陣列

- 值得注意的是，當進入 if 判斷時，不可以直接寫

   

  ```
  item.title = $event.title
  ```

   

  這樣就落入之前說的陷阱了

  - 正確應該使用

     

    ```
    Object.assign
    ```

     

    方法，回傳一個新的物件並且合併

     

    ```
    item
    ```

     

    以及

     

    ```
    $event
    ```

    - [MDN - Object.assign()](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

> 根據 MDN 的解釋，使用 `Object.assign` 方法時，如果在目標物件裡的屬性名稱 (key) 和來源物件的屬性名稱相同，將會被覆寫。若來源物件之間又有相同的屬性名稱，則後者會將前者覆寫。

**都完成了，來測試看看吧！**

[![編輯中](https://i.imgur.com/0MpYqhW.png)](https://i.imgur.com/0MpYqhW.png)

[編輯中](https://i.imgur.com/0MpYqhW.png)



[![無法順利變更標題](https://i.imgur.com/01hAhDu.png)](https://i.imgur.com/01hAhDu.png)

[無法順利變更標題](https://i.imgur.com/01hAhDu.png)



糟糕程式好像出了點問題，加上幾行 `console.log` 觀察看看吧。

[![img](https://i.imgur.com/Za4CO0u.png)](https://i.imgur.com/Za4CO0u.png)

**原來問題是沒有正確合併，因位子元件傳送給父元件的資料物件內的屬性名稱要與標題的屬性名稱一致才會覆蓋，因此必須回去修改。**

複製

```
editTitle(e) {
  console.log('editTitle', e.target);
  this.newTitle = e.target.value;
  this.changeTitle.emit({ title: this.newTitle, id: this.item.id });
}
```

**重新測試！**

[![修改成功](https://i.imgur.com/kk6Afog.png)](https://i.imgur.com/kk6Afog.png)

## [從 0 開始的 Angular 生活]No.32 介紹 ngOnChanges 生命週期 Hook

 發表於 2019-06-01 | 更新於 2019-06-09 | 分類於 [前端學習](https://pvt5r486.github.io/categories/f2e/)

## 前言

之前曾經介紹到 Angular 元件生命週期的 Hook分別是 ngOnInit 與 ngOnDestroy ，在那篇文章內曾經說過元件被實體化的過程，第一個先執行的是建構式 constructor ，也提到盡量不要再建構式裡面寫程式碼。這次要介紹的式另一個生命週期的 Hook - ngOnChanges 。

[![img](https://images.unsplash.com/photo-1557739820-f55c4bd03537?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)](https://images.unsplash.com/photo-1557739820-f55c4bd03537?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## ngOnChanges() 、 constructor() 、 ngOnInit()

在介紹之前，來一張元件生命週期的圖表：

[![img](https://i.imgur.com/eMUPWsS.png)](https://i.imgur.com/eMUPWsS.png)

ngOnChanges() 與 constructor() 、 ngOnInit() 之間的執行順序是如何，可以很容易地從這張圖表上看出來。

但秉持著實踐精神，我們還是實際寫一些程式測試看看～

複製

```
import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-article-body',
  templateUrl: './article-body.component.html',
  styleUrls: ['./article-body.component.scss']
})
export class ArticleBodyComponent implements OnInit, OnChanges {
  @Input()
  item;
  constructor() {
    console.log('ArticleBodyComponent: constructor');
  }

  ngOnInit() {
    console.log('ArticleBodyComponent: ngOnInit');
  }

  ngOnChanges() {
    console.log('ArticleBodyComponent: ngOnChanges');
  }
}
```

因為有跑 ngFor 而文章資料總共有 6 筆，因此產生 6 個 ArticleBody 元件。

[![img](https://i.imgur.com/C0ZVl6K.png)](https://i.imgur.com/C0ZVl6K.png)

- 可以從這裡觀察出無論如何一定會先執行 constructor() ，但執行過程中元件還沒被初始化。
  - 此時元件內什麼東西都沒有，也沒有透過屬性繫結傳進來的資料。
- 緊接著執行 ngOnChanges() 然後才是 ngOnInit()

這就是它們的執行順序。

## 什麼是 ngOnChanges()

ngOnChanges() 觸發的時機點

- 元件裡面的屬性如果有套用 @input() ，只要該元件的父元件透過屬性繫結傳資料進來的話， ngOnChanges() 就會被觸發

### 驗證 ngOnChanges() 觸發的時機點

- 在 ArticleBody 元件內新增一個屬性

   

  ```
  counter
  ```

  - `counter` 值會從父元件透過屬性繫結傳入
  - 當 `counter` 發生改變時 ngOnChanges() 就會觸發，由此驗證

**ArticleBody**

複製

```
export class ArticleBodyComponent implements OnInit, OnChanges {
  @Input()
  item;

  @Input()
  counter;

  constructor() {
    console.log('ArticleBodyComponent: constructor');
  }

  ngOnInit() {
    console.log(`ArticleBodyComponent ${this.item.id} : ngOnInit`);
  }

  ngOnChanges() {
    console.log(`ArticleBodyComponent ${this.item.id} : ngOnChanges`);
  }
}
```



複製

```
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <app-article-header [item]="item" (delete)="doDelete($event)" (changeTitle)="doChange($event)"></app-article-header>
  <app-article-body [item]="item" [counter]="counter"></app-article-body>
</article>
```

**ArticleList**

複製

```
export class ArticleListComponent implements OnInit {
  atticleData: Array<any>;
  counter = 0;
  constructor() { }
  ngOnInit() {
    setTimeout(() => {
      this.counter++;
    }, 2000);
  }
}
```



為了方便所以補上 `item.id` ，接著運行開發伺服器，觀察 `console.log` 變化：

[![重新整理](https://i.imgur.com/b6UurMk.png)](https://i.imgur.com/b6UurMk.png)

[重新整理](https://i.imgur.com/b6UurMk.png)



[![兩秒後](https://i.imgur.com/80PGWhX.png)](https://i.imgur.com/80PGWhX.png)

[兩秒後](https://i.imgur.com/80PGWhX.png)



**由此可知，在兩秒後六個不同的 ArticleBody 元件都觸發了 ngOnChanges()** ，證明了只有在屬性繫結傳入資料發生改變時才會觸發 ngOnChanges() 。

### ngOnChanges() 參數的作用

另外 ngOnChanges() 可以傳入一個參數，比較傳入前與傳入後的資料：

複製

```
ngOnChanges(changes) {
  console.log(`ArticleBodyComponent ${this.item.id} : ngOnChanges`);
  console.log(changes);
}
```



[![img](https://i.imgur.com/KAvpajv.png)](https://i.imgur.com/KAvpajv.png)

發現這個 `changes` 接收到一個叫物件，點開後會發現裡面還有一層以 `counter` 屬性命名的物件：

- 該物件的型別為 SimpleChange

- 代表當前值為多少的屬性 `currentValue`

- 代表前一個值為多少的屬性 `previousValue`

- ```
  firstChange
  ```

   

  是不是第一次發生改變

  - 目前已經是第二次改變了，所以是 `false`
  - 第一次改變發生於重新整理時那一次的 ngOnChanges()

> 透過這個例子得知可以利用這個參數在觸發 ngOnChanges() 時多做一些額外的判斷。

## ngOnChanges() 實務應用

前面幾篇文章提到，建議不要在子元件上直接使用雙向繫結修改傳入的資料，因為這樣會直接的修改到原始資料。

但現在我們懂得使用 ngOnChanges() 這個 Hook ，因此可以針對這個部分對整個程式碼進行重構。

### ActicleHeader

切回 ActicleHeader 元件觀察：

- 目前有一個

   

  ```
  @input()
  ```

   

  綁定了

   

  ```
  item
  ```

   

  屬性

  - 所以當接到 `item` 資料時 ngOnChanges() 會被觸發

- 透過

   

  ```
  ngOnChanges(changes)
  ```

   

  ，當接收到值時建立一份與原始資料不同的新物件

  - 如此一來就可以放心地使用雙向繫結，也不怕修改到原始資料

複製

```
import { Component, OnInit, Input, Output, EventEmitter, OnChanges} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit, OnChanges {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();

  @Output()
  changeTitle = new EventEmitter<any>();

  isEdit = false;
  newTitle = '';
  constructor() { }

  ngOnInit() {
    this.newTitle = this.item.title;
  }
  ngOnChanges(changes) {
    if (changes.item) {
      this.item = Object.assign({}, changes.item.currenValue);
    }
  }

  deleteArticle() {
    this.delete.emit(this.item);
  }
  editTitle(e) {
    console.log('editTitle', e.target);
    this.newTitle = e.target.value;
    this.changeTitle.emit({ title: this.newTitle, id: this.item.id });
  }
  editExit(e) {
    console.log('editExit', e.target);
    e.target.value = this.item.title;
    this.isEdit = false;
  }
}
```

接著修改 Template

- 在 Input 內補上雙向繫結
  - 因為改為使用雙向繫結 `editTitle()` 與 `editExit()` 不再需要傳入 `$event` 參數
- 調整取消編輯上的點擊事件，當點擊時觸發 `editExit()`

複製

```
<header class="post-header">
  <h2 class="post-title" >
    <a *ngIf="!isEdit" [href]="item.href">{{ item.title }}</a>
    <input *ngIf="isEdit" type="text" size="70" [(ngModel)]="item.title"
      (keyup.enter)="editTitle()" (keyup.escape)="editExit()">
  </h2>
  <div class="post-info clearfix">
    <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
    <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
        href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
    <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
        [href]="item['category-link']">{{item.category}}</a></span>
  </div>
  <span>
    <button (click)="deleteArticle()">刪除</button>
    <button *ngIf="!isEdit" (click)="isEdit=true">編輯標題</button>
    <button *ngIf="isEdit" (click)="isEdit=false">取消編輯</button>
  </span>
</header>
```

因為調整了 Template ，所以 class 內的方法也需要跟著調整。

邏輯部分

- 新增了一個屬性

   

  ```
  originData
  ```

   

  用途是保存原始傳入的資料，用於取消編輯時使用

  - 並於 ngOnChanges() 觸發時將原始資料賦值給

     

    ```
    originData
    ```

    - 特別注意這裡不可以寫 `this.originData = this.item;` 因為此時還沒有 `item`

- 刪除不再需要的屬性 `newTitle`

- 調整 `editTitle()` ，此時發射的 `this.item` 已經不是原始資料了

- 調整 `editExit()` ，實作不可變物件特性，使用原始資料重新建立新物件還原

複製

```
import { Component, OnInit, Input, Output, EventEmitter, OnChanges} from '@angular/core';

@Component({
  selector: 'app-article-header',
  templateUrl: './article-header.component.html',
  styleUrls: ['./article-header.component.scss']
})
export class ArticleHeaderComponent implements OnInit, OnChanges {
  @Input()
  item;

  @Output()
  delete = new EventEmitter<any>();

  @Output()
  changeTitle = new EventEmitter<any>();
  originData;
  isEdit = false;
  constructor() { }

  ngOnInit() {
  }
  ngOnChanges(changes) {
    if (changes.item) {
      this.originData = changes.item.currentValue;
      this.item = Object.assign({}, changes.item.currentValue);
    }
  }

  deleteArticle() {
    this.delete.emit(this.item);
  }
  editTitle() {
    this.changeTitle.emit(this.item);
  }
  editExit() {
    this.item = Object.assign({}, this.originData);
    this.isEdit = false;
  }
}
```

**現在 ArticleHeader 這個元件邏輯已經完成，可以測試一下。**

[![編輯成功](https://i.imgur.com/w0oJckd.png)](https://i.imgur.com/w0oJckd.png)

[編輯成功](https://i.imgur.com/w0oJckd.png)



[![編輯中](https://i.imgur.com/PoQ8LqM.png)](https://i.imgur.com/PoQ8LqM.png)

[編輯中](https://i.imgur.com/PoQ8LqM.png)



[![取消編輯](https://i.imgur.com/h1gvitC.png)](https://i.imgur.com/h1gvitC.png)

[取消編輯](https://i.imgur.com/h1gvitC.png)



- 倘若這個步驟沒辦法完成，可能是雙向繫結出了問題
  - 應檢查是否有在 Article 功能模組內匯入 `FormsModule` ，需匯入才可在 input 上使用雙向繫結

> 至此程式的運作都如預期，唯獨刪除功能出狀況了，所以我們到 ArticleList 父元件調整一下程式碼。

### ArticleList

- 造成刪除失敗的原因是，現在的 item 物件已經不是原本的 item 物件了
  - 而任意兩個物件在 JavaScript 中相比都是 False ，因此刪除導致失敗
  - 修正方法為改採 `item.id` 比較即可

因此程式碼修改如下:

複製

```
doDelete(item){
  this.atticleData = this.atticleData.filter(v => v.id !== item.id);
}
```

測試看看是否如我們預期。

[![img](https://i.imgur.com/qeWNmVM.png)](https://i.imgur.com/qeWNmVM.png)

## 小結

透過 ngOnChanges() 的特性在屬性繫結的階段時，讓 `item` 屬性變成是一個「不可變的物件」，因為只是有任何新的資料進來，馬上就會重新產生新的物件，並且賦值給 `item` ，藉由這種方式讓 `item` 值與原本傳進子物件的 `item` 值得以脫鉤。

脫鉤後就可以在 Template 內放心地使用雙向繫結而不會影響到父物件內的原始資料，這麼做也確保了修改 `item` 屬性時不會一併的修改到其他元件內 `item` 屬性的內容。

