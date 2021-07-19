---
title: "Prism.js使用筆記"
date: 2020-04-22T22:29:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
---


## hugo使用Prism.js

使用 prism.js 做為代碼高量的工具

Prism是一種輕量級的，可擴展的語法突出顯示工具，其構建考慮了現代Web標準。它已在數千個網站中使用，包括您每天訪問的一些網站。

<!--more-->

### 下載

https://prismjs.com/

### 使用

放在Hugo部落格資料夾（static）位置

```Shell

├── static
│   ├── prism.js
│   └── prism.css


```

### Config.toml

開啟Hugo配置檔 Config.toml，設定將預設代碼高亮設定false

```toml
#預設代碼區塊
pygmentsCodefences = false
pygmentsCodefencesGuessSyntax = false
```


## 參考

[Hugo動態加載prism.js](https://www.ariesme.com/post/2019/add_prism_for_hugo_automatically/)

[Hugo / 如何在 Hugo 中用 Prism.js 提供程式碼色彩標註 | sujj blog](https://sujingjhong.com/posts/how-to-add-prismjs-into-hugo/)  

[漂亮的代碼語法高亮插件Prism.js簡單使用文檔 - 嚴穎專欄 -SegmentFault 思否](https://segmentfault.com/a/1190000009122617)
