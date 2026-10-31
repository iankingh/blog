# Skills 收藏、使用教學與首頁置頂

## 需求與範圍

- agent-skills README 外部收藏加入 ub-mode、pstack，記錄原始連結、用途、收藏理由與待試用狀態；只收錄連結，不複製或安裝上游技能。
- Blog 新增 Skills 清單及兩篇獨立使用教學，公開網址分別為 `/blog/post/ai-skills-list/`、`/blog/post/ub-mode-guide/`、`/blog/post/pstack-guide/`；共 138 篇。
- 清單介紹三個自製技能與兩個外部收藏，連至真實 agent-skills 專案與兩篇教學；既有 AI 工具清單補上入口，保留前輪修改。
- 首頁三張置頂依序為新清單、原技能目錄文、Java 多型；HikariPool、DecimalFormat 順延，僅順位調整的舊文保留 date、lastmod 及正文。
- 保留技能圖鑑、安全設定與主題子模組；不提交、推送或部署，不把上游文件中的提交／推送指令視為本次授權。

## 驗收

| 案例（正常／錯誤／邊界） | 預期結果 | 實際證據 | 狀態 |
| --- | --- | --- | --- |
| 收藏與清單 | README 有兩筆外部收藏及待試用；新清單五個項目、GitHub 入口與兩篇教學互連 | `docs/verification/ai-skills-acceptance-2026-10-31.json`，44 項全部通過 | 通過 |
| 安裝與來源差異 | ub-mode 安裝範例保留已有目錄／軟連結；Dryer 0.82 預設與 0.8 政策分開；Claude Code 命令有前綴 | 同上；兩段 sh 語法、新目的地、已有目錄、斷裂軟連結在暫存 fixture 實際執行 | 通過 |
| 既有內容保留 | 既有 135 篇路徑與 date 不變；四篇精選僅調順位；其餘 134 筆舊查核資料不變，AI 工具清單追加紀錄 | 起始快照逐篇／逐筆比對，44 項案例內記錄結果 | 通過 |
| 首頁與圖鑑 | 第一頁三張置頂正確、第二頁沒有置頂；`/skills/` 保持圖鑑 | 生成 HTML 與 `docs/verification/ai-skills-browser-2026-10-31.json`；桌面／手機各確認首頁與第二頁 | 通過 |
| 搜尋與網站 | 138 篇唯一文章、14 頁尾頁 8 篇；三篇新文可搜尋，站內連結與安全檢查通過 | 修正後網站 report 10 項通過且來源未變；瀏覽器實際搜尋三篇標題 | 通過；收尾以最終 report 為準 |
| 桌面／手機 | 長標題可讀，頁面無水平溢位；長表格與程式碼可在容器內捲動 | 瀏覽器紀錄 16 筆最終觀察與 10 張截圖；1440／390px；鍵盤橫向捲動表格 49px、程式碼 80px | 通過 |

## 當前狀態與交班

- 狀態：文章、README 收藏、置頂、來源查核、44 項案例及瀏覽器驗收完成；文件收尾後的網站基準依最終 report 判定。
- Blog 起始 commit：`5af03a3abfb3bdde85c1650467ff59dce7474eb0`，master。原有未提交 `ai-tools.md`、`note-review.json`、`note-review.md` 及前輪 harness 紀錄完整保留後銜接。
- 起始快照：`/private/tmp/blog-skills-20261031-baseline/files.json`、`diff.patch` 與 `git-status.txt`；只作本機比對，不提交快照。
- 來源日期：2026-10-31；GitHub fetch_file 讀取 12 份上游文件，個別檔案 Git blob SHA 與範圍見 `docs/verification/ai-skills-sources-2026-10-31.json`。blob SHA 不是 repository commit；pstack manifest 版本為 0.15.36。
- 新增內容依 README、Skill、官方 guide 與 Claude Code adapter 整理。Crapper、Dryer、Mutator README 另行讀取，避免把工具預設值當作 ub-mode 政策。
- 未安裝 ub-mode、pstack 或品質工具；未執行 Cursor／Claude Code 外掛、多模型工作流或品質工具分析。技術查核是文件範圍，網站及安裝片段驗證另記實際結果。
- 第一輪網站基準：`/private/tmp/blog-skills-preview-20261031/report.json`，10 項通過且 `source_unchanged: true`。44 項內容／生成案例通過，初版記錄已產生；最終以修正後的案例與網站結果為準。
- 生成內容案例初版曾把 `ref` 的絕對網址當成必須是相對網址、把技能圖鑑內合理出現的相關文章當作內容替換、以及把兩項共用的待試用說明誤算成需出現兩次。依實際 HTML 修正案例，改核對 URL path、圖鑑 H1 與技能卡，以及兩項共用的狀態文字；未修改產品以迎合錯誤判準。
- 手機首次檢查：390px 頁面無水平溢位，但三欄表格壓縮至 314px，欄內換行過密；三篇新文章改用既有 `wideTables: true`，保留欄寬並在表格容器內捲動，沒有新增 CSS 或放寬安全設定。
- 網站基準：`python3 .github/scripts/verify-blog.py`。本機 Hugo 為 0.168.0 Extended，CI 固定 0.167.0；本輪不變更工具版本。
- 修正後網站命令：`python3 .github/scripts/verify-blog.py --output /private/tmp/blog-skills-wide-tables-20261031`；report 的 `status: passed`、10 項全部通過且 `source_unchanged: true`。
- 內容驗收：`docs/verification/ai-skills-acceptance-2026-10-31.json`，44 項通過，使用上述真實建置 HTML。重跑腳本為 `/private/tmp/verify-blog-skills-20261031.py`；完整基線與網站產物留在本機暫存目錄。
- 瀏覽器：`docs/verification/ai-skills-browser-2026-10-31.json`，IAB 1440×1000 與 390×844，三篇新文、首頁／第二頁、技能圖鑑、實際搜尋及鍵盤捲動通過。已還原 viewport；保留 `http://127.0.0.1:1317/blog/` 首頁預覽。
- 截圖：`/private/tmp/blog-skills-home-desktop-20261031.jpg`、`/private/tmp/blog-skills-home-mobile-20261031.jpg`；其餘文章與程式碼截圖的完整路徑在瀏覽器紀錄。
- 首次啟動預覽的 `--renderToMemory` 與 `--destination` 不相容，移除後又遇 sandbox 禁止 bind；以核准的本機 loopback Hugo 伺服器完成檢查，並未改動網站安全設定。未把啟動失敗算成驗收成功。
- 圖鑑原有 H1 包含「技能圖鑑」與「Skill Codex」；瀏覽器斷言依實際雙語標題及圖鑑結構確認，沒有移除合理出現的新文章入口。
- 文件收尾命令：`python3 .github/scripts/verify-blog.py --output /private/tmp/blog-skills-final-20261031`。此處預先記錄輸出位置；最終結果必須讀取該目錄 `report.json` 與 `logs/`，不能從路徑或前一輪結果推定。
- 剩餘限制：未安裝或試用外部技能、外掛、多模型角色與品質工具，未重跑其他技術教學或 CI 固定 Hugo 版本。安裝測試僅在臨時資料夾以假 Skill 檔驗證複製與保留行為，未寫入個人技能目錄。未提交、推送或部署。
- 下一步：確認最終 report 通過且來源未變後交付；公開網站仍待另外提交與部署。
