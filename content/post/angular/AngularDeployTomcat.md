---
title: "Angular 部署 Tomcat：base href、靜態檔與子路徑"
date: 2020-09-25T20:40:28+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "Tomcat"
toc: true
draft: false
description: "補上建置輸出與部署驗證，區分 SPA fallback、hash 路由與 API 404。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上建置輸出與部署驗證，區分 SPA fallback、hash 路由與 API 404。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 建置與放置

原部署情境為Tomcat9、Angular CLI專案，部署路徑假設`/task-app/`：

```bash
npx ng build --configuration production --base-href /task-app/
```

檢視angular.json的outputPath，新builder可能輸出到`dist/專案/browser/`。把**含index.html的目錄內容**放Tomcat的webapps/task-app，不再套一層browser。靜態SPA本身不需要Java Servlet程式才能顯示。

## 路由策略

首次開啟 `/task-app/` 應正常；history模式直接開 `/task-app/about` 時Tomcat會尋找該資源，可能404。可選hash策略：在standalone `provideRouter(routes, withHashLocation())`，或舊RouterModule.forRoot(routes,{useHash:true})。這讓網址變為`/task-app/#/about`，不用伺服器fallback。

若需history，設定該應用專用rewrite／forward到index.html，並排除JS、CSS、圖片及API。不要在全站把所有404都映到index.html，否則缺資源得到200 HTML、API錯誤被掩蓋。單純error-page可能保留404狀態且不同容器行為，需檢查Network而非只看頁面。

## 驗收順序

1. 清除舊建置殘留，用新bundle完整替換同一應用，避免index與hash檔版本不一致。
2. 首頁、點連結、直接開子路徑、重新整理與返回鍵都測。
3. Network確認JS/CSS的MIME與200回應，不是登入頁或HTML fallback。
4. API以實際base URL測，核對CORS、proxy與認證；開發server的proxy不會跟著dist部署。

Tomcat服務安裝、管理帳號與Java版本是容器維運，參考Tomcat系列，不為靜態站修改所有server.xml的Host。production與本機環境檔都是前端公開資訊，不放密碼。

## 參考資料

- [Angular 部署](https://angular.dev/tools/cli/deployment)
- [Angular Hash 路由](https://angular.dev/api/router/withHashLocation)
- [Tomcat deployment](https://tomcat.apache.org/tomcat-9.0-doc/deployer-howto.html)
- [Angular - Deployment](https://angular.io/guide/deployment)
- [Apache Tomcat 9 (9.0.59) - Windows Service How-To](https://tomcat.apache.org/tomcat-9.0-doc/windows-service-howto.html)
- [maven - Url rewriting Angular 4 on tomcat 8 server - Stack Overflow](https://stackoverflow.com/questions/51042875/url-rewriting-angular-4-on-tomcat-8-server)
- [`<base href="/">` 與 `<base href="./">` 的差別？- General - 臺灣 Angular 技術論壇](https://forum.angular.tw/t/topic/881/12)
- [如何將 Angular 2 含有路由機制的 SPA 網頁應用程式部署到 IIS 網站伺服器 | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2017/01/17/Angular-2-deploy-on-IIS)
