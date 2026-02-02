# ianhuang 的技術筆記部落格

使用 Hugo 靜態網站生成器搭配 NexT 主題建置的個人技術部落格。

## 🌐 網站資訊

- **部落格網址**：https://iankingh.github.io/blog/
- **主題**：[hugo-theme-next](https://github.com/hugo-next/hugo-theme-next)
- **語言**：繁體中文 (zh-tw)

## 📁 專案結構

```
blog/
├── content/post/       # 文章內容（依技術分類）
├── static/             # 靜態資源（圖片、CSS、JS）
├── layouts/            # 自訂版面範本
├── themes/             # Hugo 主題（git submodule）
├── public/             # 建置輸出（gh-pages 分支）
├── config.yaml         # Hugo 配置檔
└── archetypes/         # 文章範本
```

## 🚀 快速開始

### 環境需求

- [Hugo](https://gohugo.io/) Extended 版本
- Git

### 複製專案

```bash
# 複製儲存庫（包含 submodules）
git clone --recurse-submodules https://github.com/iankingh/blog.git
cd blog

# 如果已經複製，可以用以下指令初始化 submodules
git submodule update --init --recursive
```

### 本地開發

```bash
# 啟動開發伺服器（包含草稿）
hugo server -D

# 瀏覽器開啟 http://localhost:1313/blog/
```

### 建置網站

```bash
# 建置正式版本
hugo

# 輸出會產生在 public/ 目錄
```

## 📝 建立新文章

```bash
# 使用 archetype 範本建立新文章
hugo new content/post/<分類>/<文章名稱>.md

# 例如：
hugo new content/post/java/java-stream-api.md
```

### Front Matter 範例

```yaml
---
title: "文章標題"
date: 2026-02-03T12:00:00+08:00
categories:
- "筆記"  # 可選：技術、筆記、學習
tags:
- "Java"
- "Stream"
toc: true
draft: false
---
```

## 🚢 部署到 GitHub Pages

```bash
# 1. 建置網站
hugo

# 2. 切換到 public 目錄（gh-pages 分支的 submodule）
cd public

# 3. 提交變更
git add .
git commit -m "更新網站內容"
git push origin gh-pages

# 4. 回到主目錄
cd ..

# 5. 提交主專案的變更
git add .
git commit -m "更新部落格文章"
git push origin master
```

## 🔧 Submodule 管理

### 主題 Submodule

```bash
# 新增主題 submodule
git submodule add https://github.com/hugo-next/hugo-theme-next.git themes/hugo-theme-next

# 更新主題
cd themes/hugo-theme-next
git pull origin master
cd ../..
```

### 部署 Submodule (public/)

```bash
# 新增 public submodule（指向 gh-pages 分支）
git submodule add -b gh-pages "https://github.com/iankingh/blog.git" "public"
```

### Submodule 問題排解

```bash
# 如果遇到 "fatal: in unpopulated submodule XXX" 錯誤
git rm -rf --cached public
git submodule add -b gh-pages "https://github.com/iankingh/blog.git" "public"

# 更新所有 submodules
git submodule update --remote --merge
```

## 📚 文章分類

- **後端開發**：Java, Spring, Spring Boot, Spring Cloud
- **前端開發**：Angular, Vue, JavaScript
- **DevOps**：Docker, Git, Linux, Nginx
- **資料庫**：SQL, Redis, Kafka
- **開發工具**：Visual Studio Code, Eclipse

## 🛠️ 配置說明

主要配置檔案：`config.yaml`

- **第 1-100 行**：Hugo 引擎基礎設定
- **第 100-200 行**：選單與導航配置
- **第 200-500 行**：NexT 主題參數
- **第 800-1000 行**：第三方服務（分析、搜尋、留言）

詳細的開發指引請參考：[.github/copilot-instructions.md](.github/copilot-instructions.md)

## 📖 參考資料

- [Hugo 官方文件](https://gohugo.io/documentation/)
- [hugo-theme-next 主題文件](https://github.com/hugo-next/hugo-theme-next)
- [從零開始: 用 GitHub Pages 上傳靜態網站](https://medium.com/進擊的-git-git-git/從零開始-用github-pages-上傳靜態網站-fa2ae83e6276)
- [Git Submodule 指定 Branch](https://blog.yowko.com/git-submodule-specific-branch/)

## 📄 授權

本部落格內容採用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 授權。

---

**作者**：Ian Huang  
**GitHub**：[@iankingh](https://github.com/iankingh)
