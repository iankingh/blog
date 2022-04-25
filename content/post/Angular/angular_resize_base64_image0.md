---
title: "angular Resize_base64_image"
date: 2021-03-12T09:28:08+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
<<<<<<< HEAD:content/post/Angular/resize_base64_image_in_angular.md
 - "Base64"
toc: true
---

## Anguarl 調整 Base64 圖片大小筆記
<!--more-->

## 方法 1  新增方法至 component 

```typescript
=======
toc: true
---

## 還沒寫完


## Anguarl 調整 Base64 圖片大小

<!--more-->

## 方法 1

新增方法至 component

```javascript
>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6:content/post/Angular/angular_resize_base64_image0.md
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

<<<<<<< HEAD:content/post/Angular/resize_base64_image_in_angular.md
```typescript
=======
```javascript
>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6:content/post/Angular/angular_resize_base64_image0.md
compressImage(base64, 100, 100).then(compressed => {
  this.resizedBase64 = compressed;
})
```

## 方法 2 新增一個Service


<<<<<<< HEAD:content/post/Angular/resize_base64_image_in_angular.md

## 參考
=======
## 參考

>>>>>>> c4b992a9871c491fe1e8b2b832c0a5b358c4bdf6:content/post/Angular/angular_resize_base64_image0.md
typescript - how to resize base64 image in angular - Stack Overflow
https://stackoverflow.com/questions/56967991/how-to-resize-base64-image-in-angular

angular7中实现图片上传、图片压缩、图片裁剪功能_yw00yw的博客-CSDN博客
https://blog.csdn.net/yw00yw/article/details/90450000
