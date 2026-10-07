---
title: "JavaScript 表格搜尋：保留欄位並篩選整列"
date: 2021-03-16T10:02:22+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
description: "修正原本隱藏個別儲存格造成的欄位錯位，補上計數與空結果。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正原本隱藏個別儲存格造成的欄位錯位，補上計數與空結果。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 完整頁面

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>表格搜尋</title>
<label>搜尋任務 <input id="query" type="search"></label>
<p id="status" role="status"></p>
<table><caption>本地任務</caption><thead><tr><th scope="col">名稱</th><th scope="col">類型</th></tr></thead>
<tbody id="rows"><tr><td>Vue 入門</td><td>前端</td></tr><tr><td>Java 練習</td><td>後端</td></tr><tr><td>Docker 操作</td><td>維運</td></tr></tbody></table>
<script>
const input = document.querySelector('#query');
const rows = [...document.querySelectorAll('#rows tr')];
const status = document.querySelector('#status');
function filter() {
  const query = input.value.trim().toLocaleLowerCase();
  let count = 0;
  for (const row of rows) {
    row.hidden = !row.textContent.toLocaleLowerCase().includes(query);
    if (!row.hidden) count++;
  }
  status.textContent = count ? `顯示 ${count} / ${rows.length} 筆` : '沒有符合的任務';
}
input.addEventListener('input', filter);
filter();
</script></html>
```

初始3筆；輸入vue顯示1筆，輸入不存在文字顯示空結果，清除恢復3筆。隱藏整列，列中的兩個儲存格仍一起保留。原逐cell過濾會破壞欄位對齊，已移除。

## 搜尋語意與限制

此例是不分大小寫的單一子字串搜尋，不是分詞、模糊排序或後端全文索引。表格新增列後需更新rows集合；資料多時每次input遍歷可能成本高，評估debounce或伺服器分頁，並維持可分享的篩選狀態。

計數以role=status通知，不依顏色表示結果。空輸入匹配全部；trim去頭尾空白但不把中間空白拆成多關鍵字，若要AND/OR需定義規則並測試。

## 參考資料

- [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden)
- [input event](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event)
- [String.includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)
- [原始參考入口 1](https://blog.gtwang.org/web-development/light-javascript-table-filter-tutorial/)
