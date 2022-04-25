---
title: "Sql_server"
date: 2021-08-02T22:03:19+08:00
draft: true
categories:
 - "筆記"
tags:
 - "sql"
 - "sql Server"
toc: true
---

## SQL Server 筆記
<!-- 簡介 -->
<!--more-->

## 建立帳號、使用者、DB與授權角色

### 創建DB

```sql
CREATE DATABASE [DBName]
GO
```

### 創建帳號

```sql
CREATE LOGIN [Account] WITH PASSWORD=N'Password', DEFAULT_DATABASE=[DBName], DEFAULT_LANGUAGE=[Traditional Chinese], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO

```

### 帳號啟用

```sql
ALTER LOGIN [Account] EnABLE
GO
```

### 授權使用者登入[DBName]

```sql
USE [DBName]
GO
CREATE USER [UserName] FOR LOGIN [Account];
GO

```

### 授權使用者在[DBName]裡的角色

```sql
USE [DBName]
GO
ALTER ROLE [db_owner] ADD MEMBER [UserName]
GO

```

**註：**

`CHECK_EXPIRATION：密碼過期`</br>

`CHECK_POLICY：密碼原則`</br>

`db_owner`：被授予owner角色可以編輯[DBName]資料庫，通常需要設計表格的USER會賦予此角色</br>

`db_datareader`：被授予datareader角色可以對[DBName]資料庫下查詢指令
</br>

`db_datawriter`：被授予datawriter角色可以對[DBName]資料庫下新增、修改與刪除指令



## 參考

[Java 練工廠: [SQL Server]建立帳號、使用者、DB與授權角色](http://rogercode.blogspot.com/2015/08/sql-serverdb.html)
