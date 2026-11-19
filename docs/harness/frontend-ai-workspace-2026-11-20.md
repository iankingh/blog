# ＡＩ前端專案目錄

## 需求與範圍

- 整理使用者提供的 `.github/` 設定與一般前端目錄，保留一棵完整目錄樹，產出 Hugo 筆記及可貼到 Obsidian 的 Markdown 正文。
- 依 GitHub、VS Code、OpenAI、Anthropic 和 Vue 官方資料補充 Harness、Copilot 檔案及驗證流程。文中範例是目錄與工作流程示意。

## 驗收

| 案例 | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 目錄結構 | 標題使用全形「ＡＩ」，只有一棵包含 `.github/` 與一般前端目錄的樹，保留檔案案例 | Python 核對 113 個節點的縮排、路徑與唯一性，並核對 3 個 Prompt 檔名及 8 個來源網址 | 通過 |
| Copilot 與測試說明 | 檔案命名、套用條件及測試層級符合官方資料 | 八份來源列於文章及查核清單 | 文件查核完成 |
| 生成頁面 | 新文在 `/blog/post/frontend-ai-workspace/` 產生，目錄與原始檔一致，搜尋索引收錄一筆 | Python 對照兩份建置產物的 HTML、目錄文字與搜尋索引 | 通過 |
| 原工作目錄網站基準 | 正式建置與全部檢查通過 | `note-source` 和 `generated-content` 遇到既有未登錄重複檔，其他 10 項通過 | 失敗 |
| 隔離副本網站基準 | 正式建置與全部檢查通過 | 僅在副本排除既有重複檔，驗證 141 篇筆記、搜尋、分頁與內部連結 | 12 項通過 |

## 當前狀態與交班

- 開工時 `main` 為 `92c523c2`，工作目錄乾淨。
- Hugo 將新文的純日期解讀為 UTC，在台北當日午夜未收錄新文。補上 `2026-11-20T00:00:00+08:00` 後，生成頁面與搜尋索引均收錄文章。
- 正式驗證命令為 `python3 .github/scripts/verify-blog.py`。修正時區後的報告分別位於 `/private/tmp/blog-frontend-ai-workspace.zE4Ai9/workspace-evidence/report.json` 與 `/private/tmp/blog-frontend-ai-workspace.zE4Ai9/evidence-taipei/report.json`。
- 原工作目錄的 `content/post/software-design/prototype-for-requirement-clarification 2.md` 已追蹤且未登錄，正文與正式檔一致。原工作目錄保留該檔，正式網站基準仍有此阻礙。
- 本機使用 Hugo Extended 0.168.0，CI 固定 0.167.0。Vue 目錄與測試是文件範例，Copilot 配置以官方文件查核。未推送或部署。

## 部署修復

- 提交 `10dff7b4` 已推送至 `main`。GitHub Actions 的 `Verify site` 在 `note-source` 與 `generated-content` 失敗，部署步驟因此跳過。 [執行紀錄](https://github.com/iankingh/blog/actions/runs/44567654996)
- 移除未登錄的 `prototype-for-requirement-clarification 2.md`。比對確認副本正文相同，且少了正式檔的 `abilities` 欄位。正式檔的內容、日期、路徑與查核清單均維持原樣。
- 原工作目錄重跑網站基準，12 項全數通過。另核對原文章與新筆記都有生成頁面和唯一搜尋索引項目。報告位於 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-qkk7eamz/report.json`。
- 遠端驗收以本次修復提交觸發的 GitHub Actions 執行紀錄及正式頁面為準。

## 目錄範例修訂

- 依使用者新要求，將一般 ＡＩ 前端專案作為主範例，GitHub Copilot 改為簡易 `.github/` 範例。兩棵目錄樹各自使用 `text` 程式碼區塊。沿用原始發布日期，更新 `lastmod` 並同步文章查核清單。
- 網站基準 12 項通過。比對原稿與 Hugo 生成的 HTML，確認一般目錄完整，Copilot 設定限於第二個區塊。Chrome 本機預覽顯示兩段各自的複製按鈕，點擊目錄可跳至 Copilot 小節。報告位於 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-uk0pfwiu/report.json`。
