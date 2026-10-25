---
title: "AI Skills：專案與全域技能目錄"
description: "說明 AI Skills 的用途、載入流程與實際情境，整理 Codex 等工具的專案及個人技能目錄，並區分 Skills、常駐指令與 Prompt。"
date: 2026-10-25T00:17:31+08:00
lastmod: 2026-10-25T00:33:07+08:00
featuredOrder: 1
categories: ["筆記"]
tags: ["AI", "Tools", "Skills"]
toc: true
wideTables: true
draft: false
---

適用：需要在專案與個人環境管理 AI Coding 工具技能、規則及提示模板的開發者。

> 本篇保留原始筆記的正文與範例；「Skills 是做什麼的？」與表中的 OpenAI Codex 列為本次新增，官方文件差異另列於文末「官方文件補充」。

<!--more-->

## Skills 是做什麼的？（補充）

**Skills 是讓 AI 重複使用某類任務做法的工作流程**。它把任務步驟、規範、參考資料，以及選用的腳本或模板整理在同一個資料夾，以 `SKILL.md` 作為入口。當你反覆要求 AI 用相同方式處理事情，就可以把這些做法整理成 Skill，減少每次重新貼上長篇指令的需要。資料夾結構見 [Agent Skills 規格](https://agentskills.io/specification)。

### 三個使用情境

- **程式碼審查**：先讀需求與變更，再依專案規範檢查錯誤、邊界與測試覆蓋，最後輸出問題位置、原因與修改建議。
- **測試撰寫**：從功能需求整理正常、錯誤與邊界案例，依專案既有測試框架撰寫並執行測試，留下實際結果。
- **筆記匯入**：保留原文與來源，補上 Hugo front matter、轉換 Markdown、同步文章清單，再執行網站驗證，產出可閱讀的文章與驗證紀錄。

這些是可整理成技能的流程範例。技能可以只有操作指引；需要工具處理時，再搭配參考資料、模板或腳本。

### 從任務到執行

以 Codex 為例，流程可以分成三步：

1. **辨識任務**：先讀可用技能的名稱與描述，判斷是否符合目前需求；使用者也可以直接指定技能。
2. **載入技能**：選用後才讀取完整 `SKILL.md`，並依需要參考附帶資料。
3. **依流程使用工具**：按照技能步驟與專案規則執行工作，再根據實際輸出確認結果。

這種按需載入方式稱為漸進式揭露（progressive disclosure）；名稱與描述幫助代理選擇技能，完整內容在使用時才載入。見 [OpenAI 官方 Skills 文件](https://learn.chatgpt.com/docs/build-skills)。

### Skills、常駐指令與單次 Prompt 怎麼分？

- **專案常駐指令**：適合放整個專案共用的要求，例如使用哪個建置命令、程式碼風格及交付前的必要檢查，通常由 `AGENTS.md` 或各工具的指令檔維護。
- **Skills**：適合放特定任務會反覆用到的流程，例如「開始程式碼審查時要做哪些事」，需要時才載入。
- **單次 Prompt**：適合描述這一次的目標與限制，例如「幫這次登入失敗修正補上回歸案例，沿用現有測試框架」。

實務上可以一起使用：專案指令訂共通要求，Skill 提供任務做法，這次的 Prompt 指定要處理的內容。

這些 AI 技能（Skills）與指令目錄通常有專案層級（Project-level）與全域層級（Global / User-level）兩種放置位置。放在專案根目錄可以透過 Git 與團隊共享，放在使用者家目錄（~）則可跨專案共用個人常用的工作流。

以下為目前主流 AI Coding 工具的技能目錄放置位置與規範：

## 1. 各工具的目錄放置位置對照表

下表保留原稿各列；「OpenAI Codex（補充）」為 2026-10-25 新增。其他工具的現行 Skills 路徑另見文末「官方文件補充」。

| 工具 / 框架 | 專案層級（放在專案根目錄 ./ 下） | 全域層級（放在家目錄 ~/ 下） | 檔案格式與載入邏輯 |
| --- | --- | --- | --- |
| OpenAI Codex（補充） | `.agents/skills/<skill-name>/SKILL.md` | `~/.agents/skills/<skill-name>/SKILL.md` | 從目前目錄向上至儲存庫根目錄掃描各層 `.agents/skills/`。每個技能包含 `name`、`description` 與操作指引，可依描述自動選用；CLI／IDE 可用 `/skills` 或 `$skill-name` 指定。見 [OpenAI 官方文件](https://learn.chatgpt.com/docs/build-skills)。 |
| Claude Code | `.claude/skills/`、`.claude/commands/` | `~/.claude/skills/`、`~/.claude/commands/` | 每個技能可為獨立資料夾（內含 SKILL.md 及輔助腳本）或單一 .md 檔。支援透過 /skill-name 觸發或由 Agent 根據語意自動掛載。 |
| 通用 Agent 規範 (Claude / OpenClaw / 自建框架) | `.agents/skills/`、`skills/` | `~/.agents/skills/` | 社群開源技能庫（如 mattpocock/skills 或通用 Agent 框架）常用的中立路徑。通常採用 `<skill-name>/SKILL.md` 結構（含 YAML frontmatter 描述觸發條件）。 |
| GitHub Copilot | `.github/copilot-instructions.md`、`.github/instructions/`、`.github/prompts/` | (主要由 VS Code User Settings 管理) | 官方原生支援為 .github/copilot-instructions.md（全域背景）與 .github/prompts/*.prompt.md（可複用 Prompt）。若團隊自訂 .github/skills/，需在主設定檔中透過相對路徑引用。 |
| Cursor | `.cursor/rules/` | (由 Cursor 內建 Settings 管理) | 存放 .mdc 檔案，可針對特定檔案路徑（Glob pattern）或語意情境動態載入規則與技能。 |
| Windsurf | `.windsurf/rules/` | `~/.codeium/windsurf/memories/` | 存放專案專屬規則或跨專案的個人開發習慣。 |

## 2. 標準專案目錄結構範例

在實務開發中，若想同時支援多種工具（例如團隊有人用 Claude Code、有人用 GitHub Copilot），最乾淨的做法是將核心技能統一放在 .agents/skills/，再由各工具的進入點去引用（Reference），避免重複維護多份 Markdown：

```text
my-project/
├── .agents/
│   └── skills/                      # 統一存放跨工具的模組化技能
│       ├── grill-me/
│       │   └── SKILL.md
│       ├── bdd-playwright/
│       │   ├── SKILL.md
│       │   └── template.spec.ts
│       └── code-review/
│           └── SKILL.md
├── .claude/
│   ├── CLAUDE.md                    # Claude 主記憶檔（可在內文指引讀取 .agents/skills）
│   └── skills/                      # 或透過軟連結 (symlink) 指向 ../.agents/skills/
├── .github/
│   ├── copilot-instructions.md      # Copilot 主規則檔
│   └── prompts/                     # Copilot Chat 可直接用 # 呼叫的任務模板
│       └── review.prompt.md
└── AGENTS.md                        # 專案根目錄的通用 Agent 導覽檔
```

## 3. 放置與管理建議

### 專案共用 vs. 個人私藏：

放專案根目錄（Commit 進 Git）：與專案架構高度綁定的技能（例如：特定 UI 元件庫規範、E2E 測試腳本生成模板、API 錯誤處理規範）。

放家目錄 ~/（不進專案 Git）：與個人工作習慣有關的技能（例如：grill-me 蘇格拉底式拷問法、個人偏好的 Commit message 撰寫風格、卡片盒筆記整理 Prompt）。

### 使用 Symlink（軟連結）解決多工具路徑問題：

如果你習慣把所有技能統一整理在 .agents/skills/，可以在專案根目錄執行指令建立軟連結，讓 Claude Code 等工具直接原生讀取：

```bash
mkdir -p .claude
ln -s ../.agents/skills .claude/skills
```

### 每個 Skill 的標準結構：

不論放在 .agents/skills 還是 .claude/skills，建議每個技能獨立一個子資料夾並以 SKILL.md 作為入口，開頭加上 YAML Frontmatter 讓 Agent 知道何時該載入它：

```markdown
---
name: bdd-test-generator
description: 當需要根據 Gherkin 規格撰寫或修改 Playwright 測試腳本時載入此技能。
---
# 執行步驟與規範...
```


## 官方文件補充

本區為 2026-10-25 依官方文件新增的補充；前面的原始筆記與範例完整保留。工具支援範圍會隨版本及執行環境改變，以下整理本次文件所列的本機路徑。

### Skills 的原生目錄

| 工具 | 專案技能目錄 | 個人／全域技能目錄 | 官方說明 |
| --- | --- | --- | --- |
| OpenAI Codex（補充） | `.agents/skills/<skill-name>/SKILL.md` | `~/.agents/skills/<skill-name>/SKILL.md` | [OpenAI Skills 文件](https://learn.chatgpt.com/docs/build-skills)列出的本機技能位置；專案內從目前目錄逐層向上掃描至儲存庫根目錄。CLI／IDE 支援 `/skills` 或 `$skill-name` 指定，也可依描述自動選用。 |
| Claude Code | `.claude/skills/<skill-name>/SKILL.md` | `~/.claude/skills/<skill-name>/SKILL.md` | [Skills 文件](https://code.claude.com/docs/en/skills)；單一 `.md` 檔放在 `.claude/commands/` 是仍相容的舊命令格式。 |
| GitHub Copilot | `.github/skills/`、`.claude/skills/`、`.agents/skills/` | `~/.copilot/skills/`、`~/.agents/skills/` | [Agent skills 文件](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)已列為原生支援，無須為了辨識 `.github/skills/` 再由主規則檔引用。各 IDE、CLI 與雲端的支援範圍需分別確認。 |
| Cursor | `.agents/skills/`、`.cursor/skills/` | `~/.agents/skills/`、`~/.cursor/skills/` | [Agent Skills 文件](https://cursor.com/docs/skills)；`.cursor/rules/*.mdc` 屬於 Rules，另有獨立的 Skills 目錄。 |
| Windsurf／Devin Desktop Cascade | `.devin/skills/`；仍讀取舊 `.windsurf/skills/`，也支援 `.agents/skills/` | `~/.codeium/windsurf/skills/`、`~/.config/devin/skills/`，也支援 `~/.agents/skills/` | [Cascade Skills 文件](https://docs.devin.ai/desktop/cascade/skills)；原 Windsurf 文件入口已導向 Devin Desktop，`.devin/` 為目前文件偏好的名稱。 |
| OpenClaw | 工作區 `skills/`、`.agents/skills/` | 預設狀態下的 `~/.agents/skills/`，以及預設共用目錄 `~/.openclaw/skills/` | [Skills 文件](https://docs.openclaw.ai/tools/skills)；工作區可由代理設定，並不一定等於 Git 專案根目錄；自訂 state directory 時也需依設定確認。 |

[Agent Skills 規格](https://agentskills.io/specification)定義以 `SKILL.md` 為入口的技能資料夾及其 frontmatter。結合上列各工具文件可知，**技能格式可共用，搜尋目錄仍由各工具決定**；不能把 `.agents/skills/` 或 `skills/` 視為所有框架都一定會掃描的路徑。

### Codex 的舊路徑與目前建議（補充）

較早的 [OpenAI 技能測試教學](https://developers.openai.com/blog/eval-skills)曾使用 `~/.codex/skills/` 作為個人技能範例位置；目前 [Build skills 文件](https://learn.chatgpt.com/docs/build-skills)的本機搜尋位置表則列出專案 `.agents/skills/` 與個人 `~/.agents/skills/`。本篇新增技能的位置建議依目前文件整理，舊路徑留作歷史對照。

既有環境是否仍讀取 `~/.codex/skills/`，要依實際版本與設定確認；這兩份文件不能直接證明它在所有版本都已失效。本文沒有要求搬移既有技能，也不把個人家目錄的技能視為雲端環境一定會取得的檔案。

### Rules、Commands 與 Prompts 的差別

- **Skills**：把可重複的任務流程、腳本與參考資料放在同一資料夾，藉由 `name`、`description` 協助代理選擇何時使用。各工具的手動觸發方式仍以產品文件為準。
- **Rules／Instructions**：提供專案或特定檔案的規則。Copilot 的 `.github/copilot-instructions.md` 是儲存庫範圍的指令檔；Cursor 的 `.cursor/rules/*.mdc` 是專案規則。它們與技能資料夾各有用途，見 [VS Code 自訂指令](https://code.visualstudio.com/docs/agent-customization/custom-instructions)及 [Cursor Rules](https://cursor.com/docs/rules)。
- **Claude Commands**：`.claude/commands/*.md` 是仍支援的舊格式；目前自訂命令已整合至 Skills，可透過 `/skill-name` 呼叫。新建技能以資料夾內的 `SKILL.md` 為主，見 [Claude Code Skills](https://code.claude.com/docs/en/skills)。
- **VS Code Prompt files**：`.github/prompts/*.prompt.md` 是手動執行的提示模板，可在聊天輸入 `/` 選取名稱。原目錄樹中的「用 `#` 呼叫」應與 `#file:` 引用檔案分開理解；提示模板的呼叫使用斜線命令，見 [Prompt files 文件](https://code.visualstudio.com/docs/agent-customization/prompt-files)。
- **Cascade Rules／Memories**：原文中的 `.windsurf/rules/` 和 `~/.codeium/windsurf/memories/` 屬於規則與記憶機制；全域規則檔為 `~/.codeium/windsurf/memories/global_rules.md`。技能則使用上表的 Skills 目錄，見 [Memories & Rules](https://docs.devin.ai/desktop/cascade/memories)。

### 共用目錄與軟連結

先確認 `.agents/skills/` 已存在，且 `.claude/skills` 尚未是既有檔案或資料夾，再執行原文的軟連結指令。`../.agents/skills` 會從連結所在的 `.claude/` 解析，指回專案根目錄的共用技能資料夾。若工具已原生辨識 `.agents/skills/`，即可直接使用該路徑；其餘工具仍要依各自文件安排入口。

## 參考資料

- [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI：Testing Agent Skills Systematically with Evals（較早的路徑範例）](https://developers.openai.com/blog/eval-skills)
- [Claude Code：Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [GitHub Copilot：Agent skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [Cursor：Rules](https://cursor.com/docs/rules)
- [Devin Desktop Cascade：Skills（原 Windsurf 文件）](https://docs.devin.ai/desktop/cascade/skills)
- [Devin Desktop Cascade：Memories & Rules](https://docs.devin.ai/desktop/cascade/memories)
- [OpenClaw：Skills](https://docs.openclaw.ai/tools/skills)
- [Agent Skills：Specification](https://agentskills.io/specification)
- [VS Code：Custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [VS Code：Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files)
