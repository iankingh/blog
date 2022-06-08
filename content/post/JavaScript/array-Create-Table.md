---
title: "ArrayCreateTable"
date: 2021-03-16T09:55:35+08:00
draft: false
categories:
 - "筆記"
tags:
 - "JavaScript"
toc: true
---

## JavaScript利用ArrayCreateTable筆記
<!-- 簡介 -->
<!--more-->

``` html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $(document).ready(function () {
            var jsonData = '[{"BANK_ID":"005","BRANCH_NAME":"臺灣土地銀行","BRANCH_NICKNAME":"土銀"},{"BANK_ID":"006","BRANCH_NAME":"合金庫商業銀行","BRANCH_NICKNAME":"合庫商銀"},{"BANK_ID":"007","BRANCH_NAME":"第商業銀行","BRANCH_NICKNAME":"銀"},{"BANK_ID":"008","BRANCH_NAME":"華南商業銀行","BRANCH_NICKNAME":"華銀"},{"BANK_ID":"009","BRANCH_NAME":"彰化商業銀行","BRANCH_NICKNAME":"彰銀"},{"BANK_ID":"011","BRANCH_NAME":"上海商業儲蓄銀行","BRANCH_NICKNAME":"上銀"},{"BANK_ID":"012","BRANCH_NAME":"台北富邦商業銀行","BRANCH_NICKNAME":"北富銀"},{"BANK_ID":"013","BRANCH_NAME":"國泰華商業銀行","BRANCH_NICKNAME":"國銀"},{"BANK_ID":"016","BRANCH_NAME":"高雄銀行","BRANCH_NICKNAME":"高銀"},{"BANK_ID":"017","BRANCH_NAME":"兆豐國際商業銀行","BRANCH_NICKNAME":"兆豐銀"},{"BANK_ID":"018","BRANCH_NAME":"全國農業金庫","BRANCH_NICKNAME":"農業金庫"},{"BANK_ID":"020","BRANCH_NAME":"日商瑞穗實業銀行台北分行","BRANCH_NICKNAME":"瑞實銀行"},{"BANK_ID":"021","BRANCH_NAME":"花旗（台灣）商業銀行","BRANCH_NICKNAME":"花旗台灣"},{"BANK_ID":"022","BRANCH_NAME":"美國銀行台北分行","BRANCH_NICKNAME":"美銀台北"},{"BANK_ID":"023","BRANCH_NAME":"泰國盤谷銀行台北分行","BRANCH_NICKNAME":"盤谷台北"},{"BANK_ID":"025","BRANCH_NAME":"菲律賓首都銀行台北分行","BRANCH_NICKNAME":"首都台北"},{"BANK_ID":"039","BRANCH_NAME":"澳商澳盛銀行","BRANCH_NICKNAME":"澳盛銀行"},{"BANK_ID":"040","BRANCH_NAME":"中華開發工業銀行","BRANCH_NICKNAME":"開發銀行"},{"BANK_ID":"048","BRANCH_NAME":"台灣工業銀行","BRANCH_NICKNAME":"台灣工銀"},{"BANK_ID":"050","BRANCH_NAME":"臺灣中小企業銀行","BRANCH_NICKNAME":"臺企"},{"BANK_ID":"052","BRANCH_NAME":"渣打國際商業銀行","BRANCH_NICKNAME":"渣商銀"},{"BANK_ID":"053","BRANCH_NAME":"台中商業銀行","BRANCH_NICKNAME":"台中銀"},{"BANK_ID":"054","BRANCH_NAME":"京城商業銀行","BRANCH_NICKNAME":"京城銀行"},{"BANK_ID":"060","BRANCH_NAME":"兆豐票券金融股份有限公司","BRANCH_NICKNAME":"豐票"},{"BANK_ID":"061","BRANCH_NAME":"中華票券金融股份有限公司","BRANCH_NICKNAME":"華票"},{"BANK_ID":"062","BRANCH_NAME":"國際票券金融股份有限公司","BRANCH_NICKNAME":"國票"},{"BANK_ID":"066","BRANCH_NAME":"萬通票券金融股份有限公司","BRANCH_NICKNAME":"萬票"},{"BANK_ID":"072","BRANCH_NAME":"德商德意志銀行台北分行","BRANCH_NICKNAME":"德銀台北"},{"BANK_ID":"075","BRANCH_NAME":"香港商東亞銀行台北分行","BRANCH_NICKNAME":"東亞銀行"},{"BANK_ID":"076","BRANCH_NAME":"美商摩根大通銀行台北分行","BRANCH_NICKNAME":"摩根大通銀"},{"BANK_ID":"078","BRANCH_NAME":"新加坡商星展銀行台北分行","BRANCH_NICKNAME":"星展銀行"},{"BANK_ID":"081","BRANCH_NAME":"匯豐（台灣）商業銀行","BRANCH_NICKNAME":"匯豐台灣"},{"BANK_ID":"082","BRANCH_NAME":"法國巴黎銀行台北分行","BRANCH_NICKNAME":"巴黎銀行"},{"BANK_ID":"085","BRANCH_NAME":"新加坡商新加坡華僑銀行台北分行","BRANCH_NICKNAME":"新僑銀行"},{"BANK_ID":"086","BRANCH_NAME":"法商東方匯理銀行台北分行","BRANCH_NICKNAME":"東方匯理"},{"BANK_ID":"092","BRANCH_NAME":"瑞士商瑞士銀行台北分行","BRANCH_NICKNAME":"瑞士銀行"},{"BANK_ID":"093","BRANCH_NAME":"荷商安智銀行台北分行","BRANCH_NICKNAME":"安智銀行"},{"BANK_ID":"098","BRANCH_NAME":"日商三菱東京日聯銀行台北分行","BRANCH_NICKNAME":"三菱日聯"},{"BANK_ID":"101","BRANCH_NAME":"大台北商業銀行","BRANCH_NICKNAME":"大台北銀行"},{"BANK_ID":"102","BRANCH_NAME":"華泰商業銀行","BRANCH_NICKNAME":"華泰銀行"},{"BANK_ID":"103","BRANCH_NAME":"臺灣新光商業銀行","BRANCH_NICKNAME":"新光銀行"},{"BANK_ID":"104","BRANCH_NAME":"台北市第五信用合社","BRANCH_NICKNAME":"北五"},{"BANK_ID":"106","BRANCH_NAME":"台北市第九信用合社","BRANCH_NICKNAME":"北九"},{"BANK_ID":"108","BRANCH_NAME":"陽信商業銀行","BRANCH_NICKNAME":"陽信銀行"},{"BANK_ID":"114","BRANCH_NAME":"基隆第信用合社","BRANCH_NICKNAME":"基"},{"BANK_ID":"115","BRANCH_NAME":"基隆市第二信用合社","BRANCH_NICKNAME":"基二"},{"BANK_ID":"118","BRANCH_NAME":"板信商業銀行","BRANCH_NICKNAME":"板信銀行"},{"BANK_ID":"119","BRANCH_NAME":"淡水第信用合社","BRANCH_NICKNAME":"淡"},{"BANK_ID":"120","BRANCH_NAME":"台北縣淡水信用合社","BRANCH_NICKNAME":"淡信"},{"BANK_ID":"124","BRANCH_NAME":"宜蘭信用合社","BRANCH_NICKNAME":"宜信"},{"BANK_ID":"127","BRANCH_NAME":"桃園縣桃園信用合社","BRANCH_NICKNAME":"桃信"},{"BANK_ID":"130","BRANCH_NAME":"新竹第信用合社","BRANCH_NICKNAME":"竹"},{"BANK_ID":"132","BRANCH_NAME":"新竹第三信用合社","BRANCH_NICKNAME":"竹三"},{"BANK_ID":"139","BRANCH_NAME":"竹南信用合社","BRANCH_NICKNAME":"竹南信"},{"BANK_ID":"146","BRANCH_NAME":"台中市第二信用合社","BRANCH_NICKNAME":"中二"},{"BANK_ID":"147","BRANCH_NAME":"三信商業銀行","BRANCH_NICKNAME":"三信銀行"},{"BANK_ID":"158","BRANCH_NAME":"彰化第信用合社","BRANCH_NICKNAME":"彰"},{"BANK_ID":"161","BRANCH_NAME":"彰化第五信用合社","BRANCH_NICKNAME":"彰五"},{"BANK_ID":"162","BRANCH_NAME":"彰化第六信用合社","BRANCH_NICKNAME":"彰六"},{"BANK_ID":"163","BRANCH_NAME":"彰化第十信用合社","BRANCH_NICKNAME":"彰十"},{"BANK_ID":"165","BRANCH_NAME":"彰化縣鹿港信用合社","BRANCH_NICKNAME":"鹿信"},{"BANK_ID":"178","BRANCH_NAME":"嘉義市第三信用合社","BRANCH_NICKNAME":"嘉三"},{"BANK_ID":"179","BRANCH_NAME":"嘉義市第四信用合社","BRANCH_NICKNAME":"嘉四"},{"BANK_ID":"188","BRANCH_NAME":"台南第三信用合社","BRANCH_NICKNAME":"南三"},{"BANK_ID":"204","BRANCH_NAME":"高雄市第三信用合社","BRANCH_NICKNAME":"高三"},{"BANK_ID":"215","BRANCH_NAME":"花蓮第信用合社","BRANCH_NICKNAME":"花"},{"BANK_ID":"216","BRANCH_NAME":"花蓮第二信用合社","BRANCH_NICKNAME":"花二"},{"BANK_ID":"222","BRANCH_NAME":"澎湖縣第信用合社","BRANCH_NICKNAME":"澎"},{"BANK_ID":"223","BRANCH_NAME":"澎湖第二信用合社","BRANCH_NICKNAME":"澎二"},{"BANK_ID":"224","BRANCH_NAME":"金門縣信用合社","BRANCH_NICKNAME":"金門"},{"BANK_ID":"321","BRANCH_NAME":"日商三井住友銀行台北分行","BRANCH_NICKNAME":"三井住友"},{"BANK_ID":"372","BRANCH_NAME":"大慶票券金融股份有限公司","BRANCH_NICKNAME":"大慶票券"},{"BANK_ID":"503","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"504","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"505","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"506","BRANCH_NAME":"聯資中心所屬會員","BRANCH_NICKNAME":"聯資中心"},{"BANK_ID":"507","BRANCH_NAME":"聯資中心所屬會員","BRANCH_NICKNAME":"聯資中心"},{"BANK_ID":"512","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"515","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"517","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"518","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"520","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"521","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"523","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"524","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"525","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"603","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"605","BRANCH_NAME":"高雄市農會","BRANCH_NICKNAME":"高農"},{"BANK_ID":"606","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"607","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"608","BRANCH_NAME":"聯資中心所屬會員","BRANCH_NICKNAME":"聯資中心"},{"BANK_ID":"609","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"610","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"611","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"612","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"613","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"614","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"616","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"617","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"618","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"619","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"620","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"621","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"622","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"623","BRANCH_NAME":"北農中心所屬會員","BRANCH_NICKNAME":"北農中心"},{"BANK_ID":"624","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"625","BRANCH_NAME":"台中市農會","BRANCH_NICKNAME":"中市農"},{"BANK_ID":"627","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"700","BRANCH_NAME":"中華郵政股份有限公司","BRANCH_NICKNAME":"郵政公司"},{"BANK_ID":"803","BRANCH_NAME":"聯邦商業銀行","BRANCH_NICKNAME":"聯邦銀行"},{"BANK_ID":"805","BRANCH_NAME":"遠東國際商業銀行","BRANCH_NICKNAME":"遠東銀行"},{"BANK_ID":"806","BRANCH_NAME":"元大商業銀行","BRANCH_NICKNAME":"元大銀行"},{"BANK_ID":"807","BRANCH_NAME":"永豐商業銀行","BRANCH_NICKNAME":"永豐銀行"},{"BANK_ID":"808","BRANCH_NAME":"玉山商業銀行","BRANCH_NICKNAME":"玉山銀行"},{"BANK_ID":"809","BRANCH_NAME":"萬泰商業銀行","BRANCH_NICKNAME":"萬泰銀行"},{"BANK_ID":"810","BRANCH_NAME":"星展銀行－原寶華銀行","BRANCH_NICKNAME":"星展寶華銀"},{"BANK_ID":"812","BRANCH_NAME":"台新國際商業銀行","BRANCH_NICKNAME":"台新銀行"},{"BANK_ID":"814","BRANCH_NAME":"大眾商業銀行","BRANCH_NICKNAME":"大眾銀行"},{"BANK_ID":"815","BRANCH_NAME":"日盛國際商業銀行","BRANCH_NICKNAME":"日盛銀行"},{"BANK_ID":"816","BRANCH_NAME":"安泰商業銀行","BRANCH_NICKNAME":"安泰銀行"},{"BANK_ID":"822","BRANCH_NAME":"中國信託商業銀行","BRANCH_NICKNAME":"中信銀行"},{"BANK_ID":"901","BRANCH_NAME":"板農中心所屬會員","BRANCH_NICKNAME":"板農中心"},{"BANK_ID":"903","BRANCH_NAME":"新北市汐止區農會","BRANCH_NICKNAME":"汐農"},{"BANK_ID":"904","BRANCH_NAME":"新北市新莊區農會","BRANCH_NICKNAME":"莊農"},{"BANK_ID":"912","BRANCH_NAME":"板農中心所屬會員","BRANCH_NICKNAME":"板農中心"},{"BANK_ID":"916","BRANCH_NAME":"板農中心所屬會員","BRANCH_NICKNAME":"板農中心"},{"BANK_ID":"922","BRANCH_NAME":"台南市農會","BRANCH_NICKNAME":"台南市農會"},{"BANK_ID":"928","BRANCH_NAME":"板農中心所屬會員","BRANCH_NICKNAME":"板農中心"},{"BANK_ID":"952","BRANCH_NAME":"南農中心所屬會員","BRANCH_NICKNAME":"南農中心"},{"BANK_ID":"995","BRANCH_NAME":"關貿網路股份有限公司","BRANCH_NICKNAME":"關貿網路"},{"BANK_ID":"996","BRANCH_NAME":"財政部台北區支付處","BRANCH_NICKNAME":"財支"}]';
            var trHTML = '';
            $.each(JSON.parse(jsonData), function (i, item) {
                    if (i % 3 == 0) {
                        trHTML += '<tr><td  style="text-align:right;">'
                            + item.BANK_ID + '       '
                            + item.BRANCH_NAME + '      '
                            + '<button onclick=chooseBankId(' + parseInt(item.BANK_ID, 10) + ')>選我</button>'
                            + '</td>'
                    } else {
                        trHTML += '<td style="text-align:right;">'
                            + item.BANK_ID + '      '
                            + item.BRANCH_NAME + '      '
                            + '<button onclick=chooseBankId(' + parseInt(item.BANK_ID, 10) + ')>選我</button>'
                            + '</td>'
                    }
            });
            $('#Bank_table').append(trHTML);

        });

        //
        function chooseBankId(BANK_ID) {
            var lenght = 3;
            var str = BANK_ID.toString();
            if (str.length >= lenght) {
                return str;
            } else {
                alert(str.length >= lenght ? str : new Array(lenght - str.length + 1).join("0") + str);
                return str.length >= lenght ? str : new Array(lenght - str.length + 1).join("0") + str;
            }

        }
    </script>
</head>

<body>
    <table border="1" id="Bank_table">

    </table>

</body>

</html>

```

## 參考
