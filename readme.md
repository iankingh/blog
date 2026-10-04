# ianhuang 的技術筆記部落格

這是 `https://iankingh.github.io/blog/` 的 Hugo 原始碼，內容以繁體中文技術筆記為主，使用
[Hugo NexT](https://github.com/hugo-next/hugo-theme-next) 作為基礎，並以站點版面覆寫統一呈現 RPG 冒險面板。

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

### Markdown 原始 HTML 信任邊界

`config.yaml` 將 Goldmark 的 `renderer.unsafe` 設為 `true`，因為既有文章有
刻意撰寫的 HTML 範例與排版（例如換行、嵌入 HTML 文件及 Vue/Angular 範本）。
這會讓 Markdown 中的原始 HTML 原樣進入已發布頁面，可能包含可執行的
JavaScript；因此只有作者與經審核、可信任的貢獻者可以撰寫或修改發布內容。
不得直接發布未審查的使用者提交內容、外部匯入內容或不可信的 Pull Request
內容。若要開放不可信作者投稿，必須先移除或適當消毒原始 HTML，再考慮關閉
此設定並檢查既有文章的顯示效果。

全站使用共用的 RPG 冒險面板，包括首頁、關於頁、文章、分類、標籤、歸檔、分頁與 404 頁：

- `layouts/home.html`：角色卡、技能入口、每頁 8 篇的任務日誌與全站搜尋資料。
- `layouts/character.html`：關於頁的角色檔案、主要技能、技能紀錄與寫作里程碑；文字內容仍由 `content/about.md` 維護。
- `layouts/baseof.html`：文章及列表頁共用的頁首、角色側欄與搜尋。
- `layouts/page.html`：文章閱讀面板、可收合目錄、分類標籤、相鄰文章與留言。
- `layouts/section.html`、`layouts/term.html`、`layouts/taxonomy.html`：文章列表、分類與技能標籤圖鑑。
- `layouts/archives/section.html`、`layouts/404.html`：依年份整理的冒險歷程與迷途頁面。
- `layouts/_partials/rpg/`：共用頁首、導覽、搜尋、頁尾及主題切換。
- `static/css/rpg-home.css`、`static/js/rpg-home.js`：首頁樣式、搜尋視窗及手機選單。
- `static/css/rpg-pages.css`、`static/js/rpg-article.js`：全站列表與文章排版、程式碼複製；圖片原生延遲載入，表格與程式碼可水平捲動。
- `static/js/rpg-theme.js`、`static/css/rpg-theme.css`：全站右上角的黑／白版切換，預設白色；使用獨立的儲存鍵記住選擇，儲存功能被停用時仍可切換。
- `static/images/rpg-camp.svg`：像素營地插畫，無需外部圖片服務。
- 角色等級依已發布文章數計算，每 10 篇升一級；技能入口依標籤文章數排序。
- 搜尋支援標題、標籤與摘要，按 `/` 開啟、`Esc` 關閉；草稿不會出現在正式建置的首頁與搜尋中。

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
