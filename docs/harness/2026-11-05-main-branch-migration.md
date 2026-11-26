# 主分支更名與 Codex 分支清理

## 需求與範圍

- 將 Blog 的預設分支從 `master` 更名為 `main`，同步調整 GitHub Actions 的觸發條件、發布限制與 Hugo 編輯網址。
- 清理已合併的 Codex 分支，刪除前確認分支提交包含於 `main`。

## 驗收

| 案例 | 預期結果 | 證據 |
| --- | --- | --- |
| 更名 | 本機與 GitHub 預設分支為 `main`，保留原主分支歷史 | `git branch -vv`、GitHub 分支列表 |
| 已合併分支 | `codex/harness-engineering` 為主分支祖先且已清理 | `git merge-base --is-ancestor`、分支列表 |
| PR 分支 | PR #5 的目標隨更名更新，合併後可清理來源分支 | PR #5、`git merge-base --is-ancestor e8a291ed main` |
| 網站與部署設定 | 網站驗證通過，部署 push 與發布條件使用 `main` | `/tmp/blog-main-migration-final-2026-11-05/report.json`、部署工作流程差異 |

## 當前狀態與交班

- 起始主分支為 `84ac925d331382288f5bfe0473d898f5dc884c87`，工作目錄乾淨。
- `codex/harness-engineering` 的提交 `6c918ed6` 已包含於主分支，GitHub 上也已無該分支。
- GitHub 更名後，PR #5 的目標已更新為 `main`。合併提交 `db66531c` 包含 `codex/vault-blog-writing` 的提交 `e8a291ed`。
- 以 GitHub 分支列表和網站驗證報告確認結果。推送遷移提交後，核對同一來源 SHA 的 Actions、Pages 發布及部署版本紀錄。
