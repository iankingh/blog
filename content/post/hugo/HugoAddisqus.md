---
title: "Hugo 使用 disqus"
date: 2020-05-08T22:29:36+08:00
categories:
 - "筆記"
tags:
 - "notes"
---

# Hugo ADD disqus

Disqus（/dɪsˈkʌs/，與英語「discuss」同音）是一家使用社群網路形式，向網路社區提供網站留言服務的公司。
該公司的平台提供不同的功能，例如與不同社群網路服務連結、社群網路、用戶個人檔案、垃圾宣傳及審核工具、資料分析、電子郵件通知和在行動裝置留言等。

<!--more-->


##  Config.toml

開啟網站全域配置檔 Config.toml，加入下方參數，後面的 DisqusShortname 記得要改成您註冊時所填的 Shortname

```toml
disqusShortname = "DisqusShortname"
```

## 新增 disqus.html
接著在根目錄 /layouts/partials/ 裡新增 disqus.html 檔案，然後把官方提供的 Script 貼到 disqus.html 檔案裡並存檔。
注意：若您在根目錄 /layouts 下看不到 /partials 目錄，請您自行新增此目錄。

官方提供的 Script 如下：

```html
    <div id="disqus_thread"></div>
    <script type="text/javascript">

        (function () {
            // Don't ever inject Disqus on localhost--it creates unwanted
            // discussions from 'localhost:1313' on your Disqus account...
            if (window.location.hostname == "localhost")
                return;
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            var disqus_shortname = '{{ .Site.DisqusShortname }}';
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by
            Disqus.</a></noscript>
    <a href="http://disqus.com/" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>

```

## 設定  disqus.html
再到您 Hugo 主題的目錄下，找到 single.html 檔案，
以我所使用的 AllinOne 主題來說，它的路徑如下：
/themes/AllinOne/layouts/_default/single.html，
請將 single.html Copy 至根目錄 /layouts/_default/ 下。
一樣，若您在根目錄 /layouts 下看不到 /_default 目錄，請您自行新增此目錄。

開啟剛剛 Copy 至根目錄 /layouts/_default/single.html 檔案，找到適當的位置，貼上下方語法

```html
<div class="disqus markdown">
  {{ partial "disqus.html" . }}
</div>
```

何謂適當的位置，這必要需要看您所採用的主題為何，基本上就是要把上述那段語法貼在文章結束的位置，這樣 Disqus 才會出現在文章下方，以我所採用的 AllinOne 主題來說，我選擇把它貼在下圖中的位置，所以請您依您採用的主題進行微調。
single.html
大致上這樣就完成了 Hugo 加上 Disqus 的配置，這時我們把本地端的 Sever 運行起來看一下文章下方是否已經出現 Disqus？這時您會發現，咦！怎麼都沒看到 Disqus！可是卻能看到一個 comments powered by Disqus 連結。
NoDisqus

## 關閉 localhost 不顯示
這是因為官方所提供的 Script 裡面其中一段語法的關係

if (window.location.hostname == "localhost")
  return;
它的作用是當本地端 Server 運行時，就 return 中止，所以我們才會看不到 Disqus，這是因為當自己在編輯文章並運行 Server 進行預覽時，不需要用到留言的功能，所以才會採用這個判斷式來避免本地端的 Server 模式啟用Disqus功能。若您希望在本地端 Server 模式下，也能看到 Disqus，只要把上述那二行給註解掉並存檔就可以了。
Annotation

這時再看一下剛剛開啟的文章最下方，就可以看到 Disqus 出現了。
ShowDisqus




# 參考

Hugo 加入 Disqus 整合性留言管理系統  
https://coreychen71.github.io/posts/2019-05/hugoadddisqus/

给Hugo添加disqus评论服务 - Marvin's Blog【程式人生】  
https://zh4ui.net/post/2017-04-20-hugo-with-disqus/

为你博客添加disqus评论系统 | 23.9K | Vineo  
https://vineo.cn/config-disqus.html