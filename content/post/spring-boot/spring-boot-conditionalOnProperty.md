---
title: "ConditionalOnProperty：條件式 Bean 與測試"
date: 2021-02-03T11:41:55+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
description: "清除 TODO 與過時註解屬性，完整示範存在、false、true 和缺值的行為。"
lastmod: 2026-10-07T00:01:00+08:00
---

清除 TODO 與過時註解屬性，完整示範存在、false、true 和缺值的行為。

<!--more-->

適用：原 Spring／Spring Boot 歷史筆記；新的可重現練習採 Spring Boot 3.5.0、Java21與Maven，使用jakarta套件。此為固定練習組合，上線另選相容且仍受支援的修補版。

先備：先依[共用 Spring Boot 練習專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})建立 pom.xml 與 NoteApplication，再加入本文檔案。

## 最小配置

先建立[共用Spring專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})。新增src/main/java/notes/DemoConfig.java：

```java
package notes;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
@Configuration
public class DemoConfig {
    @Bean
    @ConditionalOnProperty(prefix = "notes", name = "demo", havingValue = "true", matchIfMissing = false)
    public String demoMessage() { return "demo enabled"; }
}
```

application.properties設`notes.demo=true`時bean存在；false或缺值時不存在，並非自動報錯。只有另一個bean強制依賴它且沒有替代才可能導致啟動失敗。

## 可執行測試

src/test/java/notes/DemoConfigTest.java：

```java
package notes;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.runner.ApplicationContextRunner;
import static org.assertj.core.api.Assertions.assertThat;
class DemoConfigTest {
    private final ApplicationContextRunner runner = new ApplicationContextRunner().withUserConfiguration(DemoConfig.class);
    @Test void enabled() {
        runner.withPropertyValues("notes.demo=true").run(context -> assertThat(context).hasBean("demoMessage"));
    }
    @Test void disabled() {
        runner.withPropertyValues("notes.demo=false").run(context -> assertThat(context).doesNotHaveBean("demoMessage"));
    }
    @Test void missing() {
        runner.run(context -> assertThat(context).doesNotHaveBean("demoMessage"));
    }
}
```

`mvn test -Dtest=DemoConfigTest`應三個測試通過。

## 條件語意

沒指定havingValue時，預設屬性存在且值不是false才符合，不等於只能接受true。多個name需全部符合，prefix以點連線屬性名稱。集合屬性的索引不適合直接靠此條件推斷。舊範本的relaxedNames不是此練習版本可用屬性，已移除。

條件在建立context時判定，不是每次修改env就動態切換bean。用它控制示範資料或可選整合，避免把認證／授權的必要元件以易誤設旗標關掉。

## 查核範圍

直接編譯本文 DemoConfig／DemoConfigTest，true／false／缺值 3 個 ApplicationContextRunner 測試通過。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [ConditionalOnProperty API](https://docs.spring.io/spring-boot/3.5/api/java/org/springframework/boot/autoconfigure/condition/ConditionalOnProperty.html)
- [Context runner](https://docs.spring.io/spring-boot/3.5/reference/features/developing-auto-configuration.html#features.developing-auto-configuration.testing)

### 原始筆記保留的來源

- [@ConditionalOnProperty的作用和用法_sqlgao22的部落格-CSDN部落格](https://blog.csdn.net/sqlgao22/article/details/96476754)

### 原始筆記的其他連結

- [原始參考入口 1](https://reflectoring.io/spring-boot-conditionals/)
- [原始參考入口 2](https://blog.csdn.net/u010002184/article/details/79353696)
- [原始參考入口 3](https://stackoverflow.com/questions/40477251/spring-boot-spel-conditionalonexpression-check-multiple-properties/40497419#40497419)
- [原始參考入口 4](https://stackoverflow.com/questions/45736846/spring-conditionalonexpression-with-or-statement)
