---
title: "Angular NullInjectorError：定位缺少的 provider"
date: 2020-10-27T21:28:57+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "補上錯誤鏈閱讀、服務註冊及 HttpClient 的新舊配置差異。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上錯誤鏈閱讀、服務註冊及 HttpClient 的新舊配置差異。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

## 讀出缺少的依賴

`NullInjectorError: No provider for X`表示目前injector找不到X的provider，不是單純忘記import檔案。閱讀錯誤中的依賴鏈，找最末端缺少的token；不要把整串所有服務都塞進providers。

一般應用服務可使用：

```typescript
import { Injectable } from '@angular/core';
@Injectable({ providedIn: 'root' })
export class GreetingService {
  hello(): string { return '你好，冒險者'; }
}
```

元件以constructor注入或inject(GreetingService)。放root會共享一份；放component.providers每個元件子樹可有不同例項，改動範圍會改變狀態共享。

## HttpClient 常見情境

Angular20的app.config.ts：

```typescript
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
export const appConfig: ApplicationConfig = { providers: [provideHttpClient()] };
```

NgModule舊專案使用對應版本的HttpClientModule。把HttpClient匯入TypeScript不會自動註冊provider。測試需提供測試HTTP provider，不能只因正式入口已設定就假設TestBed也有。

## 原 Angular 4 的 CustomPipe 情境

原筆記遇到的是注入 `CustomPipe`。`declarations`／`exports` 讓 NgModule 模板能使用 pipe，並不等於替 constructor 注入註冊 provider；standalone 的 `imports` 也有相同區別。如果只在模板轉換文字，使用 pipe 即可，不必注入。確實需要在方法內呼叫時，可提供相同類別：

```typescript
import { Component, Pipe, PipeTransform } from '@angular/core';
@Pipe({ name: 'trimText', standalone: true })
export class CustomPipe implements PipeTransform {
  transform(value: string): string { return value.trim(); }
}
@Component({
  selector: 'app-pipe-demo', standalone: true,
  imports: [CustomPipe], providers: [CustomPipe],
  template: `<p>{{ label | trimText }}</p>`
})
export class PipeDemoComponent {
  label = ' Ian ';
  constructor(private readonly pipe: CustomPipe) {}
  normalized(): string { return this.pipe.transform(this.label); }
}
```

Angular 4 的 NgModule 專案改在合適的元件或 module 設定 `providers: [CustomPipe]`；該版本不支援上例的 standalone 設定。若同一轉換被多處程式使用，抽成純函式或 service 通常更容易測試。

## 確認修正

執行原本出錯操作，確認服務方法回應與沒有注入錯誤，再測元件銷毀重建是否取得預期例項。若注入interface，TypeScript型別執行期不存在，改用InjectionToken並指定useValue／useFactory。迴圈依賴是不同問題，不要以重複provider掩蓋。

## 查核範圍

Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出）。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [依賴注入](https://angular.dev/guide/di)
- [HTTP 設定](https://angular.dev/guide/http/setup)
- [NG0201](https://angular.dev/errors/NG0201)

### 原始筆記保留的來源

- [No Provider for CustomPipe - angular 4 - Stack Overflow](https://stackoverflow.com/questions/46299952/no-provider-for-custompipe-angular-4)
- [Angular依賴注入的一個常見錯誤NullInjectorError,No provider for XXX - 雲+社群 - 騰訊雲 (tencent.com)](https://cloud.tencent.com/developer/article/1700456)
