---
title: "Angular CLI：開發、產生程式碼與建置"
date: 2020-08-03T11:42:02+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
description: "整理 serve、generate、build、test 與 update，補上本機 CLI 和 outputPath 確認。"
lastmod: 2026-10-07T00:01:00+08:00
---

整理 serve、generate、build、test 與 update，補上本機 CLI 和 outputPath 確認。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

## 使用專案自己的 CLI

在已有專案且依賴安裝完成的目錄：

```bash
npx ng version
npx ng serve --port 4200
npx ng generate component features/tasks/task-list --dry-run
npx ng generate service core/task
npx ng build --configuration production
```

serve持續運作，以Ctrl+C停止。dry-run先列出變更，不寫檔；確認後拿掉才生成。component檔名與standalone預設受CLI major影響，不照舊截圖硬改。

## 常用選項

`ng generate component`、service、pipe、directive各有不同責任。舊module架構可用module與指定module選項，新standalone系統未必要建立module。`--project`選workspace內專案，`--configuration`對應angular.json已存在設定，不是任意Spring profile。

新版以production configuration替代早期常見的--prod簡寫。測試用`npx ng test`，依builder支援的非監看引數在CI執行；沒有lint target時ng lint不會自動替你安裝lint工具。

## 確認與排錯

未知選項先用`npx ng build --help`與實際CLI版本檔案，不安裝另一個全域性CLI掩蓋。port衝突先選未使用port；不能以serve綁0.0.0.0就當正式部署。production建置後檢查outputPath與base-href，再測直接開子路徑，見Tomcat部署篇。

升級以`npx ng update`列建議，再按官方跨版本指引逐major處理，保留Git可回復狀態與測試。這些CLI操作會改檔，先看dry-run與diff再確認結果。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Angular CLI](https://angular.dev/tools/cli)
- [ng build](https://angular.dev/cli/build)
- [ng generate](https://angular.dev/cli/generate)

### 原始筆記保留的來源

- [Angular官網generate介紹](https://angular.io/cli/generate)
- [Angular 13 開發環境說明 (github.com)](https://gist.github.com/doggy8088/15e434b43992cf25a78700438743774a)
