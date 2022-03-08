---
title: "如何偵測使用者的裝置是否為行動裝置"
date: 2021-03-15T09:20:44+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
---

## 如何偵測使用者的裝置是否為行動裝置
<!-- 簡介 -->
<!--more-->

轉貼 


```javascript
function isMobileDevice() {
    const mobileDevice = ['Android', 'webOS', 'iPhone', 'iPad', 'iPod', 'BlackBerry', 'Windows Phone']
    let isMobileDevice = mobileDevice.some(e => navigator.userAgent.match(e))
    return isMobileDevice
}
```

## 參考 

[如何偵測使用者的裝置是否為行動裝置 | Jason's BLOG](https://tso1158687.github.io/blog/2019/03/10/detect-mobile-device/, "如何偵測使用者的裝置是否為行動裝置 | Jason's BLOG")
