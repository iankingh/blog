---
title: "HEIC 轉 JPEG：heic2any 的載入、錯誤與輸出限制"
date: 2021-06-28T04:22:43+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
 - "Heic2any"
toc: true
description: "補上 Blob 陣列、錯誤處理與 object URL 清理，區分圖片轉換和 metadata 保留。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上 Blob 陣列、錯誤處理與 object URL 清理，區分圖片轉換和 metadata 保留。

<!--more-->

適用：支援ES2015以上的現代瀏覽器。HTML範例存成獨立檔案，以本地HTTP服務開啟；程式碼僅供讀者複製，不在部落格頁面執行。

## 瀏覽器範例

在Vite等前端專案安裝並固定heic2any版本，HTML放file input、img與status，再以module匯入。主要處理碼：

```javascript
import heic2any from 'heic2any';
const input = document.querySelector('#file');
const image = document.querySelector('#preview');
const status = document.querySelector('#status');
let currentUrl;
input.addEventListener('change', async () => {
  const file = input.files?.[0];
  if (!file) return;
  input.disabled = true;
  status.textContent = '轉換中';
  try {
    const converted = await heic2any({ blob: file, toType: 'image/jpeg', quality: 0.8 });
    const blob = Array.isArray(converted) ? converted[0] : converted;
    if (!(blob instanceof Blob)) throw new Error('沒有可用的輸出');
    if (currentUrl) URL.revokeObjectURL(currentUrl);
    currentUrl = URL.createObjectURL(blob);
    image.src = currentUrl;
    status.textContent = `JPEG ${blob.size} bytes`;
  } catch (error) { status.textContent = `轉換失敗：${error.message}`; }
  finally { input.disabled = false; }
});
window.addEventListener('pagehide', () => { if (currentUrl) URL.revokeObjectURL(currentUrl); });
```

HTML對應片段：

```html
<label>HEIC 圖片 <input id="file" type="file" accept=".heic,.heif"></label>
<img id="preview" alt="轉換後的圖片預覽"><p id="status" role="status"></p>
```

## 確認與限制

選擇合法HEIC應顯示JPEG預覽，錯誤檔應顯示失敗並恢復input。accept只是選擇提示，不驗證內容；多影像檔可能回Blob陣列，此例只展示第一張，不能宣稱保留所有影格。

套件不保證保留EXIF／metadata，方向、色彩和高解析度記憶體需用實際來源樣本檢查。沒有提供HEIC樣本時只能核對API與流程，不能宣稱已解碼所有手機相片。遠端載入還需CORS；離線轉換不等於零記憶體成本。需要metadata或後端大批處理時評估有明確格式支援的服務／原生工具。

## 查核範圍

本文事件流程以假 Blob／轉換器測單張、陣列、錯誤、input 恢復與 URL 清理；未提供 HEIC 樣本，未驗證真實解碼、方向、色彩或 metadata。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [heic2any 官方](https://alexcorvi.github.io/heic2any/)
- [原始碼與限制](https://github.com/alexcorvi/heic2any)
- [object URL](https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL_static)
