---
title: "Angular 範本驅動表單：ngModel 與驗證"
date: 2021-06-24T14:00:58+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "補齊原空白筆記，以名稱表單示範 FormsModule、name、required 與提交。"
lastmod: 2026-10-07T20:50:40+08:00
---

補齊原空白筆記，以名稱表單示範 FormsModule、name、required 與提交。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

先依[Angular CLI 篇]({{< ref "/post/angular/AngularCLInotes.md" >}})建立相容版本的 standalone 專案。下例可存為 `src/app/app.component.ts`；`src/main.ts` 改為從 `./app/app.component` 匯入 `AppComponent`，並使用 `bootstrapApplication(AppComponent, appConfig)`，保留 CLI 產生的 `appConfig`。Angular 20 的預設 root 可能叫 `App`、位於 `app.ts`，檔名與啟動類別要一併對齊，不能只貼程式卻仍啟動舊元件。

## 完整 standalone 元件

在已建立的Angular20專案中以此取代app元件，入口bootstrap對應AppComponent：

```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-root', standalone: true, imports: [FormsModule],
  template: `
    <form #form="ngForm" (ngSubmit)="submit()">
      <label>名稱 <input name="name" [(ngModel)]="name" required #field="ngModel"></label>
      @if (field.invalid && field.touched) { <p>名稱不可空白</p> }
      <button [disabled]="form.invalid">送出</button>
    </form>
    <p>{{ result }}</p>`
})
export class AppComponent {
  name = '';
  result = '';
  submit(): void { this.result = this.name.trim() ? `你好 ${this.name.trim()}` : '請輸入有效名稱'; }
}
```

初始按鈕停用，輸入Ian後可送出，顯示你好Ian。required拒絕空字串但不一定拒絕只有空白，因此submit仍檢查trim；重要驗證也由後端完成。

## 舊版對照

NgModule專案在宣告元件的module匯入FormsModule，模板控制流可用`*ngIf`並匯入CommonModule。standalone的imports與NgModule的imports不是同一檔案。ngModel在form內需name，否則不能註冊到ngForm；若刻意獨立控制項可設定standalone選項。

模板驅動適合簡單表單，複雜跨欄位或動態表單先比較[Reactive Forms]({{< ref "/post/angular/Angular-forms.md" >}})。錯誤顯示使用touched/dirty，避免使用者尚未操作就整頁警告。

## 參考資料

- [Template-driven forms](https://angular.dev/guide/forms/template-driven-forms)
- [表單驗證](https://angular.dev/guide/forms/form-validation)
