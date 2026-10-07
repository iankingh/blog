# 全部筆記整理與驗證報告

此次完成 130 篇筆記，原 73 篇公開筆記與 57 篇草稿均已整理並公開。保留檔案路徑、原文章網址與原始發布日期；2026-10-06 開始修訂，2026-10-07 完成逐篇驗證範圍與公開狀態更新，lastmod 使用實際修訂日期。

64 篇有隔離執行、編譯或模擬流程測試，另 66 篇以官方文件、原廠入口或規格查核。編譯通過、假資料與實際平台執行分別記錄，不能互相替代。

## 共通驗證結果

- Hugo Extended 0.167.0 正式建置，不使用 -D；搜尋索引收錄 130 篇唯一筆記。
- 首頁和筆記列表各 13 頁，每頁 10 篇；任務卡片最多兩欄，手機單欄，列表只顯示最近更新日期。
- 130 篇摘要、情境、分類／標籤、程式碼語言、來源與查核範圍完成檢查，無空白 code fence、未完成標題或合併衝突標記。
- 346 個 HTML 頁面的內部連結、錨點、圖片／資源與圖片 alt 檢查通過；搜尋載入、快取、競態、失敗重試、文字安全與焦點測試通過，網站安全檢查通過。
- Java 六個基礎練習以 JDK25 --release8 編譯及逐字輸出比對；另三個既有 Java 範例以 --release21 重跑，DecimalFormat 加測德文預設 locale，HikariCP 使用文章指定依賴。
- Vue 38 個 SFC 語法／模板編譯及 30 個 Vite 正式建置通過，另測 composable、Pinia／Vuex、memory router、SSR renderToString。
- Angular 9 個 TypeScript 區塊通過 strict 與 strictTemplates 編譯，表單、pipe、JS 匯入與圖片錯誤尺寸分支執行通過。此為 compiler 測試，不代表完整 CLI／UI 已於 Node26 實測。
- Spring Boot3.5.0、springdoc2.8.9 共 8 個測試通過，含條件 Bean、dev profile、API／OpenAPI、JPA 分頁／查詢與真實 proxy 交易回滾；資料庫是隔離 H2。
- JavaScript DOM 範例測清單、選擇／錯誤資料、搜尋與列印呼叫；matchMedia 使用假裝置值，HEIC 使用假轉換器與 Blob 測流程，沒有宣稱實際 HEIC 解碼或紙張列印完成。
- Python IP 計算及 Git 匯出腳本實測通過，Git 涵蓋檔名空格、新增、修改、刪除與無差異。

## 平台與來源限制

Windows／IE11、CentOS／Docker daemon、Redis、Tomcat、Nginx、Eclipse、Android、SQL Server、Kafka／Eureka／Gateway 叢集與外部帳號服務，未在本次 macOS 執行實機操作。文章保留適用版本、完成操作說明與讀者可自行確認的結果；舊版情境另列替代路線。資料復原沒有操作真實磁碟，安全設定沒有操作正式服務。

來源 URL 共 324 個，其中 320 個成功開啟；HTTP 成功只證明入口可讀，不代表版本、範例與原系統全部驗證完成。Phind 官方首頁本次回 404，AI 清單保留為歷史入口，未推定服務仍可使用；catb 的提問文章與兩個 GNU 手冊入口逾時，原連結保留並記錄失敗。已搬移的 Docker／Hugo／draw.io 文件入口已修正。

## 逐篇整理結果

下表的「測試」包含編譯或明確標示的 mock；實際範圍請閱讀下表「實際驗證」及 JSON 清單的 verification 欄位。每篇均已公開，版本與原來源保留在文章和完整 JSON 清單。

| # | 原檔案／文章 | 原狀態 | 修訂重點 | 實際驗證 |
| --- | --- | --- | --- | --- |
| 1 | [AI 工具清單：聊天、搜尋與翻譯](../content/post/ai-tools.md) | 公開 → 修訂 | 依用途整理原工具入口與限制，將清單和未來 skills／agents專案的責任分開。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 2 | [Android Studio 第一個專案：模板、SDK 與執行確認](../content/post/android/AndroidBsN01.md) | 公開 → 修訂 | 保留建立專案流程，補上 Compose／Views差異、Gradle JDK與模擬器驗收。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 3 | [Angular NullInjectorError：定位缺少的 provider](../content/post/angular/Angular-NullInjectorError.md) | 公開 → 修訂 | 補上錯誤鏈閱讀、服務註冊及 HttpClient 的新舊配置差異。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出） |
| 4 | [Angular 範本驅動表單：ngModel 與驗證](../content/post/angular/Angular-forms-Template-Driven-Forms.md) | 草稿 → 公開 | 補齊原空白筆記，以名稱表單示範 FormsModule、name、required 與提交。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出） |
| 5 | [Angular Reactive Forms：模型、驗證與提交](../content/post/angular/Angular-forms.md) | 草稿 → 公開 | 整理兩種表單的適用情境，補上型別化 FormGroup 與完整範例。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出） |
| 6 | [Angular npm 安裝錯誤：peer dependency 診斷](../content/post/angular/Angular-npm-Error.md) | 公開 → 修訂 | 補上 Node、Angular、TypeScript 相容檢查，避免以 force 跳過真正的版本衝突。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 7 | [Angular CLI 專案結構：舊 NgModule 與新版差異](../content/post/angular/AngularBsN02.md) | 公開 → 修訂 | 保留 Angular 初學專案架構，補上設定檔責任、生成版本差異與啟動檢查。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 8 | [Angular CLI：開發、產生程式碼與建置](../content/post/angular/AngularCLInotes.md) | 公開 → 修訂 | 整理 serve、generate、build、test 與 update，補上本機 CLI 和 outputPath 確認。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 9 | [Angular 小抄：模板、生命週期、DI 與路由](../content/post/angular/AngularCheatSheet.md) | 草稿 → 公開 | 重整過時 API 與不完整範例，提供核心概念對照及完整路由接線。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器 |
| 10 | [Angular 部署 Tomcat：base href、靜態檔與子路徑](../content/post/angular/AngularDeployTomcat.md) | 公開 → 修訂 | 補上建置輸出與部署驗證，區分 SPA fallback、hash 路由與 API 404。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 11 | [Angular 目錄設計：依功能分組與共用邊界](../content/post/angular/AngularFileStructure.md) | 公開 → 修訂 | 保留小型與多模組專案的比較，將目錄範例整理為可依需求擴充的功能架構。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 12 | [Angular 與 IE11：歷史相容維護及遷移](../content/post/angular/AngularOnIE11.md) | 公開 → 修訂 | 標示 IE11 支援終止的版本界線，移除過時 beta shim 的直接套用建議。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 13 | [Compodoc：產生 Angular 檔案與檢查輸出](../content/post/angular/AngularUseCompodoc.md) | 公開 → 修訂 | 修正 CLI 選項與註解範例，補上輸入 tsconfig、版本固定及檔案範圍。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器 |
| 14 | [Angular 引入 JavaScript：ES module 與全域 script](../content/post/angular/AngularUseJavaScript.md) | 公開 → 修訂 | 清除原合併衝突與重複段落，區分 allowJs、型別宣告與 angular.json scripts。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出） |
| 15 | [Angular 圖片縮放：Canvas 與型別化 Service](../content/post/angular/angular-resize-base64-image.md) | 草稿 → 公開 | 補上比例計算、載入錯誤與空 context 處理，區分縮放和格式轉換。 | Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出） |
| 16 | [Gradle 編碼排錯：JavaCompile 與 Javadoc](../content/post/build-tools/gradle-error.md) | 公開 → 修訂 | 以有效 build.gradle 取代空白範本，區分來源編碼與 Javadoc 語法錯誤。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 17 | [Docker 常用指令：映像、容器與排錯](../content/post/docker/docker-command.md) | 公開 → 修訂 | 整理容器生命週期、日誌、資源與空間檢查，改用正確引數並限制操作到練習容器。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 18 | [Docker Compose：Web 與 Redis 的完整練習](../content/post/docker/docker-compose.md) | 公開 → 修訂 | 補齊原筆記空白 Dockerfile，以 Node Web 和 Redis 示範服務名稱解析、健康檢查與持久化。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 19 | [Dockerfile：建立靜態網頁映像](../content/post/docker/docker-file.md) | 公開 → 修訂 | 從完整 Dockerfile 與 HTML 建置映像，補上 context、快取、COPY 及執行結果。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 20 | [Docker Swarm：服務部署、更新與回滾](../content/post/docker/docker-swarm.md) | 草稿 → 公開 | 補上 manager 初始化與單節點練習，整理 service、replica、task 與環境變數更新。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 21 | [Docker Volume：持久化、掛載與備份](../content/post/docker/docker-volumes.md) | 草稿 → 公開 | 重整 volume、bind mount 與唯讀掛載範例，補上實際寫入確認、備份還原與多主機限制。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 22 | [CentOS 8 的 Docker 安裝紀錄與替代路線](../content/post/docker/install-docker-on-centos8.md) | 公開 → 修訂 | 標示 CentOS Linux 8 結束維護，區分歷史套件操作與目前受支援系統的安裝確認。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 23 | [Windows WSL 2 與 Docker：安裝前檢查及錯誤排除](../content/post/docker/install-docker-on-windows-WSL.md) | 公開 → 修訂 | 保留 0x80370102 與 0xc03a001a 情境，補上虛擬化、WSL 狀態與 Docker 整合的診斷順序。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 24 | [Eclipse 型別階層：檢視繼承與實作](../content/post/eclipse/OpenTypeHierarchy.md) | 公開 → 修訂 | 補上選取型別、切換階層檢視及無法找到子類別時的檢查方式。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 25 | [Eclipse UTF-8：工作區、專案與建置一致性](../content/post/eclipse/eclipseSettingUtf-8.md) | 公開 → 修訂 | 補齊編碼設定層級、換行與 Maven／Gradle 的一致性檢查，避免只改顯示設定。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 26 | [Eclipse 與 JUnit 5：建立並執行測試](../content/post/eclipse/eclipseUseJUnit.md) | 公開 → 修訂 | 補上完整測試與 Maven 依賴，確認 IDE 測試及命令列建置使用同一版本。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 27 | [Git 匯出版本差異：固定目標提交並保留空白路徑](../content/post/git/GIT-export-diff-file.md) | 公開 → 修訂 | 補齊從兩個版本匯出改動檔案的可靠指令碼，排除刪除檔並記錄刪除清單。 | 隔離Git repo測空白檔名、修改/新增/刪除與無差異ZIP，內容與目標提交一致 |
| 28 | [Git 分支同步：把主分支更新帶入工作分支](../content/post/git/git-branch-update-master.md) | 公開 → 修訂 | 說明 fetch、fast-forward 與 merge 的差異，補上衝突處理及中止方式。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 29 | [Git 基本流程：檢查、暫存與提交](../content/post/git/git-command.md) | 草稿 → 公開 | 補齊 status、diff、add、commit 的操作順序，區分工作目錄與暫存區。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 30 | [Git 提交訊息：Conventional Commits 與拆分原則](../content/post/git/git-commit-message.md) | 草稿 → 公開 | 修正 type、scope 的格式，提供繁體中文提交示例與不相容變更標示。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 31 | [Git 排錯：本機修改阻擋切換與合併衝突](../content/post/git/git-error.md) | 公開 → 修訂 | 以儲存修改為起點，補上 stash、衝突診斷與復原確認，移除無條件 hard reset 的建議。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 32 | [Git 日常筆記：遠端、忽略規則與回復提交](../content/post/git/git-note.md) | 公開 → 修訂 | 重整易混淆指令，區分 revert、reset 與工作目錄還原。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 33 | [GitLab 認證失敗：HTTPS 憑證與 SSH 診斷](../content/post/git/gitLab-error.md) | 公開 → 修訂 | 補上 token、認證快取與 SSH 的核對順序，區分 401、403、憑證和網路問題。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 34 | [Hugo 程式碼高亮：Prism 與內建 Chroma](../content/post/hugo/HugoAddPrism.md) | 公開 → 修訂 | 說明原 Prism 整合方式與現行 Hugo 高亮選擇，避免雙重包裝同一段程式碼。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 35 | [Hugo Disqus：識別碼、本機停用與留言整合](../content/post/hugo/HugoAddisqus.md) | 公開 → 修訂 | 補上穩定討論識別碼與動態載入限制，修正為本機啟用留言的錯誤建議。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 36 | [Hugo GA4：正式站載入與事件確認](../content/post/hugo/hugoAddGoogleAnalytics.md) | 公開 → 修訂 | 補上本站的本機停用行為、Measurement ID 與 GA4 的實際驗證範圍。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 37 | [Hugo 基礎：建立文章、圖片與本地建置](../content/post/hugo/hugonotes.md) | 公開 → 修訂 | 修正安裝及 static 路徑，補上草稿、發布／更新日期與子目錄預覽流程。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 38 | [HikariCP 連線逾時：診斷與可重現範例](../content/post/java/HikariPool-1-error.md) | 公開 → 修訂 | 保留連線池耗盡重現程式，補上適用依賴版本及相關 Java 筆記。 | JDK25 --release21，HikariCP7.0.2／H2 2.4.240／SLF4J2.0.17，借滿、逾時與釋放後再借的輸出逐字比對通過 |
| 39 | [Java heap space：記憶體不足的診斷與確認](../content/post/java/Java-heap-space.md) | 公開 → 修訂 | 區分堆空間不足、GC 壓力與資源未關閉，補上 heap dump 診斷及 Tomcat 設定位置。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 40 | [Java 數字格式：DecimalFormat 與 BigDecimal](../content/post/java/java-DecimalFormat.md) | 公開 → 修訂 | 保留格式與金額範例，查核 Locale、捨入及精度，補上系列連結。 | JDK25 --release21 執行，預設 locale 與德文 locale 的標準輸出逐字比對均通過 |
| 41 | [Java 排錯：編譯問題、例外與版本不一致](../content/post/java/java-error.md) | 草稿 → 公開 | 建立編譯、類別載入與執行例外的診斷順序，補齊 Eclipse unresolved compilation problems 的處理。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 42 | [Java 入門 00：JDK 安裝與環境確認](../content/post/java/java_tutorial_0.md) | 公開 → 修訂 | 保留 Windows 的 Java 8 設定情境，補上 JDK 選擇、正確版本指令與 PATH 排錯。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 43 | [Java 入門 01：編譯並執行第一支程式](../content/post/java/java_tutorial_1.md) | 公開 → 修訂 | 從 HelloJava.java 到 class 檔，補上檔名規則、classpath、預期輸出與常見錯誤。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 44 | [Java 入門 02：基本型別、預設值與跳脫字元](../content/post/java/java_tutorial_2.md) | 公開 → 修訂 | 修正 boolean 大小與浮點範圍說明，示範數值提升、欄位預設值及字元輸出。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 45 | [Java 入門 03：變數、初始化與作用域](../content/post/java/java_tutorial_3.md) | 公開 → 修訂 | 補齊區域、實體及靜態變數的差異，使用完整範例觀察兩個物件的狀態。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 46 | [Java 入門 04：封裝、繼承與多型](../content/post/java/java_tutorial_4.md) | 公開 → 修訂 | 以技能介面和角色物件示範物件導向，補上可執行程式與設計限制。 | JDK25以--release 8編譯並執行，標準輸出與本文完全一致 |
| 47 | [Java 多型：介面、覆寫與執行時派發](../content/post/java/polymorphism.md) | 公開 → 修訂 | 保留完整多型範例，補上系列導覽與編譯／執行結果查核。 | JDK25 --release21 編譯，標準輸出逐字比對通過 |
| 48 | [HEIC 轉 JPEG：heic2any 的載入、錯誤與輸出限制](../content/post/javascript/Heic2any.md) | 公開 → 修訂 | 補上 Blob 陣列、錯誤處理與 object URL 清理，區分圖片轉換和 metadata 保留。 | 本文事件流程以假 Blob／轉換器測單張、陣列、錯誤、input 恢復與 URL 清理；未提供 HEIC 樣本，未驗證真實解碼、方向、色彩或 metadata |
| 49 | [列印隱藏按鈕：CSS print media 與預覽確認](../content/post/javascript/Hide-Button-when-printing.md) | 公開 → 修訂 | 以有效 HTML 與列印樣式取代不存在的 div media 屬性，補上列印預覽驗證。 | 本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試 |
| 50 | [JavaScript 陣列產生表格：安全文字與完整欄位](../content/post/javascript/array-Create-Table.md) | 公開 → 修訂 | 以小型本地資料取代過長的銀行清單，保留陣列轉表格情境並補上文字轉義。 | 本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試 |
| 51 | [行動裝置偵測：以版面與功能能力取代 UA 猜測](../content/post/javascript/detect-mobile-device.md) | 公開 → 修訂 | 保留 userAgent 比對的歷史情境，補上 matchMedia、觸控與鍵盤測試的限制。 | 本文 HTML 在 jsdom 以 matchMedia fixture 測初始輸出與 change 事件；未辨識實際手機硬體 |
| 52 | [JavaScript 核心複習：型別、作用域與物件傳遞](../content/post/javascript/joinWillJavaScriptCourse.md) | 草稿 → 公開 | 保留課程主題，修正傳值、原始型別與全域性變數的誤解，補上可執行觀察。 | Node實際執行，輸出與本文一致 |
| 53 | [JavaScript JSON 下拉選單：解析、選項與選取結果](../content/post/javascript/select-JsonList.md) | 草稿 → 公開 | 保留機構清單選取情境，補上 JSON 格式檢查、預設選項及安全渲染。 | 本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試 |
| 54 | [JavaScript 表格搜尋：保留欄位並篩選整列](../content/post/javascript/table-Search.md) | 草稿 → 公開 | 修正原本隱藏個別儲存格造成的欄位錯位，補上計數與空結果。 | 本文HTML直接於jsdom執行，核對DOM／事件與錯誤分支；列印只驗證print呼叫及樣式，紙張輸出未實機測試 |
| 55 | [Kafka Eagle／EFAK：歷史監控配置與 Kafka 版本界線](../content/post/kafka/kafka-eagle.md) | 草稿 → 公開 | 重整舊 ZooKeeper 配置，補上 listener、JMX、認證與 KRaft 替代的核對順序。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 56 | [CentOS Linux 8 安裝紀錄：VM 流程與 EOL 說明](../content/post/linux/Install-CentOS-8.md) | 草稿 → 公開 | 補齊原本空白的安裝章節，採 VM 說明磁碟、網路與帳號設定，標示替代發行版。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 57 | [Linux 基礎指令：路徑、檔案與許可權](../content/post/linux/LinuxCommand.md) | 公開 → 修訂 | 修正 HOME 變數與 chmod 範例，以明確檔案展示讀寫及執行許可權。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 58 | [Linux 網路工具：ss、systemctl 與 firewalld](../content/post/linux/linux-must-install-software.md) | 公開 → 修訂 | 補齊網路與防火牆診斷，修正 firewalld state 和 zone 的混淆。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 59 | [IP 與子網：IPv4、IPv6、私有位址和 CIDR](../content/post/net/IP.md) | 公開 → 修訂 | 修正所有 IP 都全域唯一的說法，補上私有範圍、路由與可重現的子網計算。 | Python ipaddress實際執行，四行輸出一致 |
| 60 | [SSL、TLS 與 HTTPS：憑證、握手和驗證限制](../content/post/net/SSLandTLSandHttps.md) | 公開 → 修訂 | 修正鎖頭代表網站可信的說法，區分加密、憑證與應用安全，補上排錯順序。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 61 | [Chrome DevTools Overrides：本地模擬回應與保留修改](../content/post/net/chromeTools.md) | 公開 → 修訂 | 補上建立 override、確認生效和停用流程，區分 DOM 修改與真正來源檔案。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 62 | [hosts 設定：本地名稱對映與 DNS 診斷](../content/post/net/hosts.md) | 公開 → 修訂 | 補上有效格式、平臺路徑與驗證方式，區分 hosts、DNS 快取與 HTTPS 憑證。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 63 | [Windows 路由：字首、介面與暫時規則](../content/post/net/windows-route.md) | 公開 → 修訂 | 補上最長字首優先與 metric 比較，提供有前提的測試路由及精確移除方式。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 64 | [Windows 網路排錯：IP、DNS、TCP 與程式](../content/post/net/windowsNetCmd.md) | 公開 → 修訂 | 修正 Run 快捷鍵及混用 Linux netstat 引數，建立分層診斷順序。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 65 | [Windows Nginx：靜態站、反向代理與設定檢查](../content/post/nginx/NginxForwindows.md) | 草稿 → 公開 | 補上完整 nginx.conf，保留 Windows 路徑與 reload 操作並說明平臺限制。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 66 | [FTP、FTPS 與 SFTP：協定和連線埠差異](../content/post/other/FTPvsFTPSvsSFTP.md) | 草稿 → 公開 | 修正主動／被動模式的方向及 FTPS 分類，提供連線選擇與診斷依據。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 67 | [高可用性架構：Active-Active、備援與故障測試](../content/post/other/HighAvailability.md) | 公開 → 修訂 | 查核原 HA 說明，區分負載平衡、資料一致性、RTO/RPO 與單點故障。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 68 | [Java 工程師學習地圖：基礎、交付與架構能力](../content/post/other/Java技術人員技能.md) | 公開 → 修訂 | 將原技術名單整理為可驗證的能力層級，保留 Spring、容器、資料與測試主題。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 69 | [Markdown 筆記：語法、程式碼與 Hugo 差異](../content/post/other/Markdown.md) | 公開 → 修訂 | 修正連結語法，將示例放入程式碼區塊，區分 CommonMark、表格與 Mermaid 擴充。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 70 | [系統分析 SA：釐清需求與可驗收規格](../content/post/other/SA.md) | 公開 → 修訂 | 將原對話摘要整理為需求分析流程，補上衝突需求、產物與驗收例子。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 71 | [技術提問：重現步驟、預期結果與診斷證據](../content/post/other/ask-questions.md) | 公開 → 修訂 | 保留原提問與除錯主題，整理成可複製模板，移除難以辨識來源的個人經驗敘事。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 72 | [技術閱讀清單：Spring、全端與 JavaScript 的選讀方式](../content/post/other/book.md) | 草稿 → 公開 | 保留原待讀書單，補上主題、版本限制與閱讀產出，不假裝已完成閱讀。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 73 | [Windows MongoDB：免安裝配置與 mongosh 確認](../content/post/other/mongodb_install.md) | 公開 → 修訂 | 保留 ZIP 安裝情境，補上有效 YAML、資料目錄、localhost 與 shell 測試。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 74 | [Vagrant：VM 生命週期、SSH 與共享檔案](../content/post/other/vagrant.md) | 公開 → 修訂 | 修正 provision 和 ssh-config 的用途，保留歷史 CentOS box並補上目前選版方法。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 75 | [Windows 開發工具清單：用途與安裝後檢查](../content/post/other/windows_裝機必裝.md) | 公開 → 修訂 | 將原裝機名單分類，補上重複功能取捨、來源與版本記錄。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 76 | [Windows 修復環境複製資料：Notepad 與磁碟辨識](../content/post/other/使用notepad指令救援資料.md) | 公開 → 修訂 | 保留 WinRE 檔案對話方塊的操作情境，區分一般檔案複製與真正故障磁碟救援。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 77 | [前後端分離：API 契約、部署與成本](../content/post/other/前後端分離.md) | 公開 → 修訂 | 保留架構比較，補上契約例子、驗證責任與匯入判斷。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 78 | [軟體與網路名詞：NAT、代理、加密與認證](../content/post/other/名詞.md) | 公開 → 修訂 | 補齊原空白術語，修正 ping、Socket 與數位簽章的混淆。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 79 | [API 文件工具：OpenAPI、Slate 與 apiDoc 的選擇](../content/post/other/寫程式API文件的工具.md) | 公開 → 修訂 | 補上契約來源、生成方式與限制，提供最小 OpenAPI 檔案。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 80 | [流程圖工具：Mermaid 文字圖與圖形編輯器](../content/post/other/畫流程圖的工具.md) | 草稿 → 公開 | 補上可修改的流程圖範例、匯出方式與用途比較，不再只留下外部分享網址。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 81 | [金額計算與浮點誤差：整數單位、Decimal 與捨入](../content/post/other/算錢用浮點，遲早被人扁.md) | 公開 → 修訂 | 保留 0.1 加 0.2 的例子，補上金額表示、四捨五入與分攤規則。 | Node 實際執行三行浮點／整數輸出，與本文一致；業務捨入規則不由示例推定 |
| 82 | [Redis 安裝：本機 Docker 與平臺選擇](../content/post/redis/redis-Install.md) | 公開 → 修訂 | 修正 Redis port 對映及舊 Windows 移植版資訊，提供 localhost 測試與停止流程。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 83 | [Redis 指令：鍵值、到期與資料結構](../content/post/redis/redis-command.md) | 草稿 → 公開 | 補齊原本空白的 SET/GET，提供可核對結果的本地練習及 SCAN 注意事項。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 84 | [Redis 設定：監聽、記憶體與持久化](../content/post/redis/redis-config.md) | 草稿 → 公開 | 移除不能直接使用的編號設定片段，補上有效 redis.conf 與核對方式。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 85 | [Tomcat 設定：JNDI、環境變數與 JVM 引數](../content/post/server/tomcatSetEnvironment.md) | 公開 → 修訂 | 保留 context.xml 的 JNDI 情境，說明它與 OS 環境及 Spring profile 的差異。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 86 | [Tomcat server.xml：上傳限制與應用部署](../content/post/server/tomcatSetserverxml.md) | 公開 → 修訂 | 修正 maxPostSize 的範圍，補上 Connector、multipart 與獨立 Context 設定方式。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 87 | [Tomcat Manager：角色、使用者與存取範圍](../content/post/server/tomcatSettingUser.md) | 公開 → 修訂 | 修正不合法 XML 佔位值，補上 manager-gui 許可權及 401／403 診斷。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 88 | [Spring Boot API 文件：Swagger 2 歷史整合與 OpenAPI 3](../content/post/spring-boot/spring-boot-Swagger2.md) | 草稿 → 公開 | 保留 Springfox 2.2.2 情境，補上相容界線、現代 springdoc 替代與驗證方式。 | 本文 HelloController 於 MockMvc 回 /api/hello 與 /v3/api-docs，核對 JSON 與 API 路徑；未用瀏覽器呼叫 Swagger UI 或跑原 Springfox2 |
| 89 | [Spring Profile 與 Maven Profile：執行期和建置期](../content/post/spring-boot/spring-boot-active-profile.md) | 草稿 → 公開 | 補上可比較的配置與啟動命令，說明 profile 不會自動在兩種工具間同步。 | 本文 BannerConfig 與 application-dev.properties 於 @ActiveProfiles(dev) context 執行，確認 notes.banner=development；Maven profile 未另設情境 |
| 90 | [ConditionalOnProperty：條件式 Bean 與測試](../content/post/spring-boot/spring-boot-conditionalOnProperty.md) | 草稿 → 公開 | 清除 TODO 與過時註解屬性，完整示範存在、false、true 和缺值的行為。 | 直接編譯本文 DemoConfig／DemoConfigTest，true／false／缺值 3 個 ApplicationContextRunner 測試通過 |
| 91 | [Spring Boot 核心觀念：自動配置、設定與可驗證回答](../content/post/spring-boot/spring-boot-interview.md) | 公開 → 修訂 | 查核原面試題中的過度簡化說法，補上共用練習專案與實際診斷方式。原二十題主題逐項對照並補上版本界線。 | 隔離 Spring Boot 3.5.0／Java21 target 專案建置，本文 NoteApplication 共用入口供 8 個測試使用；未測實際生產服務 |
| 92 | [Spring Cloud Eureka：服務註冊與健康確認](../content/post/spring-cloud/spring-cloud-Eureka.md) | 草稿 → 公開 | 補齊 server/client 配置、相容版本與本地雙服務確認，區分註冊和負載平衡。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 93 | [Spring Cloud Gateway：路由、過濾與 Actuator 邊界](../content/post/spring-cloud/spring-cloud-Gateway.md) | 公開 → 修訂 | 整理舊 WebFlux Gateway 配置，補上本地後端、路徑改寫與安全的端點確認。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 94 | [Spring Data JPA：Repository 與分頁查詢](../content/post/spring/spring-data-Jpa-Notes.md) | 公開 → 修訂 | 查核原 Repository 小抄，補上 Entity、查詢範例和新版排序介面的差異。補回原 Repository 介面比較、衍生查詢／JPQL／native 分類，固定 H2 實測。 | 本文 Entity、Repository 與增補查詢片段於 H2 2.3.232 實測分頁、衍生方法、JPQL 與 native query，含查無資料分支；未連 SQL Server 等外部 DB |
| 95 | [Transactional：代理、回滾與交易範圍](../content/post/spring/spring-transactional.md) | 草稿 → 公開 | 修正 Spring 與 JTA 註解比較，補上真正經過代理的回滾測試與限制。 | 本文 TaskService／TaskServiceTest 經 Spring 真實 proxy 呼叫，例外後查詢確認回滾；未模擬分散式交易 |
| 96 | [SQL Server T-SQL：建表、修改欄位與交易練習](../content/post/sql/sql-command.md) | 公開 → 修訂 | 修正 SQL Server ADD COLUMN 說法，補上完整暫存表練習與預期查詢結果。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 97 | [SQL Server 許可權：Login、User 與最小角色](../content/post/sql/sql-server.md) | 公開 → 修訂 | 補上伺服器與資料庫身份差異，以無登入測試使用者驗證 SELECT 許可權。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 98 | [VS Code Remote SSH：連線、遠端資料夾與 Vagrant](../content/post/visual-studio-code/VSCodeUseRemote.md) | 公開 → 修訂 | 補齊原測試章節，以示例主機取代真實公網地址，說明遠端server與extension範圍。 | 官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式 |
| 99 | [Vue 教學 00：學習路線與共用練習環境](../content/post/vue/vue-00-學習路線總整理.md) | 草稿 → 公開 | 建立可重現的 Vue 3 練習專案，依基礎、元件、路由、狀態管理與工程化循序完成 31 個主題。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 100 | [Vue 教學 01：宣告式畫面與第一個元件](../content/post/vue/vue-01-Vue概述.md) | 草稿 → 公開 | 用計數器理解 Vue 如何把狀態對映成畫面，區分模板、事件與應用程式掛載。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 101 | [Vue 教學 02：模板語法、表單與條件渲染](../content/post/vue/vue-02-Vue-js基礎.md) | 草稿 → 公開 | 完成可新增留言的表單，練習 v-model、事件、屬性繫結與條件顯示。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 102 | [Vue 教學 03：列表渲染與穩定的 key](../content/post/vue/vue-03-列表渲染.md) | 草稿 → 公開 | 以排序與刪除任務示範 v-for，避免用索引作為可變動清單的識別值。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 103 | [Vue 教學 04：ref、reactive 與模板引用](../content/post/vue/vue-04-ref與reactive.md) | 草稿 → 公開 | 區分響應式資料與 DOM 引用，修正原始筆記中的 TypeScript 與模板語法。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 104 | [Vue 教學 05：watch 與副作用清理](../content/post/vue/vue-05-watch監視屬性.md) | 草稿 → 公開 | 監看特定資料並取消過期操作，區分 computed、watch 與 watchEffect 的責任。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 105 | [Vue 教學 06：生命週期與資源釋放](../content/post/vue/vue-06-生命週期.md) | 草稿 → 公開 | 以計時器示範掛載、更新與解除安裝，確保元件移除後不留下背景工作。補上主要 hook、KeepAlive 與 SSR 時機對照。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 106 | [Vue 教學 07：自訂 composable 與可重用狀態](../content/post/vue/vue-07-自定義hooks.md) | 草稿 → 公開 | 把計數器邏輯抽成 useCounter，辨識每次呼叫獨立的狀態與共用單例。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支 |
| 107 | [Vue 教學 08：進階響應式、唯讀資料與插槽](../content/post/vue/vue-08-響應式進階整理.md) | 草稿 → 公開 | 比較 shallowRef、readonly 和 toRaw，並用插槽把資料邏輯與呈現分開。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 108 | [Vue 教學 09：元件拆分、props 與事件](../content/post/vue/vue-09-元件化.md) | 草稿 → 公開 | 完成可刪除的待辦元件，讓父元件持有資料、子元件回報操作。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 109 | [Vue 教學 10：Composition API 的組織方式](../content/post/vue/vue-10-Composition-API.md) | 草稿 → 公開 | 用可搜尋的待辦列表組合 ref、computed 與函式，理解 setup 的責任與 Options API 的對照。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 110 | [Vue 教學 11：元件通訊與 Pinia 的分工](../content/post/vue/vue-11-元件通訊與Pinia.md) | 草稿 → 公開 | 依狀態的使用範圍選擇 props、事件、provide 或 Pinia，並練習 storeToRefs。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支 |
| 111 | [Vue 教學 12：attrs、公開方法與依賴注入](../content/post/vue/vue-12-元件通訊進階.md) | 草稿 → 公開 | 完成可聚焦的輸入元件，示範屬性透傳、defineExpose 與跨層 provide / inject。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 112 | [Vue 教學 13：v-model、自訂指令與衍生資料](../content/post/vue/vue-13-Vue3進階實務整理.md) | 草稿 → 公開 | 完成可雙向繫結的輸入元件，對照 Vue 3 的 modelValue 協定與 defineModel。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 113 | [Vue 教學 14：路由的角色與網址對映](../content/post/vue/vue-14-路由核心概念.md) | 草稿 → 公開 | 釐清 Router、RouterLink、RouterView 與頁面元件的分工，建立 SPA 路由的操作流程。 | Vue Router API文件查核；memory history實測命名參數、query、resolve與守衛導向 |
| 114 | [Vue 教學 15：建立可運作的路由骨架](../content/post/vue/vue-15-路由基本接線.md) | 草稿 → 公開 | 提供入口、路由器、兩個頁面與展示區的完整檔案，作為後續路由章節的基礎。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 115 | [Vue 教學 16：匹配、重新導向與找不到頁面](../content/post/vue/vue-16-Vue-Router基礎.md) | 草稿 → 公開 | 在共用骨架加入任務頁、重新導向與 404，檢查路由匹配的完整行為。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 116 | [Vue 教學 17：to 的字串與物件寫法](../content/post/vue/vue-17-to的兩種寫法.md) | 草稿 → 公開 | 比較固定網址與命名路由導航，避免以 path 搭配 params 造成引數遺失。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；memory history實測命名參數、query、resolve與守衛導向 |
| 117 | [Vue 教學 18：history、hash 與部署基底](../content/post/vue/vue-18-history與hash模式.md) | 草稿 → 公開 | 說明兩種網址模式、子目錄部署與重新整理 404 的修正方式。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 118 | [Vue 教學 19：命名與巢狀路由](../content/post/vue/vue-19-命名與巢狀路由.md) | 草稿 → 公開 | 建立帶子頁的任務殼層，理解相對 children path 與第二層 RouterView。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 119 | [Vue 教學 20：路由元件重用與資料重新整理](../content/post/vue/vue-20-路由元件生命週期.md) | 草稿 → 公開 | 以任務識別碼變動示範元件重用，避免只在 mounted 讀取一次 params。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 120 | [Vue 教學 21：query 與 params 的接收及驗證](../content/post/vue/vue-21-路由傳參query與params.md) | 草稿 → 公開 | 用任務編號與頁碼比較路徑引數、查詢引數，避免直接把網址值當成可信數字。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；memory history實測命名參數、query、resolve與守衛導向 |
| 121 | [Vue 教學 22：路由 props 與解耦的頁面](../content/post/vue/vue-22-路由props配置.md) | 草稿 → 公開 | 將 route 轉成元件 props，讓任務頁可獨立使用與測試。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 122 | [Vue 教學 23：replace 與瀏覽器歷史](../content/post/vue/vue-23-replace屬性.md) | 草稿 → 公開 | 透過返回鍵實驗 push 與 replace，選擇適合登入導向與篩選更新的行為。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 123 | [Vue 教學 24：程式導航與失敗處理](../content/post/vue/vue-24-程式設計式導航.md) | 草稿 → 公開 | 按操作結果導航，使用 useRouter、push、replace 與 navigation failure 判斷完成狀態。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 124 | [Vue 教學 25：守衛、延遲載入與導航測試](../content/post/vue/vue-25-Vue-Router進階.md) | 草稿 → 公開 | 完成本機模擬登入守衛，理解前端攔截的限制與 lazy route 的建置行為。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；memory history實測命名參數、query、resolve與守衛導向 |
| 125 | [Vue 教學 26：Pinia 狀態、getter 與非同步 action](../content/post/vue/vue-26-Pinia集中式狀態管理.md) | 草稿 → 公開 | 以本地任務資料完成 loading、錯誤與 storeToRefs 的操作流程。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支 |
| 126 | [Vue 教學 27：Vuex 4 與既有狀態管理維護](../content/post/vue/vue-27-Vuex狀態管理.md) | 草稿 → 公開 | 保留 Vuex 的 state、getter、mutation、action 流程，並對照新專案的 Pinia 路線。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證；本文store/composable直接匯入測試狀態、action與錯誤分支 |
| 127 | [Vue 教學 28：Vite 建置、環境變數與資源路徑](../content/post/vue/vue-28-Vite工具.md) | 草稿 → 公開 | 補齊 Vite 專案設定，區分開發服務、正式建置與公開環境變數。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 128 | [Vue 教學 29：Transition 與列表動畫](../content/post/vue/vue-29-Vue動畫.md) | 草稿 → 公開 | 完成進出場與排序動畫，讓 key、CSS class 與降低動態偏好互相配合。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |
| 129 | [Vue 教學 30：SSR 的伺服器邊界與最小範例](../content/post/vue/vue-30-SSR服務端渲染.md) | 草稿 → 公開 | 使用 Node 與 Vue server-renderer 回傳 HTML，釐清 SSR、hydration 與跨請求狀態。 | 直接匯入本文createPage，SSR renderToString輸出及文字轉義通過；HTTP與hydration非此測試範圍 |
| 130 | [Vue 教學 31：電影目錄實作與本地模擬資料](../content/post/vue/vue-31-實戰doubanmovie.md) | 草稿 → 公開 | 保留豆瓣電影專案的搜尋與列表情境，以本地 JSON 完成可重現的載入、錯誤與篩選流程。 | SFC/script/template編譯與隔離Vite正式建置通過；非完整瀏覽器互動驗證 |

## 重跑與原始紀錄

- [整體驗證結果](validation-results.json)。
- [64 篇範例驗證範圍](example-results.json)。

- [逐篇 JSON 檢核清單](note-review.json) 包含原始日期、版本情境、原缺漏、來源與 HTTP 結果。
- [來源 URL 結果](source-checks.json)。
- [隔離測試工具與鎖定版本](verification/README.md)。
- [本地 UI 抽查紀錄](preview-checks.json)。

上述數據記錄 2026-10-07 的內容整理與技術驗證，不代表每次部署都重跑全部範例。該版本後續已提交及部署；個別部署狀態以 GitHub Actions 與 Release 為準。

## 呈現調整與版本留存

2026-10-07 移除獨立站內查核頁與文章中的制式查核段落，將原始來源併入單一「參考資料」區塊。技術驗證證據、原始發布日期與 reviewedAt 保留；presentationUpdatedAt 記錄此次呈現調整時間，lastmod 記錄文章實際修訂時間。

完整紀錄留存在本 Markdown 與 JSON；每次正式部署成功後，以 Tag／Release 連結到該提交的固定版本，避免後續修改影響歷史查核紀錄。

此次呈現調整的驗證（2026-10-07）：

- 130 篇文章的原始網址集合、程式碼範例與參考區塊前的教學內容均與修訂前一致；原發布日期與 JSON 中的技術查核日期、來源及證據未改動。
- 移除 130 個制式查核段落與 88 個來源子標題（67 個「原始筆記保留的來源」、21 個「原始筆記的其他連結」）；參考列表均只有一個標題，沒有重複網址。
- Hugo Extended 0.167.0 正式建置成功；內容、130 筆搜尋索引、首頁／筆記各 13 × 10 分頁、內部連結與安全檢查通過，本次產出 345 個 HTML（較原查核少一個獨立頁面）。
- `test_deployment_release.py` 的 17 個隔離測試通過，涵蓋 Pages 精確 SHA、成功／失敗／逾時、Tag 衝突、跨日重跑、既有 Tag／Release、建立失敗與 CLI 引數；所有 GitHub 回應均為模擬，未建立真實版本。
- 本地抽查 SQL 的合併來源與未實測限制、Vue／Java 系列導覽及首頁，確認每頁 10 篇與 130／13 頁資訊正常。清除既有預覽目錄中的舊頁面 HTML 後，已刪頁面回傳 404。
- 部署工作流程的 YAML 語法與觸發設定檢查通過。此處記錄發布前的本地與模擬結果；正式部署及自動 Release 的執行狀態，以對應的工作流程日誌與 Release 為準。
