---
title: "列印隱藏按鈕：CSS print media 與預覽確認"
date: 2021-03-16T09:51:39+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
description: "以有效 HTML 與列印樣式取代不存在的 div media 屬性，補上列印預覽驗證。"
lastmod: 2026-10-07T00:01:00+08:00
---

以有效 HTML 與列印樣式取代不存在的 div media 屬性，補上列印預覽驗證。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 完整頁面

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><title>列印筆記</title>
<style>
@media print {
  .no-print { display: none !important; }
  body { color: #000; background: #fff; }
}
</style>
<h1>任務報表</h1><p>今天完成兩項任務。</p>
<button id="print" class="no-print">列印</button>
<script>document.querySelector('#print').addEventListener('click', () => window.print());</script>
</html>
```

按列印或Ctrl/Cmd+P，預覽應有標題與段落、沒有按鈕；關閉預覽後按鈕仍在網頁。`.no-print`樣式只在print媒體生效，不須在列印前後手動刪DOM。

## 常見問題

`<div media="print">`不會控制列印顯示，media屬性不是任意元素都支援。beforeprint/afterprint適合需要更新特殊元件的情況，單純隱藏先用CSS；print是瀏覽器對話流程，不能假設程式可以無提示指定使用者印表機。

先測PDF預覽的頁面分割、表格、長連結與紙張尺寸，再測實際印表機。圖片可能仍未載完，重要內容在列印前確認；背景圖與顏色是否列印取決於瀏覽器／使用者設定，不當唯一資訊。公司的CSP若禁止inline style/script，將兩者拆外部檔並配置允許來源。

## 查核範圍

本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [CSS printing](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Printing)
- [window.print](https://developer.mozilla.org/en-US/docs/Web/API/Window/print)

### 原始筆記保留的來源

- [在列印時不顯示列印按鈕 @ 柯佳思吃吃吃 :: 痞客邦 :: (pixnet.net)](https://awpluway.pixnet.net/blog/post/361202835)
