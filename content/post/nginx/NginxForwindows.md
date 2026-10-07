---
title: "Windows Nginx：靜態站、反向代理與設定檢查"
date: 2020-09-30T07:03:04+08:00
categories:
 - "筆記"
tags:
 - "Nginx"
toc: true
draft: false
description: "補上完整 nginx.conf，保留 Windows 路徑與 reload 操作並說明平臺限制。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上完整 nginx.conf，保留 Windows 路徑與 reload 操作並說明平臺限制。

<!--more-->

適用：Windows版Nginx本機測試；官方Windows版有功能／效能限制，正式服務按平臺需求評估。

## 本地配置

下載官方Windows版並解壓，使用無空格測試路徑如C:/nginx-note，在該目錄執行。conf/nginx.conf：

```nginx
worker_processes 1;
error_log logs/error.log;
events { worker_connections 1024; }
http {
    include mime.types;
    default_type application/octet-stream;
    upstream note_backend { server 127.0.0.1:8085; }
    server {
        listen 127.0.0.1:8087;
        server_name localhost;
        root html;
        location / { try_files $uri $uri/ =404; }
        location /api/ { proxy_pass http://note_backend/; }
    }
}
```

html/index.html放一段自製文字；另起本機8085後端，例如在有hello.txt的目錄使用Python http.server。PowerShell：

```powershell
.\nginx.exe -t
Start-Process .\nginx.exe
.\nginx.exe -s reload
```

8087首頁顯示本地HTML，`/api/hello.txt`傳至後端`/hello.txt`。proxy_pass末尾斜線影響匹配prefix替換，不帶斜線會有不同路徑行為，需以實際後端請求確認。

## 管理與診斷

quit優雅結束，stop快速結束，reopen重開日誌，reload載入配置；修改前先-t確認。命令必須在正確prefix目錄或明確-p/-c，不能因找到nginx.exe就假設讀到預期conf。logs/error.log看啟動、port衝突與upstream錯。

## 反向代理與負載

upstream多節點會按策略分派，但單純新增節點不處理session／資料一致性。HTTPS、header、超時、上傳大小與WebSocket要依需求另配；示例沒有開放公網也沒有宣稱完整安全閘道器。

Windows路徑使用正斜線，官方該平臺版本不是Windows service，不能把Start-Process當完成服務管理。正式Linux通常有不同process/IO能力與維護路線，原Windows筆記只作本機概念練習。

## 參考資料

- [Nginx Windows](https://nginx.org/en/docs/windows.html)
- [proxy_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass)
- [Nginx beginner](https://nginx.org/en/docs/beginners_guide.html)
- [ASP.NET Core](https://docs.microsoft.com/zh-tw/aspnet/core/host-and-deploy/linux-nginx)
- [ngx_http_proxy_module](http://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- [proxy_set_header](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header)
- [keepalive](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive)
- [NTLM Authentication](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#ntlm)
- [server Directives](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server)
- [worker_processes](http://nginx.org/en/docs/ngx_core_module.html#worker_processes)
- [worker_connections](http://nginx.org/en/docs/ngx_core_module.html#worker_connections)
- [error_log](http://nginx.org/en/docs/ngx_core_module.html#error_log)
- [gzip](http://nginx.org/en/docs/http/ngx_http_gzip_module.html)
- [gzip_proxied](http://nginx.org/en/docs/http/ngx_http_gzip_module.html#gzip_proxied)
- [Full Configuration](https://www.nginx.com/resources/wiki/start/topics/examples/full/)
- [原始參考入口 1](https://blog.kkbruce.net/2018/06/nginx-basic-for-windows-based.html?m=1#.XxwnEZ4vNPY)
