---
title: "行動裝置偵測：以版面與功能能力取代 UA 猜測"
date: 2021-03-15T09:20:44+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
description: "保留 userAgent 比對的歷史情境，補上 matchMedia、觸控與鍵盤測試的限制。"
lastmod: 2026-10-07T00:01:00+08:00
---

保留 userAgent 比對的歷史情境，補上 matchMedia、觸控與鍵盤測試的限制。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 先問需要偵測什麼

原函式查userAgent是否含Android/iPhone等名稱，只能猜測瀏覽器宣告，可能漏掉iPad桌面模式、可偽裝UA與新裝置。RWD應根據viewport，互動根據實際功能，而非用單一isMobile切所有流程。

```html
<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>裝置能力</title>
<p id="result" role="status"></p>
<script>
const narrow = matchMedia('(max-width: 640px)');
const coarse = matchMedia('(pointer: coarse)');
function update() {
  document.querySelector('#result').textContent = `窄版：${narrow.matches}；主要指標粗略：${coarse.matches}`;
}
narrow.addEventListener('change', update);
coarse.addEventListener('change', update);
update();
</script></html>
```

縮小視窗至640以下窄版true，寬視窗false；pointer結果依裝置，不必與窄版相同。筆電也可能觸控，手機可接滑鼠，偵測不能證明使用者沒有鍵盤。

## 使用原則

純佈局用CSS media query，處理能力先feature detection。粗略pointer可用於加大點選目標，但所有控制仍支援鍵盤與合理focus。若業務確需裝置分類，定義允許誤判範圍並保留server/client的降級流程，不把UA判斷用於安全或支付授權。

舊瀏覽器的MediaQueryList使用addListener，維護時依實際支援範圍處理；現代例子採addEventListener，不宣稱適用IE11。

## 查核範圍

本文 HTML 在 jsdom 以 matchMedia fixture 測初始輸出與 change 事件；未辨識實際手機硬體。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [避免UA偵測](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Browser_detection_using_the_user_agent)
- [matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)
- [pointer](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/pointer)

### 原始筆記保留的來源

- [原行動裝置偵測筆記（修正原網址末尾的逗號）](https://tso1158687.github.io/blog/2019/03/10/detect-mobile-device/)
