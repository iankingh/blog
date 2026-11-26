# Markdown 與 Mermaid 分篇整理

## 需求與範圍

- 使用者要達成的行為：Markdown 與 Mermaid 各自獨立，教學不重複；兩篇改用新網址，舊網址不保留、也不建立轉址。
- Markdown 保留語法、程式碼、表格、換行、目錄與 Hugo 差異；Mermaid 集中渲染需求、原流程圖範例、語法說明、驗證與匯出。
- 保留原始檔名、發布日期、範例程式碼及來源連結，使用 `slug` 產生 `/blog/post/other/markdown-basics/` 與 `/blog/post/other/mermaid-flowchart/`。
- 使用者已明確要求新網址，取代專案預設保留文章網址的限制；不設定舊網址 aliases。
- 本輪排除：新增 Mermaid 渲染器、調整版面、CSP、Goldmark 或留言板識別，以及提交、推送與部署。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 內容分工 | Markdown 不含 Mermaid／sequence／seq 教學；Mermaid 原範例集中保留 | [28 個對應案例](../verification/markdown-mermaid-acceptance-2026-10-26.json)，來源與 article-body 比對通過 | 通過 |
| 原始內容保留 | 原始日期、檔名、程式碼與來源網址保留 | 同上；各 2／1 個程式碼區塊內容、全部原來源、日期與既有 sourceChecks 保留；Mermaid fence 展示語言改為 text | 通過 |
| 新網址／舊網址 | 兩個新頁各一份；舊頁不產生、不轉址 | 乾淨建置對應案例與[瀏覽器紀錄](../verification/markdown-mermaid-browser-2026-10-26.json)；新頁正常、舊頁 404 且 URL 未轉向 | 通過 |
| 搜尋與連結 | 133 篇唯一筆記；僅收錄新網址，Mermaid 搜尋只命中專文 | 對應案例與瀏覽器實際輸入；Mermaid 與 Markdown 完整標題各命中 1 篇，href 使用新網址 | 通過 |
| 本機閱讀 | 兩篇目錄與正文可閱讀，Mermaid 維持程式碼顯示 | 1280×720 瀏覽器；目錄定位成功，pre 的 white-space 為 pre，7 行來源正確、語法表格 2 欄無破裂、頁面寬度等於 viewport | 通過 |
| 網站基準 | 既有內容、搜尋、建置、安全與單元測試全部通過 | 修正後 `/private/tmp/blog-markdown-mermaid-fixed-20261026/report.json` 為 passed，9 項通過且來源未變；最終來源見下列命令 | 通過，最終收尾以 report 為準 |

## 當前狀態與交班

- 狀態：內容整理、對應案例與瀏覽器驗收完成；文件收尾後的網站基準以最終 report 實際結果為準。
- 來源 commit：`b964d03b8c9fb2816baba5b60aee4824f1b29249`；分支 `master`；開始時工作目錄乾淨。
- 已完成：兩篇內容、slug、摘要與日期、逐篇清單及整理報告同步；沒有其他文章引用舊網址，無須改寫 ref。原始檔名保留，新頁 canonical、搜尋索引與生成 HTML 均使用新網址。
- 已完成的驗證：9 項網站基準、28 個對應案例、兩篇新頁與目錄、搜尋、舊頁 404 的實際瀏覽器檢查。
- 最近一次驗證命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-markdown-mermaid-fixed-20261026`；report 的 status 為 passed、9 項通過，source_unchanged 為 true。
- 文件收尾後最終命令：`python3 .github/scripts/verify-blog.py --output /tmp/blog-markdown-mermaid-final-20261026`；以 `/private/tmp/blog-markdown-mermaid-final-20261026/report.json` 的實際 status、各步結果與 source_unchanged 為準，各步日誌在同目錄 `logs/`。
- 未執行及限制：未操作外部 Live Editor 繪圖或 SVG／PNG 匯出；未測實體手機、輔助閱讀器或其他技術教學。曾點選既有複製按鈕，但本機瀏覽器剪貼簿讀取為空，未將複製功能記為通過，也未修改共用複製程式。
- 嘗試過的修正與取得的新證據：第一輪 9 項網站檢查通過；對應案例發現原主題的 Mermaid render hook 輸出一般 div，實際瀏覽器確認來源折行被壓平。將展示 fence 語言改為 `text`，避開主題特殊處理；圖表原始碼逐行保留，不改主題或新增渲染器。已讀官方簡介與 flowchart 文件，核對渲染需求、TD／LR 與節點連線說明。
- 下一個具體動作：讀取最終 report 並確認全部通過；提交、推送與部署另依使用者要求處理。

## 證據與預覽

- 第一輪：`/private/tmp/blog-markdown-mermaid-preview-20261026/report.json`，9 項網站檢查通過；同目錄 `acceptance.json` 保留程式碼展示驗收失敗，不能將該輪對應案例記為通過。
- 修正後：`/private/tmp/blog-markdown-mermaid-fixed-20261026/report.json`；對應案例為同目錄 `acceptance.json`，28 項通過。腳本保存在 `/tmp/check-blog-markdown-mermaid-20261026.py`，對照來源 commit 與當輪建置輸出。
- 來源與建置證據：[對應案例 JSON](../verification/markdown-mermaid-acceptance-2026-10-26.json)。
- 實際瀏覽器證據：[瀏覽器 JSON](../verification/markdown-mermaid-browser-2026-10-26.json)。預設 viewport 為 1280×720，未設定或更動使用者的視窗尺寸。
- 截圖：`/tmp/blog-markdown-mermaid-code-20261026.jpg`、`/tmp/blog-markdown-mermaid-search-20261026.jpg`、`/tmp/blog-markdown-basics-desktop-20261026.jpg`。
- 本機預覽僅綁定 loopback：`http://127.0.0.1:1327/blog/post/other/markdown-basics/` 與 `http://127.0.0.1:1327/blog/post/other/mermaid-flowchart/`。靜態伺服器的 webroot 為 `/tmp/blog-markdown-mermaid-webroot-20261026/`，`blog` 連至本輪驗證的 site 產物；未對外發布。
- 伺服器首次在 sandbox 綁定 loopback 時遇到 PermissionError；經執行權限審核後正常啟動。曾有一次瀏覽器在伺服器啟動前出現連線拒絕，啟動後已完成全部頁面驗收。
- 本機 Hugo Extended 0.168.0；部署固定 Hugo Extended 0.167.0，本輪未在該固定版本重跑；實際 Node／Python 版本與測試日誌見各輪 report。

## 官方依據與驗證界線

- [Mermaid 簡介](https://mermaid.js.org/intro/)：2026-10-26 讀取，核對文字描述需渲染器與圖表類型。
- [Mermaid flowchart](https://mermaid.js.org/syntax/flowchart.html)：2026-10-26 讀取，核對方向、節點、箭頭與分支標籤。
- 原流程圖程式碼不更動；不將網站檢查視為已執行外部 Mermaid 渲染或 SVG／PNG 匯出。
