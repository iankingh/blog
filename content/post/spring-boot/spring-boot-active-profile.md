---
title: "Spring Boot Active Profile"
date: 2023-07-06T11:48:00Z
categories:
- "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
draft: true
---

## Spring Boot Active Profile VS Maven profiles
<!-- 簡介 -->
<!--more-->

## 前言 

在java中我們有時候會根據不同的環境(dev , sit , uat , prod ) 來讀取不同的設定 ,EX: 例如連線設定 , API ... 等設定 
目前Java 主要有 **Maven Profile** 與 **Spring Boot Active Profile** 都是用來處理應用程式中不同環境的設定，但它們之間有一些重要的差異。

## Maven Profile

Maven Profile 是 Maven 的一個功能，允許您根據不同的環境和條件進行構建配置。它通常用於根據開發、測試和生產等不同環境來切換不同的構建設定。您可以在 `pom.xml` 文件中定義 Maven Profile。

舉個例子，以下是一個簡單的 Maven Profile 配置：

```xml
<profiles>
  <profile>
    <id>development</id>
    <properties>
      <env>dev</env>
    </properties>
  </profile>
  <profile>
    <id>production</id>
    <properties>
      <env>prod</env>
    </properties>
  </profile>
</profiles>
```

在此示例中，我們定義了兩個 Maven Profile，分別為開發環境和生產環境。當需要構建不同環境的應用程式時，可以通過在 Maven 命令中指定 Profile 的 ID 來選擇使用哪個 Profile。

## Spring Boot Active Profile

Spring Boot Active Profile 是用於在運行時切換 Spring Boot 應用程式的不同環境配置。它允許您根據不同環境使用不同的配置文件，以便根據當前環境運行應用程式。您可以使用 
- `application-{profile}.yml` 
- `application-{profile}.properties` 
格式的文件來定義 Spring Boot Profile。

常見的環境設定
-- application.yml
-- application-dev.yml
-- application-sit.yml
-- application-uat.yml
-- application-prod.yml

1. The Spring `Environment` has an API for this, but normally you would set a System profile (`spring.profiles.active`) or an OS environment variable (`SPRING_PROFILES_ACTIVE`). E.g. launch your application with a `-D` argument (remember to put it before the main class or jar archive):

2. 在啟動的時候設定
`$ java -jar -Dspring.profiles.active=production demo-0.0.1-SNAPSHOT.jar`

3. In Spring Boot you can also set the active profile in `application.properties`, e.g.
```yaomo
spring.profiles.active=production
```

舉個例子，以下是一個簡單的 Spring Boot Active Profile 配置：

#### `application-dev.yml`

```yaml
spring:
  profiles:
    active: dev
server:
  port: 8080
```

#### `application-prod.yml`

```yaml
spring:
  profiles:
    active: prod
server:
  port: 80
```

在此示例中，我們定義了兩個 Spring Boot Active Profile，分別為開發環境和生產環境。您可以通過設置環境變量 `SPRING_PROFILES_ACTIVE` 或在應用程式的命令行參數中指定 `--spring.profiles.active` 來選擇要不同的 Profile。

## 差異

主要差異在於：
### 運行的時機
1. Maven Profile 是在構建階段管理配置，
2. Spring Boot Active Profile 是在運行時管理配置。
### 使用時機
4. Maven Profile 主要用於不同環境的構建設定，
5. spring Boot Active Profile 用於不同環境的應用程式運行設定。

## summary 
總之，Maven Profile 和 Spring Boot Active Profile 都可以用來切換不同環境的配置，但它們運作在不同的階段（構建和運行），並滿足不同的需求。在實際開發中，可能需要結合使用兩者，以便更好地滿足不同環境的需求。

我個人偏好 Spring Boot Active Profile 並用 yaml 設定




## 參考

[Spring Profiles | Baeldung](https://www.baeldung.com/spring-profiles)

[Spring profiles or Maven profiles? (frankel.ch)](https://blog.frankel.ch/spring-profiles-or-maven-profiles/)

[深入淺出 Spring Boot 多重設定檔管理 (Spring Profiles) | The Will Will Web (miniasp.com)](https://blog.miniasp.com/post/2022/09/21/Mastering-Spring-Boot-Profiles)

[菜鳥工程師 肉豬: Spring Boot 依環境設定不同的properties檔 Use different application.properties (matthung0807.blogspot.com)](https://matthung0807.blogspot.com/2020/04/spring-boot-different-environment.html)

[54. Properties & configuration (spring.io)](https://docs.spring.io/spring-boot/docs/1.0.1.RELEASE/reference/html/howto-properties-and-configuration.html)