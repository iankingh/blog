---
title: "SQLcommand"
date: 2021-03-15T09:31:14+08:00
draft: false
categories:
 - "筆記"
tags:
 - "SQL"
toc: true
---
## SQL Server 相關的語法和操作

<!-- 簡介 -->
記錄一些 SQL Server 相關的語法和操作，以下是更完整的說明：
<!--more-->

## ALTER TABLE

ALTER TABLE：用於修改已存在的資料表結構，可以使用 ADD COLUMN 增加欄位。例如：

- 增加欄位 (ADD COLUMN)
- 語法

```SQL
ALTER TABLE table_name ADD column_name datatype;
```

要為新欄位加上預設值，可以使用以下語法：

```SQL 
ALTER TABLE customer ADD DEFAULT '未知' FOR Address;

```

## CREATE LOGIN [Account]

CREATE LOGIN：用於新增一個登入帳號，可以指定密碼、預設資料庫和語言等屬性。例如：

```sql
CREATE LOGIN [Account] WITH PASSWORD=N'!qaz2wsx', DEFAULT_DATABASE=[DATABASE_Name], DEFAULT_LANGUAGE=[Traditional Chinese], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
```

## CREATE USER

CREATE USER：用於新增一個使用者，可以指定該使用者所屬的登入帳號。例如：

```sql
USE [DATABASE_Name]
GO
CREATE USER [user_name] FOR LOGIN [Account];
GO
```

- 也可以先新增登入帳號，再使用該帳號建立使用者：

```sql
CREATE LOGIN Account WITH PASSWORD = '!qaz2wsx';  

CREATE USER  user_name FOR LOGIN user_name; 

```

## DROP USER

DROP USER：用於刪除一個使用者。例如：

```sql
DROP USER user_name
GO
```

### GRANT CREATE 

GRANT：用於授權使用者執行某些操作，例如 GRANT CREATE ANY DATABASE 可以讓使用者建立任何資料庫，而 GRANT SELECT 可以讓使用者查詢資料表中的資料。例如：

```sql
GRANT CREATE ANY DATABASE TO [user_name]
GO
```

### Grant select to user

要授權使用者執行 SELECT 操作，可以使用以下語法：

```sql
GRANT SELECT ON table_name TO user_name;
GO
```


###  SQL server 知識
 
- sql cluster 是提供服務的

- sql server 是提供連線服務介面的


## 參考

[SQL DEFAULT 預設值 - SQL 語法教學 Tutorial (fooish.com)](https://www.fooish.com/sql/default-constraint.html)
[SQL ALTER TABLE 更改資料表 - SQL 語法教學 Tutorial (fooish.com)](https://www.fooish.com/sql/alter-table.html)




