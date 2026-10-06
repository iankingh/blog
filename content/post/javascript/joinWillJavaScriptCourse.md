---
title: "JavaScript 核心複習：型別、作用域與物件傳遞"
date: 2021-03-22T11:58:06+08:00
draft: false
categories:
 - "學習"
tags:
 - "javaScript"
toc: true
description: "保留課程主題，修正傳值、原始型別與全域性變數的誤解，補上可執行觀察。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留課程主題，修正傳值、原始型別與全域性變數的誤解，補上可執行觀察。

<!--more-->

適用：現代ECMAScript與Node／瀏覽器；原課程主題保留，新增內容為官方文件與自製範例的複習。

## 閱讀定位

這是原課程大綱的自行整理與補充，不是逐字課程內容或個人實戰成果。主題包括變數、型別轉換、閉包、函式與prototype。JavaScript是動態型別，值仍有型別；不能說「只有記憶體位址，沒有傳值」。

## Node／Console 練習

```javascript
const original = { score: 1 };
function update(value) {
  value.score = 2;
  value = { score: 99 };
}
update(original);
console.log(original.score);
const primitive = 1;
function change(value) { value = 2; }
change(primitive);
console.log(primitive);
console.log(typeof null, typeof 1n);
function makeCounter() {
  let count = 0;
  return () => ++count;
}
const next = makeCounter();
console.log(next(), next());
```

```text
2
1
object bigint
1 2
```

引數按值傳遞；物件值具有引用語意，修改同一物件可被外部觀察，重新賦值引數不會讓original指向新物件。原始型別有undefined、null、boolean、number、bigint、string、symbol，BigInt補齊原清單。

## var、let、const與原型

let/const為區塊作用域，const禁止重新賦值但不禁止物件屬性更新。var的全域性行為還取決於classic script或ES module；module頂層不自動變window屬性，嚴格模式禁止未宣告賦值。delete操作物件屬性，不當變數釋放記憶體的工具。

閉包儲存可訪問的詞法環境，計數器每次呼叫共享該次makeCounter的count。class仍建立在原型模型上，call/apply指定this，箭頭函式的this來自外層，不可用call任意改。`===`避免部分隱式轉換，但NaN、-0等比較還需按需求理解Object.is。

## 查核範圍

Node實際執行，輸出與本文一致。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [型別與結構](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
- [閉包](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
- [函式參數](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

### 原始筆記的其他連結

- [原始參考入口 1](https://hsiangfeng.github.io/javascript/20200719/2719441918/)
- [原始參考入口 2](https://medium.com/pvt5r486/%E5%88%9D%E6%AC%A1%E5%8F%83%E5%8A%A0%E4%BF%9D%E5%93%A5%E7%9A%84-javascript-%E9%96%8B%E7%99%BC%E5%AF%A6%E6%88%B0-%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5%E7%AF%87-%E6%84%9F%E6%83%B3-1df18a6c0b9)
