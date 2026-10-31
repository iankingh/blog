---
title: "ub-mode 使用指南：TDD、重構與品質檢查"
description: "介紹 ub-mode 的安裝與呼叫方式，從失敗測試、最小修正到重構，並說明 Crapper、Dryer、Mutator 的品質門檻、相依工具及使用範例。"
date: 2026-10-31T00:28:15+08:00
lastmod: 2026-10-31T00:28:15+08:00
categories: ["筆記"]
tags: ["AI", "Tools", "Skills"]
toc: true
wideTables: true
draft: false
---

[ub-mode](https://github.com/unclebob/ub-mode) 是把工程紀律寫成操作指引的 Skill。它要求代理先用測試釐清行為、做出最小修正，再改善程式結構，並搭配工具檢查複雜度、重複與測試品質。

適用：已有程式碼與測試，希望讓 AI 修錯或重構時遵循一致流程的開發者。本篇依上游文件說明使用方式，尚未實機試用，收藏狀態為待試用。

<!--more-->

## ub-mode 的工作流程

上游將規則分為三組：

1. **先讓行為正確**：先釐清資料結構與邊界，寫出會因預期原因失敗的測試，再用最小修改讓測試通過。
2. **再改善結構**：修正根本原因、分段驗證，檢查複雜度與重複，再重構；每次重構後確認行為保持一致。
3. **留下可接續的紀錄**：記錄操作與原因，以小單位整理變更，檢查哪些工作目錄可以清理。

它沒有替專案帶入測試框架。使用前先確認代理知道原本的測試命令、測試資料與執行環境。上游也明確保留判斷空間：若無法寫出有意義的測試，不應為了形式補一個沒有驗證能力的測試。

## 安裝 Skill

上游目前以單一 `SKILL.md` 提供技能。先在自行選擇的下載目錄取得來源：

```sh
git clone https://github.com/unclebob/ub-mode.git ub-mode-source
```

以下以 Cursor 的個人技能目錄為例，從剛才的下載目錄執行；若已有同名目錄或軟連結，先保留既有版本，不合併覆寫：

```sh
ub_skill_dir="$HOME/.cursor/skills/ub-mode"

if [ -e "$ub_skill_dir" ] || [ -L "$ub_skill_dir" ]; then
  printf '同名技能已存在，請先確認及備份：%s\n' "$ub_skill_dir"
else
  mkdir -p "$ub_skill_dir"
  cp ub-mode-source/SKILL.md "$ub_skill_dir/SKILL.md"
fi
```

Claude Code 可將上例的目錄改成 `~/.claude/skills/ub-mode`。其他代理需依自己的技能目錄設定，保留 `ub-mode/SKILL.md` 結構；各工具的路徑差異可參考 [AI Skills：專案與全域技能目錄]({{< ref "post/ai-skills-directories.md" >}})。

在工具辨識到技能後，以 `/ub-mode` 開始任務。複製 Skill 只提供操作指引，Crapper、Dryer、Mutator 仍需另外準備。

## 品質工具與門檻

| 工具 | 用來回答的問題 | ub-mode 的要求 |
| --- | --- | --- |
| [Crapper](https://github.com/unclebob/crapper) | 哪些函式同時有高複雜度與不足的測試覆蓋？ | 每個函式的 CRAP 分數低於 `10` |
| [Dryer](https://github.com/unclebob/dryer) | 哪些程式片段在結構上相似，值得檢查重複？ | 處理相似度達 `0.8` 以上的重複候選 |
| [Mutator](https://github.com/unclebob/mutator) | 刻意改壞程式後，現有測試能否抓到？ | 補上未覆蓋處，檢查存活突變並改善測試，移除確認無用的程式碼 |

### Crapper：看複雜度，也看覆蓋率

Crapper 結合循環複雜度與覆蓋率計算 CRAP。改善方向可能是拆解過度複雜的函式、增加能驗證行為的測試，或兩者一起做。`CRAP < 10` 是 ub-mode 的目標，不能把工具的預設值直接當作這個門檻。

依 Crapper README，工具或測試執行失敗時，相關語言可能以零覆蓋率記錄並仍寫出快照；因此要一起讀測試日誌與執行狀態。`--no-coverage` 只看複雜度，CRAP 會是不可用值，也不能當作已符合目標。

### Dryer：注意預設值與 Skill 不同

Dryer README 的預設回報門檻是 `0.82`，ub-mode 則要求處理 `0.8` 以上的重複候選。要涵蓋 Skill 要求的範圍，可在工具分析時指定 `--threshold 0.8`；同時留意最小行數、最小節點數等篩選條件。

結構相似是待判讀的候選，不代表兩段業務邏輯必定相同。先確認能否共用同一個概念，再決定抽出共用函式。Dryer 正常產生報告可以回傳成功狀態，因此程序成功不等於沒有重複；若要接入 CI，需另外依報告落實專案的判準。

### Mutator：測試有執行，也要能抓錯

突變測試會刻意改變比較運算、布林值等程式內容，再看測試能否發現。測試仍通過的突變稱為存活突變，應檢查是不是缺少邊界或結果斷言，也可能需要判斷是否為等價變更。

Mutator 要求基準測試先通過，並依覆蓋報告選擇突變位置；未覆蓋處預設不執行。因而「本次執行的突變全被測試抓到」仍不能證明未覆蓋部分正確。其 README 說明，基準測試失敗回傳 `2`、有存活突變回傳 `3`，判讀時要保留這個差別。

### 先備條件從哪裡確認

這三個工具各有獨立儲存庫、語言支援與測試／覆蓋率需求；依各自 README 完成安裝，再讓代理知道工具所在位置與專案的測試命令。Mutator 的文件另外要求 Crapper 儲存庫位於它的相鄰目錄 `../crapper`。

工具的啟動器可能建立虛擬環境或補裝相依套件，先讀來源文件，從小範圍開始分析。缺工具、無法產生覆蓋率或測試失敗時，保留原因與未完成項目；此時還沒有足夠證據宣告品質檢查完成。

## 範例一：修正邊界錯誤

把可觀察的錯誤與測試入口交給代理，例如：

```text
/ub-mode 修正金額計算在數量為 0 時仍收取商品費用的錯誤。
先讀目前實作與既有測試命令，再補一個能重現問題的行為測試。
確認它因預期原因失敗後，做最小修正，接著檢查正數與邊界案例。
測試通過後再評估是否需要重構，列出實際執行的檢查與結果。
若品質工具未準備好，列出缺漏。這次只修改與驗證，先不提交或推送。
```

可以核對的結果應包含失敗測試、最小修正、修正後結果，以及品質工具的報告或具體缺漏。僅有「已補測試」的敘述，還不能證明測試曾抓到原錯誤。

## 範例二：保持行為的重構

```text
/ub-mode 整理訂單折扣計算中重複的分支，保持現有對外行為。
先整理目前規則與測試，補足一般訂單、門檻金額及不適用折扣的案例。
確認基準測試通過，再以小步驟調整結構，每一步都重跑相關測試。
使用可用的 Crapper、Dryer、Mutator 檢查結果，回報前後差異與限制。
這次只修改與驗證，先不提交、推送或清理其他工作目錄。
```

上游包含提交、推送與工作目錄清理規則。開始任務時把這次要交付的範圍說清楚，讓代理依你的需求處理；範例中的限制是這次任務設定，並非上游預設。

## 下一步

先挑一個可在本機重現、測試時間短的問題，熟悉失敗、修正、驗證與重構的順序。若需要多方案設計、平行分工或多模型審查，再看 [pstack 使用指南]({{< ref "post/pstack-guide.md" >}})。完整收藏入口見 [AI Skills 清單]({{< ref "post/ai-skills-list.md" >}}) 與 [agent-skills](https://github.com/iankingh/agent-skills)。

## 參考資料

- [ub-mode README：流程、品質工具與安裝](https://github.com/unclebob/ub-mode)
- [ub-mode SKILL.md：完整操作規則](https://github.com/unclebob/ub-mode/blob/master/SKILL.md)
- [Crapper：CRAP 分數與覆蓋率](https://github.com/unclebob/crapper)
- [Dryer：結構重複候選與回報門檻](https://github.com/unclebob/dryer)
- [Mutator：突變測試、覆蓋率與先備條件](https://github.com/unclebob/mutator)
