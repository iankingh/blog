---
title: "Eclipse 與 JUnit 5：建立並執行測試"
date: 2020-09-29T22:13:19+08:00
categories:
 - "筆記"
tags:
 - "eclipse"
toc: true
draft: false
description: "補上完整測試與 Maven 依賴，確認 IDE 測試及命令列建置使用同一版本。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上完整測試與 Maven 依賴，確認 IDE 測試及命令列建置使用同一版本。

<!--more-->

適用：JUnit Jupiter 5.10.3、Java 8以上與支援JUnit5的Eclipse。這是原JUnit5情境，非宣稱最新major。

## 建立測試

已有Maven Java專案在pom.xml加入測試依賴與plugin：

```xml
<dependencies>
  <dependency>
    <groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter</artifactId>
    <version>5.10.3</version><scope>test</scope>
  </dependency>
</dependencies>
<build><plugins><plugin>
  <groupId>org.apache.maven.plugins</groupId><artifactId>maven-surefire-plugin</artifactId><version>3.2.5</version>
</plugin></plugins></build>
```

只整合既有相應節點，不在pom放兩組dependencies/build。新增 `src/test/java/MathTest.java`：

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
class MathTest {
    @Test
    void addsTwoIntegers() { assertEquals(4, 2 + 2); }
}
```

更新Maven Project後右鍵測試 → Run As → JUnit Test，預期1 tests、0 failures。`mvn test`也應成功。把預期4改成5應得到失敗，還原後再成功，確認測試確實有執行。

## 非 Maven 專案

原操作是Build Path → Add Library → JUnit → JUnit5。這適合IDE練習，但CI仍需有明確依賴；不要同時手動加一組與Maven帶入另一組。Run Configurations的Test runner選JUnit5，確認使用的JRE。

## 常見問題

「No tests found」檢查import是否Jupiter、檔案是否在test source、名稱是否符合建置工具掃描規則；JUnit4的org.junit.Test不是同一API。JUnit assertions不依賴JVM的-ea，和Java assert不同。版本升級先核對Java最低版本與extension相容性，保留lock／pom記錄。

## 參考資料

- [JUnit 5.10.3 指南](https://junit.org/junit5/docs/5.10.3/user-guide/)
- [Surefire JUnit](https://maven.apache.org/surefire/maven-surefire-plugin/examples/junit-platform.html)
- [Embracing JUnit 5 with Eclipse | The Eclipse Foundation](https://www.eclipse.org/community/eclipse_newsletter/2017/october/article5.php)
