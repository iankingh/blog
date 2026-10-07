---
title: "Android Studio 第一個專案：模板、SDK 與執行確認"
date: 2020-05-25T10:50:35+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Kotlin"
 - "Android"
toc: true
description: "保留建立專案流程，補上 Compose／Views差異、Gradle JDK與模擬器驗收。"
lastmod: 2026-10-07T20:50:40+08:00
---

保留建立專案流程，補上 Compose／Views差異、Gradle JDK與模擬器驗收。

<!--more-->

適用：Android Studio建立Android專案；原截圖為較早的Java／Views流程，現代模板名稱與預設語言可能不同。

## 建立專案

安裝官方Android Studio與SDK，New Project選擇符合需求的模板。新Empty Activity常為Kotlin+Compose；若跟原Java/XML教學，選擇相應Empty Views Activity，不能把舊XML步驟貼到Compose模板。

填名稱、package如com.example.notelab、儲存位置與Minimum SDK。minSdk控制最低裝置API，compileSdk控制編譯API，targetSdk關係平臺行為與發布要求，三者不可互稱同一個版本。商店政策會變化，釋出前核對官方要求。

## 建置環境

等待Gradle Sync完成，保留生成的wrapper與plugin版本，先用IDE建議的相容JDK，不手動把所有Gradle、AGP、Kotlin一起升到latest。首次下載需網路，錯誤先看具體依賴、代理與SDK許可證，不反覆刪cache。

在Device Manager建立與你CPU架構相容的virtual device，下載system image；也可使用USB除錯的真實裝置。虛擬化未啟用或架構不匹配可能導致模擬器不能啟動，與app程式碼無關。

## 確認結果

按Run選裝置，app應安裝啟動並顯示模板文字。修改顯示內容為「冒險筆記」後再Run，確認變化；檢視Logcat無應用崩潰。終端用專案的gradlew/gradlew.bat執行assembleDebug，輸出debug APK的實際路徑依module而定。

真實裝置測試旋轉、字型放大、不同API與返回鍵；能在一個模擬器顯示不代表整個兼容範圍。這個入門示例不包含簽名釋出、賬號或許可權設計，新功能申請許可權需按Android版本的行為核對。

## 參考資料

- [Create project](https://developer.android.com/studio/projects/create-project)
- [Gradle JDK](https://developer.android.com/build/jdks)
- [Emulator](https://developer.android.com/studio/run/emulator)
- [Target API policy](https://developer.android.com/google/play/requirements/target-sdk)
- [Download Android Studio and SDK tools  |  Android Developers](https://developer.android.com/studio/)
- [Activity](https://developer.android.com/reference/android/app/Activity)
- [TextView](https://developer.android.com/reference/android/widget/TextView)
- [清單檔案](https://developer.android.com/guide/topics/manifest/manifest-intro)
- [Gradle外掛](https://developer.android.com/studio/releases/gradle-plugin)
- [Configure your build | Android Developers](https://developer.android.com/studio/build#module-level)
- [Create an Android project | Android Developers](https://developer.android.com/training/basics/firstapp/creating-project)
