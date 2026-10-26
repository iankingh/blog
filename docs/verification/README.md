# 隔離範例驗證

此目錄只用於筆記驗證，不是部落格的前端依賴，也不參與 Hugo 部署。逐篇結果見 [`../note-review.json`](../note-review.json)。測試直接抽取 Markdown 程式碼；路由骨架與平台替代資料另有明確 fixture。

## Java、Python、Git

```bash
python3 .github/scripts/check-basic-note-examples.py /tmp/blog-basic-results.json
python3 .github/scripts/check-java-notes.py --classpath '/tmp/blog-java-libs/*' --results /tmp/blog-java-results.json
python3 -m unittest discover -s .github/scripts -p 'test_jdk25.py'
```

兩支腳本要求 `java`、`javac` 主版本均為 25，使用 `javac -encoding UTF-8` 原生編譯，逐一確認 class major version 為 69，再比對標準輸出。第一個命令涵蓋六個 Java 練習、Python ipaddress，並在暫存 Git 儲存庫測差異匯出。第二個命令需要文章指定的 HikariCP 7.0.2、H2 2.4.240、SLF4J API 2.0.17 JAR；不會自動下載依賴。

## Vue、Angular、JavaScript

工具環境固定為 Node.js 24.22.1 LTS／npm 11.20.0（在儲存庫根目錄執行 `nvm use`）。
2026-10-23 升級驗證工具依賴至 Angular 22、TypeScript 6、Vite 8、Pinia 4 與 Vue Router 5；
文章保留各自介紹的版本，這組工具驗證的是範例在目前工具鏈上的相容性，不能當作原版本的驗證證據。

複製測試檔與鎖檔到獨立資料夾，再安裝固定依賴。先將 `BLOG_NOTES_ROOT` 設為實際儲存庫絕對路徑：

```bash
mkdir -p /tmp/blog-web-lab
cp docs/verification/*.mjs docs/verification/package*.json /tmp/blog-web-lab/
export BLOG_NOTES_ROOT="$PWD"
export BLOG_RESULTS=/tmp/blog-web-results.json
npm ci --prefix /tmp/blog-web-lab
node /tmp/blog-web-lab/check-web-examples.mjs
node /tmp/blog-web-lab/check-angular-examples.mjs
node /tmp/blog-web-lab/check-additional-examples.mjs
```

Vue 驗證 38 個 SFC、30 個 Vite 建置、直接匯入 store／composable、memory history 與 SSR 字串；14 章為路由概念，30 章為 SSR，兩者不用一般 Vite SPA 建置。Angular 使用 `ngc` 的 strict／strictTemplates 編譯，表單／pipe 等方法另執行測試；輔助 Home／About 元件是 fixture。

JavaScript DOM 使用 jsdom；列印只確認呼叫與樣式。matchMedia 的裝置能力是模擬值，HEIC 解碼器回傳假 Blob，用來核對事件與清理，不代表實際圖片解碼。Canvas 僅編譯與測錯誤尺寸，未驗證像素、方向或色彩。

此次 macOS 使用 Node 26.5.0、JDK 25.0.4.1；Java 範例均原生編譯為 Java 25，沒有設定較舊的目標版本。Angular 20 的官方 Node 相容範圍應由文章版本表選擇；本次只執行 ngc，不能以 Node 26 編譯成功推定完整 Angular CLI 受支援。

## Spring

```bash
java -version
javac -version
mvn -version
python3 docs/verification/check-spring-notes.py /tmp/blog-spring-lab --results /tmp/blog-spring-results.json
# 若需要指定隔離 Maven 快取，可加 --maven-repo /tmp/blog-m2
```

從六篇 Spring 筆記抽出主程式、設定及文章測試，額外 fixture 核對 `/api/hello`、`/v3/api-docs` 、dev profile 及衍生／JPQL／native 查詢。固定 Spring Boot 3.5.16／JDK 25／springdoc 2.8.9，資料庫使用 H2 2.3.232，共 8 個測試；未連外部 DB 或叢集。共用文章 POM 以 dependency plugin 的 properties goal 取得 mockito-core JAR 路徑，Surefire 透過 `-javaagent` 載入該版本；不需填入機器專屬路徑。驗證工具確認 Maven 使用 JDK 25、執行 `clean test`、檢查主程式與測試 class 均為版本 69，並核對 8 tests／0 failure／0 error／0 skipped。Spring Cloud 舊筆記提供 JDK 25 的替代路線，未在本次啟動 Eureka／Gateway，不能視為這 8 項測試的範圍。

## 網站

Mermaid 圖表整合使用根目錄固定版本的 Pele，自動檢查不依賴 `node_modules`：

```bash
node .github/scripts/check-diagrams.cjs
```

此命令使用實際發布的同源 bundle 驗證圖表來源、SVG 識別碼及原始碼退路；DOM 回呼案例為隔離 fixture，實際排版、CSP 執行與晝夜／窄螢幕行為仍需瀏覽器檢查。本命令已納入網站統一驗證。

```bash
hugo --minify --destination /tmp/blog-review-output
python3 .github/scripts/check-note-content.py --site /tmp/blog-review-output
node .github/scripts/check-search.cjs
python3 .github/scripts/check-site-security.py /tmp/blog-review-output
```

內容檢查由完整且不重複的檢核清單推導筆數，核對發布日期、摘要／情境／來源、程式碼區塊、內部連結與圖片。2026-10-20 為 132 篇、搜尋 132 筆，首頁／筆記列表各 14 頁，前 13 頁每頁 10 筆，尾頁 2 筆。技術正確性仍需按逐篇查核紀錄的版本與來源閱讀。

## Fred 影片筆記的新範例

```bash
python3 docs/verification/check-fred-examples.py --results /tmp/blog-fred-results.json
```

直接抽取新文章的 Java 與 JavaScript 程式碼，在隔離暫存目錄執行。Java 要求原生 JDK 25、確認 class 69 並比較輸出；Node 核對區間邊界、無效輸入與全部 10000 個索引的權重計數。Redis Lua 僅作文件查核，沒有本機 Redis、叢集或活動壓測；沒有連線 S3。結果見 [`fred-examples-results-2026-10-20.json`](fred-examples-results-2026-10-20.json)。本命令不由一般網站驗證自動執行。
