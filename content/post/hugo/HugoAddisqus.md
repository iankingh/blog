---
title: "Hugo 使用 disqus"
date: 2020-05-08T22:29:36+08:00
categories:
 - "筆記"
tags:
 - "hugo"
---

## Hugo 使用 disqus

Disqus（/dɪsˈkʌs/，與英語「discuss」同音）是一家使用社群網路形式，向網路社區提供網站留言服務的公司。
該公司的平台提供不同的功能，例如與不同社群網路服務連結、社群網路、用戶個人檔案、垃圾宣傳及審核工具、資料分析、電子郵件通知和在行動裝置留言等。

<!--more-->

### 先申請 disqus

取得 disqusShortname

### Config.toml

開啟Hugo配置檔 Config.toml，設定 DisqusShortname。

```toml
disqusShortname = "yourDisqusShortname"
```

### 新增 disqus.html

在根目錄 /layouts/partials/ 裡新增 disqus.html 檔案，
然後把官方提供的 Script 貼到 disqus.html 檔案裡並存檔。
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

### 設定  disqus.html

到 Hugo 主題的目錄下，找到 single.html 檔案，
將 Hugo 主題的目錄下 single.html Copy 至 /layouts/_default/ 下。
開啟 /layouts/_default/single.html 檔案，貼上下方語法

```html
<div class="disqus markdown">
  {{ partial "disqus.html" . }}
</div>
```

### 解決 localhost 不顯示 的問題

這是因為官方所提供的 Script 裡面其中一段語法的關係
if (window.location.hostname == "localhost")
  return;
它的作用是當本地端 Server 運行時，就 return 中止，所以我們才會看不到 Disqus，這是因為當自己在編輯文章並運行 Server 進行預覽時，不需要用到留言的功能，所以才會採用這個判斷式來避免本地端的 Server 模式啟用Disqus功能。若您希望在本地端 Server 模式下，也能看到 Disqus，只要把上述那二行給註解掉並存檔就可以了。
ShowDisqus


## 參考

[Hugo 加入 Disqus 整合性留言管理系統](https://coreychen71.github.io/posts/2019-05/hugoadddisqus/)  

[给Hugo添加disqus评论服务 - Marvin's Blog【程式人生】](https://zh4ui.net/post/2017-04-20-hugo-with-disqus/)  

[为你博客添加disqus评论系统 | 23.9K | Vineo](https://vineo.cn/config-disqus.html)
