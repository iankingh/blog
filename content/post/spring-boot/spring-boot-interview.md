---
title: "Spring Boot 核心觀念：自動配置、設定與可驗證回答"
date: 2021-03-16T13:17:45+08:00
draft: false
categories:
 - "筆記"
tags:
 - "spring"
 - "spring Boot"
toc: true
description: "將 Spring Boot 核心觀念對照可觀察的配置與測試，釐清舊版面試題和現代專案的差異。"
lastmod: 2026-10-07T23:41:34+08:00
---

將 Spring Boot 核心觀念對照可觀察的配置與測試，釐清舊版面試題和現代專案的差異。

<!--more-->

適用：保留原 Spring／Spring Boot 歷史筆記；可重現練習統一採 Spring Boot 3.5.16、JDK 25 與 Maven，使用 jakarta 套件。編譯目標為 Java 25；上線仍需核對依賴及部署環境。

## 共用練習專案

建立pom.xml：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-parent</artifactId><version>3.5.16</version><relativePath/></parent>
  <groupId>notes</groupId><artifactId>spring-note-lab</artifactId><version>1.0.0</version>
  <properties><java.version>25</java.version></properties>
  <dependencies>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-web</artifactId></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-data-jpa</artifactId></dependency>
    <dependency><groupId>com.h2database</groupId><artifactId>h2</artifactId><scope>runtime</scope></dependency>
    <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-test</artifactId><scope>test</scope></dependency>
  </dependencies>
  <build><plugins>
    <plugin><groupId>org.springframework.boot</groupId><artifactId>spring-boot-maven-plugin</artifactId></plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId><artifactId>maven-dependency-plugin</artifactId>
      <executions><execution><goals><goal>properties</goal></goals></execution></executions>
    </plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId><artifactId>maven-surefire-plugin</artifactId>
      <configuration><argLine>-javaagent:"${org.mockito:mockito-core:jar}"</argLine></configuration>
    </plugin>
  </plugins></build>
</project>
```

src/main/java/notes/NoteApplication.java：

```java
package notes;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class NoteApplication {
    public static void main(String[] args) { SpringApplication.run(NoteApplication.class, args); }
}
```

執行`mvn test`、`mvn spring-boot:run`，初始沒有Controller所以首頁404是預期，不是啟動失敗；後續JPA與Swagger章加業務內容。

先以 `java -version`、`javac -version` 與 `mvn -version` 確認均使用 JDK 25。本次使用 OpenJDK 25.0.4.1；Maven 編譯目標為 25，產生的 class major version 為 69。

測試依賴中的 Mockito 需要 instrumentation。上面的 dependency plugin 取得實際 mockito-core JAR 路徑，再由 Surefire 以 `-javaagent` 載入；不依賴 JVM 自行附加 agent，也不需填入本機絕對路徑。此設定只影響測試 JVM。

## 面試回答應包含什麼

- Spring Boot建立在Spring之上，提供依賴管理、starter、自動配置與執行／維運整合，不是取代Spring。
- @SpringBootApplication組合配置、auto-configuration與component scan；主類別放共同根package，避免掃描漏掉。
- 自動配置依classpath、bean、properties等條件決定，使用--debug檢視conditions report；自己提供bean常使對應配置退讓，不是固定生成所有bean。
- starter-parent提供Maven慣例與依賴管理，單純import BOM不會自動帶入相同plugin配置。
- application.properties/yaml為應用配置，bootstrap是部分Spring Cloud歷史機制，不是所有Boot專案必備；新版Config Data另有spring.config.import。
- Web starter與WebFlux使用不同程式模型／容器組合，不能說所有Boot都使用同一Tomcat；外部WAR部署也需核對Servlet版本。
- Actuator提供觀測端點，但公開哪些、是否可寫和如何授權需要設計，不能全部公開。

## 驗證答案

問題要能落到一個可觀察實驗：移除starter看classpath變化、提供自訂bean看條件報告、改變profile看設定來源。配置不等於效能或微服務架構已完成；還需測試、監控與部署策略。

## 原面試題的補充範圍

保留原二十題的主題，以下是前面核心觀念之外需要講清楚的項目：

| 題目 | 回答與核對方式 |
| --- | --- |
| 配置格式 | properties 與 YAML 都可使用；YAML 依縮排、properties 依鍵名表達。用同一個設定值與啟動輸出確認解析結果，不把格式當功能差異 |
| 啟動方式 | IDE main、`mvn spring-boot:run`、可執行 JAR；傳統 WAR 需相容 Servlet 容器及 initializer，打包格式和執行方式分開討論 |
| 啟動後的程式 | CommandLineRunner／ApplicationRunner 可取得啟動參數；順序、耗時與例外會影響應用啟動，參考 Profile 篇的 banner 範例 |
| 讀取配置 | @Value 適合少量值，@ConfigurationProperties 適合型別化群組與驗證；Environment 可查來源，避免把配置散落成魔法字串 |
| 日誌 | 常用 starter 預設經 SLF4J 使用 Logback；替換日誌實作需排除衝突依賴，觀察 dependency tree，不將所有實作同時引入 |
| 開發重新啟動 | DevTools 是開發工具；restart、LiveReload、JVM HotSwap 行為不同，瀏覽器重新整理不代表後端程式已更新，也不把 DevTools 帶入正式功能 |
| 配置優先順序 | 啟動引數、環境變數、外部配置與 packaged 配置按所用 Boot 版本的官方順序覆寫；以相同 key 的可觀察值確認，參考 Profile 篇 |
| 舊 Spring 整合 | @Import 引入 Java 配置，@ImportResource 可載入需要保留的 XML；先核對 bean、掃描與相容依賴，並不保證所有舊 servlet／javax 庫可直接進 Boot3 |
| 保護應用 | 身分驗證、API 授權、輸入驗證、秘密管理與依賴維護各有責任；Actuator 管理端點另控管，不以隱藏 UI 當 API 授權 |
| 1.x／2.x／3.x 差異 | 原題的 Boot2／Spring5／Java8 是歷史版本線；Boot3 的 Java17 最低要求與 Jakarta 遷移另查 migration guide，本篇練習固定 JDK 25，不表示 Boot 3 的最低要求也變成 25 |

完整功能仍應由小專案核對；例如設定為 dev 後檢查 banner、加入 Controller 後檢查 HTTP 回應，再增加資料庫與交易。不能只背一串註解就宣稱完成整合。

## 參考資料

- [Spring Boot 3.5 系統需求與 JDK 25 相容性](https://docs.spring.io/spring-boot/3.5/system-requirements.html)
- [Mockito 在新版 JVM 的 agent 設定](https://javadoc.io/static/org.mockito/mockito-core/5.17.0/org.mockito/org/mockito/Mockito.html#0.3)
- [Maven 依賴 properties goal](https://maven.apache.org/plugins/maven-dependency-plugin/properties-mojo.html)
- [Auto configuration](https://docs.spring.io/spring-boot/3.5/reference/using/auto-configuration.html)
- [Build systems](https://docs.spring.io/spring-boot/3.5/reference/using/build-systems.html)
- [External config](https://docs.spring.io/spring-boot/3.5/reference/features/external-config.html)
- [吐血整理 20 道 Spring Boot 面試題，我經常拿來面試別人！ - Java技術棧 - SegmentFault 思否](https://segmentfault.com/a/1190000016686735)
- [什麼是Spring Boot?](https://mp.weixin.qq.com/s/jWLcPxTg9bH3D9_7qbYbfw)
- [Spring Boot 核心設定檔詳解](https://mp.weixin.qq.com/s/BzXNfBzq-2TOCbiHG3xcsQ)
- [Spring Boot 配置載入順序詳解](https://mp.weixin.qq.com/s/tFrRMM25LVE_2AG23lK5qQ)
- [Spring Boot Profile 不同環境配置](https://mp.weixin.qq.com/s/K0kdQwoo2t5FDsTUJttSAA)
- [Spring Boot開啟的2種方式](https://mp.weixin.qq.com/s/PYM_iV-u3dPMpP3MNz7Hig)
- [Spring Boot自動配置原理、實戰](https://mp.weixin.qq.com/s/gs2zLSH6m9ijO0-pP2sr9Q)
- [10 種保護 Spring Boot 應用的絕佳方法](https://mp.weixin.qq.com/s/HG4_StZyNCoWx02mUVCs1g)
- [Spring Boot 主類及目錄結構介紹](https://mp.weixin.qq.com/s/auJGrOFVGlH8uzdk9SIHPw)
- [Spring Boot Starters啟動器](https://mp.weixin.qq.com/s/9HJVGlplze5p0eBayvhFCA)
- [Spring Boot讀取配置的幾種方式](https://mp.weixin.qq.com/s/aen2PIh0ut-BSHad-Bw7hg)
- [Spring Boot實現熱部署](https://mp.weixin.qq.com/s/uv8jIztilO_QvGc7qGhSAA)
- [Spring Boot日誌整合](https://mp.weixin.qq.com/s/OAyzUNIgBPkPVCy23gh-WA)
- [SpringBoot - 第三章 | 目錄結構 | J.J.'s Blogs  ](https://morosedog.gitlab.io/springboot-20190314-springboot3/)
