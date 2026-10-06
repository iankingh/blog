---
title: "Angular 與 IE11：歷史相容維護及遷移"
date: 2021-03-10T13:21:43+08:00
aliases:
 - "/post/angular/angualronie11/"
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "標示 IE11 支援終止的版本界線，移除過時 beta shim 的直接套用建議。"
lastmod: 2026-10-07T00:01:00+08:00
---

標示 IE11 支援終止的版本界線，移除過時 beta shim 的直接套用建議。

<!--more-->

適用：Angular12及更早版本的IE11歷史維護情境；本次沒有IE11實機，僅檔案查核。

## 歷史版本定位

Angular13開始移除IE11支援。本篇原本記錄舊Angular的IE11相容工作，不適用Angular20／現行CLI。IE11本身已結束大部分桌面支援；企業Edge IE mode是不同管理與生命週期情境，不會讓新版Angular重新支援IE。

## 若仍需重現舊系統

在隔離的歷史測試環境保留原package.json、lockfile、Node與Angular major。核對該major的browser support、tsconfig target、polyfills入口和browserslist，依官方當時檔案加入必要polyfill。`X-UA-Compatible`只能影響舊瀏覽器檔案模式，不會補足Promise、Proxy或現代語法。

原筆記的Angular2 beta shim、手改Function.prototype與URL polyfill不應作通用方案；測試用shim不等於production polyfill。程式庫需要額外polyfill也要查該版本檔案，不能看到弱掃失敗便刪功能使其表面通過。

## 驗證範圍

測登入、表單、HTTP、下載、路由、中文輸入與CSS佈局；記錄IE版本／檔案模式、JS錯誤與實際失敗操作。現代Chrome測試通過不代表IE可用，語法降版也不代表DOM/Web API都可用。

## 替代路線

先確認是否真的有IE使用者與硬性系統依賴，再規劃受支援瀏覽器入口、舊系統隔離與替換時間。Angular按官方update guide逐major升級並測試，每個依賴都有自己的相容界線。若必須長期留IE，明確標記風險與維護限制，不能當作新專案預設。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Angular browser support](https://angular.dev/reference/versions#browser-support)
- [Angular13發布說明](https://github.com/angular/angular/blob/13.0.0/CHANGELOG.md)
- [Microsoft IE lifecycle](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)

### 原始筆記保留的來源

- [https://npmcdn.com/angular2@2.0.0-beta.21/es6/dev/src/testing/shims_for_IE.js](https://npmcdn.com/angular2@2.0.0-beta.21/es6/dev/src/testing/shims_for_IE.js)
- [IE 11 Syntax error after doing ng serve · Issue #9508 · angular/angular-cli (github.com)](https://github.com/angular/angular-cli/issues/9508)
