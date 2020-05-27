---
title: "AndroidBsN01"
date: 2020-05-25T10:50:35+08:00
draft: true
categories:
 - "筆記"
tags:
 - "java"
 - "Kotlin"
 - "Android"
toc: true
---

# Create an Android project(創建一個Android項目)
<!--more-->

要創建新的Android項目，請按照以下步驟操作：

1. 安裝最新版本的 [Android Studio](https://developer.android.com/studio/)。

2. 在“ **歡迎使用****Android Studio”**窗口中，單擊“ **啟動新的****Android Studio****項目****”**。

![img](file:///C:/Users/Ian/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

**圖****1.** Android Studio歡迎屏幕

如果您已經打開了一個項目，請選擇**File> New> New Project**。

3. 在“ **選擇項目模板****”**窗口中，選擇“ **清空活動****”**，然後單擊“ **下一步****”**。

4. 在“ **配置項目****”**窗口中，完成以下操作：

·    在**名稱**字段中輸入“我的第一個應用程序” 。

·    在“ **程序包名稱****”**字段中輸入“ com.example.myfirstapp” 。

·    如果要將項目放置在其他文件夾中，請更改其**保存**位置。

·    從 **語言**下拉菜單中選擇**Java**或**Kotlin**。

·    在**最低****SDK**字段中選擇您的應用將支持的**最低** Android版本。

·    如果您的應用需要舊版庫支持，**請**選中**使用舊版****android.support****庫**複選框。

·    保留其他選項不變。

5. 點擊**完成**。

經過一段時間的處理後，出現Android Studio主窗口。

![img](file:///C:/Users/Ian/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

**圖****2.** Android Studio主窗口

現在花點時間查看最重要的文件。

首先，請確保已打開“ **項目****”**窗口（選擇“ **視圖****”>“****工具窗口****”>“****項目****”**），並且從該窗口頂部的下拉列表中選擇了Android視圖。然後，您可以看到以下文件：

**應用****> Java> com.example.myfirstapp> MainActivity**

這是主要活動。這是您的應用程序的切入點。在構建和運行應用程序時，系統將啟動該應用程序的實例 [Activity](https://developer.android.com/reference/android/app/Activity) 並加載其佈局。

**應用程序****> res>****佈局****> activity_main.xml**

此XML文件定義活動的用戶界面（UI）的佈局。它包含一個[TextView](https://developer.android.com/reference/android/widget/TextView)帶有文本“ Hello，World！” 的 元素。

**應用****>****清單****> AndroidManifest.xml**

該[清單文件](https://developer.android.com/guide/topics/manifest/manifest-intro)描述了應用程序的基本特徵，並限定它的每一個組件。

**Gradle****腳本****> build.gradle**

有兩個名稱相同的文件：一個用於項目“ Project：My First App”，另一個用於應用程序模塊“ Module：app”。每個模塊都有自己的build.gradle文件，但是該項目當前只有一個模塊。使用每個模塊build.file來控制[Gradle插件](https://developer.android.com/studio/releases/gradle-plugin)如何構建您的應用程序。有關此文件的更多信息，請參見 [配置構建](https://developer.android.com/studio/build#module-level)。

參考

https://developer.android.com/training/basics/firstapp/creating-project

 