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


# hugo使用Prism.js

使用 prism.js 做為程式碼高量的工具

Prism是一種輕量級的，可擴充套件的語法突出顯示工具，其構建考慮了現代Web標準。它已在數千個網站中使用，包括您每天訪問的一些網站。

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

開啟Hugo配置檔 Config.toml，設定將預設程式碼高亮設定false

```toml
#預設程式碼區塊
pygmentsCodefences = false
pygmentsCodefencesGuessSyntax = false
```


## 參考
[Hugo / 如何在 Hugo 中用 Prism.js 提供程式碼色彩標註 | sujj blog](https://sujingjhong.com/posts/how-to-add-prismjs-into-hugo/)  

[漂亮的程式碼語法高亮外掛Prism.js簡單使用檔案 - 嚴穎專欄 -SegmentFault 思否](https://segmentfault.com/a/1190000009122617)
