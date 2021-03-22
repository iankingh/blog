---
title: "HiddenBtnByprint"
date: 2021-03-16T09:51:39+08:00
draft: true
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
---

## hiddenBtnByprint 筆記
<!-- 簡介 -->
<!--more-->


```html
<div media="print">
    <table style="margin-left:auto; margin-right:auto;" width="100%">
        <td>
            <center>

                <input id="print_button" type="button" value="列印" onClick="print_the_page()" />
            </center>
        </td>
    </table>
</div>
<Script language="JavaScript">

    function print_the_page() {
        document.getElementById("print_button").style.visibility = "hidden";    //顯示按鈕
        javascript: print();
        document.getElementById("print_button").style.visibility = "visible";   //不顯示按鈕
    }
</Script>
```



## 參考

https://awpluway.pixnet.net/blog/post/361202835
