---
title: "Hugo使用筆記"
date: 2020-04-21T22:29:36+08:00
draft: false
categories:
 - "筆記"
tags:
 - "hugo"
toc: true
---


## Hugo使用筆記

紀錄Hugo使用的筆記

<!--more-->

## Hugo 基本指令

### 安裝

透過Chocolatey 安裝

```shell
hchoco install hugo -confirm
```

 **Check version:**

```shell
hugo version
```

### 建立新Blog

```shell
hugo new site blog
```

### 新增文章

```shell
hugo new post/文章名稱.md
```

生成的文件默認為會帶上 draft: true標記，不會發布。

### run server

**不 run  draft: true 的標記(未發布)**

```shell
hugo server
```

**run 全部**

```shell
hugo server -D
```

### 插入圖片

```shell
![Example image](/static/image.png)
```

![useImageRootPath](/images/hugo/useImageRootPath.png)

![image-20200930075548139](C:\Users\Ian\AppData\Roaming\Typora\typora-user-images\image-20200930075548139.png)

## 建立及設定部落格專案  

我們先使用 hugo 命令新增一個空白專案，然後下載一個Template到我們的專案裡面  

接著新增四個我們想加到模板 Menu 的頁面: about, history, tags, categories

最後則是新增一篇空白的文章到專案內。

```Shell Script

1.create the project

$ hugo new site myblog

2.add a theme
$ git submodule add https://github.com/laozhu/hugo-nuo themes/hugo-nuo

3.add new pages

$ hugo new about.md
$ hugo new hisroty.md
$ hugo new tags.md
$ hugo new categories.md

4.add new article

$ hugo new post/welcome.md

hugo server -D

```

## 參考

[右上角github 貓 GitHub Corners](https://tholman.com/github-corners/#)

[在 Github Pages 建立 Hugo 靜態網站 · Kaichu.io](https://kaichu.io/2015/07/12/my-first-post/)

[使用Github部署Hugo靜態網站](https://kira5033.github.io/2019/05/%E4%BD%BF%E7%94%A8github%E9%83%A8%E7%BD%B2hugo%E9%9D%9C%E6%85%8B%E7%B6%B2%E7%AB%99/)  

[next模版](https://github.com/xtfly/xtfly.github.io/tree/hugo/themes/next)

[使用 Hugo 打造個人部落格](https://blog.walker088.tw/post/intro-hugo/)  

[hugo搭建静态博客 | 生信笔记](https://www.bioinfo-scrounger.com/archives/809/)

[使用Hugo搭建博客系统 - XniLe - Ops 2.0](https://blog.dianduidian.com/post/%E4%BD%BF%E7%94%A8hugo%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2%E7%B3%BB%E7%BB%9F/)
