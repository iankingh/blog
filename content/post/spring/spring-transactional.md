---
title: "Transactional：代理、回滾與交易範圍"
date: 2021-04-27T20:58:19+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "spring"
toc: true
description: "修正 Spring 與 JTA 註解比較，補上真正經過代理的回滾測試與限制。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 Spring 與 JTA 註解比較，補上真正經過代理的回滾測試與限制。

<!--more-->

適用：原 Spring／Spring Boot 歷史筆記；新的可重現練習採 Spring Boot 3.5.0、Java21與Maven，使用jakarta套件。此為固定練習組合，上線另選相容且仍受支援的修補版。

先備：先依[共用 Spring Boot 練習專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})建立 pom.xml 與 NoteApplication，再加入本文檔案。

## 註解與預設

Spring的`org.springframework.transaction.annotation.Transactional`提供propagation、isolation、readOnly、timeout等；JavaEE舊`javax.transaction.Transactional`目前對應`jakarta.transaction.Transactional`，不是JPA本身的註解。選擇依框架與交易管理器，不按出現年份判斷好壞。

Spring常見預設是REQUIRED、RuntimeException／Error回滾，checked exception需rollbackFor等明確設定；Spring6.2可配置全域預設回滾策略，因此仍要查實際設定。readOnly是最佳化提示，不保證資料庫拒絕所有寫入。

## 代理服務與測試

先完成JPA篇Task／TaskRepository，新增TaskService.java：

```java
package notes;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
@Service
public class TaskService {
    private final TaskRepository repository;
    public TaskService(TaskRepository repository) { this.repository = repository; }
    @Transactional
    public void createThenFail() {
        repository.saveAndFlush(new Task("應被回滾"));
        throw new IllegalStateException("模擬失敗");
    }
}
```

TaskServiceTest.java：

```java
package notes;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.assertj.core.api.Assertions.*;
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.NONE)
class TaskServiceTest {
    @Autowired TaskService service;
    @Autowired TaskRepository repository;
    @Test void rollsBack() {
        long before = repository.count();
        assertThatThrownBy(() -> service.createThenFail()).isInstanceOf(IllegalStateException.class);
        assertThat(repository.count()).isEqualTo(before);
    }
}
```

mvn test -Dtest=TaskServiceTest應通過；測試本身不包@Transactional，以免測試外層交易掩蓋服務是否真有代理。

## 邊界

同一物件內部self-invocation通常繞過代理，new出來的服務也不會被Spring攔截。跨執行緒、HTTP或不同資料來源不會自動共享一個交易；REQUIRES_NEW需額外連線且可能加劇pool耗盡。不要在長交易中做不可靠遠端呼叫，也不吞掉例外讓外層誤以為成功。

確認回滾以資料庫結果與交易日誌為準，不只看到exception。非關聯資料庫與reactive交易還需不同管理器和context傳播策略。

## 參考資料

- [Spring Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html)
- [交易传播](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html)
- [Jakarta Transactions](https://jakarta.ee/specifications/transactions/)
- [`Propagation`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/transaction/annotation/Propagation.html)
- [`TxType`](https://docs.oracle.com/javaee/7/api/javax/transaction/Transactional.TxType.html)
- [java - javax.transaction.Transactional vs org.springframework.transaction.annotation.Transactional - Stack Overflow](https://stackoverflow.com/questions/26387399/javax-transaction-transactional-vs-org-springframework-transaction-annotation-tr)
