---
title: "Compodoc：產生 Angular 檔案與檢查輸出"
date: 2020-07-20T16:17:45+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
draft: false
description: "修正 CLI 選項與註解範例，補上輸入 tsconfig、版本固定及檔案範圍。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正 CLI 選項與註解範例，補上輸入 tsconfig、版本固定及檔案範圍。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 安裝與產生

在既有Angular專案安裝與該專案相容的版本，並儲存lockfile：

```bash
npm install --save-dev @compodoc/compodoc
npx compodoc -p tsconfig.app.json -d documentation
npx compodoc -s -d documentation -r 8888
```

`-p`指定TypeScript專案檔，不是「產生」開關；`-d`指定輸出目錄、`-s`啟動檔案server、`-r`指定port。若workspace的tsconfig僅有references或沒有來源，先選真正包含app檔案的配置，按安裝版本`npx compodoc --help`確認。

## 檔案註解

```typescript
import { Injectable } from '@angular/core';
/** 提供本地問候文字，不發出網路請求。 */
@Injectable({ providedIn: 'root' })
export class HelloService {
  /** @param userName 要顯示的名稱 @returns 問候字串 */
  hello(userName: string): string { return `你好 ${userName}`; }
}
```

原`@Injectab()`拼字錯誤改為Injectable。TypeScript已有型別，不必在每個param重複手寫容易失真的型別。

## 確認與限制

檔案網站應包含HelloService、方法與說明，點連結能檢視相應結構。若缺服務先查tsconfig.include/exclude和工具解析錯誤。coverage只表示有沒有註解，不能證明內容正確；介面HTTP契約還需OpenAPI等獨立文件。

產物可能含內部路徑、路由及程式碼，不無條件公開到網路。升級Angular後核對Compodoc支援，不要用全域性未知版本生成與CI不同的檔案。

## 查核範圍

Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Compodoc CLI](https://compodoc.app/guides/options.html)
- [Compodoc installation](https://compodoc.app/guides/installation.html)

### 原始筆記保留的來源

- [Angular 工具篇之檔案管理 | 前端修仙之路](https://semlinker.com/ng-compodoc-intro/)
- [Angular #10 Angular Documentation](https://tpu.thinkpower.com.tw/tpu/articleDetails/864)
- [Javascript檔案註解規則使用方式@use JSDoc - ucamc](https://www.ucamc.com/e-learning/javascript/250-javascript-use-jsdoc)
- [你寫的檔案別人看得懂嗎？：compodoc | Jonny Huang 的學習筆記 (jonny-huang.github.io)](https://jonny-huang.github.io/angular/training/23_compodoc/)
