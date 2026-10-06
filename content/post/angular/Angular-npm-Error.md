---
title: "Angular npm 安裝錯誤：peer dependency 診斷"
date: 2021-07-04T18:05:34+08:00
categories:
 - "技術"
tags:
 - "Angular"
 - "npm"
toc: true
draft: false
description: "補上 Node、Angular、TypeScript 相容檢查，避免以 force 跳過真正的版本衝突。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上 Node、Angular、TypeScript 相容檢查，避免以 force 跳過真正的版本衝突。

<!--more-->

適用：原筆記的Angular CLI／NgModule專案；新範例以Angular 20的standalone元件說明。建立專案前按官方版本表選Node與TypeScript，不能把舊專案直接套最新CLI。

## 先保留錯誤與環境

```bash
node --version
npm --version
npx ng version
npm ls @angular/core @angular/cli typescript
npm explain typescript
```

在專案目錄執行，讀ERESOLVE中哪個套件要求哪個版本。Angular各核心套件通常需相容major，TypeScript也有版本上限；單純安裝最新TS可能讓compiler失敗。

## 處理順序

先核對package.json與官方相容表，選可相容的套件版本或按ng update路線升級。lockfile與package.json一致時用npm ci；npm install更新依賴圖，可能改lockfile。不要為了「乾淨」一開始就刪lockfile，否則難以追查差異。

`--legacy-peer-deps`忽略peer contract，`--force`容許多種衝突，不應作長期預設。若暫時為診斷使用，記錄原因並重新建立相容依賴圖後移除。

## 其他錯誤

EACCES檢查套件目錄許可權，不用sudo全域性install修復一切；ECONNRESET/TLS錯誤查proxy、registry與CA，不關strict-ssl。`npm cache verify`檢查快取，只有證據指向快取損壞才清理。

確認修正以npm ci、專案build及測試為準，不只install成功。網路服務／private registry錯誤要留去識別化日誌與HTTP狀態，token不貼公開。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Angular 版本表](https://angular.dev/reference/versions)
- [Angular 更新](https://angular.dev/update-guide)
- [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci)
- [npm explain](https://docs.npmjs.com/cli/v11/commands/npm-explain)
