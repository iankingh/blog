---
title: "AngularCLInotes"
date: 2020-08-03T11:42:02+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

## Angular維運指令

### 啟動本機開發server

`ng serve`  : 啟動本機server 預設4200

`npm start` : 啟動本機server 預設4200 會跑 ng serve

### build : **編譯Project**

到專案目錄執行 **編譯指令如下**

`ng build --prod --base-href /project_Name/`

可以使用以下編譯指令 但需設定在angular.js中

`ng build --prod` 

`ng build --configuration=sit`

`ng build --configuration=uat`

`ng build --configuration=production`

- **prod** : 把 `src/environments/environment.ts`檔案替換成針對特定目標的版本 , 且編譯出來的檔案會小很多
- **output-path** : 表示輸出路徑 : ex : 輸出到當前目錄的 web資料夾底下
- **base-href** : 修改 index.html 裡的 `<base href="/">` : ex : `<base href="/project_Name/">`

## Angular 常用創建指令

### 新增專案的 Angular 指令

```tsx
ng new angularProject --style=scss --routing
```

### Angular 常用創建指令

### **ng generate**

- [Angular官網generate介紹](https://angular.io/cli/generate)
- Generates and/or modifies files based on a schematic. 在已有專案中創建其他元件的指令
- ng generate <schematic> [options]
- ng g <schematic> [options]
- schematic

### component

- 縮寫 `c`
- 說明:創建元件，建構頁面的基礎。
    - 用法 : `ng g component componentName`或 `ng g c componentName`
- 需要指定路徑就 `ng g c path/componentName`

### service

- 縮寫`s`
- 說明:創建服務，通常只提供一種類型的服務，如登入、驗證等服務
- 用法: `ng g service [service name`] 或 `ng g s [service name]`
- 需要指定路徑就`ng g s [path]/[service name]`

### pipe

- 縮寫 `p`
- 說明:創建通道，通常用來將A轉換為B，如提供60秒經由通道轉換為1分鐘
- 用法: `ng g pipe [pipe name]`或 `ng g p [pipe name]`
- 需要指定路徑就 `ng g p [path]/[pipe name]`

### directive

- 縮寫 `d`
- 說明:創建指令，可以賦予標籤或元件擁有某一種功能
- 用法:`ng g directive [directive name]`或 `ng g d [directive name]`
- 需要指定路徑就`ng g d [path]/[directive name]`

### module

- 縮寫`m`
- 說明:創建模組，模組通常由功能特性劃分，如路由模組、驗證模組、報表模組，模組可以包含元件、服務、只是、通道及其他模組
- 用法:`ng g module [module name]`或 `ng g m [module name]`
- 需要指定路徑就`ng g m [path]/[module name]`

### application

- 說明 : 創建子專案，可以單獨當作一個app，也可以在主專案把子專案導入使用
- 用法 : `ng g application [application name]`
- 創建位置預設在`projects`裡

## 參考

[Angular 13 開發環境說明 (github.com)](https://gist.github.com/doggy8088/15e434b43992cf25a78700438743774a)
