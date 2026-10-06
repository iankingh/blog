---
title: "JavaScript JSON 下拉選單：解析、選項與選取結果"
date: 2021-03-16T10:04:40+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
description: "保留機構清單選取情境，補上 JSON 格式檢查、預設選項及安全渲染。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留機構清單選取情境，補上 JSON 格式檢查、預設選項及安全渲染。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 完整頁面

原資料是當時銀行清單，可能有拼字與現行名稱差異；這裡用虛構資料說明操作，不當權威名單。

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>JSON 選單</title>
<label>選擇機構 <select id="bank"><option value="">請選擇</option></select></label>
<p id="result" role="status">尚未選擇</p>
<script>
const raw = '[{"code":"001","name":"營火機構"},{"code":"002","name":"山城機構"}]';
const select = document.querySelector('#bank');
const result = document.querySelector('#result');
try {
  const records = JSON.parse(raw);
  if (!Array.isArray(records) || !records.every(x => x && typeof x.code === 'string' && typeof x.name === 'string')) {
    throw new Error('清單格式不正確');
  }
  for (const record of records) {
    const option = document.createElement('option');
    option.value = record.code;
    option.textContent = record.name;
    select.append(option);
  }
  select.addEventListener('change', () => {
    result.textContent = select.value ? `已選：${select.value} ${select.selectedOptions[0].textContent}` : '尚未選擇';
  });
} catch (error) {
  select.disabled = true;
  result.textContent = error.message;
}
</script></html>
```

初始尚未選擇；選山城應為已選：002 山城機構。把raw改成`{}`應停用選單並顯示格式錯誤，無效JSON則進catch。

## 限制與維護

JSON是資料格式，不使用eval解析。選項名稱可變，value用穩定程式碼；後端仍要驗證程式碼可用與許可權，使用者可改DOM。大量選項需要搜尋／分頁控制與a11y評估，原超長清單不適合拿來堆積範例篇幅。

這個原生版本不依賴jQuery；若維護原jQuery3.4專案，保留資料契約並用相容且受支援的庫版本，不能只換CDN就算遷移完成。

## 查核範圍

本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
- [select](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
- [selectedOptions](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/selectedOptions)
