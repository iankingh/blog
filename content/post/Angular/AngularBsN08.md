---
title: "AngularBsN08"
date: 2020-07-22T17:30:53+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Pipes 管線元件 ( Pipes Component )
<!--more-->

## Pipes 管線元件



> Pipes 管線元件主要是讓我們在透過內嵌繫結或者是屬性繫結時可以透過 Pipes 的符號 `|` 將我們原本的輸出丟給另一個 Pipes 元件處理，再把新的結果輸出到畫面上。

Angular 內有幾個內建的 Pipes 元件

- DatePipe
- UperCase
- LowerCase
- Currency
- PercentPipe

這幾個 Pipes 元件預設就可以讓我們使用在任何的 Template 上，若這些內建的 Pipes 元件不符合需求，也可以自行撰寫 Pipes 元件哦。

## UperCase

顧名思義這個 UperCase 的 Pipes 元件，就是幫我們把原本輸出有英文的部分全部轉換成大寫。

這是還沒有套用 UperCase 前，標題的英文有大寫有小寫

[![img](https://i.imgur.com/BFEh906.png)](https://i.imgur.com/BFEh906.png)

因此我要把這個 Pipes 元件套用到目前的 Template 上。

**Template**

```html
<h2 class="post-title">
  <a [href]="item.href">{{ item.title|uppercase }}</a>
</h2>
```

## LowerCase

與 UperCase 相同，顧名思義就是有英文的部分全部轉換成小寫，使用方式也非常簡單:

**Template**

```html
<h2 class="post-title">
  <a [href]="item.href">{{ item.title|lowercase }}</a>
</h2>
```

[![img](https://i.imgur.com/o8F4nc6.png)](https://i.imgur.com/o8F4nc6.png)

## DecimalPipe



```html
{{ value_expression | number [ : digitsInfo [ : locale ] ] }}
```

- value 是輸入值
- number 是這個 Pipes 元件的名稱
- digitsInfo 為字串型態的參數，非必填項目
  - 格式如 `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`
  - minIntegerDigits：在小数点前的最小位数。默认为 1。
  - minFractionDigits：小数点后的最小位数。默认为 0。
  - maxFractionDigits：小数点后的最大为数，默认为 3。
- locale 為字串型態的參數，非必填項目
  - 用來設定這一串數字要用哪一個地區的數值格式呈現

因此可以按照官方提供的範例，複製一份並且在 Template 內隨意找個地方貼上玩看看：

**Template**

```html
<div>
  <!--output '2.718'-->
  <p>e (no formatting): {{e | number}}</p>

  <!--output '002.71828'-->
  <p>e (3.1-5): {{e | number:'3.1-5'}}</p>

  <!--output '0,002.71828'-->
  <p>e (4.5-5): {{e | number:'4.5-5'}}</p>

  <!--output '0 002,71828'-->
  <p>e (french): {{e | number:'4.5-5':'fr'}}</p>

  <!--output '3.14'-->
  <p>pi (no formatting): {{pi | number}}</p>

  <!--output '003.14'-->
  <p>pi (3.1-5): {{pi | number:'3.1-5'}}</p>

  <!--output '003.14000'-->
  <p>pi (3.5-5): {{pi | number:'3.5-5'}}</p>

  <!--output '-3' / unlike '-2' by Math.round()-->
  <p>-2.5 (1.0-0): {{-2.5 | number:'1.0-0'}}</p>
</div>
```

Template 有用到 `e` 以及 `pi` 這兩個內嵌繫結，因此必須在 class 內補上這兩個屬性。

```
export class AppComponent {
  inputValue = '';
  pi: number = 3.14;
  e: number = 2.718281828459045;
}
```

> 運行開發伺服器，看看效果如何～

[![img](https://i.imgur.com/zqZBBLG.png)](https://i.imgur.com/zqZBBLG.png)

- 第一個結果 e 輸出是 2.718 ，對照後也就是說預設的情況下 DecimalPipe 會輸出小數點後三位的數字，其餘全部捨去。
  - 而這個結果是因為沒有填寫任何參數，是參數的默認值導致
- 第二個結果傳入一個參數 `3.1-5` ，對照上面的格式與參數解釋後，得到結果 e 為 002.71828

> 可透過修改第一個參數達成想要的數字格式。

- 第四個結果，傳入的第二個參數為 fr ，代表採用法國的數值格式
  - 在法國，小數點是當作千分號使用，而千分號則是使用空白替代
  - 透過不同的國家的 locale id 就可以轉換成對應的地區數值格式
    - 台灣為 zh-TW
    - 日本為 jp

**不僅僅第一個參數可以利用，配合第二個參數一起使用才是王道。**

> 而這個 Pipes 元件好玩的地方是，它的名稱叫做 DecimalPipe ，但實際使用卻是輸入 number ，這是容易搞混的地方要特別注意。

## CurrencyPipe

這是個貨幣格式的 Pipe 元件，官網文件如下：

- [CurrencyPipe](https://angular.cn/api/common/CurrencyPipe)

用法跟先前介紹的 DecimalPipe 蠻類似的，使用方式如下：

使用方式如：

複製

```
{{ value_expression | currency [ : currencyCode [ : display [ : digitsInfo [ : locale ] ] ] ] }}
```



- value 是輸入值
- currency 是這個 Pipes 元件的名稱
- currencyCode 是貨幣代碼，比如 USD 表示美元，這部分是選填的，且格式須遵守 [ISO4217](https://en.wikipedia.org/wiki/ISO_4217)
- display 是貨幣的符號，同樣是可選的，預設是顯示貨幣的符號。
- digitsInfo 為字串型態的參數，非必填項目
  - 格式如 `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`
  - minIntegerDigits：在小数点前的最小位数。默认为 1。
  - minFractionDigits：小数点后的最小位数。默认为 0。
  - maxFractionDigits：小数点后的最大为数，默认为 3。
- locale 為字串型態的參數，非必填項目
  - 用來設定這一串數字要用哪一個地區的數值格式呈現

**直接參考官網範例：**

複製

```
@Component({
  selector: 'currency-pipe',
  template: `<div>
    <!--output '$0.26'-->
    <p>A: {{a | currency}}</p>

    <!--output 'CA$0.26'-->
    <p>A: {{a | currency:'CAD'}}</p>

    <!--output 'CAD0.26'-->
    <p>A: {{a | currency:'CAD':'code'}}</p>

    <!--output 'CA$0,001.35'-->
    <p>B: {{b | currency:'CAD':'symbol':'4.2-2'}}</p>

    <!--output '$0,001.35'-->
    <p>B: {{b | currency:'CAD':'symbol-narrow':'4.2-2'}}</p>

    <!--output '0 001,35 CA$'-->
    <p>B: {{b | currency:'CAD':'symbol':'4.2-2':'fr'}}</p>

    <!--output 'CLP1' because CLP has no cents-->
    <p>B: {{b | currency:'CLP'}}</p>
  </div>`
})
export class CurrencyPipeComponent {
  a: number = 0.259;
  b: number = 1.3495;
}
```



> 這部分因為跟 DecimalPipe 很類似，所以就不一個個解釋了。

## PercentPipe

這是一個百分比的 Pipe 元件，官網文件如下：

- [PercentPipe](https://angular.cn/api/common/PercentPipe)

使用方式如：

複製

```
{{ value_expression | percent [ : digitsInfo [ : locale ] ] }}
```



- value 是輸入值
- percent 是這個 Pipes 元件的名稱
- digitsInfo 為字串型態的參數，非必填項目
  - 格式如 `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`
  - minIntegerDigits：在小数点前的最小位数。默认为 1。
  - minFractionDigits：小数点后的最小位数。默认为 0。
  - maxFractionDigits：小数点后的最大为数，默认为 3。
- locale 為字串型態的參數，非必填項目
  - 用來設定這一串數字要用哪一個地區的數值格式呈現

**直接參考官網範例：**

複製

```
@Component({
  selector: 'percent-pipe',
  template: `<div>
    <!--output '26%'-->
    <p>A: {{a | percent}}</p>
 
    <!--output '0,134.950%'-->
    <p>B: {{b | percent:'4.3-5'}}</p>
 
    <!--output '0 134,950 %'-->
    <p>B: {{b | percent:'4.3-5':'fr'}}</p>
  </div>`
})
export class PercentPipeComponent {
  a: number = 0.259;
  b: number = 1.3495;
}
```



**從這邊可以發現， DecimalPipe 、 CurrencyPipe 、 PercentPipe 使用方式感覺上其實都差不多**

## DatePipe

這是一個關於日期的 Pipe 元件，關於這個元件的官網說明如下:

- [DatePipe](https://angular.cn/api/common/DatePipe)

使用方式如：

複製

```
{{ value_expression | date [ : format [ : timezone [ : locale ] ] ] }}
```



- value 是輸入值，可以是 Date 物件、數字（从 UTC 时代以来的毫秒数）或 [ISO 字符串](https://www.w3.org/TR/NOTE-datetime)
- date 是這個 Pipes 元件的名稱
- format 為字串型態的參數，為非必填項目
  - 要包含的日期、時間部分的格式，或者是使用預先定義好的格式
  - 預設值是 ‘mediumDate’.
- timezone 為字串型態的參數，為非必填項目
  - 可以加上一個時區偏移（比如 ‘+0430’）或使用標準的 UTC/GMT
  - 預設為本地系統時區
- locale 為字串型態的參數，非必填項目
  - 用來設定日期要用哪一個地區的日期格式呈現

> 接著利用 DatePipe 來修改部落格文章上的日期格式吧

**Template**

複製

```
<span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
```



[![修改前](https://i.imgur.com/uLsDMpj.png)](https://i.imgur.com/uLsDMpj.png)

[修改前](https://i.imgur.com/uLsDMpj.png)



[![修改後](https://i.imgur.com/cBZmn1L.png)](https://i.imgur.com/cBZmn1L.png)

[修改後](https://i.imgur.com/cBZmn1L.png)



這樣子的用法是直接轉換成我們希望的格式，但其實 format 參數內有一些已經預先定義好的格式可以使用，例如：

**Template**

複製

```
<span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'shortDate'}}</span>
```



[![shortDate](https://i.imgur.com/dyLOgal.png)](https://i.imgur.com/dyLOgal.png)

[shortDate](https://i.imgur.com/dyLOgal.png)



## JsonPipe

JsonPipe 可以把任意值全部轉換成 Json 的格式，所以這些值可以是字串、數字、物件。

而官網的文件如下：

- [JsonPipe](https://angular.cn/api/common/JsonPipe)

> JsonPipe 的功能主要是拿來偵錯，像是輸出之前在練習 ngFor 時的用到的資料。

**Template**

複製

```
<!-- Article START-->
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData; let idx = index">
  <header class="post-header">
    <h2 class="post-title">
      <a [href]="item.href">{{ item.title|lowercase }}</a>
    </h2>
    <div class="post-info clearfix">
      <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
      <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
          href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
      <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
          [href]="item['category-link']">{{item.category}}</a></span>
    </div>
  </header>
  <section class="post-body text" [innerHTML]="item.summary">
  </section>
  <pre>{{item}}</pre>
</article>
<!-- Article END-->
```



如果直接把 `item` 進行內嵌繫結輸出的話，只會得到奇怪的結果

[![img](https://i.imgur.com/AAMZcs2.png)](https://i.imgur.com/AAMZcs2.png)

> 如果想要得到 `item` 物件序列化之後的 Json 資料，則可以使用 JsonPipe 來達成。

**Template**

複製

```
<pre>{{item|json}}</pre>
```



[![img](https://i.imgur.com/qIAN6xH.png)](https://i.imgur.com/qIAN6xH.png)

## SlicePipe

Slice 這個單字有切割的意思，所以這個 SlicePipe 可以幫助我們把某個物件、集合切割出其中的某一塊資料出來。

而官網的文件如下：

- [SlicePipe](https://angular.cn/api/common/SlicePipe)

使用方式如：

複製

```
{{ value_expression | slice : start [ : end ] }}
```



- value 是輸入值，可以是陣列或字串
- slice 是這個 Pipes 元件的名稱
- start 必填參數，表示要返回的子集的初始索引，數值型別
  - 正整數的情況：從列表或字符串表達式中返回從 start 索引處及之後的所有項目
  - 負整數的情況：從列表或字符串表達式中返回從结尾开始的第 start 索引處及之後的所有項目
  - 如果是正整數而且大於表達式的項目數：返回空列表或空字符串
  - 如果是正整數而且大於表達式的項目數：返回整個列表或字符串
- end 非必填參數，表示所要返回的子集的结尾索引，數值型別
  - 省略：返回结尾之前的全部項目
  - 正整數的情況：從列表或字符串中返回 end 索引之前的所有項目
  - 負整數的情況：從列表或字符串末尾返回 end 索引之前的所有項目

> 看完這些敘述似乎有點混亂，可以先試著把 SlicePipe 用在部落格的標題看看情況。

**順帶一提， Pipe 與 Pipe 之間是可以串接的。**

**Template**

複製

```
<h2 class="post-title">
  <a [href]="item.href">{{ item.title|lowercase|slice:0:20 }}</a>
</h2>
```



**這麼寫的意思代表，我希望標題的英文可以是小寫，且字數可以從 0 取到第 20 的位置**

觀察一下情況

[![img](https://i.imgur.com/7px4gGO.png)](https://i.imgur.com/7px4gGO.png)

> 可以看到標題顯示到 visual st 就結束了，因為前面加起來剛好是 20 個字元。

如果想要取標題從後面數來第 20 個字元後的內容，也是辦的到的：
**Template**

複製

```
<h2 class="post-title">
  <a [href]="item.href">{{ item.title|lowercase|slice:-20 }}</a>
</h2>
```



[![img](https://i.imgur.com/SOU69Z1.png)](https://i.imgur.com/SOU69Z1.png)

> 可以看到標題顯示從 「o code 如何避免顯示惱人的偵錯訊息」，這邊數來剛好 20 個字元。

**以上是 SlicePipe 用在字串上的範例** ，而 SlicePipe 還可以用在陣列上。

舉例來說，之前在練習 ngFor 時傳入的資料總共有六筆，而傳入的資料型態是個陣列。

**這代表可以將 SlicePipe 用在這個地方，像是一頁只顯示二筆資料這樣。**

**Template**

複製

```
<article class="post" id="post{{idx}}" *ngFor="let item of atticleData|slice:0:2; let idx = index">
  <header class="post-header">
    <h2 class="post-title">
      <a [href]="item.href">{{ item.title|lowercase|slice:-20 }}</a>
    </h2>
    <div class="post-info clearfix">
      <span class="post-date"><i class="glyphicon glyphicon-calendar"></i>{{item.date|date:'yyyy-MM-dd HH:mm'}}</span>
      <span class="post-author"><i class="glyphicon glyphicon-user"></i><a
          href="http://blog.miniasp.com/author/will.aspx">{{item.author}}</a></span>
      <span class="post-category"><i class="glyphicon glyphicon-folder-close"></i><a
          [href]="item['category-link']">{{item.category}}</a></span>
    </div>
  </header>
  <section class="post-body text" [innerHTML]="item.summary">
  </section>
</article>
```



[![img](https://i.imgur.com/2N5rZar.png)](https://i.imgur.com/2N5rZar.png)

