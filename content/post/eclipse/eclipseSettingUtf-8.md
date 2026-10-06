---
title: "Eclipse UTF-8：工作區、專案與建置一致性"
date: 2021-04-12T09:08:22+08:00
categories:
 - "筆記"
tags:
 - "eclipse"
toc: true
draft: false
description: "補齊編碼設定層級、換行與 Maven／Gradle 的一致性檢查，避免只改顯示設定。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊編碼設定層級、換行與 Maven／Gradle 的一致性檢查，避免只改顯示設定。

<!--more-->

適用：Eclipse Java專案；原截圖為Windows偏好設定，macOS可從應用程式Settings／Preferences開啟。

## 工作區與專案

在Preferences → General → Workspace，Text file encoding選Other:UTF-8，New text file line delimiter可選Unix。套用後檢查Project → Properties → Resource，確認專案採繼承或明確UTF-8；個別檔案也可能有自己的編碼覆寫。

![Eclipse 工作區 UTF-8 與換行設定](/images/eclipse/eclipseSettingUtf-8.png)

## 建置工具

Maven pom.xml在properties內設定：

```xml
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

Gradle見[編碼排錯]({{< ref "/post/build-tools/gradle-error.md" >}})，只改IDE不能保證CI用同樣編碼。可加入.editorconfig：

```ini
root = true
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
```

## 確認與限制

新增含「繁體中文」的來源註解，儲存、關閉再開，確認沒有亂碼，並用專案正式建置命令編譯。比較git diff，避免換行變更讓整個檔案被改寫。

設定UTF-8不會修復已被錯誤解碼並儲存的檔案。舊Big5檔先備份，以正確原編碼開啟再轉存UTF-8；單純指定新編碼可能只把損壞內容再次儲存。Console顯示編碼、HTTP response編碼與資料庫編碼是不同層，不應把所有亂碼都歸因IDE。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Eclipse Resource Properties](https://help.eclipse.org/latest/topic/org.eclipse.platform.doc.user/reference/ref-40.htm)
- [Maven Model](https://maven.apache.org/pom.html#properties)
- [EditorConfig](https://editorconfig.org/)
