# Hugo 獨立建置

## 需求與範圍

移除 Hugo NexT v4.8.3 子模組與 CI 遞迴下載步驟。本站維護 RPG 版面、程式碼渲染與舊版 XML 搜尋索引。保留上游 MIT 授權，移除只有舊主題使用的版型與設定。README、Hugo 建置筆記與作品頁同步更新。

## 驗收

| 案例 | 結果與證據 |
| --- | --- |
| 全新取得原始碼 | 只複製本次版本要納入 Git 的檔案到暫存目錄；目錄中沒有 Git、中繼產物、主題或 node_modules。Hugo Extended 0.168.0 執行壓縮建置並將警告視為失敗，成功。 |
| 與遷移前相同內容比對 | 在兩個獨立目錄放入相同版本的文章，用相同 Hugo 建置。388 個 HTML 逐位元一致。少掉的 116 個檔案全是上游靜態資源，共 9,952,500 bytes。JSON 的 141 篇筆記、XML 的 145 筆及所有 RSS 內容在正規化空白後相同。 |
| 搜尋索引與子路徑 | 完整網站檢查核對 XML 是否包含 JSON 每篇文章的原網址。回歸案例確認遺漏 /blog/ 的 XML 網址會被拒絕。手動邊界案例另確認含 &、角括號與 CDATA 結束字元的內文可讀回。 |
| 瀏覽器 | 本機 Chromium 桌面實測搜尋導至 Hugo 筆記、顯示程式碼複製按鈕、Pele 產生 SVG。390px 寬度的留言板保有討論識別碼，可開啟手機選單，頁面無水平溢出。未呼叫外部分析或留言服務。 |

## 當前狀態與交班

- 來源為 main 的 bd26d698。本次改動完成於工作區。
- 對照產物及結果位於 `/private/tmp/blog-hugo-final.QCtGTY/parity.json`，同目錄的 `compare.py` 記錄比較方式。瀏覽器與 XML 邊界證據分別為 `/private/tmp/blog-hugo-standalone.C0j5nX/browser.log` 和 `xml-edge-result.txt`。
- 完整網站驗證命令為 `python3 .github/scripts/verify-blog.py --output /private/tmp/blog-hugo-final.QCtGTY/verification`，結果與逐步日誌見該目錄的 `report.json` 及 `logs/`。本機 Hugo 為 0.168.0，CI 固定 0.167.0。
- 建置只需 Hugo Extended；完整驗證另用 Git、Python 與 Node。發布由既有工作流程處理。
