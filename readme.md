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
- Hugo **Extended 0.167.0 以上**（目前部署工作流程固定使用 `0.167.0`）

此版本包含文章渲染與主題檔案存取的安全修正。建議本機使用與
`.github/workflows/deploy.yml` 相同的 Hugo Extended 版本。
舊版 Hugo 會在建置時報錯，避免誤用尚未修補的版本發布。

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
- `content/guestbook.md`：公開想法留言板，獨立於技術筆記篇數與 EXP；留言由既有 Disqus 保存。
- `content/projects.md`：本站作品案例，獨立於技術筆記數與 EXP；Markdown 圖片使用實際首頁截圖。
- `archetypes/default.md`：新文章的 front matter 與內容範本。
- `layouts/`：相對於主題的站點專用版面與 partial 覆寫。
- `static/`：圖片、CSS、JavaScript 等直接複製的靜態資源。
- `i18n/zh-tw.yaml`：繁體中文翻譯覆寫。

### Markdown 原始 HTML 信任邊界

`config.yaml` 將 Goldmark 的 `renderer.unsafe` 設為 `false`。HTML、JavaScript
及 Vue/Angular 範例必須放在 fenced code block 或反引號內，讓讀者看到程式碼，
而不會執行它；一般排版使用 Markdown。既有已發布文章的原始 HTML 已轉換。

共用頁首在載入資源前套用 CSP，禁止內嵌 JavaScript、`eval`、外掛物件與
表單送出，並限制脚本來源。語法高亮仍需內嵌 CSS，因此只在 `style-src`
保留 `'unsafe-inline'`。GitHub Pages 不支援自訂 HTTP 標頭，這裡使用 CSP meta；
它無法提供 `frame-ancestors` 防護，若改用能設定 HTTP 標頭的主機，再補上該指令。

Google Analytics 與 Disqus 使用獨立腳本載入，保留既有服務；本機預覽不載入
Analytics，loopback 主機不載入 Disqus。不蒜子計數已停用。新增外部服務時，需
同步審查 CSP 的來源清單。文章與主題來源仍需審核，CSP 不會取代內容審查。

全站使用共用的 RPG 冒險面板，包括首頁、關於頁、文章、分類、標籤、歸檔、分頁與 404 頁：

- `layouts/home.html`：全端工程師／AI 規劃師介紹、GitHub 入口與每頁 8 篇的任務日誌。
- `layouts/character.html`：關於頁的角色檔案、主要技能、技能紀錄與寫作里程碑；文字內容仍由 `content/about.md` 維護。
- `layouts/baseof.html`：文章及列表頁共用的頁首、角色側欄與搜尋。
- `layouts/page.html`：文章閱讀面板、可收合目錄、分類標籤、相鄰文章與留言。
- `layouts/guestbook.html`、`static/js/rpg-guestbook.js`：想法營地與 Disqus 載入狀態。留言板使用固定的 `disqusIdentifier`，請勿隨意更換，以免分離既有討論；本機只預覽版面，正式站台提供留言。留言區使用固定淺色底，避免切換網站主題時影響正在編輯的留言。
- `layouts/section.html`、`layouts/term.html`、`layouts/taxonomy.html`：文章列表、分類與技能標籤列表。
- `layouts/archives/section.html`、`layouts/404.html`：依年份整理的冒險歷程與迷途頁面。
- `layouts/_partials/rpg/`：共用頁首、導覽、搜尋、頁尾及主題切換；右上角保留連至個人 GitHub 的 Octocat，使用既有 githubBanner 設定。
- `static/css/rpg-home.css`、`static/js/rpg-home.js`：首頁樣式、搜尋視窗及手機選單。
- `static/css/rpg-pages.css`、`static/js/rpg-article.js`：全站列表與文章排版、程式碼複製；圖片原生延遲載入，表格與程式碼可水平捲動。
- `static/js/rpg-theme.js`、`static/css/rpg-theme.css`：全站右上角的黑／白版切換，預設白色；使用獨立的儲存鍵記住選擇，儲存功能被停用時仍可切換。
- `static/css/rpg-portfolio.css`：作品、精選文章、專業定位與共用導覽的樣式，沿用既有 RPG 色彩。
- `static/images/rpg-camp.svg`：像素營地插畫，無需外部圖片服務。
- 角色等級依已發布文章數計算，每 10 篇升一級。技能圖鑑位於 `/skills/`，與 `/tags/` 的文章標籤分開；首頁技能數量、角色檔案和圖鑑共用技能資料，技能等級與進度顯示於角色檔案和圖鑑。
- `data/skills.json`：維護技能名稱、分組、描述及對應的文章標籤；`layouts/skills/section.html` 呈現 Lv. 與 EXP 進度條。每篇相關公開筆記累積 1 EXP（多個匹配標籤只計一次），每 10 EXP 升一級；進度條顯示距下一級的累積值。Lv. 表示筆記累積，不是專業能力評分。沒有筆記的技能仍顯示 Lv. 1、0 / 10，圖鑑可展開閱讀相關紀錄。
- `layouts/home.searchindex.json`：產生 `/blog/search-index.json`，只收錄公開技術筆記，連 `--buildDrafts` 預覽也排除草稿與作品頁。既有 `searchindexes.xml` 仍保留供 NexT 使用。
- 全文搜尋在首次開啟時才載入 JSON，同頁快取並共用載入中的請求；支援標題、標籤與正文，按 `/` 開啟、`Esc` 關閉。錯誤可重試，快速輸入或關閉重開不會顯示舊結果；結果保留精簡摘要。
- 搜尋關閉後焦點回到觸發入口，手機導覽內按 `Esc` 關閉則回到選單按鈕。

### 精選筆記與更新時間

文章使用 Hugo 的 `description` 作為文章卡片、搜尋與分享摘要。只有實際修訂後才增加 `lastmod`，文章頁同時保留原始 `date` 與更新日期。`featuredOrder` 為選填正整數，決定 Java 技能卡中的精選顯示順序；不要為一般文章填入。

目前精選為 Java 多型、HikariPool 連線取得逾時與 DecimalFormat。Java 範例以 OpenJDK 21 驗證，重跑方式見下方驗證指令。

### 搜尋摘要與分享圖

共用 metadata 輸出標準 description、Open Graph 與 Twitter card，摘要與圖片共用來源。`params.sharingImage` 指向 1200×630 的 `static/images/ian-java-share.png`；文章可用 `images` 清單中的第一張覆蓋，空清單使用網站預設。支援 static 圖片、文章 bundle 圖片與外部 URL；外部圖不會填入未知的尺寸或 MIME。

分享圖沿用營地插畫，向量來源為 `static/images/ian-java-share.svg`。如已安裝 `sharp`，可重新產生：

```bash
node .github/scripts/create-share-card.mjs
# 也可傳入已安裝的 sharp package 絕對路徑，無需在 Hugo 專案安裝套件
node .github/scripts/create-share-card.mjs /path/to/node_modules/sharp
```

### 驗證

```bash
# 搜尋載入、快取、競態、失敗重試與焦點（Node.js，無外部套件）
node .github/scripts/check-search.cjs

# Java 21 範例；HikariCP / H2 / SLF4J JAR 的提供方式見 --help
python3 .github/scripts/check-java-notes.py --help

# 正式建置與既有安全檢查，勿輸出到 public 子模組
hugo --minify --destination .local-public
python3 .github/scripts/check-site-security.py .local-public
```

建立文章：

```bash
hugo new content/post/<分類>/<文章名稱>.md
```

新檔預設為草稿；完成後再將 front matter 的 `draft` 改為 `false`。

## 部署

推送至 `master` 後，`.github/workflows/deploy.yml` 會：

1. 唯讀的 `build` job 取出原始碼與 submodules，且不保留 Git 憑證；
2. 安裝 Hugo Extended `0.167.0`，驗證搜尋互動，再執行 `hugo --minify`；
3. 檢查產出 HTML 的 CSP、內嵌腳本與事件處理器，再上傳建置產物；
4. 獨立 `deploy` job 只下載通過檢查的產物，發布至 `gh-pages` 分支。

工作流程也可由 GitHub Actions 頁面手動執行，只有 `master` 能發布。
僅發布 job 具有 `contents: write`；不會更新或提交本機 `public/` submodule。
Actions 固定為官方 release 對應的完整 commit SHA，由 Dependabot 每週提出
更新 PR。Hugo 版本需另外檢查正式 release，升級時同步修改 workflow 與本文件。

本機可用相同的安全檢查：

```bash
python3 .github/scripts/check-site-security.py .local-public
```

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
