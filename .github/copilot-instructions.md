# ianhuang 部落格的 Copilot 指引

本站是繁體中文 Hugo 技術筆記部落格，版面以 RPG 冒險者為主題，正式網址為 `https://iankingh.github.io/blog/`。

## 專案與建置

- 最新架構、維護方式、建置與部署說明以根目錄 `readme.md` 為準；Hugo 版本以 `.github/workflows/deploy.yml` 固定的 Extended 版本為準。
- `master` 保存網站原始碼；`themes/hugo-theme-next/` 是唯一的 Git submodule。使用 `git submodule update --init --recursive` 取得主題。
- `content/` 保存文章，`layouts/` 保存站點版面覆寫，`static/` 保存圖片、CSS 與 JavaScript。
- `public/`、`.local-public/`、`resources/_gen/` 與 `.hugo_build.lock` 為可重新產生的本機建置產物，已由 Git 忽略。
- 正式部署使用通過檢查的暫存產物發布到 `gh-pages`，完成 Pages 建置後自動建立 Tag／Release。

## 內容維護

- 保留既有文章路徑與原始發布日期 `date`；實際修改內容時更新 `lastmod`。
- 新筆記包含清楚的標題、摘要、適用情境、分類、標籤與來源；草稿完成後才設為 `draft: false`。
- 使用 Markdown 章節，程式碼區塊標明語言，內部文章連結使用 Hugo `ref`／`relref`，圖片補上合適的替代文字。
- 文末統一為一個「參考資料」區塊，官方文件在前，保留原來源；合併相同網址並保留說明。
- 技術查核與驗證證據留在 `docs/note-review.md`／JSON；文章保留與操作有關的版本及未實測限制。
- 修改筆記後同步維護逐篇清單；正式建置的內容、搜尋、連結與安全檢查方式見 `readme.md`。

## 主題維護

- 優先在本站 `layouts/` 或 `static/` 調整版面；升級主題時選定明確的 release／commit，驗證後更新子模組指標。
- 網站設定、搜尋及留言的實際行為，以 `config.yaml` 與站點覆寫為準，不依上游範例推定。
