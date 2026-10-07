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
lastmod: 2026-10-07T20:50:40+08:00
---

從文章與圖片到子目錄預覽，建立可重現的 Hugo 內容維護與建置流程。

<!--more-->

適用：Hugo現行Extended版本與本站NexT版面覆寫。原文的TOML／舊設定保留為歷史對照，實際以config.yaml及部署固定版本為準。

## 使用本站

先`hugo version`核對README及workflow要求的Extended版本，Git submodule需初始化。預覽與輸出分開：

```bash
git submodule update --init --recursive
hugo server --bind 127.0.0.1 --port 1315
hugo --minify --destination /tmp/blog-build-check
```

網址依終端顯示，本站含`/blog/`。正式建置不含draft:true；-D僅用於草稿預覽。本站public是gh-pages的submodule，測試輸出別直接寫public。

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
- [右上角github 貓 GitHub Corners](https://tholman.com/github-corners/#)
- [使用Github部署Hugo靜態網站](https://kira5033.github.io/2019/05/%E4%BD%BF%E7%94%A8github%E9%83%A8%E7%BD%B2hugo%E9%9D%9C%E6%85%8B%E7%B6%B2%E7%AB%99/)
- [hugo搭建靜態部落格 | 生信筆記](https://www.bioinfo-scrounger.com/archives/809/)
- [使用Hugo搭建部落格系統 - XniLe - Ops 2.0](https://blog.dianduidian.com/post/%E4%BD%BF%E7%94%A8hugo%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E7%B3%BB%E7%BB%9F/)
- [原始參考入口 1](https://hugo-next.eu.org)
