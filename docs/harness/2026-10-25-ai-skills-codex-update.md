# AI Skills 標題、用途介紹與 Codex 補充

## 需求與範圍

- 使用者已確認：標題改為「AI Skills：專案與全域技能目錄」；新增用途、流程與三個例子；兩張目錄表補 OpenAI Codex。
- 保留文章路徑、原始 date、精選順序、寬表格及其餘原文。原稿快照不變，新增內容明確標示。
- 同步 lastmod、摘要、逐篇檢核清單與 README；不搬動或安裝技能，不修改工具設定，不提交、推送或部署。
- 延續前輪所有未提交變更；起始來源仍為 master／3704c1695f9bc4df2c44d657805e742a11ab0e53。

## 驗收

| 案例 | 預期結果 | 證據 | 狀態 |
| --- | --- | --- | --- |
| 改名與保留 | 新標題出現在首頁、文章及搜尋；網址、date、featuredOrder 與原稿快照不變 | 本輪匯入 JSON；瀏覽器首頁、H1 與搜尋一筆結果均為新標題 | 通過 |
| 用途介紹 | 定義、三階段流程、審查／測試／匯入三例、Skills 與常駐指令及單次 Prompt 的差別 | 新增段落、桌面／手機介紹截圖，定義粗體正常渲染 | 通過 |
| Codex | 兩表均有明確新增標記，正確的專案／個人路徑與觸發方式；舊路徑分開註記 | 官方文件、匯入 JSON 與兩列渲染內容 | 通過 |
| 來源完整 | 去掉明確新增的內容後與原稿正文相同；三個原始 code block 不變，無關檔案不改 | 本輪匯入 JSON；原稿 SHA-256 不變，132 筆其他紀錄不變 | 通過 |
| 網站與瀏覽器 | 9 項檢查通過，133 篇／14 頁尾頁 3 篇；1440／390px 可讀且無頁面水平溢位 | preview report 9 項通過、瀏覽器 JSON 與截圖 | 通過 |

## 當前狀態與交班

- 狀態：內容及桌面／手機驗收完成；文件收尾後的最終網站結果以文末 final report 的實際狀態為準。
- 已完成：改名、用途介紹、Codex 兩列與歷史路徑補充，lastmod／摘要／清單／README 同步，原稿及前輪變更比對、9 項網站檢查、桌面／手機與搜尋驗收。
- 起始工作內容快照：`/tmp/blog-ai-skills-codex-baseline-20261025/`，用於確認不覆蓋前輪未提交工作。
- 下一步：使用者可閱讀更新後的本機文章；提交、推送與部署另依要求處理。

## 官方依據與驗證界線

- [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)：原 Codex skills 文件入口已導向此官方頁；本輪依其 Where Codex loads local skills 與 How ChatGPT and Codex use skills 小節整理 `.agents/skills`、`~/.agents/skills`、逐層發現與 CLI／IDE 的 `/skills`／`$` 呼叫。
- [OpenAI：Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)：較早範例使用 `~/.codex/skills/setup-demo-app/SKILL.md`；只作歷史路徑來源，不推定目前所有版本的相容性。
- 本輪只更動部落格內容，未登入 AI 產品、未安裝或實測技能載入。範例為用途說明，不建立可執行技能或執行三種工作流。
- 本機工具版本沿用前輪：Hugo Extended 0.168.0、Node 26.12.1、Python 3.13.17；未重現 CI 固定 Hugo 0.167.0／Node 24.22.1，不將本機結果等同 CI。

## 本輪驗證與瀏覽器回饋

- 原文比對：`docs/verification/ai-skills-codex-import-2026-10-25.json`。明確新增的導讀、表格說明與 Codex 列不混算成原稿；移除它們後正文與快照相同，三個原始範例完全不變。
- 原稿 SHA-256：`4b2c88213f7433b38094ecb3ce889cd4ac2945ac5ad3a440dfeebc891b55a24a`。舊標題保留於原稿快照，文章新標題是本次使用者明確授權的修訂。
- 瀏覽器前：`/private/tmp/blog-ai-skills-codex-browser-20261025/report.json`，9 項通過且 source_unchanged 為 true。
- 初次桌面截圖發現新定義句的粗體結束標記緊接中文標點及正文，導致 `**` 原樣顯示；將句號移至粗體外後重新建置。修正後在手機 DOM 確認 strong 的文字正確，原稿完全不受影響。
- 修正後：`/private/tmp/blog-ai-skills-codex-preview-20261025/report.json`，9 項通過且來源未變；133 篇、14 頁尾頁 3 篇及 361 個 HTML 的連結／安全檢查通過。
- 瀏覽器：`docs/verification/ai-skills-codex-browser-2026-10-25.json`。桌面 1440×1000／手機 390×844；首頁三張精選，新標題第一；搜尋完整新標題命中一篇；文章兩表均含 Codex。頁面寬度與 viewport 一致，手機表格可見寬 314px、內容寬 1171px，ArrowRight 使表格捲動 40px、頁面 scrollX 仍為 0。
- 截圖：`/tmp/blog-ai-skills-codex-desktop.png`、`/tmp/blog-ai-skills-codex-mobile.png`、`/tmp/blog-ai-skills-codex-intro-desktop.png`、`/tmp/blog-ai-skills-codex-intro-mobile.png`、`/tmp/blog-ai-skills-codex-table-mobile.png`、`/tmp/blog-ai-skills-codex-home-desktop.png`、`/tmp/blog-ai-skills-codex-home-mobile.png`。
- 文件收尾後最終命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-ai-skills-codex-final-20261025`；以 `/private/tmp/blog-ai-skills-codex-final-20261025/report.json` 的 status 與 source_unchanged 為準。前輪報告只代表前輪版本。
- 預覽沿用僅綁定 loopback 的 `http://127.0.0.1:1316/blog/post/ai-skills-directories/`；viewport 已還原，保留文章分頁。只更動部落格內容及紀錄，未安裝／搬動任何技能或改工具設定。

## 提交與推送（2026-10-25）

- 使用者已明確要求依 git-commit-content 提交並 push；取代前述「不提交、推送」的本機交付限制。
- 範圍：本次新增 AI Skills 筆記及 Codex／用途補充、首頁精選排序、文章可選寬表格、AI 工具失效與重複連結清理，以及原稿快照、查核與瀏覽器證據。開始提交時暫存區為空，所有待提交檔案均屬本次對話範圍。
- 目標：沿用目前 master 分支，推送 origin/master；既有 workflow 會因 master push 自動執行部署，不額外手動啟動發布流程。
- 提交訊息：`feat: 新增 AI Skills 置頂筆記並清理工具連結`。
- 提交前網站命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-ai-skills-precommit-20261025`；以 `/private/tmp/blog-ai-skills-precommit-20261025/report.json` 的實際 status、各步結果與 source_unchanged 為準。
- 本次沒有再次更動網站內容、樣式或技術範例；瀏覽器證據及未實測範圍沿用上述最終內容版本，部署結果需依 GitHub 當次工作流程另外判讀。
