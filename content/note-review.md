---
title: "筆記內容查核紀錄"
date: 2026-10-07T00:01:00+08:00
lastmod: 2026-10-07T00:01:00+08:00
layout: page
toc: true
description: "130 篇筆記的版本、整理結果與實際驗證範圍。"
---

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

下表的「測試」包含編譯或明確標示的 mock；實際範圍請閱讀每篇的「查核範圍」。每篇均已公開，版本與原來源保留在文章和完整 JSON 清單。

| # | 筆記 | 原狀態 | 查核方式 |
| --- | --- | --- | --- |
| 1 | [AI 工具清單：聊天、搜尋與翻譯]({{< ref "/post/ai-tools.md" >}}) | 公開 → 修訂 | 文件查核 |
| 2 | [Android Studio 第一個專案：模板、SDK 與執行確認]({{< ref "/post/android/AndroidBsN01.md" >}}) | 公開 → 修訂 | 文件查核 |
| 3 | [Angular NullInjectorError：定位缺少的 provider]({{< ref "/post/angular/Angular-NullInjectorError.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 4 | [Angular 範本驅動表單：ngModel 與驗證]({{< ref "/post/angular/Angular-forms-Template-Driven-Forms.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 5 | [Angular Reactive Forms：模型、驗證與提交]({{< ref "/post/angular/Angular-forms.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 6 | [Angular npm 安裝錯誤：peer dependency 診斷]({{< ref "/post/angular/Angular-npm-Error.md" >}}) | 公開 → 修訂 | 文件查核 |
| 7 | [Angular CLI 專案結構：舊 NgModule 與新版差異]({{< ref "/post/angular/AngularBsN02.md" >}}) | 公開 → 修訂 | 文件查核 |
| 8 | [Angular CLI：開發、產生程式碼與建置]({{< ref "/post/angular/AngularCLInotes.md" >}}) | 公開 → 修訂 | 文件查核 |
| 9 | [Angular 小抄：模板、生命週期、DI 與路由]({{< ref "/post/angular/AngularCheatSheet.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 10 | [Angular 部署 Tomcat：base href、靜態檔與子路徑]({{< ref "/post/angular/AngularDeployTomcat.md" >}}) | 公開 → 修訂 | 文件查核 |
| 11 | [Angular 目錄設計：依功能分組與共用邊界]({{< ref "/post/angular/AngularFileStructure.md" >}}) | 公開 → 修訂 | 文件查核 |
| 12 | [Angular 與 IE11：歷史相容維護及遷移]({{< ref "/post/angular/AngularOnIE11.md" >}}) | 公開 → 修訂 | 文件查核 |
| 13 | [Compodoc：產生 Angular 檔案與檢查輸出]({{< ref "/post/angular/AngularUseCompodoc.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 14 | [Angular 引入 JavaScript：ES module 與全域 script]({{< ref "/post/angular/AngularUseJavaScript.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 15 | [Angular 圖片縮放：Canvas 與型別化 Service]({{< ref "/post/angular/angular-resize-base64-image.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 16 | [Gradle 編碼排錯：JavaCompile 與 Javadoc]({{< ref "/post/build-tools/gradle-error.md" >}}) | 公開 → 修訂 | 文件查核 |
| 17 | [Docker 常用指令：映像、容器與排錯]({{< ref "/post/docker/docker-command.md" >}}) | 公開 → 修訂 | 文件查核 |
| 18 | [Docker Compose：Web 與 Redis 的完整練習]({{< ref "/post/docker/docker-compose.md" >}}) | 公開 → 修訂 | 文件查核 |
| 19 | [Dockerfile：建立靜態網頁映像]({{< ref "/post/docker/docker-file.md" >}}) | 公開 → 修訂 | 文件查核 |
| 20 | [Docker Swarm：服務部署、更新與回滾]({{< ref "/post/docker/docker-swarm.md" >}}) | 草稿 → 公開 | 文件查核 |
| 21 | [Docker Volume：持久化、掛載與備份]({{< ref "/post/docker/docker-volumes.md" >}}) | 草稿 → 公開 | 文件查核 |
| 22 | [CentOS 8 的 Docker 安裝紀錄與替代路線]({{< ref "/post/docker/install-docker-on-centos8.md" >}}) | 公開 → 修訂 | 文件查核 |
| 23 | [Windows WSL 2 與 Docker：安裝前檢查及錯誤排除]({{< ref "/post/docker/install-docker-on-windows-WSL.md" >}}) | 公開 → 修訂 | 文件查核 |
| 24 | [Eclipse 型別階層：檢視繼承與實作]({{< ref "/post/eclipse/OpenTypeHierarchy.md" >}}) | 公開 → 修訂 | 文件查核 |
| 25 | [Eclipse UTF-8：工作區、專案與建置一致性]({{< ref "/post/eclipse/eclipseSettingUtf-8.md" >}}) | 公開 → 修訂 | 文件查核 |
| 26 | [Eclipse 與 JUnit 5：建立並執行測試]({{< ref "/post/eclipse/eclipseUseJUnit.md" >}}) | 公開 → 修訂 | 文件查核 |
| 27 | [Git 匯出版本差異：固定目標提交並保留空白路徑]({{< ref "/post/git/GIT-export-diff-file.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 28 | [Git 分支同步：把主分支更新帶入工作分支]({{< ref "/post/git/git-branch-update-master.md" >}}) | 公開 → 修訂 | 文件查核 |
| 29 | [Git 基本流程：檢查、暫存與提交]({{< ref "/post/git/git-command.md" >}}) | 草稿 → 公開 | 文件查核 |
| 30 | [Git 提交訊息：Conventional Commits 與拆分原則]({{< ref "/post/git/git-commit-message.md" >}}) | 草稿 → 公開 | 文件查核 |
| 31 | [Git 排錯：本機修改阻擋切換與合併衝突]({{< ref "/post/git/git-error.md" >}}) | 公開 → 修訂 | 文件查核 |
| 32 | [Git 日常筆記：遠端、忽略規則與回復提交]({{< ref "/post/git/git-note.md" >}}) | 公開 → 修訂 | 文件查核 |
| 33 | [GitLab 認證失敗：HTTPS 憑證與 SSH 診斷]({{< ref "/post/git/gitLab-error.md" >}}) | 公開 → 修訂 | 文件查核 |
| 34 | [Hugo 程式碼高亮：Prism 與內建 Chroma]({{< ref "/post/hugo/HugoAddPrism.md" >}}) | 公開 → 修訂 | 文件查核 |
| 35 | [Hugo Disqus：識別碼、本機停用與留言整合]({{< ref "/post/hugo/HugoAddisqus.md" >}}) | 公開 → 修訂 | 文件查核 |
| 36 | [Hugo GA4：正式站載入與事件確認]({{< ref "/post/hugo/hugoAddGoogleAnalytics.md" >}}) | 公開 → 修訂 | 文件查核 |
| 37 | [Hugo 基礎：建立文章、圖片與本地建置]({{< ref "/post/hugo/hugonotes.md" >}}) | 公開 → 修訂 | 文件查核 |
| 38 | [HikariCP 連線逾時：診斷與可重現範例]({{< ref "/post/java/HikariPool-1-error.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 39 | [Java heap space：記憶體不足的診斷與確認]({{< ref "/post/java/Java-heap-space.md" >}}) | 公開 → 修訂 | 文件查核 |
| 40 | [Java 數字格式：DecimalFormat 與 BigDecimal]({{< ref "/post/java/java-DecimalFormat.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 41 | [Java 排錯：編譯問題、例外與版本不一致]({{< ref "/post/java/java-error.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 42 | [Java 入門 00：JDK 安裝與環境確認]({{< ref "/post/java/java_tutorial_0.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 43 | [Java 入門 01：編譯並執行第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 44 | [Java 入門 02：基本型別、預設值與跳脫字元]({{< ref "/post/java/java_tutorial_2.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 45 | [Java 入門 03：變數、初始化與作用域]({{< ref "/post/java/java_tutorial_3.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 46 | [Java 入門 04：封裝、繼承與多型]({{< ref "/post/java/java_tutorial_4.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 47 | [Java 多型：介面、覆寫與執行時派發]({{< ref "/post/java/polymorphism.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 48 | [HEIC 轉 JPEG：heic2any 的載入、錯誤與輸出限制]({{< ref "/post/javascript/Heic2any.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 49 | [列印隱藏按鈕：CSS print media 與預覽確認]({{< ref "/post/javascript/Hide-Button-when-printing.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 50 | [JavaScript 陣列產生表格：安全文字與完整欄位]({{< ref "/post/javascript/array-Create-Table.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 51 | [行動裝置偵測：以版面與功能能力取代 UA 猜測]({{< ref "/post/javascript/detect-mobile-device.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 52 | [JavaScript 核心複習：型別、作用域與物件傳遞]({{< ref "/post/javascript/joinWillJavaScriptCourse.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 53 | [JavaScript JSON 下拉選單：解析、選項與選取結果]({{< ref "/post/javascript/select-JsonList.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 54 | [JavaScript 表格搜尋：保留欄位並篩選整列]({{< ref "/post/javascript/table-Search.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 55 | [Kafka Eagle／EFAK：歷史監控配置與 Kafka 版本界線]({{< ref "/post/kafka/kafka-eagle.md" >}}) | 草稿 → 公開 | 文件查核 |
| 56 | [CentOS Linux 8 安裝紀錄：VM 流程與 EOL 說明]({{< ref "/post/linux/Install-CentOS-8.md" >}}) | 草稿 → 公開 | 文件查核 |
| 57 | [Linux 基礎指令：路徑、檔案與許可權]({{< ref "/post/linux/LinuxCommand.md" >}}) | 公開 → 修訂 | 文件查核 |
| 58 | [Linux 網路工具：ss、systemctl 與 firewalld]({{< ref "/post/linux/linux-must-install-software.md" >}}) | 公開 → 修訂 | 文件查核 |
| 59 | [IP 與子網：IPv4、IPv6、私有位址和 CIDR]({{< ref "/post/net/IP.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 60 | [SSL、TLS 與 HTTPS：憑證、握手和驗證限制]({{< ref "/post/net/SSLandTLSandHttps.md" >}}) | 公開 → 修訂 | 文件查核 |
| 61 | [Chrome DevTools Overrides：本地模擬回應與保留修改]({{< ref "/post/net/chromeTools.md" >}}) | 公開 → 修訂 | 文件查核 |
| 62 | [hosts 設定：本地名稱對映與 DNS 診斷]({{< ref "/post/net/hosts.md" >}}) | 公開 → 修訂 | 文件查核 |
| 63 | [Windows 路由：字首、介面與暫時規則]({{< ref "/post/net/windows-route.md" >}}) | 公開 → 修訂 | 文件查核 |
| 64 | [Windows 網路排錯：IP、DNS、TCP 與程式]({{< ref "/post/net/windowsNetCmd.md" >}}) | 公開 → 修訂 | 文件查核 |
| 65 | [Windows Nginx：靜態站、反向代理與設定檢查]({{< ref "/post/nginx/NginxForwindows.md" >}}) | 草稿 → 公開 | 文件查核 |
| 66 | [FTP、FTPS 與 SFTP：協定和連線埠差異]({{< ref "/post/other/FTPvsFTPSvsSFTP.md" >}}) | 草稿 → 公開 | 文件查核 |
| 67 | [高可用性架構：Active-Active、備援與故障測試]({{< ref "/post/other/HighAvailability.md" >}}) | 公開 → 修訂 | 文件查核 |
| 68 | [Java 工程師學習地圖：基礎、交付與架構能力]({{< ref "/post/other/Java技術人員技能.md" >}}) | 公開 → 修訂 | 文件查核 |
| 69 | [Markdown 筆記：語法、程式碼與 Hugo 差異]({{< ref "/post/other/Markdown.md" >}}) | 公開 → 修訂 | 文件查核 |
| 70 | [系統分析 SA：釐清需求與可驗收規格]({{< ref "/post/other/SA.md" >}}) | 公開 → 修訂 | 文件查核 |
| 71 | [技術提問：重現步驟、預期結果與診斷證據]({{< ref "/post/other/ask-questions.md" >}}) | 公開 → 修訂 | 文件查核 |
| 72 | [技術閱讀清單：Spring、全端與 JavaScript 的選讀方式]({{< ref "/post/other/book.md" >}}) | 草稿 → 公開 | 文件查核 |
| 73 | [Windows MongoDB：免安裝配置與 mongosh 確認]({{< ref "/post/other/mongodb_install.md" >}}) | 公開 → 修訂 | 文件查核 |
| 74 | [Vagrant：VM 生命週期、SSH 與共享檔案]({{< ref "/post/other/vagrant.md" >}}) | 公開 → 修訂 | 文件查核 |
| 75 | [Windows 開發工具清單：用途與安裝後檢查]({{< ref "/post/other/windows_裝機必裝.md" >}}) | 公開 → 修訂 | 文件查核 |
| 76 | [Windows 修復環境複製資料：Notepad 與磁碟辨識]({{< ref "/post/other/使用notepad指令救援資料.md" >}}) | 公開 → 修訂 | 文件查核 |
| 77 | [前後端分離：API 契約、部署與成本]({{< ref "/post/other/前後端分離.md" >}}) | 公開 → 修訂 | 文件查核 |
| 78 | [軟體與網路名詞：NAT、代理、加密與認證]({{< ref "/post/other/名詞.md" >}}) | 公開 → 修訂 | 文件查核 |
| 79 | [API 文件工具：OpenAPI、Slate 與 apiDoc 的選擇]({{< ref "/post/other/寫程式API文件的工具.md" >}}) | 公開 → 修訂 | 文件查核 |
| 80 | [流程圖工具：Mermaid 文字圖與圖形編輯器]({{< ref "/post/other/畫流程圖的工具.md" >}}) | 草稿 → 公開 | 文件查核 |
| 81 | [金額計算與浮點誤差：整數單位、Decimal 與捨入]({{< ref "/post/other/算錢用浮點，遲早被人扁.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 82 | [Redis 安裝：本機 Docker 與平臺選擇]({{< ref "/post/redis/redis-Install.md" >}}) | 公開 → 修訂 | 文件查核 |
| 83 | [Redis 指令：鍵值、到期與資料結構]({{< ref "/post/redis/redis-command.md" >}}) | 草稿 → 公開 | 文件查核 |
| 84 | [Redis 設定：監聽、記憶體與持久化]({{< ref "/post/redis/redis-config.md" >}}) | 草稿 → 公開 | 文件查核 |
| 85 | [Tomcat 設定：JNDI、環境變數與 JVM 引數]({{< ref "/post/server/tomcatSetEnvironment.md" >}}) | 公開 → 修訂 | 文件查核 |
| 86 | [Tomcat server.xml：上傳限制與應用部署]({{< ref "/post/server/tomcatSetserverxml.md" >}}) | 公開 → 修訂 | 文件查核 |
| 87 | [Tomcat Manager：角色、使用者與存取範圍]({{< ref "/post/server/tomcatSettingUser.md" >}}) | 公開 → 修訂 | 文件查核 |
| 88 | [Spring Boot API 文件：Swagger 2 歷史整合與 OpenAPI 3]({{< ref "/post/spring-boot/spring-boot-Swagger2.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 89 | [Spring Profile 與 Maven Profile：執行期和建置期]({{< ref "/post/spring-boot/spring-boot-active-profile.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 90 | [ConditionalOnProperty：條件式 Bean 與測試]({{< ref "/post/spring-boot/spring-boot-conditionalOnProperty.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 91 | [Spring Boot 核心觀念：自動配置、設定與可驗證回答]({{< ref "/post/spring-boot/spring-boot-interview.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 92 | [Spring Cloud Eureka：服務註冊與健康確認]({{< ref "/post/spring-cloud/spring-cloud-Eureka.md" >}}) | 草稿 → 公開 | 文件查核 |
| 93 | [Spring Cloud Gateway：路由、過濾與 Actuator 邊界]({{< ref "/post/spring-cloud/spring-cloud-Gateway.md" >}}) | 公開 → 修訂 | 文件查核 |
| 94 | [Spring Data JPA：Repository 與分頁查詢]({{< ref "/post/spring/spring-data-Jpa-Notes.md" >}}) | 公開 → 修訂 | 測試／編譯 |
| 95 | [Transactional：代理、回滾與交易範圍]({{< ref "/post/spring/spring-transactional.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 96 | [SQL Server T-SQL：建表、修改欄位與交易練習]({{< ref "/post/sql/sql-command.md" >}}) | 公開 → 修訂 | 文件查核 |
| 97 | [SQL Server 許可權：Login、User 與最小角色]({{< ref "/post/sql/sql-server.md" >}}) | 公開 → 修訂 | 文件查核 |
| 98 | [VS Code Remote SSH：連線、遠端資料夾與 Vagrant]({{< ref "/post/visual-studio-code/VSCodeUseRemote.md" >}}) | 公開 → 修訂 | 文件查核 |
| 99 | [Vue 教學 00：學習路線與共用練習環境]({{< ref "/post/vue/vue-00-學習路線總整理.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 100 | [Vue 教學 01：宣告式畫面與第一個元件]({{< ref "/post/vue/vue-01-Vue概述.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 101 | [Vue 教學 02：模板語法、表單與條件渲染]({{< ref "/post/vue/vue-02-Vue-js基礎.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 102 | [Vue 教學 03：列表渲染與穩定的 key]({{< ref "/post/vue/vue-03-列表渲染.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 103 | [Vue 教學 04：ref、reactive 與模板引用]({{< ref "/post/vue/vue-04-ref與reactive.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 104 | [Vue 教學 05：watch 與副作用清理]({{< ref "/post/vue/vue-05-watch監視屬性.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 105 | [Vue 教學 06：生命週期與資源釋放]({{< ref "/post/vue/vue-06-生命週期.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 106 | [Vue 教學 07：自訂 composable 與可重用狀態]({{< ref "/post/vue/vue-07-自定義hooks.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 107 | [Vue 教學 08：進階響應式、唯讀資料與插槽]({{< ref "/post/vue/vue-08-響應式進階整理.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 108 | [Vue 教學 09：元件拆分、props 與事件]({{< ref "/post/vue/vue-09-元件化.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 109 | [Vue 教學 10：Composition API 的組織方式]({{< ref "/post/vue/vue-10-Composition-API.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 110 | [Vue 教學 11：元件通訊與 Pinia 的分工]({{< ref "/post/vue/vue-11-元件通訊與Pinia.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 111 | [Vue 教學 12：attrs、公開方法與依賴注入]({{< ref "/post/vue/vue-12-元件通訊進階.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 112 | [Vue 教學 13：v-model、自訂指令與衍生資料]({{< ref "/post/vue/vue-13-Vue3進階實務整理.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 113 | [Vue 教學 14：路由的角色與網址對映]({{< ref "/post/vue/vue-14-路由核心概念.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 114 | [Vue 教學 15：建立可運作的路由骨架]({{< ref "/post/vue/vue-15-路由基本接線.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 115 | [Vue 教學 16：匹配、重新導向與找不到頁面]({{< ref "/post/vue/vue-16-Vue-Router基礎.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 116 | [Vue 教學 17：to 的字串與物件寫法]({{< ref "/post/vue/vue-17-to的兩種寫法.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 117 | [Vue 教學 18：history、hash 與部署基底]({{< ref "/post/vue/vue-18-history與hash模式.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 118 | [Vue 教學 19：命名與巢狀路由]({{< ref "/post/vue/vue-19-命名與巢狀路由.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 119 | [Vue 教學 20：路由元件重用與資料重新整理]({{< ref "/post/vue/vue-20-路由元件生命週期.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 120 | [Vue 教學 21：query 與 params 的接收及驗證]({{< ref "/post/vue/vue-21-路由傳參query與params.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 121 | [Vue 教學 22：路由 props 與解耦的頁面]({{< ref "/post/vue/vue-22-路由props配置.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 122 | [Vue 教學 23：replace 與瀏覽器歷史]({{< ref "/post/vue/vue-23-replace屬性.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 123 | [Vue 教學 24：程式導航與失敗處理]({{< ref "/post/vue/vue-24-程式設計式導航.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 124 | [Vue 教學 25：守衛、延遲載入與導航測試]({{< ref "/post/vue/vue-25-Vue-Router進階.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 125 | [Vue 教學 26：Pinia 狀態、getter 與非同步 action]({{< ref "/post/vue/vue-26-Pinia集中式狀態管理.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 126 | [Vue 教學 27：Vuex 4 與既有狀態管理維護]({{< ref "/post/vue/vue-27-Vuex狀態管理.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 127 | [Vue 教學 28：Vite 建置、環境變數與資源路徑]({{< ref "/post/vue/vue-28-Vite工具.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 128 | [Vue 教學 29：Transition 與列表動畫]({{< ref "/post/vue/vue-29-Vue動畫.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 129 | [Vue 教學 30：SSR 的伺服器邊界與最小範例]({{< ref "/post/vue/vue-30-SSR服務端渲染.md" >}}) | 草稿 → 公開 | 測試／編譯 |
| 130 | [Vue 教學 31：電影目錄實作與本地模擬資料]({{< ref "/post/vue/vue-31-實戰doubanmovie.md" >}}) | 草稿 → 公開 | 測試／編譯 |
