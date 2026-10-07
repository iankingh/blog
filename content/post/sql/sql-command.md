---
title: "SQL Server T-SQL：建表、修改欄位與交易練習"
date: 2021-03-15T09:31:14+08:00
draft: false
categories:
 - "筆記"
tags:
 - "SQL"
toc: true
description: "修正 SQL Server ADD COLUMN 說法，補上完整暫存表練習與預期查詢結果。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 SQL Server ADD COLUMN 說法，補上完整暫存表練習與預期查詢結果。

<!--more-->

適用：SQL Server2019/2022的T-SQL；在測試session操作#暫存表，不對正式資料庫做DDL。

## 單一 session 的完整練習

```sql
CREATE TABLE #NoteTasks (
    Id int NOT NULL PRIMARY KEY,
    Title nvarchar(100) NOT NULL
);
ALTER TABLE #NoteTasks ADD Done bit NOT NULL DEFAULT 0;
INSERT INTO #NoteTasks (Id, Title) VALUES (1, N'讀文件'), (2, N'寫測試');
BEGIN TRANSACTION;
UPDATE #NoteTasks SET Done = 1 WHERE Id = 1;
SELECT Id, Title, Done FROM #NoteTasks ORDER BY Id;
ROLLBACK TRANSACTION;
SELECT Id, Title, Done FROM #NoteTasks ORDER BY Id;
DROP TABLE #NoteTasks;
```

第一次SELECT的Done應為1、0，rollback後0、0。N字首為Unicode字串，中文欄位用nvarchar；#暫存表在目前session，換連線後看不到是預期。

## ALTER 與 DEFAULT

T-SQL增加欄位是`ALTER TABLE table ADD column type`，不是通用`ADD COLUMN`。新增default constraint為未提供值的INSERT設預設，不會把明確寫入NULL自動改成預設；既有資料補值要按nullable與WITH VALUES規則規劃。

大量表DDL可能鎖表、重建或影響索引，正式改動先做migration、備份與回復設計。測試temp table的成本不等於production大表成本。

## 查詢與許可權

SELECT指定必要欄位並提供穩定ORDER BY，TOP無排序不保證取到哪筆。client引數使用引數化，不把使用者輸入拼成SQL。登入LOGIN、DB USER與角色授權見[SQL Server帳號篇]({{< ref "/post/sql/sql-server.md" >}})，不要為日常查詢隨意授db_owner。

## 驗證範圍

本次無SQL Server instance，T-SQL依官方文件查核；共通INSERT/UPDATE/ROLLBACK邏輯可以本地SQLite模擬，但#table、bit、N字串與許可權並非SQLite語法，不能把模擬通過稱為SQL Server實機通過。

## 參考資料

- [ALTER TABLE](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql)
- [交易ROLLBACK](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/rollback-transaction-transact-sql)
- [暫存表](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql)
- [SQL DEFAULT 預設值 - SQL 語法教學 Tutorial (fooish.com)](https://www.fooish.com/sql/default-constraint.html)
- [SQL ALTER TABLE 更改資料表 - SQL 語法教學 Tutorial (fooish.com)](https://www.fooish.com/sql/alter-table.html)
