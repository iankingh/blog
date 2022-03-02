---
title: "AngularFileStructure"
date: 2020-08-03T09:18:12+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

## Angular 代碼目錄結構
<!--more-->

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

`ng build --prod`

`ng build --configuration=sit`

`ng build --configuration=uat`

`ng build --configuration=production`


--prod  : 把 `src/environments/environment.ts` 檔案替換成針對特定目標的版本 , 且編譯出來的檔案會小很多

--output-path : 表示輸出路徑  : ex : 輸出到當前目錄的 web資料夾底下

--base-href : 修改 index.html 裡的 <base href="/"> : ex : <base href="/web/">

**編譯完成後 確認** 

index.html 裡的 : <base href="/web/">

### 部署

1. 部署 facial-identity-web: $Tomcat/webapps/web
2. 部署 facial-identity-admin: $Tomcat/webapps/admin

## Single Module File Structure

```markdown
├── README.md # 
├── angular.json # Angular CLI 的設定檔
├── node_modules # npm 
├── package-lock.json # 鎖定安裝時的包的版本號，以保證其他人在npm install時大家的依賴能保證一致。
├── package.json # 配置工作區中所有項目的相依套件
├── proxy.config.json # 代理伺服器設定
├── src
│   ├── app
│   │   ├── app.README.md 
│   │   ├── app.component.css
│   │   ├── app.component.html
│   │   ├── app.component.ts #根目錄的TS controller
│   │   ├── app.module.ts #根目錄的TS module
│   │   ├── app-routing.module.ts # 路由定義 
│   │   ├── components # component資料夾
│   │   ├── directives # directives資料夾
│   │   ├── http-interceptors # http-interceptors資料夾
│   │   ├── guard # guard資料夾
│   │   ├── models #models資料夾
│   │   ├── pipes #pipes資料夾
│   │   ├── services #service資料夾
│   │   ├── shared # 共用的資料夾 不會被路由開啟的 component
│   ├── assets # 靜態資源資料夾，用來放images、多國語系…等
│   │   ├── browser #
│   │   ├── doc # 文檔
│   │   ├── fonts # 字體資料夾
│   │   ├── image # 圖片資料夾
│   │   ├── plugin # 第三方套件
│   ├── environments # 環境變數
│   │   ├── environment.dev.ts # 開發環境變數
│   │   ├── environment.sit.ts # 測試環境變數
│   │   └── environment.prod.ts # 正式環境變數
│   ├── favicon.ico # 網站圖示
│   ├── index.html # 起始頁面
│   ├── main.ts # 應用程式的入口點,AppModule bootstrap 的程式進入點
│   ├── polyfills.ts # 提供對舊版本的 IE 或舊版瀏覽器的設定
│   ├── styles.less # 整個網頁應用程式共用的scss設定檔
│   ├── test.ts # test 的程式進入點
├── tsconfig.json 
├── tslint # TypeScript 程式碼風格檢查器。
├── .gitignore #  設定git 忽略那些檔案不要加入版本控管
└── .editorconfig #  編輯器設定檔，設定處理 tab 符號、換行等等。
```


## Multiple Modules

```markdown
├── README.md # 
├── angular.json # Angular CLI 的設定檔
├── node_modules # npm 
├── package-lock.json # 鎖定安裝時的包的版本號，以保證其他人在npm install時大家的依賴能保證一致。
├── package.json # 配置工作區中所有項目的相依套件
├── proxy.config.json # 代理伺服器設定
├── src
│   ├── app
│   │   ├── app.README.md 
│   │   ├── app.component.css 
│   │   ├── app.component.html
│   │   ├── app.component.ts       # 進入點TS
│   │   ├── app.module.ts          # 根目錄的TS module
│   │   ├── app-routing.module.ts  # 路由定義
│   │   ├── module1               # 模組的目錄
│   │   │   ├── components         # 元件的資料夾
│   │   │   ├── user-info.ts                      # 如：(e.g. UserInfo)
│   │   │   ├── module2.services.ts  # 處理component間的資料傳遞
│   │   │   ├── routes.ts           # 處理component間的資料傳遞
│   │   ├── module2               # 模組的目錄
│   │   │   ├── components         # 元件的資料夾
│   │   │   ├── user-info.ts                      # 如：(e.g. UserInfo)
│   │   │   ├── module2.services.ts  # 處理component間的資料傳遞
│   │   │   ├── routes.ts           # 處理component間的資料傳遞
│   │   ├── shared # 共用的模組
│   │   │   ├── components         # 不會被路由開啟的共用的 component
│   │   │   │   ├──dialog.component.ts                # 如：對話框 (e.g. DialogComponent)
│   │   │   ├── directives         # 共用的 自訂directives(指令)的資料夾
│   │   │   │   ├──twid-validator.directive           # 如：驗證身份證 (e.g. TwidValidatorDirective)
│   │   │   ├── guards             # 共用的 guards 資料夾 
│   │   │   │   ├──auth.guard.ts                      # 如：驗證身份證 (e.g. AuthGuard)
│   │   │   ├── http-interceptors  # 共用的interceptors(路由攔截)的資料夾
│   │   │   │   ├──http-mock-request.interceptor      # 如：假資料用 (e.g. HttpMockRequestInterceptor)
│   │   │   ├── pipes              # 共用 處理資料 pipes 的資料夾
│   │   │   │   ├──date-format.pipe.ts                # 如：日期格式化用的 (e.g. DateFormatPipe)
│   │   │   ├── services           # 共用 services 的資料夾
│   │   │   │   ├──messages.service.ts                # 如：開啟DialogComponent用的 (e.g. MessagesService)
│   ├── assets # 靜態資源資料夾，用來放images、多國語系…等
│   │   ├── browser #
│   │   ├── doc # 文檔
│   │   ├── fonts # 字體資料夾
│   │   ├── image # 圖片資料夾
│   │   ├── plugin # 第三方套件
│   ├── environments # 環境變數
│   │   ├── environment.dev.ts # 開發環境變數
│   │   ├── environment.sit.ts # 測試環境變數
│   │   └── environment.prod.ts # 正式環境變數
│   ├── favicon.ico # 網站圖示
│   ├── index.html # 起始頁面
│   ├── main.ts # 應用程式的入口點,AppModule bootstrap 的程式進入點
│   ├── polyfills.ts # 提供對舊版本的 IE 或舊版瀏覽器的設定
│   ├── styles.less # 整個網頁應用程式共用的scss設定檔
│   ├── test.ts # test 的程式進入點
├── tsconfig.json 
├── tslint # TypeScript 程式碼風格檢查器。
├── .gitignore #  設定git 忽略那些檔案不要加入版本控管
└── .editorconfig #  編輯器設定檔，設定處理 tab 符號、換行等等。
```


## Multiple Modules -layout
```markdown
├── README.md # 
├── angular.json # Angular CLI 的設定檔
├── node_modules # npm 
├── package-lock.json # 鎖定安裝時的包的版本號，以保證其他人在npm install時大家的依賴能保證一致。
├── package.json # 配置工作區中所有項目的相依套件
├── proxy.config.json # 代理伺服器設定
├── src
│   ├── app
│   │   ├── app.README.md 
│   │   ├── app.component.css 
│   │   ├── app.component.html
│   │   ├── app.component.ts       # 進入點TS
│   │   ├── app.module.ts          # 根目錄的TS module
│   │   ├── app-routing.module.ts  # 路由定義
│   │   ├── /features               # 功能模組的目錄
│   │   │   ├── /home               # HomeModule
│   │   │   ├── /Layout             # 登入後的 Module
│   │   │   │   ├── /article        # 物品功能模組
│   │   │   │   │   ├── article-body
│   │   │   │   │   ├── article-header
│   │   │   │   │   ├── article-list
│   │   │   │   │   ├── article.module.ts
│   │   │   │   │   ├── data.service.spec.ts
│   │   │   │   │   ├── data.service.ts
│   │   │   │   ├── /articlemodule2
│   │   │   │   │   ├── module2              # 模組的目錄
│   │   │   │   │   ├── components         # 元件的資料夾
│   │   │   │   │   ├── user-info.ts                      # 如：(e.g. UserInfo)
│   │   │   │   │   ├── module2.services.ts  # 處理component間的資料傳遞
│   │   │   │   │   ├── routes.ts           # 處理component間的資料傳遞
│   │   │   │   ├── layout-routing.module.ts  # layout路由定義
│   │   │   ├── /Login              # 登入模組
│   │   │   ├── /models             # 用來跟用來跟頁面互動的資料容器（可以移動至各模組）
│   │   │   │   ├── user-info.ts   # 如：(e.g. UserInfo)
│   │   │   ├── /services           # 處理component間的資料傳遞（可以移動至各模組）
│   │   │   │   ├──user-info-Serviec.ts
│   │   ├── /shared # 共用的模組
│   │   │   ├── /components         # 不會被路由開啟的共用的 component
│   │   │   │   ├──/Layout  
│   │   │   │   │  ├──dialog.component.ts  # 如：對話框 (e.g. DialogComponent)
│   │   │   │   │  ├──header.component.ts  # 如：header (e.g. headerComponent)
│   │   │   │   ├──/controls  
│   │   │   │   │  ├──control-text.ts      # 如：自訂輸入項 (e.g. ControlTextComponent)
│   │   │   ├── /directives         # 共用的 自訂directives(指令)的資料夾
│   │   │   │   ├──twid-validator.directive           # 如：驗證身份證 (e.g. TwidValidatorDirective)
│   │   │   ├── /guards             # 共用的 guards 資料夾 
│   │   │   │   ├──auth.guard.ts                      # 如：驗證身份證 (e.g. AuthGuard)
│   │   │   ├── /http-interceptors  # 共用的interceptors(路由攔截)的資料夾
│   │   │   │   ├──http-mock-request.interceptor      # 如：假資料用 (e.g. HttpMockRequestInterceptor)
│   │   │   ├── /pipes              # 共用 處理資料 pipes 的資料夾
│   │   │   │   ├──date-format.pipe.ts                # 如：日期格式化用的 (e.g. DateFormatPipe)
│   │   │   ├── /services           # 共用 services 的資料夾
│   │   │   │   ├──messages.service.ts                # 如：開啟DialogComponent用的 (e.g. MessagesService)
│   ├── /assets # 靜態資源資料夾，用來放images、多國語系…等
│   │   ├── browser #
│   │   ├── doc # 文檔
│   │   ├── fonts # 字體資料夾
│   │   ├── image # 圖片資料夾
│   │   ├── plugin # 第三方套件
│   ├── /environments # 環境變數
│   │   ├── environment.dev.ts # 開發環境變數
│   │   ├── environment.sit.ts # 測試環境變數
│   │   └── environment.prod.ts # 正式環境變數
│   ├── favicon.ico # 網站圖示
│   ├── index.html # 起始頁面
│   ├── main.ts # 應用程式的入口點,AppModule bootstrap 的程式進入點
│   ├── polyfills.ts # 提供對舊版本的 IE 或舊版瀏覽器的設定
│   ├── styles.less # 整個網頁應用程式共用的scss設定檔
│   ├── test.ts # test 的程式進入點
├── tsconfig.json 
├── tslint # TypeScript 程式碼風格檢查器。
├── .gitignore #  設定git 忽略那些檔案不要加入版本控管
└── .editorconfig #  編輯器設定檔，設定處理 tab 符號、換行等等。
```


PS：特別感謝Java 社群的 GC 大神的指導



## 參考

[Angular 4 File Structure | John Wu's Blog](https://blog.johnwu.cc/article/angular-4-file-structure.html)

[為中大型的Angular專案設計專案結構. 最近有一個新專案要用 Angular 8開發，因為之前開發的都是以傳統C#… | by Tim Tsai | Medium](https://medium.com/@sky22357168/angular-8-file-structure-6cda90142ba4)