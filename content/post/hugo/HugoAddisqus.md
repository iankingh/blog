---
title: "Hugo Disqus：識別碼、本機停用與留言整合"
date: 2020-05-08T22:29:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
description: "補上穩定討論識別碼與動態載入限制，修正為本機啟用留言的錯誤建議。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上穩定討論識別碼與動態載入限制，修正為本機啟用留言的錯誤建議。

<!--more-->

適用：Hugo現行Extended版本與本站NexT版面覆寫。原文的TOML／舊設定保留為歷史對照，實際以config.yaml及部署固定版本為準。

## 設定與主題差異

先在Disqus建立站點取得shortname。通用Hugo內建模板使用services.disqus.shortname；本站NexT設定及自訂rpg-disqus載入器可能讀取不同params，先從config.yaml與partial核對，不同主題不必同一key。

一般Hugo設定示意：

```yaml
services:
  disqus:
    shortname: your-site-shortname
```

在自訂版面用Hugo內建Disqus模板或本站既有partial，擇一。不要在文章再插一個embed script造成重複thread。實際本文只沿用現有服務，不建立新shortname。

## 討論識別

每篇頁面的identifier與canonical URL需穩定，改標題或主題不能改成另一個討論。本站留言板有固定disqusIdentifier，用於避免討論分裂；文章以自己的穩定路徑設定，不讓所有文章共用同一個identifier。

若採官方JavaScript接線，配置`this.page.url`及`this.page.identifier`要在載入embed前完成，並使用正式HTTPS canonical URL。SPA導頁另按Disqus的resetAPI處理，Hugo一般整頁導航不用做SPA reset。

## 本機與正式驗證

loopback主機停用Disqus，避免把localhost建成正式討論。本文本機只驗證容器、載入狀態與說明，不發測試留言。正式站臺讀既有討論、檢查Network與Console及CSP來源；ad blocker或第三方cookie策略可能使載入失敗，應有可理解的提示與重試。

Disqus為外部服務，停用JS、斷網或指令碼被擋時文章仍應能閱讀。管理員稽核、通知及資料處理政策由站點設定維護，不把賬號管理token放前端。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Hugo services](https://gohugo.io/configuration/services/)
- [Disqus configuration](https://help.disqus.com/en/articles/1717084-javascript-configuration-variables)
- [Disqus localhost](https://help.disqus.com/en/articles/1717163-troubleshooting-disqus-on-localhost)

### 原始筆記保留的來源

- [Hugo 加入 Disqus 整合性留言管理系統](https://coreychen71.github.io/posts/2019-05/hugoadddisqus/)
- [給Hugo新增disqus評論服務 - Marvin's Blog【程式人生】](https://zh4ui.net/post/2017-04-20-hugo-with-disqus/)
- [為你部落格新增disqus評論系統 | 23.9K | Vineo](https://vineo.cn/config-disqus.html)
