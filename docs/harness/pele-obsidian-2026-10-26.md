# Pele：Obsidian 使用文章與 Blog 圖表整合

## 需求與範圍

- 新增一篇繁體中文 Pele／Obsidian 使用教學，區分 Mermaid 語法、Pele 渲染器與 Obsidian 應用程式；依官方文件標示版本、操作方式、範例與排錯。
- 使用者要求安裝到目前專案；本輪將 Pele 接入 Hugo，讓文章中的 Mermaid fence 顯示圖表，保留可展開來源及載入／語法錯誤時的文字退路。
- 沿用 RPG 主題與深淺色設定；使用固定版本、同源靜態腳本，不調整 CSP 或 Goldmark unsafe，不修改主題子模組。
- 本輪新需求取代上一輪「不新增 Mermaid 渲染器」的範圍限制；Markdown 與 Mermaid 分篇、新網址及無轉址的既有結果維持。
- 不操作使用者的 Obsidian 應用程式或私人 vault，不安裝第三方 Obsidian 外掛，不提交、推送或部署。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 新文章與版本說明 | 正確說明 Obsidian 1.15.0 early access 已內建 Pele，保留官方來源，不將 npm 套件說成社群外掛 | 官方文件與[整合案例](../verification/pele-integration-2026-10-26.json)；新文搜尋完整標題命中 1 篇 | 通過 |
| 固定安裝與可重現資源 | npm lock 固定版本、保留授權，可從 npm ci 重建同源資源 | 安裝 Pele 1.10.0；離線 npm ci 與 vendor 重建成功，版本、lock 與 SHA-256 一致 | 通過 |
| 正常與多圖 | Mermaid 範例可繪成 SVG；多圖識別碼不衝突，來源可展開且逐字保留 | 7 個 Node 測試與[瀏覽器紀錄](../verification/pele-browser-2026-10-26.json)；同頁 3 張成功圖 SVG ID 無重複，原始碼以 Enter 開關 | 通過 |
| 語法錯誤／資源不可用 | 個別圖表失敗不影響其他圖；錯誤以文字顯示，來源仍可閱讀 | 瀏覽器 4 個 fixture 圖依序 rendered／error／rendered／rendered；缺 library 為 unavailable 且保留來源；移除圖表腳本也保留來源 | 通過 |
| 安全與資源範圍 | 原 CSP／unsafe 不變、無 CDN、無內嵌腳本；只有圖表文章載入 Pele | 17 個整合案例與生成安全檢查；只有 Mermaid 與 Pele 兩篇載入函式庫，惡意標籤未產生 script／image／a 或事件屬性 | 通過 |
| 主題與窄螢幕 | 深淺色圖文清楚；窄螢幕無頁面橫向溢位；來源可鍵盤操作 | 1440×1000／390×844；390 的 pageWidth 為 390、圖表寬 196，來源 summary 高 44；暗色文字 rgb(236,232,220)、底色 rgb(26,33,28) | 通過 |
| 網站基準 | `python3 .github/scripts/verify-blog.py` 全部通過；搜尋 134 篇唯一筆記，前輪新舊網址規則維持 | 預覽 report 為 passed，10 項通過且來源未變；134 篇、14 頁尾頁 4 篇、364 HTML 連結／安全通過；最終來源見下列 report | 通過，最終來源以 report 為準 |

## 當前狀態與交班

- 狀態：文章、安裝與整合、回歸案例及瀏覽器驗收完成；文件收尾後以最終 report 的實際結果為準。
- 來源 commit：`b964d03b8c9fb2816baba5b60aee4824f1b29249`，分支 `master`。
- 開始時已有上一輪 7 個未提交檔案，完整快照在 `/tmp/blog-pele-baseline-20261026/`。保留 Markdown 篇與前輪驗收紀錄；本輪只接續修改 Mermaid 篇及逐篇清單／整理報告。
- 已讀 Pele 官方 README、API、theming、compatibility、security 與 Obsidian 2026-10-22 桌面 1.15.0 early access 更新說明。
- UI/UX Pro Max 定向搜尋：`chart text alternatives`，命中 Accessibility／Alt Text；採用有意義的圖像提供文字替代的指引，保留原始碼並使用 Mermaid 的 accessibility title／description。
- npm registry 查得 Pele 1.10.0，安裝命令使用 `--ignore-scripts --no-audit --no-fund` 與獨立 `/tmp/blog-pele-npm-cache`，只安裝 1 個套件；沒有執行套件安裝腳本或操作全域環境。
- 離線重建：`npm ci --offline --ignore-scripts --no-audit --no-fund --cache /tmp/blog-pele-npm-cache`、`npm run vendor:pele` 均成功。bundle 為 709352 bytes，SHA-256 為 `dd70e44152f7d70d62fedc622f588db3f5855859b444f4d8cf274925c12f2651`，保留完整 MIT 授權；版本與雜湊在 `static/lib/pele/version.json`。
- 最近一次網站命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-pele-preview-20261026`；`/private/tmp/blog-pele-preview-20261026/report.json` 為 passed，10 項通過且 source_unchanged 為 true。
- 文件收尾後最終命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-pele-final-20261026`；以 `/private/tmp/blog-pele-final-20261026/report.json` 的實際 status、各步結果與 source_unchanged 為準；日誌在同目錄 `logs/`。
- 新增圖表檢查已納入統一入口；一般 Hugo 建置使用 vendored 檔案，不需要安裝 npm 依賴或連線 CDN。新需求的 17 個整合／來源案例證實前輪 Markdown 篇及 3 份紀錄未改、132 筆其他文章紀錄保留、所有既有原始發布日期與圖表節點／連線內容保留。
- 未測範圍：未操作或升級 Obsidian，未驗該應用程式的實際畫面／帳號權限；未測實體手機、螢幕閱讀器、全域關閉 JavaScript 或其他 Java／Spring／Vue／Angular 教學。無圖表腳本的 fixture 已驗證靜態來源退路，但不把它稱為已在瀏覽器設定全域停用 JavaScript。
- 本機 Hugo Extended 0.168.0，部署固定 0.167.0；本輪未以該部署版本重跑，Node／Python 版本在 report 日誌。
- 下一步：讀取最終 report 並交付本機文章與預覽；提交、推送或部署另依使用者要求處理。

## 證據、修正與預覽

- [17 個整合／來源案例](../verification/pele-integration-2026-10-26.json)：新文、版本、前輪未提交工作、日期與來源保留、條件載入資源、初始靜態來源退路、搜尋及新舊網址。
- [實際瀏覽器紀錄](../verification/pele-browser-2026-10-26.json)：新文章與既有 Mermaid 圖表、搜尋、SVG title／desc、主題、390px、來源鍵盤操作、多圖與失敗退路。預覽頁無 console warning／error。
- 可見畫面已透過瀏覽器工具實看：預設 620×909 閱讀區中的圖表、來源入口與旁邊說明清楚。1440／390 測試後已清除臨時 viewport 設定，主題還原為 light。另存 JPEG 在本機圖片檢視中呈空白，不列為有效截圖證據；瀏覽器 JSON 保留實際 DOM、主題、寬度與操作結果，也明確記錄此工具限制。
- 測試 fixture 只放在 `/tmp/blog-markdown-mermaid-webroot-20261026/fixtures/`，不寫入內容目錄或發布產物；涵蓋多圖、無 library 與無圖表腳本三頁。
- npm 查詢最初因 sandbox DNS 回 ENOTFOUND；取得執行權限後從官方 registry 安裝成功。沒有將初次失敗視為安裝成功。
- Node 測試首輪 6／7：SVG ID 比對誤將 `data-id` 的節點名稱也算入，檢查器已改為精確比對 `id` 屬性；同一個多圖／accessibility 案例保留，再跑 7／7，瀏覽器也確認實際 SVG IDs 無重複。沒有更改產品驗收標準。
- 瀏覽器在虛擬桌面寬度下曾有指標定位失敗，改以鍵盤操作並用 DOM／可見畫面確認；來源以 Enter 開關、主題切換及搜尋已實測。此為操作工具的失敗，不計為功能通過證據。
- 新文章預覽：`http://127.0.0.1:1327/blog/post/other/obsidian-pele/`；原 Mermaid 篇：`http://127.0.0.1:1327/blog/post/other/mermaid-flowchart/`。沿用僅綁定 loopback 的靜態伺服器，webroot 的 `blog` 連至本輪乾淨 site 產物；未推送或對外部署。

## 來源

- [Obsidian 1.15.0 Desktop early access](https://obsidian.md/changelog/2026-10-22-desktop-v1.15.0/)
- [Pele 官方儲存庫](https://github.com/obsidianmd/pele)
- [Pele API](https://pele.run/api)
- [Pele 主題](https://pele.run/theming)
- [Pele 相容性](https://pele.run/compatibility)
- [Pele 安全說明](https://pele.run/security)

## 提交與發布（2026-10-26）

- 使用者已明確要求套用 git-commit-content 技能「提交發佈」，取代前述不提交／推送／部署的本機交付限制。
- 提交範圍：本次對話的 Markdown／Mermaid 分篇與新網址、Pele／Obsidian 使用文章、Pele 固定版安裝與同源渲染、回歸檢查及維護／驗證紀錄。開始提交時暫存區為空，沒有混入其他工作。
- 目標：沿用 `master`，推送 `origin/master`；由既有 push 工作流程執行驗證、GitHub Pages 發布與對應 Tag／Release，不額外手動觸發第二次部署。
- 提交訊息：`feat!: 新增 Pele 圖表與使用筆記並調整 Markdown、Mermaid 網址`；內文列出功能與測試，BREAKING CHANGE footer 記錄兩個舊網址停用、新網址與沒有轉址的行為。
- 提交前重新核對暫存差異，執行 `python3 .github/scripts/verify-blog.py --output /tmp/blog-pele-precommit-20261026`；只有該輪 report 的實際 status、10 項檢查及 source_unchanged 才代表本輪通過，日誌在同目錄 `logs/`。
- 瀏覽器與整合案例對應的網站內容未再次修改；既有證據及 Obsidian 未實機操作的限制保留。提交後的 workflow／Pages／Release 狀態需核對本次來源 SHA，不能以先前成功的部署代替。
