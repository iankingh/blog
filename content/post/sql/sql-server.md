---
title: "SQL Server 許可權：Login、User 與最小角色"
date: 2021-08-02T22:03:19+08:00
categories:
 - "筆記"
tags:
 - "sql"
 - "SQL Server"
toc: true
draft: false
description: "補上伺服器與資料庫身份差異，以無登入測試使用者驗證 SELECT 許可權。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上伺服器與資料庫身份差異，以無登入測試使用者驗證 SELECT 許可權。

<!--more-->

適用：SQL Server2019/2022測試資料庫，需由有相應管理許可權的帳號建立測試物件。

## 兩層身份

LOGIN在伺服器層負責認證，USER在資料庫層負責資料庫存取，通常以FOR LOGIN建立對應。contained user是另一種配置，Azure SQL與本機也有差異，先確認實際服務。

原`CHECK_POLICY=OFF`與共用Password、預設db_owner不適合作通用範例。真實SQL登入使用部署提供強密碼並核對Windows身份／SQL身份模式；本篇用WITHOUT LOGIN展示DB授權，沒有可直接登入的密碼帳號。

## 測試 DB 內操作

在隔離測試DB中：

```sql
CREATE TABLE dbo.NoteTasks (Id int PRIMARY KEY, Title nvarchar(100) NOT NULL);
INSERT INTO dbo.NoteTasks VALUES (1, N'測試任務');
CREATE USER NoteReader WITHOUT LOGIN;
CREATE ROLE NoteReadRole;
GRANT SELECT ON OBJECT::dbo.NoteTasks TO NoteReadRole;
ALTER ROLE NoteReadRole ADD MEMBER NoteReader;
EXECUTE AS USER = 'NoteReader';
SELECT Id, Title FROM dbo.NoteTasks;
REVERT;
```

SELECT應回1／測試任務。另在EXECUTE AS之後測試UPDATE應被拒絕，再REVERT；錯誤測試要確保還原身份，不讓後續DDL在低許可權context執行。

## 清理與許可權邊界

```sql
ALTER ROLE NoteReadRole DROP MEMBER NoteReader;
DROP USER NoteReader;
DROP ROLE NoteReadRole;
DROP TABLE dbo.NoteTasks;
```

只清除本篇建立的測試物件。db_datareader可讀DB內廣泛user表、db_datawriter可寫，仍需判斷是否比單表授權過大；db_owner是很高許可權，不等於「所有開發者都需要」。DROP USER不會自動DROP LOGIN，兩者生命週期不同。

確認許可權用受測身份執行允許／拒絕操作與資料庫metadata，不只看GRANT沒有報錯。本文僅官方文件核對，未對實際SQL Server寫入賬號或修改許可權。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [CREATE USER](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql)
- [CREATE LOGIN](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql)
- [GRANT](https://learn.microsoft.com/en-us/sql/t-sql/statements/grant-object-permissions-transact-sql)
- [Roles](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles)
