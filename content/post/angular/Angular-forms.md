---
title: "Angular Reactive Forms：模型、驗證與提交"
date: 2021-06-24T14:00:58+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "整理兩種表單的適用情境，補上型別化 FormGroup 與完整範例。"
lastmod: 2026-10-07T00:01:00+08:00
---

整理兩種表單的適用情境，補上型別化 FormGroup 與完整範例。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

## 比較

| 方式 | 資料模型 | 適合 |
| --- | --- | --- |
| Template-driven | 由ngModel在模板建立 | 簡單欄位、少量規則 |
| Reactive | TypeScript明確建立control | 多欄位、動態規則、較多測試 |

新版另有Signal Forms，需依實際Angular版本評估，不把本篇Reactive API混寫成Signal API。FormControl管理單欄、FormGroup管理鍵名集合、FormArray管理動態清單。

先依[Angular CLI 篇]({{< ref "/post/angular/AngularCLInotes.md" >}})建立相容版本的 standalone 專案。下例可存為 `src/app/app.component.ts`；`src/main.ts` 改為從 `./app/app.component` 匯入 `AppComponent`，並使用 `bootstrapApplication(AppComponent, appConfig)`，保留 CLI 產生的 `appConfig`。Angular 20 的預設 root 可能叫 `App`、位於 `app.ts`，檔名與啟動類別要一併對齊，不能只貼程式卻仍啟動舊元件。

## 完整元件

```typescript
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
@Component({
  selector: 'app-root', standalone: true, imports: [ReactiveFormsModule],
  template: `<form [formGroup]="form" (ngSubmit)="submit()">
    <label>名稱 <input formControlName="name"></label>
    <label>Email <input formControlName="email" type="email"></label>
    <button [disabled]="form.invalid">送出</button>
  </form><p>{{ result }}</p>`
})
export class AppComponent {
  form = new FormGroup({
    name: new FormControl('', { nonNullable: true, validators: [Validators.required] }),
    email: new FormControl('', { nonNullable: true, validators: [Validators.required, Validators.email] })
  });
  result = '';
  submit(): void {
    this.form.markAllAsTouched();
    if (this.form.invalid) return;
    this.result = JSON.stringify(this.form.getRawValue());
  }
}
```

空表單停用送出，填Ian與ian@example.test後顯示JSON。nonNullable使reset回初始字串而不是null；getRawValue包含disabled欄位，value可能不含，所以選擇需符合目的。

## 常見問題

setValue要求完整結構，patchValue允許部分欄位。valueChanges訂閱要清理，可用takeUntilDestroyed；大量訂閱或HTTP搜尋要處理去抖與取消。不要在同一輸入同時使用ngModel與formControlName。前端email驗證只檢查格式，不證明信箱存在或歸屬。

## 查核範圍

Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出）。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Reactive Forms](https://angular.dev/guide/forms/reactive-forms)
- [Typed Forms](https://angular.dev/guide/forms/typed-forms)
- [Forms比較](https://angular.dev/guide/forms)

### 原始筆記的其他連結

- [原始參考入口 1](https://angular.io/api/forms/FormControl)
