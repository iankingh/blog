# GitHub／GitLab Issue 管理教學

## 需求與範圍

- 依 skills-manager 的置頂 Issue 寫繁體中文教學，涵蓋 Markdown 導覽、Bug 與功能建議範本、GitHub 置頂與 GitLab 固定入口。
- 新增 `content/post/git/github-gitlab-issue-management.md`，以及 `docs/note-review.json` 中的文章項目。
- 教學範例放在文章內。遠端專案設定、測試 Issue 與部落格部署不在本輪範圍。

## 驗收

| 案例 | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 比對兩個平台 | 置頂與看板排序的適用位置明確，範本目錄及參數與官方文件相符 | skills-manager #155 和兩平台官方文件，來源收錄在文章及查核清單 | 通過 |
| 擷取文章範例 | 兩個 Markdown 同頁連結各有對應標題，自訂 HTML 錨點的名稱相符 | 從文章擷取程式碼，核對標題轉換與具名錨點 | 通過 |
| 核對範本與快速連結 | GitHub YAML 可解析，兩個平台的快速連結指向相符的範本 | Ruby YAML 解析兩個範本的 metadata 與選單設定，Python 解析四個快速連結及比對 13 個來源網址 | 通過 |
| 瀏覽器檢查 | 文章表格、六個程式碼區塊與目錄可用 | 本機瀏覽器開啟 `/blog/post/git/github-gitlab-issue-management/`，確認 HTML 錨點以程式碼呈現，點擊目錄後 GitLab 章節標題進入可視範圍 | 通過 |
| 原工作目錄網站基準 | 正式建置與全部檢查成功 | `note-source` 和 `generated-content` 因既有未登錄文章失敗，建置及其餘檢查通過 | 失敗 |
| 隔離副本網站基準 | 新文章納入正式建置與搜尋索引 | 從同一個 commit 建立本機副本，套用本輪三個檔案，只在副本排除既有重複文章，執行相同驗證命令 | 12 項通過 |

## 當前狀態與交班

- 基準為 `main` 的 `eab12d58`，開工時工作目錄乾淨。
- `HEAD` 已追蹤的 `content/post/software-design/prototype-for-requirement-clarification 2.md` 沒有查核清單項目，正文與正式檔相同，差異是正式檔多了 `abilities` front matter。原工作目錄保留兩份檔案。
- 驗證命令為 `python3 .github/scripts/verify-blog.py`。原工作目錄報告在 `/private/var/folders/pc/ck1ls3rd5hg6920pxlk8xgj00000gn/T/blog-harness-31tq11e3/report.json`，隔離副本報告在 `/private/tmp/blog-issue-management.ROfNdL/evidence/report.json`。
- 本機使用 Hugo Extended 0.168.0，CI 固定為 0.167.0。平台步驟以公開原例與官方文件核對，遠端操作與部署未執行。
- 後續若要推送與部署，需先處理原儲存庫的重複文章並重跑完整驗證。
