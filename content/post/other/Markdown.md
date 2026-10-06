---
title: "Markdown 筆記：語法、程式碼與 Hugo 差異"
date: 2020-11-06T22:22:00+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Markdown"
toc: true
description: "修正連結語法，將示例放入程式碼區塊，區分 CommonMark、表格與 Mermaid 擴充。"
lastmod: 2026-10-07T00:01:00+08:00
---

修正連結語法，將示例放入程式碼區塊，區分 CommonMark、表格與 Mermaid 擴充。

<!--more-->

適用：CommonMark基礎與Hugo Goldmark；不同編輯器的額外語法不保證通用。

## 常用語法

````markdown
# 一級標題
## 二級標題

段落以空白行分開。**粗體**與*斜體*，行內程式碼 `count`。

- 第一項
- 第二項

1. 操作一
2. 操作二

[顯示文字](https://example.com "連結標題")
![描述圖片內容](images/example.png)

> 引用文字，來源另附連結。

```javascript
console.log('campfire');
```
````

連結不是`(網址 , 標題)`，標題需加引號並以空格隔開。範例外層用四個反引號，內層三個才不會提前結束。語言名稱決定高亮，不影響程式可否執行。

## 表格與換行

表格是Goldmark/GFM等實作常見擴充，不是所有CommonMark工具預設支援：

```markdown
| 工具 | 用途 |
| --- | --- |
| Hugo | 靜態網站 |
| Git | 版本控制 |
```

表格單元格內literal管線需轉義，長內容在本站可橫向捲動。一般換行不一定變`<br>`，段落用空行；不要依賴不同編輯器的自動換行偏好。

## 目錄與圖表

[TOC]不是所有Markdown渲染器都會建立目錄；本站使用front matter toc與Hugo.TableOfContents。Mermaid、sequence、seq等都需要額外renderer，不能只寫fence就保證出圖。本站未接入Mermaid執行器，示例會顯示程式碼，需用官方Live Editor檢查或輸出SVG。

Hugo unsafe=false，不在文章插原始script／iframe來排版。圖片路徑依據static對映與站點base，內部文章用ref；新例子檔案要存在才能發布，不留下不存在的示範圖連結。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [CommonMark](https://spec.commonmark.org/)
- [Hugo Goldmark](https://gohugo.io/configuration/markup/)
- [GFM表格](https://github.github.com/gfm/#tables-extension-)

### 原始筆記保留的來源

- [link](https://iankingh.github.io/)
- [markdown語法介紹 - HackMD](https://hackmd.io/@wootu/SkY0M5wsZ?type=view)
