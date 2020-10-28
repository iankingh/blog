---
title: "AngularFileStructure"
date: 2020-08-03T09:18:12+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angular 代碼目錄結構
<!--more-->



File Structure

```markdown
├── README.md # 
├── angular.json # Angular CLI 的設定檔
├── node_modules # npm 
├── package-lock.json # 鎖定安裝時的包的版本號，以保證其他人在npm install時大家的依賴能保證一致。
├── package.json # 配置工作區中所有項目的相依套件
├── proxy.config.json # 代理伺服器設定
├── src
│   ├── app
│   │   ├── app.README.md 
│   │   ├── app.component.css  
│   │   ├── app.component.html
│   │   ├── app.component.ts #根目錄的TS controller
│   │   ├── app.module.ts #根目錄的TS module
│   │   ├── app-routing.module.ts # 路由定義 
│   │   ├── components # component資料夾
│   │   ├── services #service資料夾
│   │   ├── directives #directives資料夾
│   │   ├── shared # 共用的資料夾 不會被路由開啟的 component
│   ├── assets # 靜態資源資料夾，用來放images、多國語系…等
│   │   ├── browser #
│   │   ├── doc # 文檔
│   │   ├── fonts # 字體資料夾
│   │   ├── image # 圖片資料夾
│   │   ├── plugin # 第三方套件
│   ├── environments # 環境變數
│   │   ├── environment.dev.ts # 開發環境變數
│   │   ├── environment.test.ts # 測試環境變數
│   │   └── environment.prod.ts # 正式環境變數
│   ├── favicon.ico # 網站圖示
│   ├── index.html # 起始頁面
│   ├── main.ts # 應用程式的入口點,AppModule bootstrap 的程式進入點
│   ├── polyfills.ts # 提供對舊版本的 IE 或舊版瀏覽器的設定
│   ├── styles.less # 整個網頁應用程式共用的scss設定檔
│   ├── test.ts # test 的程式進入點
├── tsconfig.json 
├── tslint # TypeScript 程式碼風格檢查器。
├── .gitignore #  設定git 忽略那些檔案不要加入版本控管
└── .editorconfig #  編輯器設定檔，設定處理 tab 符號、換行等等。
```





參考

Angular 4 File Structure | John Wu's Blog

https://blog.johnwu.cc/article/angular-4-file-structure.html

為中大型的Angular專案設計專案結構. 最近有一個新專案要用 Angular 8開發，因為之前開發的都是以傳統C#… | by Tim Tsai | Medium

https://medium.com/@sky22357168/angular-8-file-structure-6cda90142ba4

