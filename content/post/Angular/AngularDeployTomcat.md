---
title: "AngularDeployTomcat"
date: 2020-09-25T20:40:28+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Angular"
toc: true
---


# Angular Deploy Tomcat 
<!--more-->



## 1. 編譯

到專案目錄執行 **編譯指令如下**

````
ng build --prod --base-href /project_Name/
````

匯出 index.html 如下

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Title</title>
  <base href="/project_Name/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link rel="stylesheet" href="styles.479444a78a429503e78e.css"></head>
<body class="mat-typography">
  		<app-root></app-root>
        <script src="runtime.c51bd5b1c616d9ffddc1.js" defer></script>
        <script src="polyfills-es5.272209ba9e789fcad1c2.js" nomodule defer></script>
        <script src="polyfills.7f244a820a4deda6d9fd.js" defer></script>
        <script src="main.d604dab66ca826078124.js" defer></script>
    </body>
</html>

```



--prod  : 把 `src/environments/environment.ts` 檔案替換成針對特定目標的版本 , 且編譯出來的檔案會小很多

--output-path : 表示輸出路徑  : ex : 輸出到當前目錄的 web資料夾底下

--base-href : 修改 index.html 裡的 <base href="/"> : ex : <base href="/project_Name/">



## **2.部屬** 

把project/dist裡的project的資料夾 移動到  $Tomcat/webapps

## 3. Deploy Tomcat9

調整 server.xml，將 http port 改為 80，https port 改為 443。

```xml
<Connector port="80" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="443" />
```
### 4. Installing services

Install the service named 'Tomcat9'

```
service.bat install
```



##  5. 404 如何解決

因為 Angular 是 SPA，所以在網頁伺服器要將所有的 request 全部導回到 index.html 才可以正常地顯示，如果在沒有設定下直接打開網址 web/home，他會去找 home 資料夾下的 index.html

**(1)將以下代碼放在部署文件夾的web.xml中：**

```xml
<error-page>
     <error-code>404</error-code>
     <location>/index.html</location>
</error-page>
```

**(2)將HashLocationStrategy與路由的URL中的＃一起使用**

修改 app-routing.module.ts

使用:
RouterModule.forRoot(routes, { useHash: true })
代替:
RouterModule.forRoot(routes)

使用HashLocationStrategy，您的網址將類似於：

http://localhost/#/route

app-routing.module.ts

```typescript
@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
```



**(3) Tomcat URL Rewrite Valve：如果找不到資源，則使用服務器級別的配置來重寫URL，以重定向到index.html。**

(3.1)在server.xml中配置RewriteValve

```xml
<?xml version="1.0" encoding="utf-8"?>
<Context>
  <Valve className="org.apache.catalina.valves.rewrite.RewriteValve" />
</Context>
```

(3.2)在rewrite.config中寫入重寫規則 

創建目錄結構–〜/ conf / Catalina / localhost /並使用以下內容在其中創建rewrite.config文件。注意-這裡我考慮將其`/web`作為應用程序的上下文路徑。

```xml
RewriteCond %{REQUEST_PATH} !-f
RewriteRule ^/web/(.*) /web/index.html
```

### 參考

[Angular](https://angular.io/guide/deployment)

[Apache Tomcat 9 (9.0.53) - Windows Service How-To](https://tomcat.apache.org/tomcat-9.0-doc/windows-service-howto.html)

[maven - Url rewriting Angular 4 on tomcat 8 server - Stack Overflow](https://stackoverflow.com/questions/51042875/url-rewriting-angular-4-on-tomcat-8-server)

[如何將 Angular 2 含有路由機制的 SPA 網頁應用程式部署到 IIS 網站伺服器 | The Will Will Web](https://blog.miniasp.com/post/2017/01/17/Angular-2-deploy-on-IIS)


<base href="/"> 與 <base href="./"> 的差別 ? - General - 台灣 Angular 技術論壇

https://forum.angular.tw/t/topic/881/12

https://forum.angular.tw/t/topic/1839/2