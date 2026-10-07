---
title: "Angular 目錄設計：依功能分組與共用邊界"
date: 2020-08-03T09:18:12+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "保留小型與多模組專案的比較，將目錄範例整理為可依需求擴充的功能架構。"
lastmod: 2026-10-07T20:50:40+08:00
---

保留小型與多模組專案的比較，將目錄範例整理為可依需求擴充的功能架構。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 建議起點

```text
src/app/
  app.component.ts
  app.config.ts
  app.routes.ts
  core/
    auth/
    http/
  shared/
    ui/
  features/
    tasks/
      task.routes.ts
      task-list.component.ts
      task-api.service.ts
      task.model.ts
    profile/
      profile.component.ts
```

這是責任分組示意，不是CLI必然產生的完整專案。小專案可直接把相關檔案放同一feature，需求變多再拆；不必第一天建立所有空目錄。NgModule系統可在features中放feature module，standalone使用routes與component組成。

## 與原技術分組比較

只按components/services/models分全站目錄，初學容易找到型別，但一個功能會分散多處；依功能分組讓同一需求的UI、API與型別一起維護。shared只放多處使用且無業務繫結的UI／utility；core放應用層服務，不把所有無處可放的檔案堆入兩者。

## 依賴與載入

feature可依賴shared/core，但shared不反向依賴feature。route以loadComponent或loadChildren延遲載入，驗證實際bundle而非僅看資料夾名；把所有service預先import到root可能影響拆包。path alias需同步tsconfig與工具設定，不能只改import字串。

移動檔案後確認CLI build、路由、測試與迴圈引用。Angular不是傳統伺服器MVC，component/template/service責任可以比較，但不能把資料夾命名當成架構正確的保證。部署細節在Tomcat篇，目錄設計不應包含硬編碼production機器路徑。

## Build 與部署的位置

原筆記同時列出 build 和部署，這兩步仍保留在架構決策中。先在 workspace root 執行 `ng build --configuration production`，輸出位置看 angular.json 的 builder 與 outputPath；新版 application builder 可在輸出下另有 browser 子目錄，不把所有版本都寫成同一路徑。

靜態檔需由 HTTP 主機服務，SPA 的深層路由重整要回 index.html，而靜態資源不存在時仍應正確回 404。Tomcat 的 context path／base href 與伺服器 fallback 見[部署篇]({{< ref "/post/angular/AngularDeployTomcat.md" >}})。依 feature 分目錄不會自行產生 lazy bundle，路由仍要明確使用動態匯入。

## 參考資料

- [Angular Style Guide](https://angular.dev/style-guide)
- [延遲載入路由](https://angular.dev/guide/routing/define-routes)
- [Angular - Router tutorial: tour of heroes](https://angular.io/guide/router-tutorial-toh)
- [Angular - Guidelines for creating NgModules](https://angular.io/guide/module-types)
- [Angular 4 File Structure | John Wu's Blog](https://blog.johnwu.cc/article/angular-4-file-structure.html)
- [為中大型的Angular專案設計專案結構. 最近有一個新專案要用 Angular 8開發，因為之前開發的都是以傳統C#… | by Tim Tsai | Medium](https://medium.com/@sky22357168/angular-8-file-structure-6cda90142ba4)
