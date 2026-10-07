---
title: "Spring Data JPA：Repository 與分頁查詢"
date: 2020-06-04T05:45:59+08:00
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring Data JPA"
toc: true
draft: false
description: "理解 Repository 介面與分頁，以 H2 範例比較衍生查詢、JPQL 及 native SQL。"
lastmod: 2026-10-07T23:41:34+08:00
---

理解 Repository 介面與分頁，以 H2 範例比較衍生查詢、JPQL 及 native SQL。

<!--more-->

適用：保留原 Spring／Spring Boot 歷史筆記；可重現練習統一採 Spring Boot 3.5.16、JDK 25 與 Maven，使用 jakarta 套件。編譯目標為 Java 25；上線仍需核對依賴及部署環境。

先備：先依[共用 Spring Boot 練習專案]({{< ref "/post/spring-boot/spring-boot-interview.md" >}})建立 pom.xml 與 NoteApplication，再加入本文檔案。

## 三個層次

JPA是持久化規格，Hibernate是實作之一，Spring Data JPA在其上提供Repository抽象。它不會替你決定所有業務交易，也不是「永遠不用SQL」；複雜查詢、索引、N+1與資料庫差異仍要理解。

使用共用Boot3.5.16專案（web、data-jpa與H2）。src/main/java/notes/Task.java：

```java
package notes;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
@Entity
public class Task {
    @Id @GeneratedValue private Long id;
    private String title;
    protected Task() {}
    public Task(String title) { this.title = title; }
    public Long getId() { return id; }
    public String getTitle() { return title; }
}
```

TaskRepository.java：

```java
package notes;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
public interface TaskRepository extends JpaRepository<Task, Long> {
    Page<Task> findByTitleContaining(String keyword, Pageable pageable);
}
```

## 測試

src/test/java/notes/TaskRepositoryTest.java：

```java
package notes;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import static org.assertj.core.api.Assertions.assertThat;
@DataJpaTest
class TaskRepositoryTest {
    @Autowired TaskRepository repository;
    @Test void findsAndPages() {
        repository.save(new Task("Vue 練習"));
        repository.save(new Task("Java 練習"));
        var page = repository.findByTitleContaining("Vue", PageRequest.of(0, 10, Sort.by("id")));
        assertThat(page.getTotalElements()).isEqualTo(1);
        assertThat(page.getContent().get(0).getTitle()).isEqualTo("Vue 練習");
    }
}
```

mvn test -Dtest=TaskRepositoryTest應通過；H2只供本機模擬，不證明正式SQL dialect全部一致。

## 查詢與版本差異

方法名屬性需與entity一致，JPQL查entity／屬性，nativeQuery查表／欄位。@Query可描述複雜條件；動態條件可用Specification，批次update/delete需@Modifying與交易，且留意persistence context中的舊資料。

Spring Data3起部分sorting repository不再繼承CRUD介面，舊繼承圖不能直接套用；JpaRepository仍提供常用CRUD與分頁能力。分頁從0開始、穩定排序加入唯一鍵；Page通常另做count查詢，若不需總數可評估Slice。Lazy關聯、open-in-view與N+1需用SQL日誌與查詢計劃確認，不靠新增註解盲修。

## Repository 介面與舊版筆記對照

| 介面 | 責任與選擇 |
| --- | --- |
| `Repository<T, ID>` | 標記介面，亦可只宣告需要的方法，限制暴露的 API |
| `CrudRepository<T, ID>` | `save`、`findById`、`existsById`、`delete` 等 CRUD；查無資料時 `findById` 回 Optional |
| `PagingAndSortingRepository<T, ID>` | `findAll(Pageable)` 與排序；Spring Data 3 起不再自行帶入 CRUD，需要組合介面 |
| `JpaRepository<T, ID>` | JPA 常用 CRUD、排序分頁及 `flush`／批次相關操作 |
| `JpaSpecificationExecutor<T>` | 將可組合的 Criteria 條件用於動態查詢；與 JpaRepository 一起繼承 |

原 Spring Data 2.x 範例多用 `javax.persistence`，Boot 3／Hibernate 6 改用 `jakarta.persistence`；不要在同一 Entity 混用兩者。`save` 不保證方法回傳時 SQL 已立即送出，flush 也不等於 transaction commit。使用 `getReferenceById` 取得代理與 `findById` 實際查詢的語意不同，存取不存在資料時發生例外的位置也可能不同。

## 方法名、JPQL 與 native SQL

保留原筆記的查詢分類，選擇最易讀且能測試的方式。將下列方法加入既有 `TaskRepository`，並加入兩個 import：

```java
import java.util.List;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
```

```java
List<Task> findByTitleStartingWithOrderByIdAsc(String prefix);
@Query("select t from Task t where t.title = :title order by t.id")
List<Task> findExact(@Param("title") String title);
@Query(value = "select * from task where title = :title order by id", nativeQuery = true)
List<Task> findExactNative(@Param("title") String title);
```

上例是介面內的增補片段，不是另一個完整 Java 檔案。JPQL 使用 `Task` 與 `title` 物件名稱，native SQL 使用實際表／欄位名稱；資料庫大小寫、分頁和函式仍需在目標 dialect 測試。參數綁定不等於可以把外部輸入拼接成查詢字串。

常用衍生條件有 `And`、`Or`、`Between`、`LessThan`、`IsNull`、`Containing`、`In`，屬性拼字需和 Entity 一致；查詢名字過長時用 @Query 或 Specification，比堆疊難閱讀的方法名更合適。Specification 以 Criteria API 組合 predicate，並不取代授權、穩定排序或查詢成本評估。

## 參考資料

- [Query methods](https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html)
- [Repository 介面](https://docs.spring.io/spring-data/commons/reference/repositories/definition.html)
- [JPA交易](https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html)
- [Spring Data](https://spring.io/projects/spring-data)
- [Spring Data JPA - Reference Documentation](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#reference)
- [Spring For All 社群 Spring Data JPA 從入門到進階系列教程 | Spring For All (spring4all.com)](http://www.spring4all.com/article/500)
