---
title: "Hugo 程式碼高亮：Prism 與內建 Chroma"
date: 2020-04-22T22:29:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
description: "說明原 Prism 整合方式與現行 Hugo 高亮選擇，避免雙重包裝同一段程式碼。"
lastmod: 2026-10-07T20:50:40+08:00
---

說明原 Prism 整合方式與現行 Hugo 高亮選擇，避免雙重包裝同一段程式碼。

<!--more-->

適用：Hugo現行Extended版本與本站NexT版面覆寫。原文的TOML／舊設定保留為歷史對照，實際以config.yaml及部署固定版本為準。

## 先選一個高亮來源

本站使用Hugo內建Chroma與文章fence，程式碼在建置時產生高亮HTML，不需要Prism JS。原筆記採Prism瀏覽器端高亮：需下載指定語言的JS/CSS、放static或assets、在自訂head/footer partial載入，並檢查CSP是否允許。

現行Hugo關閉預設code fence高亮可用：

```yaml
markup:
  highlight:
    codeFences: false
```

這是選Prism時的設定示意，不能和本站現在的Chroma設定不加判斷一起套。舊pygmentsCodefences等頂層設定已不是建議配置路線。

## Prism 接線

在一個使用Prism的測試主題partial可載入：

```go-html-template
<link rel="stylesheet" href="{{ "css/prism.css" | relURL }}">
<script src="{{ "js/prism.js" | relURL }}" defer></script>
```

檔案對應static/css/prism.css、static/js/prism.js，Markdown的語言名稱需與下載的Prismcomponent一致。普通code fence輸出language-java等class，Prism據此選語法。資源可改用HugoPipes雜湊，改檔能更新快取。

## 驗證與限制

檢查Java／bash／Vue各一段，無JS時仍可閱讀與複製文字，手機橫向捲動不使整頁溢位。若出現兩組highlight包裝，確認render hook與codeFences，不要再靠CSS隱藏其中一組。

Prism加上執行期JS成本；Chroma在建置時處理，語言支援與樣式來源不同。不要因換高亮器就開Goldmark unsafe讓文章script執行。本站實際沿用Chroma，本次僅查核Prism替代路線，不額外安裝第二套高亮。

## 參考資料

- [Hugo高亮](https://gohugo.io/content-management/syntax-highlighting/)
- [Prism官方](https://prismjs.com/)
- [Hugo资源雜湊](https://gohugo.io/functions/resources/fingerprint/)
- [Hugo / 如何在 Hugo 中用 Prism.js 提供程式碼色彩標註 | sujj blog](https://sujingjhong.com/posts/how-to-add-prismjs-into-hugo/)
- [漂亮的程式碼語法高亮外掛Prism.js簡單使用檔案 - 嚴穎專欄 -SegmentFault 思否](https://segmentfault.com/a/1190000009122617)
