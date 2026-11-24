---
title: "ＡＩ專案目錄"
description: "整理 AI 協作專案的共用規則、Agent 角色、技能與文件，再以 Vue 前端專案示範程式碼、測試與驗證紀錄的放置方式，文末附 GitHub Copilot 目錄範例。"
date: 2026-11-20T00:00:00+08:00
lastmod: 2026-11-24T21:51:00+08:00
categories: ["筆記"]
tags: ["AI", "Harness", "GitHub Copilot", "Vue"]
toc: true
draft: false
---

這份目錄適用於和 AI 一起開發、需要共用專案規則的團隊。成員和 Agent 都能從根目錄找到開工規則、架構決策與驗證紀錄。下面先整理共用目錄，再以 Vue 投組頁面為例，走一遍從查文件、改程式到驗證的流程。

<!--more-->

## ＡＩ專案用

`AGENTS.md` 記錄團隊共用規則與開工順序，`agents/` 放自訂角色，`skills/` 放可重用的任務流程，`docs/` 則保存架構、決策與驗證紀錄。根目錄的 `agents/` 和 `skills/` 是本例的整理方式。各工具實際會從哪裡載入技能，見[〈AI Skills：專案與全域技能目錄〉]({{< relref "post/ai-skills-directories.md" >}})。

下例採用 npm、TypeScript、Vite、ESLint 與 Prettier，因此列出對應設定檔。使用其他技術的團隊，可以在相同位置列出自己的建置與檢查入口。

```text
project-root/
├── README.md                         # 專案介紹、啟動與快速開始
├── AGENTS.md                         # Agent 開發與協作入口
├── agents/                           # 自訂 Agent 角色
├── skills/                           # 可重用的任務流程
├── package.json                      # 套件與開發、測試、建置指令
├── package-lock.json                 # npm 套件版本鎖定
├── tsconfig.json                     # TypeScript 編譯設定
├── vite.config.ts                    # Vite 建置設定
├── eslint.config.js                  # ESLint 檢查規則
├── .prettierrc                       # Prettier 格式化規則
├── .gitignore                        # Git 忽略清單
└── docs/
    ├── architecture/                 # 架構圖、API、前端能力與 Agent 流程
    │   ├── api-catalog.md
    │   ├── frontend-capabilities.md
    │   ├── harness-layers.md
    │   └── system-map.md
    ├── decisions/                    # ADR、Prompt 與 Skill 設計決策
    │   ├── 001-provide-inject-instead-of-pinia.md  # 狀態共享方案
    │   ├── 002-api-via-makeapi.md                 # API 統一存取
    │   ├── 003-action-audit-in-wmc-auth.md        # 操作稽核
    │   └── 004-frontend-error-reporting.md        # 前端錯誤追蹤
    ├── failures/                     # 踩坑、問題分析與事故復盤
    │   ├── 2026-10-edit-built-utils-artifact.md   # Agent 誤改建置產物
    │   └── 2026-10-native-arithmetic-on-money.md  # 金額浮點數問題
    ├── guides/                       # 開發、導入及維運指南
    │   ├── onboarding.md
    │   ├── deployment-flow.md
    │   └── troubleshooting.md
    ├── examples/                     # 可參考的操作與實作範例
    └── verification/                 # 測試輸出、審查結果與任務驗證紀錄
```

## 前端專案用

Vue 專案沿用上一節的協作規則與文件。修改頁面時，可從 `src/views/` 找到畫面，沿著 `composables/`、`services/` 和 `api/` 追查資料來源，再依修改範圍到 `tests/` 找對應案例。

```text
project-root/
├── README.md                         # 專案介紹、啟動與快速開始
├── AGENTS.md                         # Agent 開發與協作入口
├── agents/                           # 自訂 Agent 角色
├── skills/                           # 可重用的任務流程
├── package.json                      # 套件與開發、測試、建置指令
├── package-lock.json                 # npm 套件版本鎖定
├── tsconfig.json                     # TypeScript 編譯設定
├── vite.config.ts                    # Vite 建置設定
├── eslint.config.js                  # ESLint 檢查規則
├── .prettierrc                       # Prettier 格式化規則
├── .gitignore                        # Git 忽略清單
├── docs/                             # 完整文件目錄見上一節「ＡＩ專案用」
├── public/                           # 直接提供的靜態資源
│   ├── favicon.ico
│   └── images/
├── src/
│   ├── api/                          # API 呼叫層
│   │   ├── customerApi.ts
│   │   ├── portfolioApi.ts
│   │   └── investmentApi.ts
│   ├── assets/                       # 圖片、圖示與全域樣式
│   │   ├── images/
│   │   ├── icons/
│   │   └── styles/
│   ├── components/                   # 共用元件
│   │   ├── common/
│   │   ├── layout/
│   │   ├── form/
│   │   └── chart/
│   ├── composables/                  # 可重用的 Vue 邏輯
│   │   ├── useCustomer.ts
│   │   ├── usePortfolio.ts
│   │   └── useInvestment.ts
│   ├── constants/                    # API、路由及業務常數
│   │   ├── api.ts
│   │   ├── route.ts
│   │   └── business-rule.ts
│   ├── dto/                          # API 請求與回應的資料傳輸物件
│   │   ├── request/
│   │   └── response/
│   ├── router/                       # Vue Router 設定
│   │   └── index.ts
│   ├── services/                     # 業務服務層
│   │   ├── customer/
│   │   ├── portfolio/
│   │   └── investment/
│   ├── stores/                       # 狀態管理
│   │   └── app.store.ts
│   ├── types/                        # API 與業務型別
│   │   ├── api.ts
│   │   └── business.ts
│   ├── utils/                        # 金額、格式化及驗證函式
│   │   ├── currency.ts
│   │   ├── formatter.ts
│   │   └── validator.ts
│   ├── views/                        # 頁面模組
│   │   ├── dashboard/
│   │   ├── customer/
│   │   ├── portfolio/
│   │   └── report/
│   ├── App.vue                       # Vue 根元件
│   └── main.ts                       # 應用程式入口
├── tests/
│   ├── unit/                         # 單元測試
│   ├── integration/                  # 整合測試，含本例的元件測試
│   ├── e2e/                          # 瀏覽器端到端測試
│   └── mocks/                        # 模擬資料與替身
├── coverage/                         # 測試工具產生的覆蓋率報告
└── scripts/                          # 建置、部署與 API 文件產生
    ├── build.sh
    ├── deploy.sh
    └── generate-api-doc.sh
```

### 修改投組頁面的驗證流程

假設要修正投組頁面的合計金額，並補上 API 失敗時的提示。先從 `AGENTS.md` 找到 `docs/architecture/api-catalog.md`，核對投組 API 的傳輸格式，再讀 `docs/decisions/002-api-via-makeapi.md` 和 `docs/failures/2026-10-native-arithmetic-on-money.md`，確認 API 呼叫慣例與金額計算的既有問題。接著在 `src/utils/currency.ts` 修正加總邏輯，並在 `src/views/portfolio/` 補上錯誤提示。

1. 在 `tests/unit/` 用單元測試檢查 `src/utils/currency.ts` 的加總與捨入，涵蓋曾發生的浮點數案例。
2. 在本例的 `tests/integration/` 用 API mock 測試元件，確認等待回應時顯示載入狀態、成功時顯示合計金額、失敗時顯示錯誤提示。
3. 在 `tests/e2e/` 從瀏覽器執行端到端測試，開啟投組頁面並選取投組，確認明細與合計同步更新。
4. 執行 `package.json` 已定義的檢查，將驗收條件、實際命令、結果、證據位置和未測項目寫進 `docs/verification/`。例如，元件測試使用 mock 時，紀錄應明確標示真實 API 的驗證狀態。

## GitHub Copilot 簡易版

團隊使用 GitHub Copilot 時，可在專案根目錄加上這些設定。`copilot-instructions.md` 裡的共用規則可指向 `AGENTS.md` 或同一份專案文件。

```text
.github/
├── copilot-instructions.md   # 儲存庫層級指引
├── instructions/            # 依路徑套用的 *.instructions.md 規則
├── prompts/                 # VS Code Local harness 的 *.prompt.md 範本
├── agents/                  # 自訂 Agent
└── skills/                  # 可重用的任務流程
    └── <skill-name>/
        └── SKILL.md
```

## 參考資料

- [OpenAI：Harness Engineering 與儲存庫知識庫](https://openai.com/index/harness-engineering/)
- [Anthropic：長時間執行的 Agent 與跨會話交接](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)
- [GitHub Docs：Copilot 自訂設定速查](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)
- [VS Code：自訂指引檔案](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference)
- [VS Code：自訂 Agent 檔案](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)
- [VS Code：Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [VS Code：Prompt 檔案](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- [Vue：單元、元件與端到端測試](https://vuejs.org/guide/scaling-up/testing.html)
