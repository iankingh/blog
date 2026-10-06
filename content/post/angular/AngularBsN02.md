---
title: "Angular CLI 專案結構：舊 NgModule 與新版差異"
date: 2020-07-05T19:02:31+08:00
draft: false
categories:
- "筆記"
tags:
- "Angular"
- "FrontEnd"
toc: true
description: "保留 Angular 初學專案架構，補上設定檔責任、生成版本差異與啟動檢查。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 Angular 初學專案架構，補上設定檔責任、生成版本差異與啟動檢查。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

## 認識目錄

| 路徑 | 責任 |
| --- | --- |
| angular.json | workspace、builder、build/serve設定 |
| package.json / lockfile | 指令、依賴與可重現版本 |
| tsconfig*.json | TypeScript與Angular編譯設定 |
| src/main.ts | bootstrap入口 |
| src/index.html | HTML殼與根元件host |
| src/app | 應用元件、服務與路由 |
| public 或 src/assets | 依CLI版本設定的靜態資源 |
| node_modules | 安裝的依賴，不提交 |

原筆記稱node_modeles是拼字錯誤。Angular舊CLI常生成app.module.ts、polyfills.ts、karma.conf.js與tslint.json；新版可能生成standalone app.config.ts、不同測試builder與檔名，不代表缺檔。TSLint已是歷史工具，需lint時依專案選ESLint整合。

## 建立與檢查

選定相容Node與CLI major後，例如歷史練習Angular20：

```bash
npx @angular/cli@20 new angular-note-lab --standalone --routing --style=css
cd angular-note-lab
npm start
npm run build
```

以終端顯示地址開啟，應看到初始app；build輸出依angular.json的outputPath，別假設永遠dist/project根層。入口的bootstrapApplication與App元件需配對，NgModule則是bootstrapModule。

## 修改規則

只改src業務來源，不直接改node_modules產物。加套件讓package與lock一起更新；移動資料夾後修正import與路由。`.editorconfig`處理編輯器格式，不控制HTTP／DB編碼；`.gitignore`不會移除已追蹤秘密。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Angular workspace](https://angular.dev/reference/configs/workspace-config)
- [版本相容](https://angular.dev/reference/versions)
- [Angular 安裝](https://angular.dev/installation)

### 原始筆記保留的來源

- [EditorConfig](https://editorconfig.org/)
- [Karma - Spectacular Test Runner for Javascript (karma-runner.github.io)](https://karma-runner.github.io/latest/index.html)
- [Angular CLI 7.3 使用 ES2015 的 nomodule 屬性載入 Polyfills 函式庫 | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2019/02/03/Angular-CLI-73-Use-ES2015-nomodule-load-polyfills)
