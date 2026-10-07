---
title: "Spring Profile 與 Maven Profile：執行期和建置期"
date: 2023-07-06T11:48:00Z
categories:
- "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
draft: false
description: "補上可比較的配置與啟動命令，說明 profile 不會自動在兩種工具間同步。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上可比較的配置與啟動命令，說明 profile 不會自動在兩種工具間同步。

<!--more-->

適用：原 Spring／Spring Boot 歷史筆記；新的可重現練習採 Spring Boot 3.5.0、Java21與Maven，使用jakarta套件。此為固定練習組合，上線另選相容且仍受支援的修補版。

先備：先依[共用 Spring Boot 練習專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})建立 pom.xml 與 NoteApplication，再加入本文檔案。

## 兩種Profile

Maven profile在建置時選依賴、plugin或property，Spring profile在應用context建立時選設定與bean。同名dev也不會自動連動；要連動必須明確寫filter或plugin引數，並注意是否把環境內容烘進jar。

共用專案的src/main/resources/application.properties：

```properties
notes.banner=default
```

application-dev.properties：

```properties
notes.banner=development
```

新增BannerConfig.java：

```java
package notes;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
@Configuration
public class BannerConfig {
    @Bean
    CommandLineRunner showBanner(@Value("${notes.banner}") String banner) {
        return args -> System.out.println("notes.banner=" + banner);
    }
}
```

## 執行確認

```bash
mvn package
java -jar target/spring-note-lab-1.0.0.jar --spring.profiles.active=dev
```

日誌應包含notes.banner=development。不指定dev則default。JVM系統引數寫在-jar之前，如`java -Dspring.profiles.active=dev -jar ...`；寫在jar後是應用引數，不是JVM引數。

Maven可在pom profiles定義id後用`mvn -Pdev help:active-profiles`確認；僅加-Pdev不會啟用Spring dev。部署可使用OS SPRING_PROFILES_ACTIVE或命令引數，但屬性優先順序需按Boot文件核對，同一key不要散落多個來源。

## 常見問題

spring.profiles.active不放在已由profile啟用的專屬檔案內遞迴決定自身。profile不是秘密管理系統，勿提交prod密碼。Config Data／Spring Cloud bootstrap機制在不同major有變化，新專案按所用版本選spring.config.import，不複製舊bootstrap.yml當通用配置。

## 參考資料

- [Spring profiles](https://docs.spring.io/spring-boot/3.5/reference/features/profiles.html)
- [外部配置](https://docs.spring.io/spring-boot/3.5/reference/features/external-config.html)
- [Maven profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
- [Spring Profiles | Baeldung](https://www.baeldung.com/spring-profiles)
- [Spring profiles or Maven profiles? (frankel.ch)](https://blog.frankel.ch/spring-profiles-or-maven-profiles/)
- [深入淺出 Spring Boot 多重設定檔管理 (Spring Profiles) | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2022/09/21/Mastering-Spring-Boot-Profiles)
- [菜鳥工程師 肉豬: Spring Boot 依環境設定不同的properties檔 Use different application.properties (matthung0807.blogspot.com)](https://matthung0807.blogspot.com/2020/04/spring-boot-different-environment.html)
- [54. Properties & configuration (spring.io)](https://docs.spring.io/spring-boot/docs/1.0.1.RELEASE/reference/html/howto-properties-and-configuration.html)
