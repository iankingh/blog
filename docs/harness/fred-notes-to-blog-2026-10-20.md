# Fred 抽獎系統與 SOLID 筆記整理至部落格

## 需求與範圍

- 將使用者指定的兩篇既有 Obsidian 筆記整理成公開的繁體中文文章。
- 保留兩篇完整原檔名與標題（含 ▶️ YT-、副標題與「筆記」），網址以 slug 保持簡短。
- 保留影片來源、主要觀點與必要時間連結；移除 callout／wikilink、私人 Notion 入口與個人任務追蹤。
- 區分影片筆記與新增技術補充；不宣稱重看完整影片，不推定影片發布日期。
- 以 2026-10-20 作為新部落格文章日期；既有文章日期、網址及來源不變。
- 更新逐篇清單及文章數檢查，預期 132 篇、每頁 10 篇、14 頁且最後一頁 2 篇。
- 不提交、推送或部署，不修改原始 Obsidian 檔案。

## 驗收

| 案例 | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 公開文章 | 兩篇有摘要、情境、來源、互連，無私人筆記語法 | 文章檔案、來源名稱比對、手機／桌面實看 | 通過 |
| 教學範例 | Node 權重邊界與 JDK 25 範例輸出一致，class 69 | 範例結果 JSON、內容檢查與 6 個新增單元測試 | 通過 |
| 新增文章／分頁邊界 | 132 筆索引，14 頁尾頁 2 筆，漏登／重複／錯誤尾頁會失敗 | 範例結果 JSON、內容檢查與 6 個新增單元測試 | 通過 |
| 網站基準 | verify-blog.py 全部 checks 通過 | 範例結果 JSON、內容檢查與 6 個新增單元測試 | 通過 |
| 本地預覽 | 桌面／手機文章、目錄、表格與搜尋可閱讀 | 390／1440px、Fred 搜尋兩筆、目錄定位與第 14 頁兩筆 | 通過 |

## 當前狀態與交班

- 狀態：內容與瀏覽器驗收完成；最終網站驗證以以下 report 實際結果為準。
- 起始分支：codex/harness-engineering；開始時工作目錄乾淨。
- 已完成：保留兩篇完整名稱與檔名，完成文章、slug、相互 ref、逐篇 JSON 與參考來源；既有 130 筆 JSON 與來源筆記 SHA-256 比對未變。Node 與 JDK 25 範例輸出通過。
- 限制：本機沒有 redis-server／redis-cli；Redis 腳本先列為文件查核示意，不宣稱實機或叢集驗證。
- 下一步：供使用者閱讀本地文章；提交、推送及部署另依指示處理。

### 驗證證據

- 起始來源 commit：`ea29c4947b1857c95725927ca9c7bcaa8e77cd7e`。
- 首輪網站：`python3 .github/scripts/verify-blog.py --output /tmp/blog-fred-site-20261020`，9 項通過且來源未變；132 篇／14 頁（尾頁 2 篇）與 358 個 HTML 的連結及安全檢查通過。
- 文件收尾後最終網站命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-fred-final-20261020`；report 為 `/tmp/blog-fred-final-20261020/report.json`，以其中 status 為準。
- 新增單元測試：`python3 -m unittest discover -s .github/scripts -p test_note_content.py`，6 項通過，包含重複／漏登與分頁、索引失敗案例。
- 教學範例：`python3 docs/verification/check-fred-examples.py --results /tmp/blog-fred-examples-20261020.json`，Node 26.5.0、JDK 25.0.4.1；6 個 class 為 69。已保存結果於 `docs/verification/fred-examples-results-2026-10-20.json`。
- 瀏覽器：`docs/verification/fred-browser-checks-2026-10-20.json`；兩篇均有完整 H1、目錄、4 張表格與可捲動程式碼，390／1440px 無頁面溢位；沒有私人 Notion 連結。Fred 搜尋命中兩篇，目錄定位到 Java 範例標題，首頁第 14 頁兩篇。
- 截圖：`/tmp/blog-fred-mobile-preview.png`、`/tmp/blog-fred-lottery-preview.png`。預覽 `http://localhost:1315/blog/`，兩篇文章分頁已開啟，viewport 已還原。
- 限制：影片依原稿整理，未重新觀看、取得新字幕或逐一驗證時間。Redis Lua 僅文件查核；沒有 Redis 叢集、真實雲端、活動服務負載或實體手機測試。

## 影片介紹還原（2026-10-20）

- 使用者指出「這部影片是什麼」不應被改寫成摘要；本輪將兩篇該段落直接從原筆記還原，包含來源、背景／來賓、想回答的問題、核心觀點、適合對象與注意事項，SOLID 保留講解順序。
- SOLID 的介紹逐字比對相同；抽獎介紹僅將一個 Obsidian 站內連結轉成 Hugo ref，其餘文字與影片時間連結保留。標題、檔名、slug、date、程式範例不變；只更新兩篇 lastmod 與對應 JSON。
- 靜態比對證據：`/tmp/blog-fred-intro-restoration.json`。程式範例本輪未更動，不重跑；先前範例證據仍只代表那些範例。
- 本輪網站驗證：`python3 .github/scripts/verify-blog.py --output /tmp/blog-fred-intro-restored-20261020`；結果以 `/tmp/blog-fred-intro-restored-20261020/report.json` 為準。
- 本地會重新開啟 SOLID 的介紹段落，供使用者確認；未提交、推送或部署。

## 提交與推送（2026-10-20）

- 最新使用者指示：依 git-commit-content 提交並推送本輪變更。
- 提交範圍：兩篇完整原名文章與影片介紹還原、檢核清單、可容納新增文章的分頁／搜尋檢查與回歸測試、教學範例驗證及相關文件。
- 目標分支：`codex/harness-engineering`；保留現有分支，推送至同名遠端分支。
- 提交前網站命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-fred-precommit-20261020`；結果以同目錄 `report.json` 為準。
- 本輪沒有再次修改程式範例；Node／JDK 與 Redis 未實測限制沿用上述紀錄。
