---
title: "Angular 引入 JavaScript：ES module 與全域 script"
date: 2021-01-22T13:38:06+08:00
categories:
- "筆記"
tags:
- "Angular"
- "FrontEnd"
toc: true
draft: false
description: "比較 ES module、allowJs、型別提示與全域 scripts，確認 JavaScript 在 Angular 中的載入方式。"
lastmod: 2026-10-07T20:50:40+08:00
---

比較 ES module、allowJs、型別提示與全域 scripts，確認 JavaScript 在 Angular 中的載入方式。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 優先使用 module

自己的小函式可轉成TypeScript。若保留JS，建立src/app/greeting.js：

```javascript
/** @param {string} name */
export function greeting(name) { return `你好 ${name}`; }
```

在既有tsconfig的compilerOptions加入`allowJs: true`，將檔案納入編譯；元件使用：

```typescript
import { greeting } from './greeting.js';
export const example = greeting('Ian');
```

結果應為你好Ian。allowJs允許JS進TS專案，不會自動建立全域性變數，也不會修復第三方庫缺型別。npm庫優先使用ESM匯入與內建型別／相容@types，保留依賴版本。

## 全域 script 的舊情境

僅對確實不是module的legacy script，在angular.json對應build.options.scripts加入路徑；需和檔案中window上的名稱一致。TypeScript宣告只告訴型別系統該符號存在，不會載入檔案。先在Network與Console確認實際script載入，再呼叫API。

不得同時以scripts與import載入同一庫以免重複例項。手動createElement(script)是另一種動態載入設計，需處理load/error、CSP與來源可信性，不能用來繞過建置配置。

## SSR 與維護

window／document不存在於Node SSR，browser-only庫要限制在瀏覽器流程初始化，並於元件解除安裝清理監聽。全域性指令碼難以tree-shake與測試，逐步包裝成明確service或module；先保留原行為測試再替換。

確認方式是build成功、問候輸出符合預期且script只載入一次。原合併衝突標記與重複compilerOptions範本已經移除。

## 參考資料

- [Angular workspace scripts](https://angular.dev/reference/configs/workspace-config#styles-and-scripts-configuration)
- [TypeScript allowJs](https://www.typescriptlang.org/tsconfig/allowJs.html)
- [angular在ts中使用第三方js_weixin_43182222的部落格-CSDN部落格](https://blog.csdn.net/weixin_43182222/article/details/105205283?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control)
- [How to call JavaScript functions from Typescript in Angular 5? - Stack Overflow](https://stackoverflow.com/questions/49526681/how-to-call-javascript-functions-from-typescript-in-angular-5)
- [Angular引入自己寫的js或者其他_qq_43205711的部落格-程式設計師宅基地_angular引用自己的js - 程式設計師宅基地 (cxyzjd.com)](https://www.cxyzjd.com/article/qq_43205711/84139445)
