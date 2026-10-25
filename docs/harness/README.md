# Blog 的 Harness：規則、驗證與失敗回饋

這套流程沿用目前的 Coding Agent 與既有 Hugo 檢查，讓每次改動都有可重跑的驗證、
失敗日誌及可接續的任務紀錄。`AGENTS.md` 是開發入口，檢查器提供機械式回饋；
Agent 根據錯誤修正，再重新驗證。指令文字不會取代執行環境的權限控管。

## 先跑一輪

準備 Git、Python 3、Node.js、與部署 workflow 相同的 Hugo Extended 版本，以及已初始化的主題子模組。
從儲存庫執行：

```bash
python3 .github/scripts/verify-blog.py
```

命令回傳 0 才表示本輪所有網站檢查通過。預設每個檢查最多 300 秒，結果保存在
新建的系統暫存目錄，終端會印出完整路徑。明確指定位置時，必須是儲存庫外尚未存在的目錄：

```bash
python3 .github/scripts/verify-blog.py --output /tmp/blog-verification-new --timeout 300
```

每次使用新目錄，不重用既有 HTML。`report.json` 記錄各步命令、結束碼、耗時與日誌路徑，
以及驗證前後的來源 commit／工作內容指紋。`running` 是尚未完成的 checkpoint；
只有 `status: passed`、所有 checks 通過且來源未改變，才是成功。
忽略檔不在來源指紋範圍內；套件與執行環境仍需配合版本日誌判讀。

## 會跑哪些檢查

| 檢查 | 驗證範圍 |
| --- | --- |
| 工具版本 | Hugo、Node 與 Python 的實際版本，記錄於日誌 |
| 文章來源 | 涵蓋所有文章且不重複的檢核清單、發布日期、摘要、來源、程式碼區塊與引用（目前 133 篇） |
| 搜尋互動 | 既有 Node 測試：載入、快取、競態、錯誤重試與焦點 |
| Python 單元測試 | 部署版本邏輯、JDK 檢查器與驗證入口的成功／失敗處理 |
| Hugo 建置 | 正式壓縮建置，網站、快取與資源均放在當輪暫存目錄 |
| 生成內容 | 搜尋筆數、分頁、內部連結、圖片與錨點 |
| 生成安全檢查 | CSP、腳本來源、內嵌程式及事件處理器等既有規則 |

建置失敗時，依賴該產物的兩個生成檢查會標為 skipped，整輪仍失敗；獨立檢查可繼續產生診斷。
缺少工具與逾時也失敗。Ctrl-C 會停止當前命令及其子程序，剩餘步驟標為 skipped；
checkpoint 留下已完成的結果。若硬關閉程序，先查殘留程序與日誌，再用新輸出目錄重跑。

這個網站入口不重跑 Java／Spring／Vue／Angular 的全部文章範例，也不驗證瀏覽器外觀。
技術範例變更另見 [隔離驗證](../verification/README.md)，UI 變更需另外留下實際瀏覽器證據。
文件或 CSS 的檢查通過，不能推廣成全部教學技術內容都正確。

## 做一次有回饋的開發

1. 讀需求、當前程式與適用規則；先確認真正要改的行為。
2. 多步驟任務複製 [任務範本](task-template.md)，寫出正常、錯誤及邊界案例。
3. 修改程式，執行本入口，讀失敗步驟的 log。環境問題與產品問題分開記錄。
4. 依證據修復並重跑；必要時補能抓到這類錯誤的回歸案例。
5. 核對需求的行為證據與剩餘限制，留下下一步；新會話以當前程式重新確認狀態。

`report.json` 證明的是當輪來源與檢查範圍。之後任何修改都可能讓它過期，不能只引用舊綠燈。
規則逐步依真實失敗調整，機械式規則放進檢查器，判斷性提醒保持短小並限縮範圍。

## CI 與證據

- `.github/workflows/verify.yml` 在 PR 執行相同入口，僅有 `contents: read`。
- 既有部署 workflow 的 build job 使用相同入口；發布仍由既有 deploy job 管理。
- CI 無論通過或失敗都嘗試上傳當輪 report 與 logs；網站產物只在驗證成功後交給後續步驟。
- PR workflow 加入儲存庫不代表已設成分支保護的 required check；該設定需要另外在 GitHub 配置。
- 日誌可能包含文章或程式片段；提交與分享前依資料性質檢查，環境機密不寫入任務紀錄。

## 來源

- [OpenAI：repo 內的規則、Skills 與 CI](https://developers.openai.com/blog/skills-agents-sdk)
- [OpenAI：Review → Repair → Validate](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex)
- [OpenAI：具體且限縮範圍的 repository rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex)

這是針對本站既有工具整理的導入，未增加模型 API 或假定自動修復程式已在背景執行。
