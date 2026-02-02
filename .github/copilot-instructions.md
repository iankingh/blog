# ianhuang 部落格的 Copilot 指引

## 專案概述
這是一個使用 hugo-theme-next 主題的 Hugo 靜態網站部落格（技術筆記），內容為繁體中文。網站部署於 GitHub Pages：`https://iankingh.github.io/blog/`

## 架構

### 目錄結構
- `content/post/` - 依主題分類的部落格文章（java、docker、angular、spring 等）
- `config.yaml` - Hugo 主要配置檔（1137 行，NexT 主題的大量客製化設定）
- `themes/hugo-theme-next/` - 主題的 Git submodule
- `public/` - 連結到 gh-pages 分支的 Git submodule，用於部署
- `archetypes/default.md` - 新文章的範本
- `layouts/` - 自訂版面覆寫檔案（404、首頁、搜尋、partials）

### 內容組織
文章依技術主題分類在 `content/post/` 下的資料夾：
- 後端：`java/`、`spring/`、`spring-boot/`、`spring-cloud/`、`kafka/`、`redis/`
- 前端：`angular/`、`vue/`、`JavaScript/`
- DevOps：`docker/`、`git/`、`linux/`、`ubuntu/`、`nginx/`
- 工具：`visual-studio-code/`、`eclipse/`、`build-tools/`

## 建立新文章

### 使用 Hugo 內建的 Archetype
```bash
hugo new content/post/<category>/<post-name>.md
```

### 必要的 Front Matter（來自 archetype）
```yaml
---
title: "文章標題"
date: 2026-02-03T12:00:00+08:00
categories:
- "筆記"  # 或 "技術"、"學習"
tags:
- "tag1"
- "tag2"
toc: true
draft: false  # 準備發布時設為 false
---
```

### 內容結構模式
1. Front matter 後的 H1 標題
2. 簡短介紹
3. `<!--more-->` 註解設定摘要邊界
4. 使用 H2/H3 標題的章節
5. 文末可選的「Summary」章節

## 建置與開發流程

### 本地開發
```bash
# 啟動 Hugo 開發伺服器
hugo server -D

# 建置正式版本
hugo

# 輸出會產生在 public/ 目錄（這是一個 git submodule）
```

### 部署到 GitHub Pages
`public/` 目錄是指向 gh-pages 分支的 git submodule：
```bash
# 建置網站
hugo

# 部署到 GitHub Pages
cd public
git add .
git commit -m "Update site"
git push origin gh-pages
cd ..
```

### 管理 Submodules
```bash
# 新增主題 submodule（已完成）
git submodule add https://github.com/hugo-next/hugo-theme-next.git themes/hugo-theme-next

# 新增 public submodule 用於部署（已完成）
git submodule add -b gh-pages "https://github.com/iankingh/blog.git" "public"

# 如果 submodule 發生問題：
git rm -rf --cached public
```

## 設定慣例

### 關鍵設定（config.yaml）
- **Base URL**：`https://iankingh.github.io/blog/`（連結的重要設定）
- **語言**：`zh-tw`（繁體中文）
- **Scheme**：Gemini（NexT 主題變體）
- **分頁**：每頁 10 篇文章
- **搜尋**：啟用本地搜尋，索引位於 `/blog/searchindexes.xml`
- **留言**：預設停用（`comments.enable: false`）
- **選單項目**：首頁、技術、筆記、歸檔、關於

### 重要設定區段
- 第 1-100 行：Hugo 引擎基礎設定、markup 設定
- 第 100-200 行：選單配置與中文標籤
- 第 200-500 行：NexT 主題參數（作者、側邊欄、頭像、頁尾）
- 第 800-1000 行：第三方服務（分析、搜尋、留言）

### 中文分類標籤
為保持一致性，請使用這些確切的中文詞彙：
- 分類：`技術`、`筆記`、`學習`
- 選單標籤遵循 config.yaml 中的 menus.main 區段

## 主題客製化

### layouts/ 中的自訂檔案
- `layouts/404.html` - 自訂 404 頁面
- `layouts/index.html` - 首頁版面覆寫
- `layouts/partials/` - Partial 範本覆寫
- `layouts/searchindex.xml` - 自訂搜尋索引格式

### 資源檔案位置
- 自訂 CSS：`static/css/` 或 `themes/hugo-theme-next/assets/css/`
- 圖片：`static/imgs/` 或 `content/post/images/`
- JavaScript：`static/js/`

## 常見模式

### 程式碼區塊範例
使用三個反引號並指定語言：
````markdown
```javascript
const example = "程式碼範例";
```
````

### 圖片引用
相對於 static 目錄引用圖片：
```markdown
![替代文字](/imgs/folder/image.png)
```

### 內部連結
使用 Hugo 的 ref/relref 建立內部連結：
```markdown
[連結文字]({{< ref "post/category/post-name.md" >}})
```

## 疑難排解

### 常見問題
1. **Submodule 衝突**：使用 `git rm -rf --cached <path>` 後重新加入
2. **建置錯誤**：檢查 Hugo 版本與主題的相容性
3. **連結失效**：確認 baseURL 與部署 URL 相符
4. **搜尋無法運作**：確保輸出中有產生 `searchindexes.xml`

### 檔案沒有顯示？
- 檢查 front matter 中的 `draft: false`
- 確認日期不是未來時間
- 確保檔案位於 `mainSections: ["post"]` 目錄中

## 參考資料
- 主題文件：https://github.com/hugo-next/hugo-theme-next
- Hugo 文件：https://gohugo.io/documentation/
- 部署指南：參見 [readme.md](readme.md)
