# ianhuang 的技術筆記部落格

這是 `https://iankingh.github.io/blog/` 的 Hugo 原始碼，內容以繁體中文技術筆記為主，使用
[Hugo NexT](https://github.com/hugo-next/hugo-theme-next) 主題的 Gemini 配色方案。

## 專案關係

- 本儲存庫的 `master` 分支保存網站設定、文章與版面覆寫。
- `themes/hugo-theme-next/` 是上游 Hugo NexT 主題的 Git submodule。
- `public/` 是同一個 `iankingh/blog` 儲存庫 `gh-pages` 分支的 Git submodule，僅保留既有的發布快照；目前正式部署不會寫入它。
- [`iankingh/hugo-theme-next-starter`](https://github.com/iankingh/hugo-theme-next-starter) 是可重用的主題範例，不是此站的部署來源。
- [`iankingh/iankingh.github.io`](https://github.com/iankingh/iankingh.github.io) 的根頁面會將瀏覽器導向本部落格。
- [`iankingh/iankingh`](https://github.com/iankingh/iankingh) 是 GitHub 個人檔案 README，並非網站建置的一部分。

## 環境需求

- Git
- Hugo **Extended 0.146.0 以上**（目前部署工作流程固定使用 `0.164.0`）

最低版本來自目前主題的 `theme.toml`。建議本機使用與
`.github/workflows/deploy.yml` 相同的 Hugo Extended 版本。

## 取得原始碼

```bash
git clone --recurse-submodules https://github.com/iankingh/blog.git
cd blog
```

若已經複製但尚未取得 submodules：

```bash
git submodule update --init --recursive
```

這會同時取得主題與 `public/` 所記錄的發布快照。

## 預覽與建置

```bash
# 包含草稿的本機預覽
hugo server -D
```

網站的 `baseURL` 含有 `/blog/`，預覽網址通常是
`http://localhost:1313/blog/`；請以 Hugo 啟動時顯示的網址為準。

```bash
# 與自動部署相同的壓縮建置；輸出到獨立目錄以免改動 public submodule
hugo --minify --destination .local-public

# 驗證完成後移除本機輸出
rm -rf .local-public
```

直接執行 `hugo` 會把預設輸出寫到 `public/`。因為該路徑本身是 Git
submodule，這會改動其工作目錄；一般維護與部署不需要提交這些輸出。

## 內容與設定

- `config.yaml`：Hugo 與 NexT 設定，包括 `baseURL`、語言、選單、搜尋及第三方整合。
- `content/post/`：依 Java、Spring、Vue、Docker、Git 等主題分類的文章。
- `content/about.md`：關於頁面。
- `archetypes/default.md`：新文章的 front matter 與內容範本。
- `layouts/`：相對於主題的站點專用版面與 partial 覆寫。
- `static/`：圖片、CSS、JavaScript 等直接複製的靜態資源。
- `i18n/zh-tw.yaml`：繁體中文翻譯覆寫。

建立文章：

```bash
hugo new content/post/<分類>/<文章名稱>.md
```

新檔預設為草稿；完成後再將 front matter 的 `draft` 改為 `false`。

## 部署

推送至 `master` 後，`.github/workflows/deploy.yml` 會：

1. 以 recursive submodules 取出原始碼；
2. 安裝 Hugo Extended `0.164.0`；
3. 執行 `hugo --minify`；
4. 以 `peaceiris/actions-gh-pages` 將結果發布到同一儲存庫的 `gh-pages` 分支。

工作流程也可由 GitHub Actions 頁面手動執行。它需要儲存庫授予
`contents: write`，不會更新或提交本機 `public/` submodule。

## Submodule 維護

日常同步至儲存庫記錄的版本：

```bash
git submodule update --init --recursive
```

升級主題時，請在 `themes/hugo-theme-next/` 選定並測試明確的 release 或
commit，再由本儲存庫提交新的 submodule pointer。不要在 `public/` 內維護
文章或手動部署內容；`gh-pages` 由工作流程管理。

## 已知注意事項

- `config.yaml` 內含留言、分析、搜尋等可選整合；啟用前應逐項填入自己的服務設定。
- 本儲存庫未提供授權檔，不能由此 README 推定內容或程式碼的再利用授權。
- 主題本身有獨立的 README 與授權，且其授權不會自動涵蓋本站文章。
