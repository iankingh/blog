---
title: "Create an Android project(創建一個Android項目)"
date: 2020-05-25T10:50:35+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Kotlin"
 - "Android"
toc: true
---

## Create an Android project(創建一個Android項目)

<!--more-->

## 要創建新的Android項目，請按照以下步驟操作

### 1. 安裝最新版本的 Android Studio

   [Download Android Studio and SDK tools  |  Android Developers](https://developer.android.com/studio/)

   下載完後點擊安裝一路安裝到結束。

### 2. 開啟新專案(cerate new project )

在**Welcome to Android Studio**窗口中，單擊啟動新的**Strat a new Android Studio project**。

![Welcome to Android Studio](/images/Android/Welcome_to_Android_Studio.png)

### 3. 選擇模板

在**Select a Project Template**窗口中，選擇**Empty Activity**，然後單擊**next**。

![Configure Your Project](/images/Android/Select_a_Project_Template.png)

### 4. 設定專案配置

在**Configure Your Project**窗口中，完成以下操作：

![Configure Your Project](/images/Android/Configure_Your_Project.png)

- 在**Name**輸入 "Myfirstapp" 。
- 在**Package name**字段中輸入"com.example.myfirstapp" 。
- `Save Location` 預設專案放置位置，如果要將項目放置在其他文件夾中，請更改其**保存**位置。
- 從`Language`下拉菜單中選擇**Java**或**Kotlin**。
- 在`Minimum SDK`選擇您的應用將支持的**最低** Android版本。
- 保留其他選項不變。

### 5 .**完成專案建置**

經過一段時間的處理後，出現Android Studio主窗口。

Android Studio主窗口

現在花點時間查看最重要的文件。

首先，請確保已打開項目窗口`> Java> com.example.myfirstapp> MainActivity`（選擇"視圖>工具窗口>項目），並且從該窗口頂部的下拉列表中選擇了Android視圖。

- Activity

這是主要活動。這是您的應用程序的切入點。在構建和運行應用程序時，系統將啟動該應用程序的實例 [Activity](https://developer.android.com/reference/android/app/Activity) 並加載其佈局。

應用程序> res>佈局> activity_main.xml

此XML文件定義活動的用戶界面（UI）的佈局。它包含一個[TextView](https://developer.android.com/reference/android/widget/TextView)帶有文本" Hello，World！" 的 元素。

- **AndroidManifest.xml > 應用清單**

該[清單文件](https://developer.android.com/guide/topics/manifest/manifest-intro)描述了應用程序的基本特徵，並限定它的每一個組件。

- **build.gradle  > Gradle 腳本**

有兩個名稱相同的文件：一個用於項目" Project：My First App"，另一個用於應用程序模塊" Module：app"。每個模塊都有自己的build.gradle文件，但是該項目當前只有一個模塊。使用每個模塊build.file來控制[Gradle插件](https://developer.android.com/studio/releases/gradle-plugin)如何構建您的應用程序。有關此文件的更多信息，請參見 [配置構建]([Configure your build | Android Developers](https://developer.android.com/studio/build#module-level))。

## 參考
[Create an Android project | Android Developers](https://developer.android.com/training/basics/firstapp/creating-project)


