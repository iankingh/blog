---
title: "JavaScript 陣列產生表格：安全文字與完整欄位"
date: 2021-03-16T09:55:35+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
description: "以小型本地資料取代過長的銀行清單，保留陣列轉表格情境並補上文字轉義。"
lastmod: 2026-10-07T20:50:40+08:00
---

以小型本地資料取代過長的銀行清單，保留陣列轉表格情境並補上文字轉義。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 完整頁面

原銀行資料僅是當時示例，不作現行銀行名單。以下使用虛構記錄，重點是建立thead/tbody與安全文位元組點：

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>陣列表格</title>
<table><caption>練習機構</caption><thead><tr><th scope="col">代碼</th><th scope="col">名稱</th></tr></thead><tbody id="rows"></tbody></table>
<script>
const banks = [{ code: '001', name: '營火機構' }, { code: '002', name: '<示例機構>' }];
const body = document.querySelector('#rows');
for (const bank of banks) {
  const row = document.createElement('tr');
  for (const value of [bank.code, bank.name]) {
    const cell = document.createElement('td');
    cell.textContent = value;
    row.append(cell);
  }
  body.append(row);
}
</script></html>
```

應有兩列、每列兩欄，第二個名稱顯示含尖括號的文字而不是HTML。程式碼以字串儲存，避免001轉成數字1。

## 資料與更新

實際API先核對資料schema，不依物件屬性列舉順序決定業務欄位。重新渲染前使用replaceChildren清除或建立新fragment替換，避免重複追加。多筆資料可用DocumentFragment集中插入，資料量大時分頁或虛擬列表。

表格提供caption與th scope供輔助技術讀取，不用div硬模擬所有語意。使用textContent而非把使用者內容串進innerHTML；即使資料來源目前受控，也要清楚區分文字與HTML。

## 參考資料

- [createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
- [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)
- [HTML table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
