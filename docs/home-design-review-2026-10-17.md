# 首頁設計 skills 首輪評估

Method: dual-agent（A: `/root/design_assessment`；B: `/root/design_detector`）

評估對象：`layouts/home.html`，來源 `885d2ce5`，分支 `codex/harness-engineering`。
2026-10-17 完成安裝、指引閱讀、獨立設計評估、來源掃描與實際瀏覽器檢視。
以下為修改前的歷史評估。使用者試看 A 工程野帳後明確表示「我比較喜歡原本的排版，我只是不要 AI 味」，因此 A 結構重整已撤回。最終只保留原 RPG 構圖的文案與操作細節修整；本文件的版型建議未全部採用，不能當成待辦清單。實作與最終驗證見 `docs/harness/home-design-skills-2026-10-17.md`。

## 安裝與實際使用

全部使用內建 skill-installer 的 `install-skill-from-github.py`，安裝到 `/Users/ian/.codex/skills/`，未覆蓋既有 skill。

| Skill | 官方來源與安裝路徑 | 本輪用途 |
| --- | --- | --- |
| Impeccable 4.6.0 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable)，`.agents/skills/impeccable` → `impeccable/` | context、critique、獨立 A/B 評估、來源 detector 與 snapshot |
| frontend-design | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design)，`skills/frontend-design` → `frontend-design/` | 從真實內容檢視通用 Hero、重複卡片、字體與兩個構圖方向 |
| UI UX Pro Max | [nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)，`.claude/skills/ui-ux-pro-max` → `ui-ux-pro-max/` | 執行內附搜尋器，查觸控尺寸、標題斷行與閱讀導航；資料與 scripts 均已安裝 |
| web-design-guidelines | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines)，`skills/web-design-guidelines` → `web-design-guidelines/` | 讀取本輪最新 [Web Interface Guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md)，核對語意、焦點、尺寸、換行及圖片 |

四套 skills 已安裝並出現在可用清單，本輪已直接讀取與使用安裝檔案。
Impeccable 引擎由官方 launcher 下載並校驗。安裝器 ZIP 未保留 launcher 執行位元，初次以 `sh` 呼叫，之後已補齊執行位元並直接執行。
不安裝 hooks、不變更 CSP 或專案子模組。沒有新增外部字型、圖片或分析服務。

UI UX Pro Max 使用查詢：`touch target size`、`orphan heading line balance`、`blog reading navigation`，均指定 `--domain ux -n 3`。
前兩項命中對應的 Web 目標尺寸與標題斷行；第三項的 sticky navigation 對非固定頁首不適用，僅採用其中鍵盤導覽建議。
本站為 Hugo + 原生 CSS/JavaScript，沒有假定 Tailwind 或 React stack。

## 設計判斷與優點

模式為 Read：讀者要找到、判讀並理解技術筆記。
有辨識度，但主要來自 RPG 外殼。拿掉文章標題後，「側欄＋個人介紹 Hero＋精選三卡＋文章卡」仍可套在其他個人站。
不能由外觀判定是否 AI 生成；問題是內容具體，承載內容的結構仍通用。

- 保留營火像素圖、暖金與森林綠、中文襯線標題形成的安靜學習氣氛。
- 保留具體文章摘要，例如連線耗盡重現、JDK 版本確認與數字精度處理。
- 保留已實看正常的搜尋、空結果、Esc 關閉、焦點返回、文章更新日期與閱讀時間。

## Nielsen 評分

這是本次設計評估的主觀分數，不是測試通過率或完整無障礙認證。

| 準則 | 分數（0–4） | 主要依據 |
| --- | --- | --- |
| 狀態可見 | 3 | 導覽、更新、頁碼與搜尋數量清楚；固定世界狀態文字資訊價值低 |
| 使用者語言 | 2 | 技術標題具體；探索地圖／歷程圖鑑仍需轉譯 |
| 使用者控制 | 3 | 搜尋與選單可 Esc 關閉並返回焦點 |
| 一致與標準 | 3 | 內部文章與 GitHub 混用外連箭頭 |
| 錯誤預防 | 3 | 閱讀風險低，搜尋有標示與純文字結果 |
| 辨識優於回憶 | 2 | 主題／標籤／分類／歷程入口分散 |
| 效率與彈性 | 3 | 有全文搜尋與 `/` 捷徑；手機閱讀入口過低 |
| 美感與精簡 | 2 | 作者資訊、中繼資料、卡框與字幕重複 |
| 錯誤復原 | 3 | 空結果清楚；載入失敗重試僅讀原始碼，未誘發網路失敗實測 |
| 說明與引導 | 3 | 有三篇入門提示與 EXP 解釋；未說明各篇適合目的 |
| **合計** | **27 / 40** | **Acceptable，無 P0 阻斷** |

認知負荷：8 項檢核中，單一焦點、分塊、最少選項共 3 項未滿足，屬中度。
情緒路徑：營地帶來溫暖且可信的第一眼；接著大量重複作者資訊與文章卡增加翻找工作，手機閱讀低谷最明顯。

## 五個優先問題

| 優先度 | 問題與證據 | 對讀者的影響 | 修正方向 |
| --- | --- | --- | --- |
| 1・P1 | `layouts/home.html:16` 的個人 Hero 在 390×844 高 574px，首張精選 y=836；主要 CTA 是外部 GitHub | 首屏看不到文章標題，帶問題進站的人先經過自我介紹 | 縮短介紹，閱讀／搜尋成主要動作；營地縮為有辨識度的小景（adapt/layout） |
| 2・P2 | `layouts/home.html:23` 與 `layouts/_partials/rpg/featured-card.html`：三張精選約 1078px，最新清單 y=1902；DecimalFormat 重複出現 | 每篇相同重要性，反覆日期、時間與通用閱讀連結拖長頁面 | 精選分主次並交代選文用途；最新改文章列（distill） |
| 3・P2 | `layouts/_partials/rpg/sidebar.html:4` 的作者等級／EXP／數字排在次要閱讀入口之前 | 不容易直接選 Java／Spring／前端，手機選單更長 | 首頁提供少量真實主題路徑，角色面板精簡或移至關於頁（layout/clarify） |
| 4・P2 | `layouts/home.html:17` 重複職稱；前三篇全 Java，`content/about.md` 說 AI 應用與提示詞為後續探索 | 讀者看不到身分與目前內容的關聯 | 以現有內容定位，區分已公開主題與未來方向，不新增能力宣稱（clarify） |
| 5・P3 | 重複英文眉標、金線與圖示，多種圖像語言 | 裝飾未幫助區分原理、排錯與系列教學 | 精簡字幕，讓內容類型決定圖解／log／系列路徑（distill/typeset） |

## 兩個設計方向

### A．工程野帳（建議）

目的：讓繁中技術讀者快速讀到、判斷並重現一篇解法。

```text
精簡導覽／搜尋
一篇具體主打文章       小型營火／實作證據
最新文章列             兩篇相關精選入口
更新、摘要、主題        作者簡介
```

- 版型由主打與緊湊文章列構成；手機先見文章與閱讀入口。作者儀表板降為次要資訊。
- 保留中文襯線標題與清楚 sans 正文；等寬字只用於版本、指令、檔名、日期。
- 沿用既有淺色森林紙面 `#f7f8f4`、白色 `#ffffff`、正文 `#253021`、金 `#795922`、綠 `#426044`、框線 `#d9dfd3`；暗色沿用既有 token。
- 營火變成刊頭／頁尾簽名；主要圖像用真實程式輸出、流程與排錯資料。未有素材時不虛構截圖或結果。
- 文案說明現有 Java、Spring、前端實作，避免抽象身分口號。可提案「把原理與排錯，寫成可以重跑的筆記」，正式採用仍以文章的實際驗證範圍為準。
- 特點：精準、內容優先；風險是 RPG 敘事會比現況收斂。

### B．冒險路線圖

目的：陪讀者沿現有系列學習，讓 RPG 承擔實際導航。

```text
精簡導覽／搜尋
營地出發點：選擇閱讀路線
Java 入門    Spring 排錯    前端實作
章節與先備條件／可閱讀的線性連結
最新補充筆記／作者營地
```

- 首頁直接選真實路線；Java 00→01→02 等用已有系列關係，排錯按症狀→重現→修復組織。手機垂直章節。
- 主要操作與技術標題用 CJK sans；襯線留給敘事章節，mono 只作版本與有意義的節點序列。
- 沿用相同金綠 token 與明暗模式，區別來自閱讀結構，不靠換色。
- 營地成為出發點；原生 SVG 路徑需與文章關係相符，旁邊永遠有線性文字連結。不虛構讀者進度。
- 動作名稱如「從 JDK 環境開始」「排查連線逾時」，RPG 用語作副標。
- 特點：品牌與學習導航結合；風險是需要逐條確認跨技術路線，不能把無先後的三篇精選假設為課程。

兩案皆左對齊、保留少量字體與語意色、不新增無用途動態效果。A 首屏是一篇值得讀的筆記，B 首屏是一條可開始的路線。

## Persona 與次要發現

- 手機讀者 Casey：首屏看不到文章；頂部三個控制為 34×40px、間隔 4px，應改善命中區。
- 工程師 Alex：搜尋有效，但手機入口只見小圖示，精選與最新重複；希望直接看到問題詞與主題。
- 初學者 Jordan：多型、連線池、精度不是同一條入門順序，「從三篇開始」未說選文目的。
- 站內卡片 ↗ 與外部 GitHub 箭頭語意混淆。
- Vercel 檢視：`static/css/rpg-portfolio.css:136` 窄螢幕控制目標偏小；`layouts/_partials/rpg/search.html:2` 搜尋 input 缺少 `name`；標題未採平衡換行。這些是後續修正項，未假稱已修復。

## 機械檢查與證據界線

- Impeccable CLI 對 `layouts/home.html` 執行一次，JSON：`/tmp/blog-design-before-detector.json`。
- 1 個 `flat-type-hierarchy` warning，位置為 aggregate line 0，不是可定位程式行。
- 掃描稱 body/h1/h2/h3 均 16px；瀏覽器實際為 body 16、h1 30.72、h2 23、h3 17px，相鄰比值超過 1.25。判定為獨立 Hugo 模板掃描未讀到外部 CSS 的誤判。
- detector 原始結束碼未獨立保存；外層輸出 JSON 的命令 0 不能當成 detector clean。
- CUA evaluate 為唯讀，未注入 overlay、未啟動 live-server。沒有宣稱存在可見的檢測覆層。
- A/B 先隔離評估，A 完成後 B 才回傳 findings。各自臨時 tab 已關閉。
- 實看桌面 1280×720、1440×1000 及手機 390×844。已操作手機選單、Hikari 命中、空搜尋、Esc 關閉與焦點返回。
- 持久截圖位於 `/Users/ian/.codex/visualizations/2026/10/17/01a14a0a-ad65-7563-8a61-12521e3c05c9/blog-design/before-desktop.jpg` 與同目錄 `before-mobile.jpg`，均為修改前畫面。
- 未測實體手機、VoiceOver 完整流程、200% 縮放與雙主題對比；不宣稱完整無障礙通過。
- 網站統一驗證結果以交付回覆及 task 紀錄列出的 report 為準；本輪不重跑文章全部技術範例。

## 待確認的實作決策

1. 採 A 工程野帳，或 B 冒險路線圖？
2. 首頁作者等級與 EXP 保留精簡版，或移至關於頁？

這兩項直接影響首頁層級；依 Impeccable critique 在 3 個以上優先問題時必須詢問方向的規則，實作暫停於此決策。
