# Node 26 LTS 與維護檢查修正

## 需求與範圍

- 修正前輪建議：保存可重跑的 Skills 驗收案例、明示工具版本差異、移除 README 過時分頁數。
- 使用者要求重新安裝 Node 26 LTS；官方 2026-11-01 發行索引顯示最新為 26.13.0（Lithium），npm 11.20.0。
- 起始根目錄 `package-lock.json` 已刪除。使用者回覆「重新安裝最新的」，本輪核對並安裝根目錄最新套件、重建鎖檔。
- 保留文章與日期、Goldmark／CSP、留言識別碼、主題子模組；不提交、推送或部署。
- 技術教學驗證工具只更新 Node 環境宣告，不任意更新其整組套件。
- 根目錄最新 Pele 為 1.13.0；同步 vendor、MIT 授權與 SHA-256、README 及 Pele 文章中的本站版本／安裝命令。僅這篇實際修訂的文章更新 lastmod，保留原始 date 並同步 note-review。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| Node 重裝 | Homebrew 重裝完成，新登入 shell 回報 26.13.0／Lithium | `/private/tmp/blog-node26-20261101/node-reinstall.log`、`runtime-after.json`；npm 11.20.0，全域套件清單與重裝前一致 | 通過 |
| 版本檢查 | Node 版本／LTS 不符會失敗；Hugo 與 CI 不同會明示 | `test_tool_version.py` 含版本不符、非 LTS、舊版／非 Extended Hugo、workflow 不一致案例；`test_verify_blog.py` 確認警告留在結果 | 通過 |
| 可重跑 Skills 案例 | 不依賴個人路徑、相鄰 repo 或舊暫存基線；實測安裝保留與首頁置頂 | `check-skills.py` 的 2 個文章 shell 區塊、5 種目的地；`test_skills.py` 可抓出失效軟連結保護移除、置頂順序錯誤、第二頁重複、互連／圖鑑／搜尋錯誤 | 通過 |
| 最新根目錄套件 | 版本／授權／鎖檔與 vendor 資源一致 | `npm-install.log`；Pele 1.13.0，`npm ci --offline --ignore-scripts --cache /private/tmp/blog-node26-20261101/npm-cache` 成功，7 個圖表案例通過 | 通過 |
| 瀏覽器 | 圖表在桌面／手機與晝夜主題可讀，來源可操作 | `docs/verification/node26-browser-2026-11-01.json`：6 筆觀察與 4 張截圖；1280／390px 無頁面溢位，兩篇圖表均 rendered，來源可滑鼠展開及 Space 收合 | 通過 |
| 網站基準 | `python3 .github/scripts/verify-blog.py` 全部通過、來源未變 | 首輪 `site-first/report.json` 12 項通過；文件與文章同步後的最終結果讀下列 `site-final/report.json` | 收尾以最終 report 為準 |

## 當前狀態與交班

- 狀態：實作、安裝、回歸案例與瀏覽器驗收完成；最終網站收尾以指定 report 判定。
- 來源：`1c4efa02c3e1e90f5deb213ff50b3dddc00536ce`，`master`；起始只有根目錄鎖檔刪除。
- 本機 Node 由 Homebrew `node` 提供，`node@26` 目前是該 formula 的別名；已安裝版本 26.13.0。
- 來源：https://nodejs.org/en/about/previous-releases 、https://nodejs.org/dist/index.json 。
- Node 重裝命令：`HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_INSTALL_CLEANUP=1 brew reinstall node@26`；當輪 formula 已核對為 26.13.0，保留舊 keg 與原全域套件，未改 shell 設定或安裝其他版本管理器。
- 本機 `.nvmrc` 與兩個 CI workflow 統一為 Node 26.13.0；技術驗證 package／lock engines 同步為 `^26.13.0`。Hugo 本機 0.168.0／CI 0.167.0 保留，現在終端與 report 的 check warnings 都會明示不同版本。
- 根目錄安裝命令：`npm install pele@1.13.0 --save-exact --ignore-scripts --omit-lockfile-registry-resolved=false --cache /private/tmp/blog-node26-20261101/npm-cache`；以命令覆寫個人省略 resolved 的設定，保留根目錄鎖檔的固定 registry URL 與 integrity，未改個人 npm 設定。安裝當輪回報 0 vulnerabilities，不代表未來或全部技術教學的安全性。
- 本輪 Python 單元測試 48 項通過；圖表 7 項通過；首輪網站 12 項全部通過。沒有把歷史 44 項 Skills 差異比較當作本輪重跑結果。
- 首次未升權的 npm registry 查詢因 sandbox DNS 失敗；經核准的 registry 查詢與安裝成功。首次瀏覽器導航早於預覽服務啟動而失敗，服務啟動後重新開頁完成驗收；失敗沒有列為通過。
- 互動式 zsh 啟動時，sandbox 阻止 oh-my-zsh 快取／completion 檔案寫入，留下啟動警告；未更動 shell 設定。後續乾淨的登入 shell 已確認 Node 版本，證據為 `runtime-after.json`，互動式嘗試輸出另留 `runtime-interactive-attempt.log`。
- 文件收尾命令：`python3 .github/scripts/verify-blog.py --output /private/tmp/blog-node26-20261101/site-final`。此處預先記錄位置；最終成功需實際確認該 report 的 `status: passed`、12 項通過及 `source_unchanged: true`。
- 限制：未在本輪執行 CI 固定 Hugo 0.167.0、Ubuntu CI、全部 Java／Spring／Vue／Angular 技術教學或 Obsidian 應用程式；技術工具套件未整組升級。圖表載入失敗／語法錯誤由自動案例驗證，本輪瀏覽器未注入這些故障。
- 未提交、推送或部署。下一步：讀取最終 report，確認通過且來源未變後交付。
