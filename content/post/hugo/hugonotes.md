---
title: "Hugo 基礎：建立文章、圖片與本地建置"
date: 2020-04-21T22:29:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
description: "從文章與圖片到子目錄預覽，建立可重現的 Hugo 內容維護與建置流程。"
lastmod: 2026-11-27T07:35:30+08:00
---

從文章與圖片到子目錄預覽，建立可重現的 Hugo 內容維護與建置流程。

<!--more-->

適用：Hugo Extended 與本站 RPG 版面。原文的 TOML／舊設定保留為歷史對照，實際以 config.yaml 及部署固定版本為準。

## 使用本站

取得本站原始碼後，用 `hugo version` 核對 README 與 workflow 指定的 Extended 版本。從儲存庫根目錄執行預覽或建置：

```bash
hugo server --bind 127.0.0.1 --port 1315
hugo --minify --destination /tmp/blog-build-check
```

網址依終端顯示，本站含`/blog/`。正式建置不含draft:true；-D僅用於草稿預覽。public是Hugo預設建置輸出，已由Git忽略，可重新產生。正式部署使用暫存產物發布至gh-pages。

## 移除主題前，先比對建置產物

本站的 RPG 首頁早已使用自己的版型，但舊版搜尋索引 `/blog/searchindexes.xml` 仍由 NexT 主題產生。在測試副本裡只刪掉主題，Hugo 會因為找不到設定指定的主題而停止。連同 `theme` 設定一起移除後，首頁和目前使用的 `/blog/search-index.json` 都能正常產生，舊的 XML 索引卻消失了。只打開首頁，很容易漏掉這個差異。

這次用相同的文章和 Hugo 版本，把改動前後的網站各自建置到新的空目錄。先比對輸出檔案清單，找出消失的網址，再比對文章 HTML、搜尋索引的標題與網址，以及程式碼區塊的輸出。本站最後保留 XML 索引模板、上游授權和程式碼渲染方式，才移除主題子模組及 CI 的下載步驟。乾淨副本可以直接用 Hugo Extended 建置，兩次產生的 388 個 HTML 檔案內容完全相同。

### 用日期整理維護紀錄

每次調整建置流程，我會在 `docs/harness/` 用 `YYYY-MM-DD-主題.md` 留一份紀錄。例如這次是 `2026-11-26-standalone-hugo.md`，在檔案清單按名稱排序，就能依日期找到當時的改動。紀錄寫下要保留的網址、重現用的命令、實際結果與測試版本。下次升級 Hugo 時，可以用同一組案例重跑。

新增紀錄時從 `task-template.md` 複製；整理舊檔時沿用原紀錄日期，並同步更新 README 和文章檢核清單裡的引用。歷史驗證輸出若列出當時的 Git 路徑，則保留原值，方便對照當時的提交。

## 新站與文章

新站可`hugo new site myblog`，再安裝相容主題、配置theme與baseURL。本站新文章用`hugo new content post/topic/new-note.md`，檢查archetype產生的front matter：

```yaml
title: "具體的技術主題"
date: 2026-10-06T12:00:00+08:00
lastmod: 2026-10-06T12:00:00+08:00
draft: true
description: "說明用途與讀者能完成的事。"
categories: ["筆記"]
tags: ["Git"]
```

date記原發布時間，lastmod僅在實際修訂時更新，不能為了看起來新而改原date。本站任務列表用lastmod排序與顯示，每頁10篇、每列最多2篇。

## 圖片與內部連結

static/images/demo.png對映為images/demo.png，不在網址加/static。baseURL有/blog時優先用Hugo的ref／資源處理以配合部署；本站Markdown圖片render hook處理根路徑的站點字首。圖片必須有描述性alt，純裝飾由版面明確決定空alt。

程式碼用有語言fence，如bash/java/vue，不把原始script放文章HTML。內部文章使用ref，檔案路徑不變即保持既有URL。建置成功後還需查連結、資源、搜尋索引與手機排版。

原`hchoco`是拼字錯誤；Windows安裝可按Hugo官方方式選hugo-extended，package來源與版本另核對，不任意全域性升級造成CI差異。

## 參考資料

- [Hugo安裝](https://gohugo.io/installation/)
- [New content](https://gohugo.io/commands/hugo_new_content/)
- [Static files](https://gohugo.io/getting-started/directory-structure/)
- [Front matter](https://gohugo.io/content-management/front-matter/)
- [本站維護與驗收紀錄](https://github.com/iankingh/blog/tree/main/docs/harness)
- [右上角github 貓 GitHub Corners](https://tholman.com/github-corners/#)
- [使用Github部署Hugo靜態網站](https://kira5033.github.io/2019/05/%E4%BD%BF%E7%94%A8github%E9%83%A8%E7%BD%B2hugo%E9%9D%9C%E6%85%8B%E7%B6%B2%E7%AB%99/)
- [hugo搭建靜態部落格 | 生信筆記](https://www.bioinfo-scrounger.com/archives/809/)
- [使用Hugo搭建部落格系統 - XniLe - Ops 2.0](https://blog.dianduidian.com/post/%E4%BD%BF%E7%94%A8hugo%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E7%B3%BB%E7%BB%9F/)
- [原始參考入口 1](https://hugo-next.eu.org)
