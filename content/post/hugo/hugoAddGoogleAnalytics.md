---
title: "Hugo 加入 Google Analytics"
date: 2021-07-22T18:37:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
---

## Hugo 使用 Google Analytics
<!-- 簡介 -->
<!--more-->

1. 在 Google Analytics 建立 GA4 資源，取得 `G-` 開頭的 Measurement ID。

2. 本專案的 NexT 主題覆寫模板讀取 `params.analytics.google`，在 `config.yaml` 設定：

   ```yaml
   params:
     analytics:
       google: G-MEASUREMENT_ID
   ```

3. 啟動本地伺服器後，使用瀏覽器開發者工具確認 `gtag.js` 已載入。正式環境還應確認隱私權與 Cookie 告知符合部署地區的規範。

## 參考

[Hugo Google Analytics 模板](https://gohugo.io/templates/embedded/#google-analytics)
