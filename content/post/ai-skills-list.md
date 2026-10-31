---
title: "AI Skills 清單：自製技能與工作流收藏"
description: "整理 agent-skills 專案的 Git 提交訊息、IG 與 YouTube 筆記技能，以及 ub-mode、pstack 外部收藏，附用途、來源與使用教學。"
date: 2026-10-31T00:28:15+08:00
lastmod: 2026-10-31T00:28:15+08:00
featuredOrder: 1
categories: ["筆記"]
tags: ["AI", "Tools", "Skills"]
toc: true
wideTables: true
draft: false
---

**專案入口：[iankingh/agent-skills](https://github.com/iankingh/agent-skills)**。這裡整理自己使用、製作與探索的 AI agent skills；完整技能檔案、支援工具及外部收藏由專案 README 維護。

這篇清單方便先看用途，再決定要讀哪個技能或教學。適用：希望重複使用 Git 提交訊息、影音筆記整理流程，或想研究工程紀律與代理工作流的開發者。

<!--more-->

## 自製技能

| Skill | 可以幫忙做什麼 | 使用入口 |
| --- | --- | --- |
| [git-commit-content](https://github.com/iankingh/agent-skills/blob/main/skills/git-commit-content/SKILL.md) | 根據實際 Git 變更產生、修改或檢查繁體中文提交訊息，遵循 Conventional Commits 與專案規則 | 提供目前變更，要求產生提交訊息；實際提交或推送需另行要求 |
| [ig-post-to-notes](https://github.com/iankingh/agent-skills/blob/main/skills/ig-post-to-notes/SKILL.md) | 整理 Instagram 單篇貼文及完整輪播，保留來源與提示詞；依要求存入 Obsidian | 提供貼文網址；需要存檔時再指定筆記庫位置 |
| [yt-video-to-notes](https://github.com/iankingh/agent-skills/blob/main/skills/yt-video-to-notes/SKILL.md) | 整理 YouTube 影片重點與時間戳，或原文匯入已整理文稿；另附章節建置與繁中檢查工具 | 提供影片網址或既有文稿，指定要整理還是原文匯入 |

IG 與 YouTube 技能在專案中提供共用版本，沒有預設個人筆記庫路徑。僅要求整理時可直接取得對話中的筆記；要寫入 Obsidian 時才指定目的地。影片網址帶有播放清單參數，也不會自動擴大成整個播放清單。

安裝時保留完整技能資料夾與支援檔案，實際步驟見 [agent-skills 使用方式](https://github.com/iankingh/agent-skills#使用方式)。若正在釐清工具會從哪個目錄載入技能，可先讀 [AI Skills：專案與全域技能目錄]({{< ref "post/ai-skills-directories.md" >}})。

## 外部收藏

以下兩項保留原始來源，尚未複製進專案的技能目錄，試用狀態均為**待試用**。教學依上游文件整理，方便理解安裝與使用流程。

| 項目 | 簡介與收藏理由 | 使用教學 |
| --- | --- | --- |
| [ub-mode](https://github.com/unclebob/ub-mode) | 強調 TDD、重構與品質檢查的工程紀律 Skill，把開發步驟與複雜度、重複程式碼、突變測試連在一起；適合研究如何落實品質要求 | [ub-mode 使用指南]({{< ref "post/ub-mode-guide.md" >}}) |
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | 涵蓋任務規劃、開發、驗證與多代理協作的工作流外掛，以 `/poteto-mode` 選擇適合任務的流程；適合研究從需求到驗證的完整做法 | [pstack 使用指南]({{< ref "post/pstack-guide.md" >}}) |

ub-mode 著重寫程式時應遵守的紀律與品質檢查；pstack 則提供較完整的任務路由、設計、協作與驗證流程。ub-mode 上游也說明，其部分原則來自 poteto-mode／pstack，再經精簡並結合品質工具。

## 怎麼挑選

- **反覆做相同整理工作**：先看自製技能，確認輸入、輸出與是否需要寫檔。
- **希望開發時先測試、再修正與重構**：先讀 ub-mode 教學，確認專案是否有可執行的測試及相依工具。
- **需要設計探索、分工與多角度審查**：先讀 pstack 教學，從小任務開始，提供明確的完成條件與驗證方式。

其他聊天、搜尋、翻譯與學習入口，另見 [AI 工具與學習資源清單]({{< ref "post/ai-tools.md" >}})。技能檔案與外部收藏的後續異動，以 [agent-skills README](https://github.com/iankingh/agent-skills) 為入口。

## 參考資料

- [iankingh/agent-skills](https://github.com/iankingh/agent-skills)
- [unclebob/ub-mode](https://github.com/unclebob/ub-mode)
- [Cursor plugins：pstack](https://github.com/cursor/plugins/tree/main/pstack)
