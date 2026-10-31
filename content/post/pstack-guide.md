---
title: "pstack 使用指南：從任務規劃到開發與驗證"
description: "以 Cursor 示範 pstack 安裝、模型設定與 poteto-mode，整理規劃、設計、多代理協作及驗證的使用方式，並補充 Claude Code 命令差異。"
date: 2026-10-31T00:28:15+08:00
lastmod: 2026-10-31T00:28:15+08:00
categories: ["筆記"]
tags: ["AI", "Tools", "Skills"]
toc: true
wideTables: true
draft: false
---

[pstack](https://github.com/cursor/plugins/tree/main/pstack) 把理解程式、設計、實作、驗證與多代理協作整理成一套工作流外掛。主要入口是 `/poteto-mode`：描述目標與完成條件，由它選擇適合任務的工作流程，再視需要使用其他技能。

適用：希望用 Cursor 處理需要設計、分工或驗證的開發任務，也想了解 Claude Code 適配方式的開發者。本篇依官方文件整理，尚未實機試用，收藏狀態為待試用。

<!--more-->

## 在 Cursor 安裝與設定

在 Cursor 對話輸入：

```text
/add-plugin pstack
```

完成安裝後執行模型設定：

```text
/setup-pstack
```

設定流程會偵測可用模型，詢問推理預算與各角色的模型選擇，並寫入個人的 `~/.cursor/rules/pstack-models.mdc`。選擇環境實際提供的模型即可，不必照抄別人的型號。

設定完成後開啟新對話，讓模型規則載入。若之後想降低成本，可重新設定較小的推理預算、減少審查角色的模型數，或讓部分角色繼承目前對話的模型。平行候選與多模型審查都會增加用量，小任務可以從少量角色開始。

依官方設定指南，若專案沒有既有驗證流程，設定精靈也可能提議產生專案驗證技能。先確認它提出的啟動方式、操作範圍與證據適合專案，再決定是否建立；已有可用的驗證命令時，可以直接沿用。

## 第一個任務：描述目標與驗證方式

不必一開始就列出所有技能名稱。先選一個小範圍且結果明確的任務：

```text
/poteto-mode 替這個 CLI 新增 --json 輸出。
原本文字輸出保持逐字相同；JSON 需可解析，且欄位符合既有資料結構。
先確認目前 CLI 與測試方式，再實作並實際執行兩種輸出。
交付修改內容、測試命令與結果。這次只修改與驗證，不提交或推送。
```

這個提示詞同時提供要改的行為、相容要求與完成證據。對修錯任務，也可以直接要求「先重現，再修正與驗證」。看它建立的工作清單，確認選到的流程符合這次需求。

## 規劃模式怎麼配合

pstack 沒有獨立的規劃技能。官方文件建議先理解程式，必要時用設計或原型解決不確定性，再把工作整理成可逐步驗證的計畫；Cursor 的規劃模式也可以一起使用。

若這一輪只想取得計畫，直接限制交付物：

```text
/poteto-mode 規劃將同步匯入改成背景工作。
先讀現有匯入流程、資料形狀與失敗處理，再提出可分階段驗證的計畫。
每一階段列出相容要求與驗證方式。
這次只交付計畫，先不修改產品程式碼。
```

對跨函式或模組邊界的設計，可以使用 `/architect`。它預設可能接著實作；需要先看設計時，使用官方示範的檢查點：

```text
/architect with checkpoint. 設計匯入工作 API 與狀態模型。
先列出呼叫端使用方式、型別與模組邊界，停下來展示設計，先不要實作。
```

## 設計、平行探索與審查怎麼選

| 技能 | 適合的任務 | 要看什麼結果 |
| --- | --- | --- |
| `/architect` | 設計會跨越函式或模組邊界，需要先釐清呼叫方式與資料形狀 | 呼叫端範例、型別、介面與模組安排 |
| `/arena` | 同一個問題值得嘗試多個設計或實作 | 多個候選、評估依據、選用與整合理由，以及最後的驗證 |
| `/swarm` | 可以拆成獨立範圍的檢查、探索或分工 | 各範圍的結果、缺漏與阻礙，以及彙整報告 |
| `/interrogate` | 已有實際變更，想讓不同模型找出可重現的問題 | 能以執行證據支持的問題，以及被排除的發現與原因 |

`/arena` 讓多個代理處理同一個問題，再綜合候選方案；`/swarm` 則可分配不同範圍，或執行有明確選擇規則的競賽任務。選擇時先想清楚需要的是方案比較，還是分工覆蓋。

例如，想針對多個套件檢查各自的驗證命令：

```text
/swarm 檢查 packages/ 下各套件的 check.sh，一個套件一個工作範圍。
只執行檢查，不修改檔案；彙整通過、問題與無法執行的項目。
```

要審查已完成的修改：

```text
/interrogate 檢查這個分支的變更。
優先找會造成錯誤或回歸的問題，提供可重現步驟與執行結果。
這次只交付審查結果，先不套用修改。
```

## 讓驗證成為任務的一部分

工作完成的標準要落在實際產物上。CLI 修改就跑命令並檢查輸出；UI 修改就操作實際頁面；資料匯入就讀回結果；效能調整則需要可比較的前後量測。

```text
/poteto-mode 修正匯出重試時重複寫入資料列的問題。
先用固定測試資料重現，再修正；驗證一般匯出與同一批資料重試。
回報重試前後的資料列與實際執行命令。
無法執行的檢查請說明原因。這次只修改與驗證，不合併或部署。
```

官方另提供 `/create-verification-skill`，用來為專案建立可重複操作、擷取證據與清理環境的驗證指引。產生檔案後仍要確認它確實跑過代表性功能；有測試腳本或建置成功，還不足以替代實際行為驗證。

實作與交付可以分開委派。官方的 Babysit 流程處理衝突、審查及 CI，停在可合併狀態；Shipping 是另外的合併流程。描述任務時，明確寫出這輪要到哪一步，避免將「修好並驗證」與「合併發布」混成同一個完成條件。

## 在 Claude Code 使用

依官方設定指南，先加入 marketplace 再安裝：

```text
/plugin marketplace add cursor/plugins
/plugin install pstack@cursor-plugins
```

Claude Code 中的外掛命令帶有 `pstack:` 前綴：

```text
/pstack:setup-pstack
/pstack:poteto-mode 修正匯出重試時重複寫入資料列的問題，先重現再驗證。
```

模型設定檔改為 `~/.claude/rules/pstack-models.md`。官方適配文件也列出工具、代理型別、路徑與模型欄位的對應；Cursor 的模型名稱與專有服務不能直接照搬，應依 Claude Code 當前提供的能力設定。需要 Cursor Automations、雲端代理等服務的步驟，依適配說明另行處理。

## 使用前先確認

- **先有可執行的驗證方式**：提供測試、啟動與重現入口，讓每個代理知道如何檢查結果。
- **從小任務看實際用量**：候選數、審查模型與推理預算都影響成本，再依收益擴大分工。
- **檢查缺少的技能**：上游 README 說明，部分流程引用的 `/deslop`、`control-cli`、`control-ui` 由 `cursor-team-kit` 提供；需要這些功能時再依來源準備相依外掛。

若目前只想建立 TDD、重構與品質工具的使用紀律，也可以先看 [ub-mode 使用指南]({{< ref "post/ub-mode-guide.md" >}})。其他技能與收藏入口見 [AI Skills 清單]({{< ref "post/ai-skills-list.md" >}}) 及 [agent-skills](https://github.com/iankingh/agent-skills)。

## 參考資料

- [pstack README：技能與工作流程](https://github.com/cursor/plugins/tree/main/pstack)
- [pstack 官方使用指南](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/README.md)
- [設定指南：安裝、模型與第一個任務](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/01-setup.md)
- [設計指南：architect、arena、swarm 與 interrogate](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/04-design.md)
- [驗證與交付指南](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/06-verify-and-ship.md)
- [Claude Code 適配說明](https://github.com/cursor/plugins/blob/main/pstack/docs/harness/claude-code.md)
