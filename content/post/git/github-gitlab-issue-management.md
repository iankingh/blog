---
title: "GitHub／GitLab Issue 管理：提報指南、Markdown 錨點與 Issue 範本"
date: 2026-11-17
lastmod: 2026-11-17
description: "用 Markdown 建立提報指南，透過表格連到 Bug 與功能建議範本。示範 GitHub 置頂 Issue、範本選單，以及 GitLab 的說明範本與 README 入口。"
categories:
  - "筆記"
tags:
  - "git"
  - "github"
  - "gitlab"
toc: true
draft: false
---

收到 Bug 回報時，最常需要追問的是版本、操作步驟，以及實際結果。可以在專案放一份「提報 Issue 前請先看」指南，用 Markdown 錨點和表格引導讀者選對範本，再由範本提示要填哪些資訊。原始案例把 Bug 回報、功能建議和一般討論導向不同入口。[skills-manager 的置頂 Issue #155](https://github.com/xingkongliang/skills-manager/issues/155)

<!--more-->

本文適用於 GitHub.com 和 GitLab.com。把範例 URL 裡的 `OWNER/REPO` 或 `GROUP/PROJECT` 換成自己的專案路徑。GitLab Self-Managed 也要替換網域，並以該版本的 **New issue** 頁面確認範本連結。

| 要設定的功能 | GitHub | GitLab |
| --- | --- | --- |
| 讓提報指南容易找到 | 用 **Pin issue** 顯示於 Issues 列表上方 | 在專案 `README.md` 或 Wiki 放固定入口 |
| 提供 Bug／功能建議範本 | `.github/ISSUE_TEMPLATE/` | `.gitlab/issue_templates/` |
| 直接開啟指定範本 | `/issues/new?template=bug_report.md` | `/-/work_items/new?description_template=Bug%20Report` |

## 用 Markdown 寫一份提報指南

把以下內容貼到 GitHub 的 Issue 描述。Issue 標題可填「📌 提報 Issue 前請先看 / Read Before Filing an Issue」。用在 GitLab 的 README 或 Wiki 時，保留導覽和說明，將搜尋及範本連結換成 GitLab 的網址。

```markdown
[先搜尋](#search-first) · [選擇範本](#choose-a-template)

## Search First

🔍 **先搜尋既有問題**。用錯誤訊息或功能名稱搜尋 [Issues](https://github.com/OWNER/REPO/issues)。
如果已有同一個問題，請在原 Issue 補上你使用的版本與重現步驟。

> **附上資訊**。可以用 `Ctrl+V`（Windows／Linux）或 `Cmd+V`（macOS）貼上截圖。請先遮蔽帳號資訊或存取權杖。

## Choose a Template

| 我想做什麼 | 使用哪個入口 |
| --- | --- |
| 🐞 回報已出現的錯誤 | [Bug 回報](https://github.com/OWNER/REPO/issues/new?template=bug_report.md) |
| 🚀 提議增加或改善功能 | [功能建議](https://github.com/OWNER/REPO/issues/new?template=feature_request.md) |
```

同頁連結的 `#search-first` 對應 `## Search First`。這兩個範例標題會將英文字母轉成小寫、空格轉成連字號。若要改成中文或雙語標題，或在標題加上 Emoji，先預覽並從渲染後的標題複製連結。修改標題後，重新點一次導覽，確認錨點仍能跳到正確位置。表格中的 `[文字](網址)` 則直接指向建立 Issue 的頁面。[GitHub 的標題連結](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links) · [GitLab 的標題錨點](https://docs.gitlab.com/user/markdown/#heading-anchors)

### 在 GitHub 設定自訂 HTML 錨點

如果希望修改標題時保留原網址，可在 GitHub 的 Markdown 內容加上具名錨點，並用 `#` 加上 `name` 的值連過去。跨 GitHub／GitLab 共用的指南可以沿用前面的 Markdown 標題錨點。[GitHub 的自訂錨點](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#custom-anchors)

```markdown
[直接跳到回報說明](#guide-bug-report)

<a name="guide-bug-report"></a>

## 🐞 如何回報 Bug / Bug Report
```

## GitHub 設定 Issue 範本與置頂

### 建立 Bug 回報和功能建議範本

在儲存庫的預設分支新增以下兩個檔案。如果還沒開啟 Issues，到 **Settings → General → Features** 勾選 **Issues**。GitHub 會用 Markdown 範本開頭的 `name` 和 `about` 顯示選項，用 `title` 預填標題。[GitHub Issue 範本說明](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)

`.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: "🐞 Bug 回報"
about: "回報可以重現的錯誤"
title: "[Bug] "
---

## 使用環境

- 專案版本：
- 作業系統或瀏覽器：

## 重現步驟

1. 開啟哪個頁面或執行哪個指令？
2. 接著做了什麼？

## 預期結果

## 實際結果

## 截圖或錯誤訊息
```

`.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: "🚀 功能建議"
about: "提出新功能或改善既有功能"
title: "[功能建議] "
---

## 想解決的問題

## 希望支援的行為

## 具體使用情境
```

檔案合併到預設分支後，從 **Issues → New issue** 開啟範本選單，也可用 `/issues/new/choose` 直接開啟選單。提報指南的表格使用 `/issues/new?template=檔名.md`，點進去就能看到對應範本的標題前綴與正文。[GitHub 建立 Issue 的網址參數](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue#creating-an-issue-from-a-url-query)

### 把指南置頂，並加到範本選單

1. 在專案的 **Issues** 頁面建立「📌 提報 Issue 前請先看」，貼上指南。
2. 用具備儲存庫寫入權限的帳號打開該 Issue，在右側欄點 **Pin issue**。
3. 回到 **Issues** 列表，確認指南出現在列表上方。每個儲存庫最多置頂三個 Issue。[GitHub 置頂 Issue 操作說明](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/pinning-an-issue-to-your-repository)

如果讀者常直接點 **New issue**，可再增加一個連回指南的入口。將下方內容存成 `.github/ISSUE_TEMPLATE/config.yml`，把 `123` 換成指南的 Issue 編號，再合併到預設分支。

```yaml
blank_issues_enabled: true
contact_links:
  - name: "📌 提報指南"
    url: "https://github.com/OWNER/REPO/issues/123"
    about: "先查重複問題，再選擇提報範本。"
```

`blank_issues_enabled: true` 保留空白 Issue 選項。設為 `false` 時，有寫入權限以上的成員仍看得到空白選項。若專案有啟用 Discussions，也可用同樣的 `contact_links` 格式加入一般提問入口。[GitHub 範本選單設定](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#configuring-the-template-chooser)

## GitLab 設定說明範本與固定入口

### 建立兩個 Issue 說明範本

在專案的預設分支建立 `.gitlab/issue_templates/Bug Report.md` 與 `.gitlab/issue_templates/Feature Request.md`。沿用前面兩份範本的正文，從第一個 `##` 標題開始複製。GitLab 以檔名作為範本名稱，選取後將 Markdown 正文帶入 **Description**。有需要預設說明時，也可在同一個目錄放 `Default.md`。[GitLab 說明範本與預設範本](https://docs.gitlab.com/user/project/description_templates/)

合併後打開專案的 **Plan → Work items → New item**，選擇 **Issue**，再從 **Choose a template** 測試兩份範本。部分版本可從 **Plan → Issues → New issue** 進入。要讓讀者從指南直接開啟指定範本，複製對應連結到表格。

```markdown
| 我想做什麼 | 使用哪個入口 |
| --- | --- |
| 🐞 回報已出現的錯誤 | [Bug 回報](https://gitlab.com/GROUP/PROJECT/-/work_items/new?description_template=Bug%20Report) |
| 🚀 提議增加或改善功能 | [功能建議](https://gitlab.com/GROUP/PROJECT/-/work_items/new?description_template=Feature%20Request) |
```

`description_template` 填不含 `.md` 的名稱，空格寫成 `%20`。GitLab 官方文件也列出 `issuable_template` 參數。自架版若使用不同的建立頁面，先從專案介面選取範本，再複製該版本實際產生的網址並重新開啟確認。[GitLab 建立 Issue 的網址參數](https://docs.gitlab.com/user/project/issues/create_issues/#using-a-url-with-prefilled-values)

### 在專案入口提供提報指南

GitLab 官方文件有記載看板排序，Issue 清單置頂則有一項公開功能提案。若要提供固定入口，可以把提報指南加到專案根目錄 `README.md`，讓有權查看程式碼的讀者從 **Project overview** 找到。若指南較長，可在 **Plan → Wiki** 建立頁面，從 README 放連結，並用提報者的權限確認能開啟。[GitLab 置頂 Issue 提案](https://gitlab.com/gitlab-org/gitlab/-/issues/15831) · [GitLab 專案首頁](https://docs.gitlab.com/user/project/working_with_projects/#project-overview) · [GitLab Wiki](https://docs.gitlab.com/user/project/wiki/)

團隊如果使用 **Plan → Issue boards**，也可在指南卡片的選單選 **Move to start of list**，把卡片移到該欄頂端。這個動作調整的是看板排序。[GitLab 看板排序](https://docs.gitlab.com/user/project/issue_board/#move-an-issue-to-the-start-of-the-list)

## 設定完成後怎麼驗收

- 從 GitHub 的 Issues 列表或 GitLab 的專案首頁打開指南。點「先搜尋」和「選擇範本」，確認會跳到各自的段落。
- 逐一點擊 Bug 回報和功能建議連結。Bug 範本應出現環境、重現步驟與結果欄位，功能建議範本應出現問題及使用情境欄位。看到預填內容就能完成檢查。
- 若連結只打開空白表單，先確認檔案是否已合併到預設分支，再比對檔名、大小寫和編碼。GitHub 範例使用含 `.md` 的檔名，GitLab 範例使用不含副檔名的範本名稱。

## 參考資料

- [skills-manager 提報指南 Issue #155](https://github.com/xingkongliang/skills-manager/issues/155)
- [GitHub Markdown 排版](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Issue 範本概覽](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- [GitHub 範本選單設定](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [GitHub 建立 Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)
- [GitHub 置頂 Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/pinning-an-issue-to-your-repository)
- [GitLab Flavored Markdown](https://docs.gitlab.com/user/markdown/)
- [GitLab 說明範本](https://docs.gitlab.com/user/project/description_templates/)
- [GitLab 建立 Issue](https://docs.gitlab.com/user/project/issues/create_issues/)
- [GitLab 專案首頁](https://docs.gitlab.com/user/project/working_with_projects/)
- [GitLab Wiki](https://docs.gitlab.com/user/project/wiki/)
- [GitLab Issue 看板](https://docs.gitlab.com/user/project/issue_board/)
- [GitLab 置頂 Issue 功能提案 #15831](https://gitlab.com/gitlab-org/gitlab/-/issues/15831)
