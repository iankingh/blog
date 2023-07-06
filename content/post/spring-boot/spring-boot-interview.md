---
title: "Spring_interview"
date: 2021-03-16T13:17:45+08:00
draft: false
categories:
 - "筆記"
tags:
 - "spring"
 - "spring Boot"
toc: true
---

## Spring boot 面試題
<!--more-->
### 1、什麼是 Spring Boot？

Spring Boot 是 Spring 開源組織的子專案，是 Spring 組件一站式解決方案，主要是簡化了使用 Spring 的難度，不必繁重的配置，提供了各種啟動器，開發者能快速上手。

SpringBoot是非常適合開發Web應用的，因為他內嵌有Tomcat、Jetty、Undertow或者Netty。大部分的應用可以通過載入spring-boot-starter-web模組能夠快速的創建並啟動一個Web應用。



### 2、為什麼要用 Spring Boot(優點)？

Spring Boot 優點非常多，如：

- 獨立運行
- 簡化配置
- 自動配置
- 無代碼生成和XML配置
- 應用監控
- 上手容易

### 3、Spring Boot 的核心設定檔有哪幾個？它們的區別是什麼？

Spring Boot 的核心設定檔是 application 和 bootstrap 設定檔。

application 設定檔這個容易理解，主要用於 Spring Boot 專案的自動化配置。

bootstrap 設定檔有以下幾個應用場景。

- 使用     Spring Cloud Config 配置中心時，這時需要在 bootstrap 設定檔中添加連接到配置中心的配置屬性來載入外部配置中心的配置資訊；
- 一些固定的不能被覆蓋的屬性；
- 一些加密/解密的場景；

### 4、Spring Boot 的設定檔有哪幾種格式？它們有什麼區別？

**.properties** 和 **.yml**，它們的區別主要是書寫格式不同。

(1)**.properties**

```
app.user.name = javastack
```

(2)**.yml**

```
app:
  user:
    name: javastack
```

另外，.yml 格式不支援 `@PropertySource` 注解導入配置。

### 5、Spring Boot 的核心注解是哪個？它主要由哪幾個注解組成的？

啟動類上面的注解是@SpringBootApplication，它也是 Spring Boot 的核心注解，主要組合包含了以下 3 個注解：

@SpringBootConfiguration：組合了 @Configuration 注解，實現設定檔的功能。

@EnableAutoConfiguration：打開自動配置的功能，也可以關閉某個自動配置的選項，如關閉資料來源自動配置功能： @SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })。

@ComponentScan：Spring元件掃描。

### 6、開啟 Spring Boot 特性有哪幾種方式？

- 繼承spring-boot-starter-parent專案

- 導入spring-boot-dependencies項目依賴

### 7、Spring Boot 需要獨立的容器運行嗎？

- 可以不需要，內置了 Tomcat/ Jetty 等容器。

### 8、運行 Spring Boot 有哪幾種方式？

- 打包用命令或者放到容器中運行

- 用 Maven/ Gradle 外掛程式運行

- 直接執行 main 方法運行

### 9、Spring Boot 自動配置原理是什麼？

注解 @EnableAutoConfiguration, @Configuration, @ConditionalOnClass 就是自動配置的核心，首先它得是一個設定檔，其次根據類路徑下是否有這個類去自動配置。

### 10、Spring Boot 的目錄結構是怎樣的？

#### 1.1   目錄結構

專案的目錄結構建置，基本上照著大原則去做初步的分類，像是應用主類、實體層、邏輯層、Web層；而在不同的專案中，常常會再根據自己的開發需求、功能…等等去做目錄結構的細分。

#### 1.1.2  常用目錄結構

##### 1.1.2.1      程式碼層的目錄結構

-  實體層 (Entity)

```
├── com.ian.entity (實體) 
├── com.ian.model (模型) 
```

​		Entity：包中的類是必須和資料庫相對應的。

​		Model：是為前端頁面提供資料和資料校驗的。

-  資料訪問對象 (Data Access Object 簡稱：DAO)

```
├── com.ian.dao (JPA項目)  
註：它是一個面向對象的資料庫介面，負責持久層的操作，為邏輯層提供介面，主要用來封裝對資料庫的訪問
```

- 邏輯介面層 (Service)

```
└── com.ian.service
```

- 邏輯實作層 (Service Implements)

```
└── com.ian.service.impl
```

-  Web層 (Controller)

```
└── com.ian.controller  註：如果是混和開發可以再細分頁面(web)的處理和單純的API 
├── com.ian.controller.web  
└── com.ian.controller.api
```

- 共用工具類 (utils)

```
└── com.ian.utils  註：共用性很高的類，例 DateUtil
```

-  資料傳輸層 (Data Transfer Object 簡稱：DTO)

```
└── com.ian.dto  註：資料傳輸對象（DTO）用於封裝多個實體類（domain）之間的關係，不破壞原有的實體類結構
```

##### 1.1.2.2      靜態資源的目錄結構(resources)

-  設定檔

```
resources/application.yml  註：官方推薦使用.yml來做撰寫，當然您也可以用.properties
```

- 靜態資源目錄

```
resources/static/  註：用於存放css、js、images等，基本上會再細分  
├── resources/static/css  
├── resources/static/js  
└── resources/static/images
```

- 範本目錄

```
resources/templates/  註：Spring Boot提供了默認配置的範本引擎，官方建議使用這些範本引擎(Thymeleaf、FreeMarker、Velocity、Groovy、Mustache)，避免使用JSP  
```

##### 1.1.2.3     整體目錄

```
com
 +- ian
     +- Application.java
     |
     +- customer
     |   +- Customer.java
     |   +- CustomerController.java
     |   +- CustomerService.java
     |   +- CustomerRepository.java
     |
     +- order
         +- Order.java
         +- OrderController.java
         +- OrderService.java
         +- OrderRepository.java
```

 啟動類 (Application.java)，推薦放置根目錄com.ian下

### 11、你如何理解 Spring Boot 中的 Starters？

Starters可以理解為啟動器，它包含了一系列可以集成到應用裡面的依賴包，你可以一站式集成 Spring 及其他技術，而不需要到處找示例代碼和依賴包。如你想使用 Spring JPA 訪問資料庫，只要加入 spring-boot-starter-data-jpa 啟動器依賴就能使用了。

Starters包含了許多專案中需要用到的依賴，它們能快速持續的運行，都是一系列得到支援的管理傳遞性依賴。

### 12、如何在 Spring Boot 啟動的時候運行一些特定的代碼

可以實現介面 ApplicationRunner 或者 CommandLineRunner，這兩個介面實現方式一樣，它們都只提供了一個 run 方法。

### 13、Spring Boot 有哪幾種讀取配置的方式？

Spring Boot 可以通過 @PropertySource,@Value,@Environment, @ConfigurationProperties 來綁定變數。

### 14、Spring Boot 支援哪些日誌框架？推薦和預設的日誌框架是哪個？

Spring Boot 支援 Java Util Logging, Log4j2, Lockback 作為日誌框架，如果你使用 Starters 啟動器，Spring Boot 將使用 Logback 作為預設日誌框架。

### 15、SpringBoot 實現熱部署有哪幾種方式？

主要有兩種方式：

- Spring Loaded
- Spring-boot-devtools

### 16、你如何理解 Spring Boot 配置載入順序？

在 Spring Boot 裡面，可以使用以下幾種方式來載入配置。

- properties文件；
- YAML文件；
- 系統環境變數；
- 命令列參數；

### 17、Spring Boot 如何定義多套不同環境配置？

提供多套設定檔，如：

```
applcation.properties
 
application-dev.properties
 
application-test.properties
 
application-prod.properties
```

運行時指定具體的設定檔，具體請看這篇文章。

### 18、Spring Boot 可以相容老 Spring 項目嗎，如何做？

可以相容，使用 `@ImportResource` 注解導入老 Spring 項目設定檔。

### 19、保護 Spring Boot 應用有哪些方法？

- 在生產中使用HTTPS
- 使用Snyk檢查你的依賴關係
- 升級到最新版本
- 啟用CSRF保護
- 使用內容安全性原則防止XSS攻擊

### 20、Spring Boot 2.X 有什麼新特性？與 1.X 有什麼區別？

- 配置變更
- JDK 版本升級
- 協力廠商類庫升級
- 回應式     Spring 程式設計支持
- HTTP/2 支持
- 配置屬性綁定


## 參考

[吐血整理 20 道 Spring Boot 面試題，我經常拿來面試別人！ - Java技術棧 - SegmentFault 思否](https://segmentfault.com/a/1190000016686735)

[什麼是Spring Boot?](https://mp.weixin.qq.com/s/jWLcPxTg9bH3D9_7qbYbfw)

[Spring Boot 核心設定檔詳解](https://mp.weixin.qq.com/s/BzXNfBzq-2TOCbiHG3xcsQ)

[Spring Boot 配置載入順序詳解](https://mp.weixin.qq.com/s/tFrRMM25LVE_2AG23lK5qQ)

[Spring Boot Profile 不同環境配置](https://mp.weixin.qq.com/s/K0kdQwoo2t5FDsTUJttSAA)

[Spring Boot開啟的2種方式](https://mp.weixin.qq.com/s/PYM_iV-u3dPMpP3MNz7Hig)

[Spring Boot自動配置原理、實戰](https://mp.weixin.qq.com/s/gs2zLSH6m9ijO0-pP2sr9Q)

[10 種保護 Spring Boot 應用的絕佳方法](https://mp.weixin.qq.com/s/HG4_StZyNCoWx02mUVCs1g)

[Spring Boot 主類及目錄結構介紹](https://mp.weixin.qq.com/s/auJGrOFVGlH8uzdk9SIHPw)

[Spring Boot Starters啟動器](https://mp.weixin.qq.com/s/9HJVGlplze5p0eBayvhFCA)

[Spring Boot讀取配置的幾種方式](https://mp.weixin.qq.com/s/aen2PIh0ut-BSHad-Bw7hg)

[Spring Boot實現熱部署](https://mp.weixin.qq.com/s/uv8jIztilO_QvGc7qGhSAA)

[Spring Boot日誌集成](https://mp.weixin.qq.com/s/OAyzUNIgBPkPVCy23gh-WA)

[SpringBoot - 第三章 | 目錄結構 | J.J.'s Blogs  ](https://morosedog.gitlab.io/springboot-20190314-springboot3/)