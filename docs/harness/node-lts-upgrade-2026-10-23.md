# Node.js LTS 與驗證工具升級

## 需求與範圍

- 將工作區內所有使用 Node.js 的專案環境與 npm 相依套件升級。
- Blog 使用 Node.js 24.22.1 LTS／npm 11.20.0；CI 明確載入 `.nvmrc`。
- 依使用者指示先移除 `docs/verification/node_modules` 與 `package-lock.json`，更新套件宣告後重新安裝並產生鎖檔。
- 驗證工具使用 Angular 22、TypeScript 6、Vite 8、Pinia 4、Vue Router 5；保留文章內容、日期、既有 AGENTS.md 修改及主題子模組。
- 新工具鏈上的相容性驗證不等同於文章原版本的執行證據。

## 驗收

| 案例 | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 相依套件安裝 | 一般 npm install 可解析，不使用 legacy-peer-deps | `/private/tmp/codex-node-upgrade-20261023/logs/blog__docs__verification-install.log` | 通過 |
| Vue／Angular／JS 範例 | 隔離目錄以新 lockfile 安裝並通過三支檢查 | `/private/tmp/codex-node-upgrade-20261023/logs/blog__docs__verification-check-1.log` | 通過 |
| 網站基準 | verify-blog.py 全部通過 | `/private/tmp/blog-node24-upgrade-ready-20261023/report.json`（以 status 為準） | 結果見 report |

## 當前狀態與交班

- 狀態：程式、文件、相依安裝與隔離範例驗證已完成；最終網站驗收結果以表列 report 為準。
- 目前分支 master；本次不修改原有未提交的 AGENTS.md。
- 驗證資料在 `/private/tmp/codex-node-upgrade-20261023/`；最終結果會記錄於工作區 `NODE_UPGRADE_REPORT.md`。
