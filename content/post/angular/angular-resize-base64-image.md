---
title: "Angular 圖片縮放：Canvas 與型別化 Service"
date: 2021-03-12T09:28:08+08:00
categories:
 - "筆記"
tags:
 - "Angular"
 - "Base64"
toc: true
draft: false
description: "補上比例計算、載入錯誤與空 context 處理，區分縮放和格式轉換。"
lastmod: 2026-10-07T00:01:00+08:00
---

補上比例計算、載入錯誤與空 context 處理，區分縮放和格式轉換。

<!--more-->

適用：Angular原有NgModule專案的設計情境；新程式片段採Angular20 standalone方式，舊版差異另列。先使用與專案相容的Node／TypeScript。

## 可重用 service

適用瀏覽器DOM，不可直接在SSR執行。新增image.service.ts：

```typescript
import { Injectable } from '@angular/core';
@Injectable({ providedIn: 'root' })
export class ImageService {
  resize(src: string, maxWidth: number, maxHeight: number): Promise<string> {
    if (!(Number.isFinite(maxWidth) && Number.isFinite(maxHeight) && maxWidth > 0 && maxHeight > 0)) {
      return Promise.reject(new Error('尺寸必須為正數'));
    }
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.onload = () => {
        try {
          const ratio = Math.min(maxWidth / image.width, maxHeight / image.height, 1);
          const canvas = document.createElement('canvas');
          canvas.width = Math.max(1, Math.round(image.width * ratio));
          canvas.height = Math.max(1, Math.round(image.height * ratio));
          const context = canvas.getContext('2d');
          if (!context) throw new Error('無法建立Canvas');
          context.fillStyle = '#fff';
          context.fillRect(0, 0, canvas.width, canvas.height);
          context.drawImage(image, 0, 0, canvas.width, canvas.height);
          resolve(canvas.toDataURL('image/jpeg', 0.85));
        } catch (error) { reject(error); }
      };
      image.onerror = () => reject(new Error('圖片載入失敗'));
      image.src = src;
    });
  }
}
```

注入service後await resize(dataUrl,100,100)，將結果給img的src並catch錯誤。以200×100圖測試應為100×50，50×50圖保持50×50；此例不放大。JPEG不支援透明，先鋪白底。

## 限制與確認

這是畫素縮放與重新編碼，不保證檔案更小；大型base64與Canvas會佔記憶體，檔案傳輸可考慮toBlob。遠端圖未允許CORS時canvas可能被汙染而無法匯出，應由合法來源或本機File資料測試，不繞過瀏覽器限制。

手機相片的EXIF方向、色彩與HEIC格式另需測，不能把可載入JPEG的示例稱為所有格式轉換器。驗證輸出MIME、寬高、背景與視覺品質，同時測無效src和尺寸錯誤。

## 查核範圍

Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出）。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Canvas toDataURL](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL)
- [Canvas CORS](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)

### 原始筆記保留的來源

- [typescript - how to resize base64 image in angular - Stack Overflow](https://stackoverflow.com/questions/56967991/how-to-resize-base64-image-in-angular)
- [angular7中實現圖片上傳、圖片壓縮、圖片裁剪功能_yw00yw的部落格-CSDN部落格](https://blog.csdn.net/yw00yw/article/details/90450000)
