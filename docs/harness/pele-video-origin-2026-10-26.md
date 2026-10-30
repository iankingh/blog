# Pele 文章補上影片緣由

## 需求與範圍

- 使用者補充原先認識 Pele 是來自 https://www.youtube.com/watch?v=-YlDpD8USWY 。在現有文章開頭及參考資料補上出處。
- 保留原標題、檔名、slug、date、官方來源、教學與程式碼；實際修訂時間為 2026-10-26T23:36:32+08:00，同步內容整理清單與報告。
- 這次是出處補充，沒有新增影片摘要或 Obsidian 筆記，不擴大成其他繪圖工具比較；未將影片標題的效能數字當作本站測試。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 影片來源 | 完整標題、頻道、網址與使用者提供的一致 | YouTube 頁面與展開的作者說明；標題「Mermaid 太肥太慢？Obsidian 開源的 pele，畫一張圖只要 0.3 毫秒」、頻道 MUKI WU (哈囉沐奇)、日期 2026-10-21、片長 11:08 | 已查核 |
| 原內容保留 | 原始 date、slug、教學段落、程式碼與來源不刪減 | /tmp/blog-pele-video-origin-cases-20261026.json | 7 項通過 |
| 網站基準 | 執行統一驗證並保留每步結果 | /tmp/blog-pele-video-origin-final-20261026/report.json | 結果見 report |

## 當前狀態與交班

- 狀態：文字補充完成；原內容保留 7 項案例通過，首輪網站基準 10 項通過且 source_unchanged 為 true。文件收尾後另跑最終基準，結果見下列 final report。
- 來源 commit：85b5275b2f2989e38c11494bbc5d5ee94d9d208f；分支 master；開始時工作目錄乾淨。
- 已完成文章緣由與影片參考連結、修訂時間、JSON 及內容整理報告。
- 驗證命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-pele-video-origin-final-20261026`；結果以該目錄 report.json 與 logs 為準。
- 本輪僅補文字與連結，未變更版面、互動或技術範例；無新增 Obsidian 實機驗證。未完整觀看、聽辨或取得影片字幕，查核限作者頁面資訊與說明。
- 發布狀態以 Git 與遠端為準；本紀錄不把本機檔案修改視為已發布。
- 繁中自動檢查：技能 chk.py 因缺少 OpenCC 未完成，新增段落已人工閱讀；不將工具缺漏視為通過。
- 下一步：依最終 report 交付文字補充；這次來源補充尚未另行提交／發布。
