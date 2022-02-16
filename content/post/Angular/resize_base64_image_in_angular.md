---
title: "Resize_base64_image_in_angular"
date: 2021-03-12T09:28:08+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "Base64"
toc: true
---

## Anguarl 調整 Base64 圖片大小筆記
<!--more-->

## 方法 1  新增方法至 component 

```typescript
  /**
   * 縮放圖片的方法
   * @param src 圖片
   * @param newX
   * @param newY
   * @returns
   */
  compressImage(src, newX, newY) {
    return new Promise((res, rej) => {
      const img = new Image();
      img.src = src;
      img.onload = () => {
        const elem = document.createElement('canvas');
        elem.width = newX;
        elem.height = newY;
        const ctx = elem.getContext('2d');
        ctx.drawImage(img, 0, 0, newX, newY);
        const data = ctx.canvas.toDataURL('image/jpeg');
        res(data);
      };
      img.onerror = error => rej(error);
    });
  }
```

call 方法

```typescript
compressImage(base64, 100, 100).then(compressed => {
  this.resizedBase64 = compressed;
})
```

## 方法 2 新增一個Service



## 參考
typescript - how to resize base64 image in angular - Stack Overflow
https://stackoverflow.com/questions/56967991/how-to-resize-base64-image-in-angular

angular7中实现图片上传、图片压缩、图片裁剪功能_yw00yw的博客-CSDN博客
https://blog.csdn.net/yw00yw/article/details/90450000
