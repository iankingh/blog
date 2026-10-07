---
title: "Eclipse 型別階層：檢視繼承與實作"
date: 2020-05-15T16:36:13+08:00
categories:
 - "筆記"
tags:
 - "eclipse"
toc: true
draft: false
description: "補上選取型別、切換階層檢視及無法找到子類別時的檢查方式。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上選取型別、切換階層檢視及無法找到子類別時的檢查方式。

<!--more-->

適用：Eclipse IDE 的 Java Development Tools；快捷鍵依 OS 與自訂 keymap 而異。

## 檢視操作

在Java編輯器選取class或interface名稱，右鍵選Open Type Hierarchy，預設F4；也可由Navigate選單進入。Hierarchy視窗可切換完整、父型別或子型別階層，點專案開啟對應來源。方法選取可搭配階層檢視檢查覆寫，但查「誰呼叫此方法」要用Call Hierarchy，不是Type Hierarchy。

![Eclipse Type Hierarchy 的型別階層視窗](/images/eclipse/OpenTypeHierarchy.png)

## 練習與確認

建立一個Skill介面、Heal與Fire兩個實作，選Skill開啟階層，應看到兩個子型別。可使用[Java物件導向範例]({{< ref "/post/java/java_tutorial_4.md" >}})的巢狀類別練習。檢視父型別時應顯示選取類別的繼承鏈，而非目前所有開啟檔案。

若找不到預期型別，確認專案已匯入、Build Path包含來源與依賴、filter／working set沒有排除該專案，並檢查Problems。依賴只有class沒有source時，階層仍可能有資料但不能讀到原始碼，需加入對應source attachment。

不同版本的toolbar圖示可能不同，操作以名稱辨識；macOS功能鍵可能需Fn。此工具依索引與編譯資訊分析，不保證列出執行期反射或動態載入的所有實作。

## 參考資料

- [Eclipse Type Hierarchy](https://help.eclipse.org/latest/topic/org.eclipse.jdt.doc.user/reference/views/type_hierarchy/ref-type-hierarchy.htm)
