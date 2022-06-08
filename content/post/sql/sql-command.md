---
title: "SQLcommand"
date: 2021-03-15T09:31:14+08:00
draft: true
categories:
 - "筆記"
tags:
 - "xxx"
 - "xxx"
toc: true
---

## 筆記
<!-- 簡介 -->
<!--more-->




## ALTER TABLE   

ALTER TABLE 是用來對已存在的資料表結構作更改。語法型式如下：


增加欄位 (ADD COLUMN)
語法

```
ALTER TABLE table_name ADD column_name datatype;
```
EX :

```
```


如果要加上 預設值

語法
```
ALTER TABLE customer ADD DEFAULT '未知' FOR Address;

```
EX: 

## CREATE LOGIN [Account]

```sql
CREATE LOGIN [Account] WITH PASSWORD=N'!qaz2wsx', DEFAULT_DATABASE=[DATABASE_Name], DEFAULT_LANGUAGE=[Traditional Chinese], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
```

## CREATE USER

```sql
USE [DATABASE_Name]
GO
CREATE USER [user_name] FOR LOGIN [Account];
GO


CREATE LOGIN Account WITH PASSWORD = '!qaz2wsx';  

CREATE USER  user_name FOR LOGIN user_name; 

```

### DROP USER 

```sql
DROP USER user_name
GO
```

### GRANT CREATE 

```sql
GRANT CREATE ANY DATABASE TO [user_name]
GO
```

### Grant select to user

```sql
Grant select to vvs
GO
```


-------------- SQL server 
sql cluster 是提供服務的

sql server 是提供連線服務介面的





## 參考

https://www.fooish.com/sql/default-constraint.html

https://www.fooish.com/sql/alter-table.html




