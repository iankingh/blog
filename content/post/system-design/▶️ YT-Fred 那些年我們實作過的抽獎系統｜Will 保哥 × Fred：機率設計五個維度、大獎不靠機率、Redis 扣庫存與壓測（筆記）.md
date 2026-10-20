---
title: "▶️ YT-Fred 那些年我們實作過的抽獎系統｜Will 保哥 × Fred：機率設計五個維度、大獎不靠機率、Redis 扣庫存與壓測（筆記）"
slug: fred-lottery-system
date: 2026-10-20
lastmod: 2026-10-20T21:35:29+08:00
description: "從五個需求維度整理抽獎活動，區分機率、獎品上限與放獎節奏，並說明 Redis 扣庫存、冪等與壓測的邊界。"
categories: ["筆記"]
tags: ["系統設計", "Redis", "高併發"]
toc: true
draft: false
---

抽獎系統的第一個問題，是活動想換得什麼業務成果。這篇整理 Will 保哥與 Fred 對五個需求維度、大獎放獎節奏、小獎機率、庫存競態與容量規劃的討論，並補上機率與系統保證的邊界。

<!--more-->

適用：接觸行銷活動、即時抽獎、秒殺或系統設計的工程師。本文依既有影片筆記重新整理；影片中的歷史活動與假設數字不代表現行服務規格。時間連結沿用原筆記，未重新逐段觀看影片核對。

## 這部影片是什麼

### 來源：[那些年我們實作過的抽獎系統](https://www.youtube.com/watch?v=e3DDXSMWr5w)

- **來賓**：林世鵬（Fred），當時是**街口支付**技術團隊負責人，曾任阿里巴巴技術專家；說明欄提到他負責的系統在 2019 年雙 11 扛過每秒 65 萬筆訂單的峰值。也就是 [Fred 聊 SOLID 設計原則｜五個原則環環相扣：SRP 是前提、OCP 是目標、DIP 是做法，LSP 與 ISP 守住介面（筆記）]({{< ref "post/software-design/▶️ YT-Fred 聊 SOLID 設計原則｜五個原則環環相扣：SRP 是前提、OCP 是目標、DIP 是做法，LSP 與 ISP 守住介面（筆記）.md" >}}) 的講者。
- **緣起**：保哥的 LINE 技術社群前一週在討論抽獎系統，大家發現「水很深、地雷很多、很容易做錯」，於是請 Fred 分享實戰經驗 [0:17](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=17s)。
- **想回答的問題**：抽獎系統在業務上扮演什麼角色？中獎機率要怎麼設計才不會送爆？系統上要注意哪些風險？
- **核心觀點**：抽獎一定要跟業務目標綁在一起；產品端給的「機率」常常是被過度簡化的需求，工程師要用五個維度幫忙把模型釐清。
- **適合誰**：要接行銷活動、抽獎、秒殺、搶福袋需求的後端工程師；準備系統設計面試的人。
- **注意事項**：內容由語音辨識整理，可能有少數字詞誤差。直播口語化，前 31 分鐘是 Fred 主講，後面是問答。案例來自街口 2021 年雙 11 活動，實際數字（DAU、iPhone 台數）講者刻意用假設值帶過。內容是 2022 年的經驗，提到的時事（丁特事件、尾牙抽獎爭議）。

分享者為 **Will 保哥與 Fred（林世鵬）**。下文「工程補充」及程式範例是另外整理的學習材料，不是影片逐字稿，也不代表講者使用的原始碼。

## 先掌握重點

1. **先定義活動目的。** 拉新、喚回舊使用者、提高交易頻率，會導向不同的規則與衡量方式。
2. **先釐清五個維度。** 活動週期、開獎方式、參與人數、抽獎次數、獎品數量。
3. **機率不能代替庫存與預算上限。** 固定數量的大獎，需要分配與發放規則；小獎的機率表也需要庫存和預算控制。
4. **抽獎結果要可重試、可追查。** 限流、資格、庫存、冪等與發獎紀錄要一起設計。
5. **壓測要驗證業務情境。** 達到目標流量、延遲與正確性，比單看 CPU 或最高 QPS 更有意義。

## 開發前先問：預算要換得什麼成果？

影片從 [03:23](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=203s) 說明，抽獎是行銷預算轉換成預期收益的一個管道。工程師除了實作畫面與亂數，還需要協助釐清活動是否能達到目標。

可先整理成一張需求單：

| 問題 | 需要確認的內容 |
| --- | --- |
| 活動目標 | 新註冊、回流、交易次數或其他可衡量的指標 |
| 成本邊界 | 獎品、優惠券、開發與營運成本；總額及每日上限 |
| 參與資格 | 身分、消費條件、每人可抽次數，以及退款後如何處理 |
| 發獎規則 | 何時決定結果、庫存何時扣除、得獎後如何領取 |
| 例外處理 | 重送、逾時、庫存不足、活動暫停與補償流程 |

目的與限制還沒有講清楚時，單獨決定「中獎率 1%」並不能構成可實作的規格。

## 用五個維度建立活動模型

影片 [08:01](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=481s) 的五個維度，可以拿來檢查需求中尚未確定的部分。

| 維度 | 要問的問題 | 對實作的影響 |
| --- | --- | --- |
| 活動週期 | 固定日期，還是持續到另行通知？ | 時區、開始與結束邊界、設定版本 |
| 開獎方式 | 每次立即知道，還是活動後統一公布？ | 即時交易，或先保存參與名單再抽選 |
| 抽獎人數 | 名單固定，還是任何合資格者都可加入？ | 能否先準備籤池、如何估流量 |
| 抽獎次數 | 每人一次，還是依消費累積？ | 次數帳本、重試與扣次數的時機 |
| 獎品數量 | 固定份數，還是依預算及條件決定？ | 庫存上限、每日配額與放獎節奏 |

例如「固定活動期間、立即開獎、參與人數未知、次數隨消費增加、大獎只有 10 份」，就不能只拿一次抽獎的機率去推估整場活動。

## 大獎：把機率、數量與發放節奏分開

### 期望值不是上限

影片 [14:11](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=851s) 用 iPhone 大獎說明固定機率的風險。沿用原筆記中的假設：10 萬次抽獎，每次獨立且中獎率都是 1%，預期中獎次數為：

```text
100,000 × 0.01 = 1,000 次
```

**工程補充：** 這是未加庫存限制的期望值，不是保證會送出 1,000 份，也不是送出數量的上限。若加上「發完即止」，可以限制總數，卻仍可能很早發完；庫存限制與發放節奏是兩個問題。

因此「大獎不靠機率」應放回影片情境理解：當抽獎次數未知、獎品稀少，又希望維持活動熱度時，不能只靠固定機率完成需求。它不表示所有大獎活動都必須採用同一種演算法。

### 放獎時間是一種活動規則

影片 [20:16](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=1216s) 提到，先依獎品數量與活動節奏分配每天的份額，再決定當天何時可被抽到。例如到達某個時間點後，由第一筆符合資格且成功取得名額的請求得獎。

這種做法仍須定義：

- 多個已到期名額累積時，一次請求最多取得幾份？
- 當天無人參加，名額延到隔天、活動結束統一處理，還是失效？
- 多個服務節點同時處理時，如何用原子條件更新保證同一名額只被認領一次？
- 誰能查閱或修改放獎時間？規則變更是否留下版本與稽核紀錄？

「時間點後先到先得」與「所有抽獎機會等機率」並不相同。對外規則、介面文案與實際程式必須一致；隨機產生時間點本身，也不能取代公平性與存取權限的設計。

## 小獎：從預算推導機率表

影片 [23:24](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=1404s) 以平台幣與優惠券說明小獎機率表。以下是**自行整理的假設資料**，不是街口支付的活動設定：

| 結果 | 權重 | 單次機率 | 簡化面額 |
| --- | ---: | ---: | ---: |
| 10 元獎勵 | 50 | 0.5% | 10 元 |
| 5 元獎勵 | 200 | 2% | 5 元 |
| 店家折價券 | 750 | 7.5% | 另依成本模型計算 |
| 未中獎 | 9,000 | 90% | 0 元 |
| 合計 | 10,000 | 100% | — |

若暫時只計前兩種獎勵面額，每次抽獎的期望支出為 `10 × 0.005 + 5 × 0.02 = 0.15 元`。實際成本還要考慮券的核銷條件、參與次數與活動規則；期望支出不能替代硬性的預算上限。

### Node.js 範例：加權選取與邊界

將以下完整程式存成 `weighted-draw.mjs`。使用 Node.js 內建的 `crypto.randomInt`，沒有外部套件；本次以 Node.js 26.5.0 執行。函式接受測試用的亂數索引，實際使用時省略引數。

```javascript
import { randomInt } from 'node:crypto';
import assert from 'node:assert/strict';

const table = [
  { prize: '10 元獎勵', weight: 50 },
  { prize: '5 元獎勵', weight: 200 },
  { prize: '店家折價券', weight: 750 },
  { prize: '未中獎', weight: 9000 },
];
const total = table.reduce((sum, row) => sum + row.weight, 0);

function draw(index = randomInt(total)) {
  if (!Number.isInteger(index) || index < 0 || index >= total) {
    throw new RangeError('index 超出機率表範圍');
  }
  let cumulative = 0;
  for (const row of table) {
    cumulative += row.weight;
    if (index < cumulative) return row.prize;
  }
  throw new Error('機率表不完整');
}

for (const [index, prize] of [
  [0, '10 元獎勵'], [49, '10 元獎勵'],
  [50, '5 元獎勵'], [249, '5 元獎勵'],
  [250, '店家折價券'], [999, '店家折價券'],
  [1000, '未中獎'], [9999, '未中獎'],
]) {
  assert.equal(draw(index), prize);
}
for (const invalid of [-1, 10000, 1.5, NaN]) {
  assert.throws(() => draw(invalid), RangeError);
}
assert.ok(table.some(row => row.prize === draw()));
console.log('PASS: 機率區間與無效輸入');
```

執行 `node weighted-draw.mjs`，預期輸出：

```text
PASS: 機率區間與無效輸入
```

`randomInt(total)` 的範圍是 `0 <= index < total`，因此每段區間使用上界不含的判斷；API 也避免取模偏差，見 [Node.js 文件](https://nodejs.org/api/crypto.html#cryptorandomintmin-max-callback)。這個範例只選結果，**沒有扣庫存、扣抽獎次數或發獎**。測試使用可控索引核對邊界，不以隨機跑幾次的分布來證明活動公平。

## 庫存：Redis 原子操作能解決哪一段？

影片 [27:28](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=1648s) 提醒，熱門活動要限制抽獎頻率、提早攔截已無名額的請求，並留意資料庫熱點與鎖競爭。

**工程補充：** 資料庫條件更新或交易並非不能使用；是否形成瓶頸，要看資料模型、熱點與壓測。Redis 可以縮短部分熱路徑，但不能直接推論任一 Redis 部署都一定比資料庫更適合，也不能把影片中的 QPS 經驗值當作通用容量。

下面沿用原筆記的 Redis Lua 概念：假設庫存 key 是非負整數字串，得獎者 key 是 set，每名使用者在該活動／獎項最多成功一次。

```lua
-- KEYS[1] = lottery:{demo}:stock
-- KEYS[2] = lottery:{demo}:winners
-- ARGV[1] = 已由後端完成身分與資格檢查的 userId
if redis.call('SISMEMBER', KEYS[2], ARGV[1]) == 1 then
  return -1
end
local stock = tonumber(redis.call('GET', KEYS[1]) or '0')
if not stock or stock <= 0 then
  return 0
end
redis.call('DECR', KEYS[1])
redis.call('SADD', KEYS[2], ARGV[1])
return 1
```

回傳 `1` 表示成功保留一份庫存，`0` 表示無庫存，`-1` 表示該使用者已成功過。這是 **Redis 內部的扣庫存示意**，本次沒有啟動 Redis 實測；使用前需初始化正確的 key 型別與庫存值，再測試成功、重複、無庫存及併發搶最後一份的情境。

依 [Redis Lua 文件](https://redis.io/docs/latest/develop/programmability/eval-intro/)，腳本執行期間不會與其他客戶端命令交錯，也會阻塞其他活動，應保持短小。原子執行不等於腳本錯誤時自動回滾，更不等於 Redis 與資料庫之間有共同交易。若採 Redis Cluster，多 key 操作還要符合 hash slot 限制；示意 key 共用 `{demo}` hash tag，見 [Cluster 規格](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)。

### 發獎仍需要一份可追查的帳本

扣庫存成功後，如果網路斷線、服務重啟，或寫入資料庫失敗，不能只靠「之後非同步寫回」六個字處理。完整流程還需要：

- **請求識別與冪等結果：** 同一抽獎請求重送時，回傳同一結果；「每人限中一次」與「每筆請求只執行一次」是不同限制。
- **持久化與對帳：** 保存請求、使用者、活動版本、獎項、狀態與時間，能查出庫存已扣但發獎未完成的紀錄。
- **可靠事件與重試：** 明確設計待發獎紀錄、事件投遞、消費去重、失敗重試及補償；不要假設兩個系統的寫入自然會一起成功。
- **容量與故障演練：** 把 Redis 的持久化、淘汰策略、切換與資料遺失風險納入測試；不從單一正常案例宣稱不超發或 exactly-once。

前端暫停按鈕有助於減少誤按，但真正的次數限制與資格檢查必須由後端執行。

## 容量估算與壓測：先有業務情境

影片 [31:32](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=1892s) 與 [39:52](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=2392s) 強調，容量不能只靠想像，需從使用者與推播等活動資料反推。

以下是另設的估算例子：30 萬位可觸及使用者，假設其中 10% 在 60 秒內進入，每人送出 2 次 API 請求，該分鐘的**平均**流量為：

```text
300,000 × 10% × 2 ÷ 60 = 1,000 requests/second
```

它不是瞬間尖峰的保證值。要再評估到達分布、重試、推播同時送達、其他 API 與各層設備的限制，並用與目標環境接近的路徑驗證。

| 情境 | 除了延遲與錯誤率，還要看什麼 |
| --- | --- |
| 一般負載與預期尖峰 | 達成目標吞吐量，結果帳本與庫存一致 |
| 最後一份獎品遭多人搶取 | 只有允許數量的請求成功，庫存不負數 |
| 同一請求逾時後重試 | 不再次扣次數或重複發獎，查得到原結果 |
| 庫存耗盡後仍有大量請求 | 能快速回應，不繼續壓垮資料庫 |
| 發獎服務故障或活動結束 | 失敗可重試、狀態可追查，時間邊界一致 |

測試前依業務需求訂定 p95／p99 延遲、錯誤率與正確性條件；k6 可用 [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) 把通過標準寫入測試。本文未執行活動服務壓測，也沒有提供可套用到正式環境的 QPS 或 CPU 門檻。

## 讓規則與系統都能被理解

影片 [47:37](https://www.youtube.com/watch?v=e3DDXSMWr5w&t=2857s) 回到公平性：規則越複雜，越需要說明、測試與稽核。不要把不透明的動態調整當成解決預算問題的方法。

可在實作前用這份清單對齊：

- 活動目的、五個維度與公開規則是否一致？
- 總庫存、每日配額、預算及參與次數是否都有上限？
- 規則變更、結果重送、故障補償是否有紀錄？
- 已到期但未領取的名額，以及活動結束的邊界如何處理？
- 壓測是否包含完整入口、重試與結果正確性，而不只測單支 API？

至於模組如何拆分，可以接著閱讀 [Fred 聊 SOLID 設計原則]({{< ref "post/software-design/▶️ YT-Fred 聊 SOLID 設計原則｜五個原則環環相扣：SRP 是前提、OCP 是目標、DIP 是做法，LSP 與 ISP 守住介面（筆記）.md" >}})：抽獎資格、獎項選取、庫存與發獎各有不同變更來源，適合用職責與契約檢查邊界。Redis 指令基礎可參考 [Redis 常用指令]({{< ref "post/redis/redis-command.md" >}})。

## 參考資料

- [Redis：Scripting with Lua](https://redis.io/docs/latest/develop/programmability/eval-intro/)
- [Redis Cluster specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
- [Node.js：crypto.randomInt](https://nodejs.org/api/crypto.html#cryptorandomintmin-max-callback)
- [Grafana k6：Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [原影片：那些年我們實作過的抽獎系統](https://www.youtube.com/watch?v=e3DDXSMWr5w)
- [Will 保哥：The Will Will Web](https://blog.miniasp.com/)
- [Apache JMeter](https://jmeter.apache.org/)、[Locust](https://locust.io/)：原筆記提到的其他壓測工具。
