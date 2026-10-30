# npm 鎖檔省略 registry resolved 設定筆記

## 需求與範圍

- 使用者要求將 `omit-lockfile-registry-resolved=true` 寫成一篇繁體中文 Blog 筆記。
- 新增 npm 主題文章，說明 `.npmrc` 設定、鎖檔差異、適用情境、既有鎖檔更新與排錯；同步逐篇清單及新增紀錄。
- 依 npm 官方文件查核，另用隔離專案確認實際行為；不將設定套用到本站。
- 保留開工前未提交的 `content/post/other/obsidian-pele.md`、`docs/note-review.json`、`docs/note-review.md` 及未追蹤的 `docs/harness/pele-video-origin-2026-10-26.md`；共用清單與報告僅追加本次內容。
- 不提交、推送或部署；不修改主題、版面、安全設定與既有文章。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 官方定義與設定範圍 | 清楚說明 npm 選項、預設 false、registry 依賴及重新查詢成本 | npm config／npmrc／package-lock.json／npm install／npm ci 官方文件；查核日期 2026-10-30 | 通過 |
| 開關與既有鎖檔 | true 省略 registry resolved，保留版本與 integrity；無需刪鎖檔 | `docs/verification/npm-omit-lockfile-results-2026-10-30.json`；實際鎖檔在下列暫存目錄 | 通過 |
| 安裝與邊界 | 省略 resolved 後可 npm ci；明確 URL 依賴保留來源；完整性錯誤仍失敗 | 同上，8 項斷言；`integrity-mismatch-rejected` 預期退出碼 1 且含 EINTEGRITY | 通過 |
| 網站基準 | 文章清單、建置、搜尋、分頁與安全檢查通過 | 首輪 `blog-harness-v4w22x0z/report.json` 全部 10 項通過，來源未變；文件收尾另執行下列最終命令 | 首輪通過；最終以 report 為準 |

## 當前狀態與交班

- 狀態：文章、查核清單與隔離案例完成；最終網站結果以收尾 report 的 status 為準。
- 來源：master，`85b5275b2f2989e38c11494bbc5d5ee94d9d208f`；開工差異如上。
- 新增文章 `content/post/node/npm-omit-lockfile-registry-resolved.md`；已同步 JSON、整理報告與兩處目前篇數，總數為 135。沒有修改既有文章、主題、版面或專案 npm 設定。
- 透過開工快照核對：Pele 文章與前輪任務紀錄逐位元相同；原 JSON 的全部紀錄值保持不變，只新增一筆；整理報告完整保留原前綴後追加本次紀錄。
- 環境：Node.js 26.13.0、npm 11.20.0、Hugo Extended 0.168.0；部署 workflow 固定 0.167.0，本機實際版本另列。
- 官方來源：
  - https://docs.npmjs.com/cli/v11/using-npm/config/#omit-lockfile-registry-resolved
  - https://docs.npmjs.com/cli/v11/configuring-npm/npmrc/
  - https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json/
  - https://docs.npmjs.com/cli/v11/commands/npm-install/
  - https://docs.npmjs.com/cli/v11/commands/npm-ci/
- 來源透過 web.run 成功讀取；工具未提供 HTTP 狀態碼。未測公司 Nexus／Artifactory、認證、Git 依賴或其他 npm 版本。
- npm 案例證據：`/private/tmp/blog-npm-lockfile-note-20261030/`。`check.py` 建立臨時 HTTP registry、兩個 tarball（registry 依賴與明確 URL 依賴），使用空白 user/global config，僅連 loopback；不使用外部套件或安裝腳本。`default-lock.json`／`omitted-lock.json` 保存前後差異，`logs/` 保存全部 npm 命令輸出。
- 最後一輪使用獨立的 `project-v3` 與 `v3-*` 新快取，`npm ci` 的 HTTP 請求證明查詢新 registry 並取得新 tarball，鎖檔位元內容不變。錯誤雜湊案例在空白快取下仍以 EINTEGRITY 失敗。
- 診斷紀錄：首次啟動 loopback server 被沙箱禁止，取得執行工具授權後完成。初版案例誤以為 false 加上 package-lock-only 會補回既有 resolved，實際未補回，已修正測試期待；文章未提供此還原承諾。後來另用全新快取重跑，排除前輪快取的疑慮，8 項斷言皆通過。
- 首輪網站證據：`/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-v4w22x0z/report.json`，status 為 passed，10 項通過且來源指紋一致。
- 文件收尾最終命令：`python3 .github/scripts/verify-blog.py --output /private/tmp/blog-npm-note-final-20261030`；結果與各步日誌在 `/private/tmp/blog-npm-note-final-20261030/report.json` 及 `logs/`。此路徑預先記錄，是否成功須直接核對 report，不能從本段推定。
- 限制：npm 案例是本機合成 registry，未測公司 Nexus／Artifactory、認證、Git 依賴、其他 npm 版本或安裝效能；本機 Hugo 0.168.0，未另以 CI 固定的 0.167.0 建置。僅新增文章，未改版面與互動，因此沒有另做瀏覽器外觀驗收；既有互動測試由網站入口執行。未重跑其他教學、未提交、推送或部署。暫存完整日誌可能由系統清除，npm 摘要結果已另存入版本控制範圍。
- 下一步：核對最終 report 為 passed 後交付；使用者若另要求發布，再處理提交與部署。
