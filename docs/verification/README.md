# 隔離範例驗證

此目錄只用於筆記驗證，不是部落格的前端依賴，也不參與 Hugo 部署。逐篇結果見 [`../note-review.json`](../note-review.json)。測試直接抽取 Markdown 程式碼；路由骨架與平台替代資料另有明確 fixture。

## Java、Python、Git

```bash
python3 .github/scripts/check-basic-note-examples.py /tmp/blog-basic-results.json
python3 .github/scripts/check-java-notes.py --classpath '/tmp/blog-java-libs/*'
```

第一個命令使用 JDK 的 `--release 8` 編譯六個 Java 練習、執行 Python ipaddress，並在暫存 Git 儲存庫測差異匯出。第二個命令需要文章指定的 HikariCP 7.0.2、H2 2.4.240、SLF4J API 2.0.17 JAR；不會自動下載依賴。

## Vue、Angular、JavaScript

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

此次 macOS 使用 Node 26.5.0、JDK 25.0.4.1；Java 分別以 release 8／21 編譯。Angular 20 的官方 Node 相容範圍應由文章版本表選擇；本次只執行 ngc，不能以 Node 26 編譯成功推定完整 Angular CLI 受支援。

## Spring

```bash
python3 docs/verification/prepare-spring-lab.py /tmp/blog-spring-lab
mvn -f /tmp/blog-spring-lab/pom.xml test
```

從六篇 Spring 筆記抽出主程式、設定及文章測試，額外 fixture 核對 `/api/hello`、`/v3/api-docs` 、dev profile 及衍生／JPQL／native 查詢。固定 Spring Boot 3.5.0／springdoc 2.8.9，資料庫使用 H2 2.3.232，共 8 個測試；未連外部 DB 或叢集。若 JDK／執行環境禁止 Mockito 自行附加 agent，可依 Mockito 官方說明於 Surefire `argLine` 提供該版本 mockito-core 的 `-javaagent`；此次 JDK 25 隔離執行採此方式。

## 網站

```bash
hugo --minify --destination /tmp/blog-review-output
python3 .github/scripts/check-note-content.py --site /tmp/blog-review-output
node .github/scripts/check-search.cjs
python3 .github/scripts/check-site-security.py /tmp/blog-review-output
```

內容檢查涵蓋 130 篇檢核紀錄、保留發布日期、摘要／情境／來源、程式碼區塊、內部連結與圖片、搜尋 130 筆，以及首頁／筆記列表各 13 頁，每頁 10 筆。技術正確性仍需按逐篇查核紀錄的版本與來源閱讀。
