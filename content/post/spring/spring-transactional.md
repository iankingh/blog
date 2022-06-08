---
title: "Spring_transactional"
date: 2021-04-27T20:58:19+08:00
draft: true
categories:
 - "筆記"
tags:
 - "java"
 - "spring"
toc: true
---

## 筆記
<!-- 簡介 -->



<!--more-->

## 聲明式交易範圍

`Spring`和`JPA` 均有`@Transaction`批註均允許您定義給定應用程序事務的範圍。

因此，如果使用註釋對服務方法進行`@Transactional`註釋，則它將在事務上下文中運行。如果服務方法使用多個`DAO`或存儲庫，則所有讀取和寫入操作將在同一數據庫事務中執行。

## Spring `@Transactional`

`org.springframework.transaction.annotation.Transactional`自`Spring`框架的1.2版本（大約2005年）以來，該註釋已可用，它允許您設置以下事務屬性：

- `isolation`：基礎數據庫隔離級別
- `noRollbackFor`和`noRollbackForClassName`：`Exception`可以在不觸發事務回滾的情況下觸發的Java類的列表
- `rollbackFor`和`rollbackForClassName`：`Exception`拋出時觸發事務回滾的Java類的列表
- `propagation`：由[`Propagation`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/transaction/annotation/Propagation.html)Enum給出的事務傳播類型。例如，如果可以繼承事務上下文（例如`REQUIRED`），或者應該創建新的事務上下文（例如`REQUIRES_NEW`），或者如果不存在事務上下文（例如`MANDATORY`）或者應該引發異常，則應該引發異常如果找到了當前的交易環境（例如`NOT_SUPPORTED`）。
- `readOnly`：當前事務是否僅應讀取數據而不進行任何更改。
- `timeout`：應允許事務上下文運行多少秒，直到引發超時異常。
- `value`或`transactionManager`：`TransactionManager`綁定事務上下文時要使用的Spring bean的名稱。

## Java EE `@Transactional`

該javax.transaction.Transactional批註是由Java EE 7規範（大約在2013年）添加的。因此，Java EE註釋比Spring註釋晚了8年。

Java EE `@Transactional`僅定義了3個屬性：

- `dontRollbackOn`：`Exception`可以在不觸發事務回滾的情況下觸發的Java類的列表
- `rollbackOn`：`Exception`拋出時觸發事務回滾的Java類的列表
- `value`：由[`TxType`](https://docs.oracle.com/javaee/7/api/javax/transaction/Transactional.TxType.html)Enum給出的傳播策略。例如，如果可以繼承事務上下文（例如`REQUIRED`），或者應該創建新的事務上下文（例如`REQUIRES_NEW`），或者如果不存在事務上下文（例如`MANDATORY`）或者應該引發異常，則應該引發異常如果找到了當前的交易環境（例如`NOT_SUPPORTED`）。

## Which one to choose?

如果您使用的是Spring或Spring Boot，請使用Spring`@Transactional`批註，因為它允許您配置比Java EE`@Transactional`批註更多的屬性。

如果單獨使用Java EE，並且將應用程序部署在Java EE應用程序服務器上，請使用Java EE`@Transactional`批註。



## 參考

[java - javax.transaction.Transactional vs org.springframework.transaction.annotation.Transactional - Stack Overflow](https://stackoverflow.com/questions/26387399/javax-transaction-transactional-vs-org-springframework-transaction-annotation-tr)



