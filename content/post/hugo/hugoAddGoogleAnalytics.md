---
title: "Hugo GA4：正式站載入與事件確認"
date: 2021-07-22T18:37:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
description: "補上本站的本機停用行為、Measurement ID 與 GA4 的實際驗證範圍。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上本站的本機停用行為、Measurement ID 與 GA4 的實際驗證範圍。

<!--more-->

適用：Hugo現行Extended版本與本站NexT版面覆寫。原文的TOML／舊設定保留為歷史對照，實際以config.yaml及部署固定版本為準。

## GA4 與本站配置

舊Universal Analytics的UA-ID不是GA4的G-ID。建立GA4 web data stream取得Measurement ID，本站自訂模板讀params.analytics.google：

```yaml
params:
  analytics:
    google: G-MEASUREMENT_ID
```

G-MEASUREMENT_ID是佔位值，需換成自己的streamID。通用Hugo內建模板則使用services.googleAnalytics.ID，不能同時啟用兩套導致page_view重複。

## 本機與正式站

本站loopback主機不載入Analytics，因此本機看不到gtag.js是預期。正式頁面從Network檢查googletagmanager script和collect請求，核對G-ID與頁面URL，再於GA4 Realtime／DebugView檢查事件。檢查可能有資料延遲，devtools請求成功也不一定馬上顯示在標準報表。

同意策略、ad blocker、瀏覽器隱私設定或CSP會影響是否傳送，先依實際選擇確認，不強行繞過。需要consent管理時按Google檔案配置，避免把自訂cookie流程與站點政策混寫。

## 資料品質

只記必要頁面與事件，不送email、使用者姓名或敏感query到Analytics。若網站含搜尋詞或站內路徑，先確認目的與去識別化方式。SPA才需要額外處理虛擬page_view；Hugo整頁導航通常不需要重複事件。

本次確認的是本站模板與靜態產物，本地不會向GA寫事件，無法據此宣稱帳號報表已驗收。正式部署後再按上面順序進行賬號端檢查。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Hugo Analytics](https://gohugo.io/configuration/services/)
- [Google tag設定](https://developers.google.com/analytics/devguides/collection/ga4)
- [DebugView](https://support.google.com/analytics/answer/7201382)

### 原始筆記保留的來源

- [Hugo Google Analytics 模板](https://gohugo.io/templates/embedded/#google-analytics)
