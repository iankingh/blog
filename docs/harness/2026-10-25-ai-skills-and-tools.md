# Skills 置頂筆記與 AI 工具連結清理

## 需求與範圍

- 依使用者確認的計畫新增完整 Skills 筆記；原文只轉換 Markdown 格式，官方文件補充另設區塊。
- 首頁維持三張精選，順序為 Skills、Java 多型、HikariPool；DecimalFormat 排第四，仍保留 Java 技能卡入口。
- 移除 AI 工具清單中的 Phind 失效入口及 Monica、Poe、Felo 的過時或重複參考入口；保留原始發布日期及歷史查核證據。
- 更新文章檢核清單與相關說明，不修改安全設定、主題子模組，不安裝依賴，不提交、推送或部署。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 原文完整匯入 | 標題、正文、章節與範例完整，補充與原文分開 | `docs/verification/ai-skills-import-2026-10-25.json`；三個範例、全文與快照相同 | 通過 |
| 精選順序 | 首頁三張且 Skills 第一；第二頁不顯示；Java 圖鑑保留 DecimalFormat | 瀏覽器 JSON：三張精選順序、第二頁零張精選／10 張筆記卡、Java 三筆入口 | 通過 |
| 清理連結 | Phind 兩入口、Monica /home、Poe /ChatGPT、Felo /search 不再出現於 AI 工具文章 | 匯入檢查 JSON、瀏覽器四列工具與四筆參考入口 | 通過 |
| 文章數邊界 | 搜尋 133 篇，首頁與筆記共 14 頁，末頁 3 篇 | 寬表格修正後網站 report：9 項通過，361 個 HTML 的連結／安全檢查通過 | 通過 |
| 桌面／手機 | 長標題可讀，表格和程式碼可捲動，頁面不水平溢位 | `docs/verification/ai-skills-browser-2026-10-25.json`，1440／390px；手機表格實際鍵盤水平捲動 40px | 通過 |

網站基準：`python3 .github/scripts/verify-blog.py`。

## 當前狀態與交班

- 狀態：內容、來源比對、連結清理與瀏覽器驗收完成；文件收尾後的最終網站結果以文末 final report 為準。
- 起始來源：`master`，`3704c1695f9bc4df2c44d657805e742a11ab0e53`；工作目錄乾淨。
- 來源原稿：使用者在本次對話提供的全文；Markdown 格式快照將保存在 `docs/sources/ai-skills-directories-original.md`，不推定原稿發表日期。
- 已完成：新增完整原文及獨立官方文件補充；精選排序、三篇 Java 僅順序變更、AI 工具清理、逐篇清單、寬表格及相關說明；131 筆無關清單紀錄與歷史來源紀錄未變。
- 未執行：各 AI 產品的登入功能及實際技能載入、實體手機、Java／Spring／Vue／Angular 教學重跑；本輪未修改既有技術範例。軟連結只在系統暫存目錄執行，不在專案建立技能或連結。
- 下一步：閱讀本機新增文章與清理結果；提交、推送或部署另依使用者指示處理。

## 首輪驗證與修正

- `/private/tmp/blog-ai-skills-initial-20261025/report.json`：來源、搜尋互動、Python 測試、Hugo 建置與安全檢查通過；生成內容檢查失敗，不能算整輪通過。
- 失敗日誌為同目錄 `logs/generated-content.log`：檢核清單有 133 篇，但搜尋索引不足 133 篇。
- 原因：新文章只填 `date: 2026-10-25`，Hugo 依預設 UTC 解讀；台灣已跨日而 UTC 尚未跨日，導致新文章被視為 future 而排除。
- 修正：新文章 date 使用與 lastmod 相同的台灣時間戳及 `+08:00`；同步新文章 originalDate，不改站台時區、建置旗標或檢查標準。既有文章日期不變。

## 連結查核與移除依據（2026-10-25）

本次以網頁開啟工具查核；下列為本輪觀察，不覆寫 `docs/source-checks.json` 與既有紀錄。

| 原入口 | 觀察 | 處理 |
| --- | --- | --- |
| https://www.phind.com/ | 開啟回報 HTTP 404 | 移除文章中的工具列、參考連結及歷史失效說明 |
| https://www.phind.com/search?home=true | 開啟回報 HTTP 404 | 移除參考連結 |
| https://monica.im/home | 可讀，與 Monica 主入口為同一服務的額外入口 | 移除額外參考，保留 https://monica.im/ |
| https://poe.com/ChatGPT | 頁面名稱為 ChatGPT-4o-Latest_DEPRECATED，顯示 Hidden／PRIVATE | 移除過時 bot 入口，保留 https://poe.com/ |
| https://felo.ai/search | 可讀，本輪另開啟首頁確認導向此入口 | 移除重複參考，保留 https://felo.ai/ |
| https://immersivetranslate.com/ | 可讀，導向 /en/ | 保留官方主入口 |

Monica 首頁可讀，Poe 首頁導向登入畫面；未登入或提交資料。本輪只有工具入口整理，不重新比較價格、模型清單或功能品質。

## 官方文件補充與原文對照

- 原始快照僅轉換 Markdown 標題、表格、inline code 與 fenced code block；文章標題移入 front matter，正文與三個範例與快照比對相同。原稿沒有外部來源網址，官方連結均在補充區及統一參考資料新增。
- Claude Code 的技能目錄與仍相容的單檔 Commands 分開說明；Copilot 的原生 Skills 路徑、Cursor 的 Skills 與 Rules、Cascade 的 Skills 與 Memories／Rules、OpenClaw 工作區與個人目錄均依各工具文件補充。
- Agent Skills 規格處理技能格式；搜尋路徑仍由工具決定。VS Code Prompt files 以 `/` 手動呼叫，與 `#file:` 引用區分；專案 copilot-instructions.md 不是個人全域規則檔。
- 本輪實際開啟的官方來源：
  - https://code.claude.com/docs/en/skills
  - https://docs.github.com/en/copilot/concepts/customizations/agent-skills
  - https://cursor.com/docs/skills
  - https://cursor.com/docs/rules
  - https://docs.devin.ai/desktop/cascade/skills（原 Windsurf 官方入口轉址）
  - https://docs.devin.ai/desktop/cascade/memories
  - https://docs.openclaw.ai/tools/skills
  - https://agentskills.io/specification
  - https://code.visualstudio.com/docs/agent-customization/custom-instructions
  - https://code.visualstudio.com/docs/agent-customization/prompt-files

## 瀏覽器回饋與寬表格修正

- 首次手機量測雖然頁寬維持 390px，但截圖顯示四欄表被擠窄、路徑被拆成多行，不能只以「沒有頁面溢位」判為可讀。
- 使用 UI/UX Pro Max 的 `responsive table readability scroll --domain ux` 查詢，命中 Web／Responsive 的 Table Handling 指引：保留表格內水平捲動，不讓寬表格破壞頁面寬度。
- 新增可選 front matter `wideTables: true`，只在本篇啟用；文章 class 與 CSS 保留欄寬、最後說明欄至少 320px、程式碼路徑不斷行。未啟用的文章沿用原樣式，沒有放寬 Goldmark 或 CSP。
- 修正後桌面頁寬 1440px、手機頁寬 390px 均無水平溢位；手機兩表內容寬 1060／1171px、可見寬 314px，實際 ArrowRight 捲動 40px 且頁面 scrollX 維持 0。程式碼保留既有局部水平捲動。
- 瀏覽器搜尋「AI 技能目錄」找到一筆新文章；目錄連結能定位原文第一張表。測試結束已還原 viewport，保留首頁置頂預覽。

## 驗證證據與限制

- 原文與軟連結：`docs/verification/ai-skills-import-2026-10-25.json`。
- 瀏覽器：`docs/verification/ai-skills-browser-2026-10-25.json`；包含初始窄表格量測與修正後量測，最後採修正後的結果。
- 桌面首頁截圖：`/tmp/blog-ai-skills-home-desktop.png`；手機首頁：`/tmp/blog-ai-skills-home-mobile.png`。
- 文章桌面／手機截圖：`/tmp/blog-ai-skills-article-desktop.png`、`/tmp/blog-ai-skills-article-mobile.png`；寬表格修正後：`/tmp/blog-ai-skills-table-desktop.png`、`/tmp/blog-ai-skills-table-mobile.png`。
- AI 工具清單：`/tmp/blog-ai-tools-desktop.png`、`/tmp/blog-ai-tools-mobile.png`。
- 瀏覽器前完整網站：`/private/tmp/blog-ai-skills-browser-20261025/report.json`，9 項通過且來源未變。
- 寬表格修正後完整網站：`/private/tmp/blog-ai-skills-wide-tables-20261025/report.json`，9 項通過且來源未變；含 36 個 Python 單元測試、搜尋互動、133 篇／14 頁尾頁 3 篇及 361 個 HTML 的連結／安全檢查。
- 文件收尾後最終命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-ai-skills-final-20261025`；以 `/private/tmp/blog-ai-skills-final-20261025/report.json` 的實際 status 與 source_unchanged 為準，不沿用先前版本的通過狀態。
- 執行環境：Hugo Extended 0.168.0、Node 26.12.1、Python 3.13.17。部署固定 Hugo 0.167.0、.nvmrc 為 Node 24.22.1；本輪使用現有本機工具，未安裝依賴或重現這兩個 CI 固定版本，不宣稱與 CI 環境完全相同。
- 本機靜態預覽為 `http://127.0.0.1:1316/blog/`，只綁定 loopback；初次 sandbox bind 被拒後，透過工具審批啟動成功。未開放外網、未登入第三方工具、未提交／推送／部署。
