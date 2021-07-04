---
title: "JoinWillJavaScriptCourse"
date: 2021-03-22T11:58:06+08:00
draft: true
categories:
 - "上課"
tags:
 - "javaScript"
toc: true
---


## 參加保哥的JavaScript 開發實戰：核心概念篇 課程筆記

<!-- 簡介 -->

紀錄一下的保哥 JavaScript 的課程筆記。

<!--more-->

本次保哥主要的課程大綱是以下

- JavaScript 核心部分

  - 物件、變數與型別詳解
  - 詳細介紹 JS 基礎型別
  - **資料型態**與**型別轉換**陷阱

- JavaScript 基礎物件概念

  - JavaScript 物件資料結構
  - 徹底了解函式物件與使用技巧
  - **根物件**的觀念 (**全域變數**與**區域變數**)
  - **閉包** (Closure) 與 **範圍鏈** (Scope chain) 的關係
  - 常見 JavaScript 設計模式

- JavaScript 物件導向基礎

  - 函式 (function) 與 建構式 (constructor)
  - 關於物件與繼承
  - prototype 與 constructor
  - apply & call

  

### JavaScript 核心部分

JavaScript 本身就是指標概念

在JavaScript 裡 只有傳記憶體位址 ,沒有傳值


### javaScript 語言特性

javaScript  物件宣告就會存在 記憶體裡


無法在開發時期宣告 , 只能在執行時期檢查型別

變數沒有型別的觀念

javascript 在宣告物件時都會創建一個記憶體位址來存放值

就算宣告 相同值(value) 也會創建新的記憶體位址存放

變數是刪不掉的



### 物件、變數

#### 變數

​	var 變數 = 物件

變數指向物件的記憶體位址，不包含物件的內容亦不會有型別

​	無法在開發時期宣告型別 

​	只能在執行時期檢查型別

#### 物件

​	物件 : 在記憶體中的資料 ，僅存在執行時期



物件下 只有屬性一種成分

屬性可以指向 另一個 物件(型別)

當一個屬性不是 合法的識別元

要用 [' ']



#### 變數與屬性

屬性宣告

windows.a = 1;
window['a'] = 2;



變數與屬性大部分的表現都相同，其中較為明顯的差異是：

屬性可透過 delete 刪除
變數不可透過 delete 刪除

關於變數與屬性
只有用 var / let / const 宣告的才能算變數
變數只存在於當前範圍下，而且不能刪除
變數指向物件的記憶體位址，不包含物件的內容亦不會有型別
屬性也是指向物件的記憶體位址，跟變數一樣。
使用 var 建立一個全域變數 a ，這時的變數 a 會被掛到 window 物件下成為屬性，並且無法被刪除。
例子驗證 - 變數和屬性之間的關係一
var a = 1;
window['a'] = 2;
delete window.a;
console.log(a);  // 2
例子驗證 - 變數和屬性之間的關係二
b = 2;
delete b;
console.log(b); // is not defined


### 型別詳解

 所有物件都是物件型別 (Object Type)，除了以下 6 個 原始型別 ( Primitive Type)：
- number (數值)
- string (字串)
- boolean (布林)
- null (空值)
- undefined (未定義)
- symbol (符號) ES6+


### 理解 var, let, const 的觀念差異



const 表示變數不能變 : 記憶體位址不能變



變數宣告 範圍一樣 會打架  



let 的有效範圍 是 

{

}


### 詳細介紹 JS 原始型別與物件型別

原始型別 無法自由擴增屬性

也無法擁有屬性





### 資料型別轉換陷阱與技巧

任何 2個物件相比都是   false ;






## 參考

https://hsiangfeng.github.io/javascript/20200719/2719441918/

https://medium.com/pvt5r486/%E5%88%9D%E6%AC%A1%E5%8F%83%E5%8A%A0%E4%BF%9D%E5%93%A5%E7%9A%84-javascript-%E9%96%8B%E7%99%BC%E5%AF%A6%E6%88%B0-%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5%E7%AF%87-%E6%84%9F%E6%83%B3-1df18a6c0b9
