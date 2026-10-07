---
title: "Git 提交訊息：Conventional Commits 與拆分原則"
date: 2021-02-04T12:52:04+08:00
draft: false
categories:
 - "學習"
tags:
 - "git"
toc: true
description: "修正 type、scope 的格式，提供繁體中文提交示例與不相容變更標示。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 type、scope 的格式，提供繁體中文提交示例與不相容變更標示。

<!--more-->

適用：採 Conventional Commits 1.0 的專案；團隊原有規範優先。

## 格式

```text
type(scope): 簡短摘要

說明修改原因與使用者可觀察的結果。

BREAKING CHANGE: 描述相容性影響與遷移方式。
```

scope 可省略，不寫成 `type: scope : subject`。feat 表示新增功能、fix 表示修正錯誤；docs、test、refactor、build、ci、chore 為常見團隊擴充，不由此規格統一定義發布版本。原筆記的 modify/delete 可保留為歷史團隊習慣，但不要混稱標準 type。

## 依結果命名

```text
fix(search): 修正更新日期的顯示

搜尋結果改用 lastmod，缺值時才回退到發布日期。
```

```text
feat(api)!: 調整任務查詢回應格式

BREAKING CHANGE: items 改為 tasks，客戶端需更新欄位名稱。
```

不相容變更可以用 ! 或 BREAKING CHANGE footer 表示。摘要說明改變，不只寫「修改程式」或羅列檔名。若只是資料層重構且行為不變，使用 refactor 比 feat 清楚。

## 提交前檢查

閱讀 `git diff --cached`，確認訊息與 staged 內容相符。一個提交有一個可理解目的；功能和必要測試可同一提交，不相關格式化另外拆。不要為了美觀把本來可獨立回滾的改動混在一起。產生訊息工具只協助草擬，提交者仍需核對實際 diff。

## 參考資料

- [Conventional Commits 1.0](https://www.conventionalcommits.org/zh-hant/v1.0.0/)
- [git-commit](https://git-scm.com/docs/git-commit)
- [如何規範你的Git commit？-阿里雲開發者社群](https://developer.aliyun.com/article/770277)
- [Git Commit Message 這樣寫會更好，替專案引入規範與範例](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)
