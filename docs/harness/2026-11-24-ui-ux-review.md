# 全站 UI/UX 審查與局部修正（2026-11-24）

## 需求與範圍

- 使用者要求：用 UI UX Pro Max 檢查網站並修正問題。核准計畫後回覆「修正好」，兩個待決事項依計畫建議處理：英文眉標採 (a)，刪除重複的英文、獨立的英文標籤改為中文；文章外部連結加上 ↗ 與螢幕閱讀器提示。
- 修改區域：共用頂部按鈕與小型點擊區（新增 `static/css/rpg-ux.css`，在 `rpg/head.html` 最後載入）、10–11px 標籤提高到 12px、↗ 只用於外部連結、外部新視窗連結加「（另開新視窗）」、`/post/` 與標籤頁補上隱藏的 H2、關於頁面板標題改為 H2 且技能項目改為 H3／H4、英文眉標中文化。
- 保留：RPG 構圖、色彩、字體、明暗模式、首頁三精選與雙欄卡片、文章內容／日期／路徑、CSP、Goldmark `unsafe: false`、`disqusIdentifier`、主題子模組。
- 排除：文章正文、技術教學範例、發布、推送與部署。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 網站基準 | 全部步驟通過 | `python3 .github/scripts/verify-blog.py`，12 項通過，本輪報告位於 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-zefez228/report.json` | 通過 |
| 連結規則回歸（錯誤案例） | 站內連結使用 ↗、新視窗連結沒有提示或沒有 `noopener` 時檢查失敗 | `test_site_security.py` 5 個案例；舊 `public/` 建置執行新檢查後失敗（RSS ↗、GitHub 等） | 通過 |
| 文章外部連結 | Markdown 外部連結保留原 `rel`/`target` 並加上 ↗ 與提示；錨點連結不變 | issue 管理文章 27 個 `exturl` 全部有提示；`#` 錨點連結不受影響 | 通過 |
| 手機頂部按鈕 | 首頁以外的頁面也是 44×44 | Chromium 390×844，14 個代表頁面量測中心及上下左右點擊位置 | 通過 |
| 小型點擊區 | 視覺不變，點擊區擴大到 44px | 驗證文章標籤、摘要、導覽連結等控制項的實際命中區域，見本輪瀏覽器報告 | 通過 |

## 當前狀態與交班

- 狀態：本機驗收完成。
- 來源 commit：`99e4aa62`（main）。開始時工作目錄乾淨，未提交。
- 審查計畫與證據：Antigravity artifact `ui-ux-fix-plan.md`；修改前截圖與 `results.json` 在同一會話的 `scratch/audit-before/`，修改後在 `scratch/audit-out/`。
- 首輪驗證與截圖保留在前述 Antigravity 會話。首輪網站報告位於 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-7vna3vmk/report.json`。

## 2026-11-25 互動驗收

- 在 Chromium 用 Tab、Shift+Tab、Enter、Esc、搜尋快捷鍵與觸控事件操作本機 Hugo 網站。修正手機選單開啟後的焦點位置、焦點移出時的收合，以及在選單內呼叫搜尋並點選輸入框後，關閉搜尋無法回到原連結的問題。搜尋與選單的回歸案例已加入 `.github/scripts/check-search.cjs`。
- 手機搜尋關閉鈕原為約 24 × 33 px；站名、文章標籤、目錄摘要、留言提示及返回技能圖鑑連結也有點擊範圍不足的情形。本輪補齊手機控制項的 44 px 目標，並修正桌面站名副標被既有選擇器覆寫為 10 px 的問題。
- 75 項瀏覽器檢查通過。視窗寬度涵蓋 320、390、720 和 1440 CSS px。390 px 下抽查首頁、分頁、文章、列表、分類、技能、能力、歷程、作品、關於、留言與 404 等 14 頁。另驗證跳至主要內容、搜尋失敗重試、跨頁主題保存與手機 200% 視窗放大。
- Chromium 測試程式與結果在 `/private/tmp/blog-ux-check.5ecLrY/browser.mjs` 和 `final.json`，同目錄另有 `mobile-menu.png`、`mobile-search.png`。測試使用本機 Chromium 與觸控模擬，未驗實體手機、VoiceOver 或 Safari。

## 2026-11-25 推送前驗收

本次以 `898527bf` 為基準，將前述全站無障礙修正納入發布。首頁文案與置頂筆記已有獨立的[驗收紀錄](2026-11-25-home-featured-notes.md)。

- 重新建置後，在 Chromium 的 14 個代表頁面和互動流程完成 75 項檢查。另完成首頁 36 項檢查，涵蓋明暗主題、首屏、置頂文章與搜尋摘要。測試報告在 `/private/tmp/blog-site-publish.QksICj/site.json` 和同目錄的 `browser.json`。
- 新增回歸案例，確認當連結的 aria-label 覆蓋子元素文字時，檢查器會以標籤內的「另開新視窗」提示為準。
- `python3 .github/scripts/verify-blog.py` 的 12 項檢查全部通過。報告在 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-u_owkjty/report.json`。本機 Hugo 為 0.168.0，部署流程使用 0.167.0。
