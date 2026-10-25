# AI 技能目錄：.agents/skills、.github/skills 等放在哪裡

這些 AI 技能（Skills）與指令目錄通常有專案層級（Project-level）與全域層級（Global / User-level）兩種放置位置。放在專案根目錄可以透過 Git 與團隊共享，放在使用者家目錄（~）則可跨專案共用個人常用的工作流。

以下為目前主流 AI Coding 工具的技能目錄放置位置與規範：

## 1. 各工具的目錄放置位置對照表

| 工具 / 框架 | 專案層級（放在專案根目錄 ./ 下） | 全域層級（放在家目錄 ~/ 下） | 檔案格式與載入邏輯 |
| --- | --- | --- | --- |
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
