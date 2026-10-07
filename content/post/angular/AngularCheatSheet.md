---
title: "Angular 小抄：模板、生命週期、DI 與路由"
date: 2020-11-06T22:11:38+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "重整過時 API 與不完整範例，提供核心概念對照及完整路由接線。"
lastmod: 2026-10-07T20:50:40+08:00
---

重整過時 API 與不完整範例，提供核心概念對照及完整路由接線。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 快速對照

| 需求 | API／寫法 | 注意事項 |
| --- | --- | --- |
| 顯示文字 | `{{ value }}` | 不當作HTML執行 |
| 屬性／事件 | `[disabled]` / `(click)` | 分別為資料與事件方向 |
| 表單雙向繫結 | `[(ngModel)]` | 需FormsModule，form內需name |
| 資料初始化 | ngOnInit | 不保證子檢視已完成 |
| DOM／子檢視 | ngAfterViewInit | 避免在此無條件修改造成檢查錯誤 |
| 清理 | ngOnDestroy／DestroyRef | timer、listener與subscription都需處理 |
| 共用服務 | providedIn:root | provider層級影響例項範圍 |

新控制流@for需track穩定鍵；舊*ngFor的trackBy同樣為節點識別。Signal適合響應式狀態，RxJS適合非同步流，兩者可互通但不能混稱同一API。

## 最小路由

假設已有HomeComponent、AboutComponent，app.routes.ts：

```typescript
import { Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { AboutComponent } from './about.component';
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: '**', redirectTo: '' }
];
```

app.config providers加入provideRouter(routes)，根元件imports加入RouterLink/RouterOutlet。模板：

```html
<a routerLink="/">首頁</a> <a routerLink="/about">關於</a>
<router-outlet />
```

點關於顯示對應元件，瀏覽器返回回首頁。前端guard不是後端許可權；HttpClient請求需獨立配置provider與錯誤處理。

## 原版本差異

舊`Http`改HttpClient，TSLint與--prod是歷史情境，standalone不一定有AppModule。RxJS訂閱應清理、HTTP用可取消／可組合的流，不把每個subscribe巢狀在另一個裡。這是查詢小抄，完整操作見表單、CLI與部署各篇。

## 參考資料

- [模板](https://angular.dev/guide/templates)
- [生命週期](https://angular.dev/guide/components/lifecycle)
- [路由](https://angular.dev/guide/routing)
- [RxJS interop](https://angular.dev/ecosystem/rxjs-interop)
- [原始參考入口 1](https://dev.to/suniljoshi19/angular-cheat-sheet-46bo?fbclid=IwAR1hL9OTHVIthSFCqOH4pGuMK3447-ru5vPxKT-EI4AAOyGoLAJ3iiQ7K8I)
- [原始參考入口 2](https://gist.github.com/doggy8088/7f148e6288cdd8a3588f0ebbd57735ef?fbclid=IwAR2vPjd4AFcPZFHW_74n43bL5eQ-420yFGbntB-mTNoftuTPIOfjScgVddw)
