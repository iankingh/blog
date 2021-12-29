---
title: "JavaScript 實作簡易網頁表格資料搜尋與篩選功能 "
date: 2021-03-16T10:02:22+08:00
draft: true
categories:
 - "xx"
tags:
 - "xxx"
 - "xxx"
toc: true
---

## JavaScript 實作簡易網頁表格資料搜尋與篩選功能 
<!-- 簡介 -->
<!--more-->


```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        (function (document) {
            'use strict';
            // 建立 LightTableFilter
            var LightTableFilter = (function (Arr) {
                var _input;
                // 資料輸入事件處理函數
                function _onInputEvent(e) {
                    _input = e.target;
                    var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
                    Arr.forEach.call(tables, function (table) {
                        Arr.forEach.call(table.tBodies, function (tbody) {
                            Arr.forEach.call(tbody.rows, _filter);
                        });
                    });
                }
                // 資料篩選函數，顯示包含關鍵字的列，其餘隱藏
                function _filter(row) {
                    var text = row.textContent.toLowerCase();
                    var val = _input.value.toLowerCase();
                    row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
                    Arr.forEach.call(row.cells, _filter_cells);
                }
                // 資料篩選函數，顯示包含關鍵字的行，其餘隱藏
                function _filter_cells(cells) {
                    var text = cells.textContent.toLowerCase();
                    var val = _input.value.toLowerCase();
                    cells.style.display = text.indexOf(val) === -1 ? 'none' : 'table-cell';
                }
                return {
                    // 初始化函數
                    init: function () {
                        var inputs = document.getElementsByClassName('light-table-filter');
                        Arr.forEach.call(inputs, function (input) {
                            input.oninput = _onInputEvent;
                        });
                    }
                };

            })(Array.prototype);
            // 網頁載入完成後，啟動 LightTableFilter
            document.addEventListener('readystatechange', function () {
                if (document.readyState === 'complete') {
                    LightTableFilter.init();
                }
            });
        })(document);

    </script>

    搜尋：<input type="search" class="light-table-filter" data-table="order-table" placeholder="請輸入關鍵字">

    <table class="order-table" border="1">
        <tbody>
            <tr>
                <td>004 臺灣銀行 <button>選我</button></td>
                <td>005 土地銀行 <button>選我</button></td>
                <td>006 合庫商銀 <button>選我</button></td>
            </tr>
            <tr>
                <td>007 第一銀行 <button>選我</button></td>
                <td>008 華南銀行 <button>選我</button></td>
                <td>009 彰化銀行 <button>選我</button></td>
            </tr>
            <tr>
                <td>011 上海銀行 <button>選我</button></td>
                <td>012 台北富邦 <button>選我</button></td>
                <td>013 國泰世華 <button>選我</button></td>
            </tr>
            <tr>
                <td>016 高雄銀行 <button>選我</button></td>
                <td>017 兆豐商銀 <button>選我</button></td>
                <td>018 農業金庫 <button>選我</button></td>
            </tr>
        </tbody>
    </table>
</body>



</html>

```


## 參考
JavaScript 實作簡易網頁表格資料搜尋與篩選功能 - G. T. Wang
https://blog.gtwang.org/web-development/light-javascript-table-filter-tutorial/
