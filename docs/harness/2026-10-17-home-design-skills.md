# 首頁設計 skills 導入與原排版修整

## 需求與範圍

- 安裝並使用 Impeccable、Anthropic frontend-design、UI UX Pro Max、Vercel web-design-guidelines。
- 最新使用者指示：「我比較喜歡原本的排版，我只是不要 AI 味」。先前 A「工程野帳」結構重整已撤回，以原 RPG 排版作為本輪視覺依據。
- 保留原角色側欄、等級／EXP、營火 Hero、原職稱、三張置頂精選、雙欄任務卡、色彩與字體、分頁及手機選單。
- 僅修改首頁空泛口號、重複英文標籤、文案、標題字距／換行及手機控制尺寸；共用搜尋標題改為「搜尋筆記」，欄位補 `name="q"`。
- 不修改文章、日期、網址、主題子模組、Goldmark、CSP、留言板識別及部署。未提交、推送或發布。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| skills 安裝 | 四套官方來源安裝並可使用 | `/Users/ian/.codex/skills/`；context、雙代理評估、detector、UX 搜尋與 Vercel 指引已使用；來源見首輪評估 | 通過 |
| 原版構圖 | 側欄與 EXP、營火 Hero、三精選與雙欄任務卡保留 | 1440×1000、1280×720 實看；3 張精選、雙欄 grid、角色面板存在；`refined-original-desktop.jpg` | 通過 |
| 文案與細節 | 去除空泛口號及重複英文標籤，沿用真實主題與既有字體 | 首頁 diff 與桌面／手機實看；H1 34.56px、日誌 H2 23px、精選 H4 21px | 通過 |
| 手機正常／邊界 | 原 Hero／卡片順序不變，控制 44×44，無溢位或遮擋 | 390×844、320×740 實看；390 兩個 CTA 並列；320 品牌至搜尋間隔 8px、選單至折角間隔 10px；scrollWidth 等於視窗寬度 | 通過 |
| 平板邊界 | 保留搜尋與主題文字，不擠進 44px | 768×1024 實看；搜尋 92×44、主題 96×44、選單 44×44；無文字溢出 | 通過 |
| 搜尋成功／無結果 | 關鍵字命中及空結果可理解，Esc 還原焦點 | Hikari 命中 1 篇；不存在的關鍵字 0 篇並顯示提示；Esc 關閉且焦點回到搜尋按鈕 | 通過 |
| 選單／主題 | 角色面板可由手機選單開啟，Esc 返回；明暗可切換 | 選單 expanded true／false、焦點回到開啟按鈕；明暗手機截圖，無控制台 error | 通過 |
| 分頁／隔離 | 第二頁不重複精選；非首頁不載入修整 CSS | 實際點擊第 2 頁：10 張任務卡、0 精選；about 無 polish CSS 且保留角色面板；網站檢查涵蓋 13 頁與 /blog/ 連結 | 通過 |
| 網站基準／錯誤復原 | 既有網站、安全與搜尋測試完整通過 | `python3 .github/scripts/verify-blog.py`，9 checks passed；搜尋快取、競態、錯誤重試、焦點由既有 Node 測試覆蓋 | 通過，最終來源見下列 report |

## 當前狀態與交班

- 狀態：完成原版恢復、局部修整與瀏覽器驗收；最終文件整理後的網站基準結果以 `/tmp/blog-original-polish-final-20261018-01a14a0a/report.json` 的實際 status 為準。
- 來源 commit：`885d2ce50f36002d44186f71c5d72836aaf43859`；分支 `codex/harness-engineering`。開始時工作目錄乾淨，本輪未覆蓋其他人的修改。
- 程式差異：`layouts/home.html`、`layouts/_partials/rpg/featured-card.html`、`layouts/_partials/rpg/search.html`；新增首頁專用 `static/css/rpg-home-polish.css`。原先的 `rpg-journal.css`／`journal-entry.html` 已移除，沒有殘留 journal 版型。README 僅增加一行目前修整範圍。
- 實作驗證：`python3 .github/scripts/verify-blog.py` 結束碼 0，9 項通過，來源未變；report：`/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-l5knv2p0/report.json`。
- 文件整理後最終驗證命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-original-polish-final-20261018-01a14a0a`。各步日誌位於該目錄 `logs/`，只有 report 的 passed 代表該輪完成。
- 實際瀏覽器證據：`/tmp/blog-original-polish-browser-evidence.json`，包含尺寸、原版結構、搜尋、選單、分頁與隔離案例。
- 截圖目錄：`/Users/ian/.codex/visualizations/2026/10/17/01a14a0a-ad65-7563-8a61-12521e3c05c9/blog-design/`；最終檔案以 `refined-original-` 開頭，包括 desktop、desktop-full、desktop-1280、mobile、mobile-full、mobile-dark、mobile-320、tablet。
- 瀏覽器發現並修正一項回歸：44px 固定寬度原先套用到平板，導致文字直排；現改為 ≤820px 最小寬高 44px，≤540px 才固定寬度。768px 與 320px 已重驗。
- 獨立 finish reviewer 依最新需求重新完整審查，結論 `ship`；確認原版構圖、字體、金綠色與營地保留，無剩餘修正。獨立 documenter：`No changes`，不新增全站 DESIGN.md／PRODUCT.md 或 sidecar。
- Impeccable 靜態掃描：`/tmp/blog-original-polish-detector.json` 與 `/tmp/blog-original-polish-detector-status.json`，原始結束碼 2，1 項 `flat-type-hierarchy` warning。工具無法解析 Hugo stylesheet partial，將 H1/H2/H3 誤讀為全 16px；實際瀏覽器字級不同。未放寬規則或為使掃描變綠修改階層。掃描後僅修正上述控制寬度，未重跑相同來源掃描。
- 先前瀏覽器讀取阻礙已解除：預覽進程曾隨中斷結束，錯誤頁變為 data URL；以正常 HTTP 頁面重新開啟並改用可持續的本機 Hugo 預覽後，已完成本輪操作。沒有使用其他協定或 raw CDP 繞過限制。
- 預覽保留於 `http://127.0.0.1:1313/blog/`，本輪 PID 記錄 `/tmp/blog-journal-preview.pid`、日誌 `/tmp/blog-journal-preview.log`；僅綁定 loopback。瀏覽器 viewport 已 reset，首頁作為成品預覽保留。
- 歷史資料：`docs/home-design-review-2026-10-17.md`、`.impeccable/critique/2026-10-17T13-41-30Z__layouts-home-html.md` 是原版首輪評估；`after-*.jpg` 與 `/tmp/blog-journal-*` 是已撤回 A 的證據，不代表最終版本。原評估提出的結構重整未列為本輪待辦，不能因舊評分繼續修改使用者要保留的排版。
- 剩餘限制：未驗實體手機、VoiceOver、200% 縮放與瀏覽器網路失敗注入；錯誤重試由既有搜尋測試覆蓋。沒有修改技術文章，未重跑 Java／Spring／Vue／Angular 的全部教學範例。
- 下一步：依使用者對保留原版後的實際畫面回饋，僅作明確指定的局部修整；發布、推送與部署另依使用者要求處理。
