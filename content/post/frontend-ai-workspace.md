---
title: "ＡＩ前端專案目錄"
description: "以 Vue、TypeScript 與 Vite 專案為例，整理 GitHub Copilot 設定、專案文件、前端程式碼與測試的目錄結構，並示範如何驗證與交接一項改動。"
date: 2026-11-20T00:00:00+08:00
lastmod: 2026-11-20T00:00:00+08:00
categories: ["筆記"]
tags: ["AI", "Harness", "GitHub Copilot", "Vue"]
toc: true
draft: false
---

這份筆記適用於使用 Vue、TypeScript、Vite 與 GitHub Copilot 的前端團隊。從專案根目錄可以找到開發規則、架構決策、程式碼，以及修改後要跑的驗證。

<!--more-->

## 專案目錄結構

在 AI 輔助開發中，Harness 涵蓋 Agent 取得專案脈絡、操作工具、驗證結果與接續任務所需的環境和流程。這個範例以 `AGENTS.md` 作為入口，連到 `docs/` 的專案知識及 `package.json` 的驗證指令。`.github/` 則放 GitHub Copilot 的設定。

```text
project-root/
├── README.md                         # 專案介紹、啟動與快速開始
├── AGENTS.md                         # Agent 開發與協作入口
├── package.json                      # 套件與開發、測試、建置指令
├── package-lock.json                 # npm 套件版本鎖定
├── tsconfig.json                     # TypeScript 編譯設定
├── vite.config.ts                    # Vite 建置設定
├── eslint.config.js                   # ESLint 檢查規則
├── .prettierrc                        # Prettier 格式化規則
├── .gitignore                        # Git 忽略清單
├── .github/
│   ├── copilot-instructions.md        # Copilot 儲存庫層級指引
│   ├── instructions/                 # 依路徑套用的規則
│   │   ├── coding-standards.instructions.md
│   │   ├── api-development.instructions.md
│   │   ├── unit-test.instructions.md
│   │   └── security-guideline.instructions.md
│   ├── prompts/                      # 選用，供 VS Code Local harness
│   ├── agents/                       # 可選用的專門角色
│   │   ├── frontend-architect.md
│   │   ├── code-reviewer.md
│   │   ├── unit-test-writer.md
│   │   └── api-analyzer.md
│   └── skills/                       # 可重用的任務流程
│       ├── vue-management/
│       │   └── SKILL.md
│       ├── api-document-generator/
│       │   ├── SKILL.md
│       │   ├── scripts/
│       │   └── references/
│       ├── dto-validator/
│       │   └── SKILL.md
│       └── test-case-generator/
│           └── SKILL.md
├── docs/
│   ├── architecture/                 # 架構圖、API、前端能力與 Agent 流程
│   │   ├── api-catalog.md
│   │   ├── frontend-capabilities.md
│   │   ├── harness-layers.md
│   │   └── system-map.md
│   ├── decisions/                    # ADR、Prompt 與 Skill 設計決策
│   │   ├── 001-provide-inject-instead-of-pinia.md  # 狀態共享方案
│   │   ├── 002-api-via-makeapi.md                 # API 統一存取
│   │   ├── 003-action-audit-in-wmc-auth.md        # 操作稽核
│   │   └── 004-frontend-error-reporting.md       # 前端錯誤追蹤
│   ├── failures/                     # 踩坑、問題分析與事故復盤
│   │   ├── 2026-10-edit-built-utils-artifact.md  # Agent 誤改建置產物
│   │   └── 2026-10-native-arithmetic-on-money.md # 金額浮點數問題
│   ├── guides/                       # 開發、導入及維運指南
│   │   ├── onboarding.md
│   │   ├── deployment-flow.md
│   │   └── troubleshooting.md
│   ├── examples/                     # 可參考的操作與實作範例
│   └── verification/                 # 測試輸出、審查結果與任務驗證紀錄
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

## GitHub Copilot 檔案怎麼分工

- `AGENTS.md` 是專案入口，寫開工順序、必守規範、驗證指令，以及各類文件去哪裡找。團隊若需要 Copilot 專用的儲存庫層級指引，可另外使用 `.github/copilot-instructions.md`。兩處的共用規則指向同一份文件，減少日後更新時出現差異。
- 路徑規則使用 `*.instructions.md`。原稿的 `api-development.md` 若要作為 Copilot 路徑指引，可命名為 `api-development.instructions.md`，在 YAML front matter 設定 `applyTo: "src/api/**/*.ts"`，讓它套用到 API 呼叫層的 TypeScript 檔案。
- 自訂 Agent 定義角色的工作範圍與可用工具，例如讓 `code-reviewer.md` 以程式碼審查為任務。在 VS Code，`.github/agents/` 支援 `.md` 和 `.agent.md`，可沿用原稿的 `.md` 檔名。
- Skill 封裝可重用的任務流程。每個 Skill 以 `SKILL.md` 作為入口，用 `name` 和 `description` 說明名稱與使用時機。API 文件產生流程可把檢查步驟寫在 `SKILL.md`，把專用腳本與格式範本放進該 Skill 的 `scripts/` 和 `references/`。
- 原有 Prompt 檔案如 `code-review.prompt.md`、`bug-analysis.prompt.md` 和 `feature-development.prompt.md` 可放在 `.github/prompts/`。依 VS Code 文件，這些檔案在 Local harness 的聊天工作階段執行。若團隊使用 Copilot harness，可將常用的任務步驟與輸入、輸出要求移到 Skill。

## 修改投組頁面的驗證流程

假設要修正投組頁面的合計金額，並補上 API 失敗時的提示。先從 `AGENTS.md` 找到 `docs/architecture/api-catalog.md`，核對投組 API 的傳輸格式，再讀 `docs/decisions/002-api-via-makeapi.md` 和 `docs/failures/2026-10-native-arithmetic-on-money.md`，確認 API 呼叫慣例與金額計算的既有問題。

1. 在 `tests/unit/` 用單元測試檢查 `src/utils/currency.ts` 的加總與捨入，涵蓋曾發生的浮點數案例。
2. 在本例的 `tests/integration/` 用 API mock 測試元件，確認等待回應時顯示載入狀態、成功時顯示合計金額、失敗時顯示錯誤提示。
3. 在 `tests/e2e/` 從瀏覽器執行端到端測試，開啟投組頁面並選取投組，確認明細與合計同步更新。
4. 執行 `package.json` 已定義的檢查，將驗收條件、實際命令、結果、證據位置和未測項目寫進 `docs/verification/`。例如，元件測試使用 mock 時，紀錄應明確標示真實 API 的驗證狀態。

## 參考資料

- [OpenAI：Harness Engineering 與儲存庫知識庫](https://openai.com/index/harness-engineering/)
- [Anthropic：長時間執行的 Agent 與跨會話交接](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)
- [GitHub Docs：Copilot 自訂設定速查](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)
- [VS Code：自訂指引檔案](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference)
- [VS Code：自訂 Agent 檔案](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)
- [VS Code：Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [VS Code：Prompt 檔案](https://code.visualstudio.com/docs/agent-customization/prompt-files)
- [Vue：單元、元件與端到端測試](https://vuejs.org/guide/scaling-up/testing.html)
