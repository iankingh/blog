# AI 工具與學習資源清單補充

## 需求與範圍

- 將原 AI 工具清單改名為「AI 工具與學習資源清單」，同步摘要與開頭說明。
- 在「Skills 與工作流資源」收錄 Tenten 技能年鑑，在「AI 新聞與學習資源」收錄 AI 郵報，補上用途及來源。
- 保留 `content/post/ai-tools.md` 路徑、原始發布日期、四個既有工具入口及來源；更新 lastmod 與逐篇查核紀錄。
- 本次不新增 ub-mode／pstack 或其他文章，不修改版面、互動、主題、安全設定或依賴；不提交、推送或部署。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 新資源與分類 | 兩個指定章節各收錄正確名稱、網址與用途，參考資料保留來源 | 下列 acceptance JSON，兩個新網址在生成頁各有正文與參考資料連結 | 通過 |
| 保留既有內容 | 路徑與原始 date 不變，原四個工具及來源仍在 | 與 HEAD 比對原始 date、完整工具列及來源 | 通過 |
| 範圍邊界 | 未新增文章，檢核清單仍為 135 篇，其餘 134 筆紀錄不變 | JSON 比對及網站檢查；文章未加入 ub-mode／pstack | 通過 |
| 網站基準 | 10 項網站檢查通過，生成頁與搜尋使用新標題、原網址 | 首輪 report 全部通過且來源未變；生成頁與搜尋案例通過；文件收尾結果另見最終 report | 首輪通過；最終以 report 為準 |

## 當前狀態與交班

- 狀態：文章、來源查核、清單同步與 8 項內容核對完成；最終網站結果以收尾 report 的 status 為準。
- 起始來源：master，`5af03a3abfb3bdde85c1650467ff59dce7474eb0`；工作目錄乾淨。
- 來源查核日期：2026-10-31；使用 web.run 讀取兩個公開首頁，工具未提供 HTTP 狀態碼。
  - https://skills.tenten.co/：首頁自稱 Tenten 技能年鑑，提供技能、教學、工作流文件、搜尋與分類。
  - https://www.aiposthub.com/：首頁提供 AI 新聞及各類實戰指南，屬於新聞與學習資源。
- 查核限於網站定位與公開首頁；未登入、訂閱、安裝 Skills 或重跑個別教學。
- 已完成：標題、摘要與開頭更新；兩個新章節、網站用途及參考來源；分工文字配合擴充範圍調整。JSON 保留歷史查核並新增兩筆來源與本輪修訂日期，整理報告只追加本次內容。
- 內容驗收：`/private/tmp/blog-ai-learning-resources-20261031-acceptance.json`，8 項核對通過；使用真實建置 HTML 與 `search-index.json`，確認 `/blog/post/ai-tools/` 保持、唯一搜尋結果使用新標題／摘要並含兩個新增資源。
- 首輪網站命令：`python3 .github/scripts/verify-blog.py`；證據 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-mbobswtj/report.json`，status 為 passed、全部 10 項通過且 source_unchanged 為 true。
- 文件收尾命令：`python3 .github/scripts/verify-blog.py --output /private/tmp/blog-ai-learning-resources-final-20261031`；結果與各步日誌為 `/private/tmp/blog-ai-learning-resources-final-20261031/report.json` 及 `logs/`。此位置預先記錄，最終成功與否須讀取 report，不能從本段推定。
- `git diff --check` 通過。本次只改內容，未調整版面或互動，未另做瀏覽器外觀驗收；未登入或驗證外部服務功能、未重跑其他技術教學。未提交、推送或部署。
- 下一步：確認最終網站 report 為 passed 後交付；後續 ub-mode／pstack 專文依使用者另行要求處理。
