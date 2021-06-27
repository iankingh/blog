---
title: "Angular Forms"
date: 2021-06-24T14:00:58+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

## Angular Forms 
<!-- 簡介 -->

Angular 中有2種表單 :

Template-Driven Forms - 模板驅動表單

Model-Driven Forms (基本上都說是 Reactive Forms)- 響應式的表單


<!--more-->

### Template-Driven Forms 與 Model-Driven Forms的介紹

#### Template-Driven Forms

Template-driven forms是將組件驗證控制的功能寫在像是
的標籤內，並利用ngModel來確認是否輸入了合法的內容。
使用表單驅動驗證不需要自己創建control objects，因為angular已經為我們建好了。
ngModel會處理使用者改變與輸入表單的事件，並更新ngModel裡面的可變數據，讓我們可以去處理後續的事。
也因此ngModel並不是ReactiveFormsModule的一部份。
這代表著使用表單驅動驗證，我們需要撰寫的程式碼更少。
但是如果我們的表單需要很複雜的驗證步驟並且要顯示很多不同的錯誤訊息時，使用表單驅動驗證會使事情變得更複雜並難以維護。

#### Model-Driven Forms Reactive forms

Reactive forms的驗證大多是直接寫在controller裡的，會是一個明確的、非UI的data flowing。
Reactive forms的reactive patterns可以讓測試與驗證更加簡單。
使用Reactive forms可以用一個樹狀的控制物件來binding到表單template的元件上，這讓所有驗證的程式碼都集中在一起，方便維護與管理，在撰寫單元測試時也會較為容易。
使用Model-Driven Forms也較符合reactive programming的概念（延伸閱讀：Functional Reactive Programming 的入門心得）

#### 最大的差異，同步與非同步

Reactive forms是同步的而Template-driven forms為非同步處理，是這兩者間最大的差異。
對Reactive forms來說，所有表單的資料是在code裡以tree的方式來呈現，所以在任一個節點可以取得其他表單的資料，並且這些資料是即時同步被更新的。我們也可以在使用者修改了某個input的值時，去為使用者自動update另一個input內的預設值，這是因為所有資料都是隨時可取得的。
Template-driven forms在每一個表單元件各自透過directive委派檢查的功能，為了避免檢查後修改而造成檢查失效的問題，directive會在更多的時後去檢查輸入的值的正確性，因此並沒有辦法立即的得到回應，而需要一小段的時間才有辦法得到使用者輸入的值是否合法的回應。這會讓我們在撰寫單元測試時更加複雜，我們會需要利用setTimeout去讓取得的檢查結果是正確的

### Template-Driven Forms vs Model-Driven Form (Reactive Forms)

Template-Driven Forms (範本驅動表單) 的特點

採用宣告的方式建立表單 (較為簡單) (維護較為容易)

適合固定欄位數量的表單
會員註冊、登入、線上下單、修改會員資料、…

透過 ngModel 進行數據綁定

不易於單元測試


Model-Driven Form (Reactive Forms)- (響應式表單) 的特點

採用程式的方式建立表單 (較為繁瑣) (程式碼維護較為麻煩)

適合動態欄位數量的表單 (動態表單)
由後台定義的動態問卷系統、變動選項的投票系統、…

把部分邏輯抽離Template至component

易於單元測試


## 參考
