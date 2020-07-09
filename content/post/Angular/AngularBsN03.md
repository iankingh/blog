---
title: "AngularBsN03"
date: 2020-07-06T05:09:18+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# 從 0 開始的 Angular 生活 第3天-理解 Angular 應用程式與元件
<!--more-->

一個完整的 Angular 應用程式，它會包含一個模組，通常稱它為 AppModule ，而一個模組下會包含非常多的元件，如以下這張圖：





一個模組下可能會有:

- App Componet 根元件
- Child Componet 子元件
- Services Componet 服務元件
- Pipe Componet 管道元件

元件的類型可能會有很多種，我們會透過一個模組把這些元件封裝起來。

> 因為一個完整的 Angular 應用程式至少會包含一個模組，也至少會有一個元件以上，因此我們可以說一個 Angular 應用程式就是由元件所組成的

## Angular 頁面的組成

而 Angular 的開發模式，全部都是元件化的開發模式跟以往我們使用 JQuery 的開發模式是不一樣的，我們不需要頻繁的操作 DOM 。在元件化的開發方式裡，我們鮮少會直接操作 DOM 元素，都是透過元件的切換來達成畫面的渲染。

**可以想像成一個網頁載入後， HTML 內的 body 都是空白的，只有 JavaScript 。**

所以頁面要如何渲染到瀏覽器上呢？

- JavaScript 呼叫 元件
- 元件 再呼叫 樣板
- 樣板呈現到畫面上

**而這個過程是動態的透過 JavaScript 達成。**

我們可以再次想像一個 Angular 頁面：

- 最外層是由一個 AppComponent 元件(或稱為根元件)包覆
- 最上方頁首的部分可以拆成 HeaderConponent 為獨立元件
- 左邊則是拆成子選單的部分 AsideCompoent
- 右邊則是網站主要內容 ArticleCompoent

[![img](https://i.imgur.com/KU2LunY.png)](https://i.imgur.com/KU2LunY.png)

> 如圖，AppComponent 包覆著 HeaderConponent 、 AsideCompoent 、 ArticleCompoent 這些元件，也就是說 AppComponent 就是父元件，而被包覆在裡面的就稱為子元件，最後組合成一個完整的網頁。

然而實際上的網頁開發可能元件架構上沒有這麼單純，一個元件內可能又包覆一個子元件，而這個子元件可能又有另一個子元件，這種狀況是蠻常見的。像這樣一層包著一層的開發方式，就是所謂的元件化的開發方式。

