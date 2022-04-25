---
title: "Heic2any"
date: 2021-06-28T04:22:43+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
 - "Heic2any"
toc: true
---

## Heic2any 使用筆記
<!-- 簡介 -->

客戶端（瀏覽器端，使用 Javascript）將HEIC/HEIF圖像文件轉換為 JPEG、PNG 或 GIF。
<!--more-->

範例環境：

- chrome
- heic2any.js


```javaScript

    // 引用heic2any.js 
    <script src="./heic2any.js"></script>

    <script language="javascript">

        function readFile(fileDOM) {
            console.log('getImgURL input fileDOM' + fileDOM);
            const frontendFile = fileDOM.files[0]; // 獲取檔案
            heicConvertJpg(frontendFile)
        }

        function heicConvertJpg(file) {
            const showImage = document.getElementById("showImage");
            console.log('getImgURL input file' + file);
            // 轉成 Blob
            heic2any({
                // required: the HEIF blob file
                blob: file,
                // (optional) MIME type of the target file
                // it can be "image/jpeg", "image/png" or "image/gif"
                // defaults to "image/png"
                toType: 'image/jpeg',
                // conversion quality
                // a number ranging from 0 to 1
                quality: 0.5
            }).then((conversionResult) => {
                console.log('conversionResult: ' + conversionResult);
                getFileBase64Encode(conversionResult).then(
                    // b64 => console.log(b64),
                    b64 => showImage.src = b64
                );
            })
        }
        // 
        function getFileBase64Encode(blob) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(blob);
                reader.onload = () => resolve(reader.result);
                reader.onerror = error => reject(error);
            });
        }

    </script>

```

```html
    <img id="showImage" src="" alt="" style="border:2px green dashed;" width="300" height="300">
	<br>
	<input type="file" onchange="readFile(this)" value="readImage" />

```



## 參考

[Heic2any: Client-side conversion of HEIC/HEIF image files to JPEG, PNG, or GIF in the browser.](https://alexcorvi.github.io/heic2any/)