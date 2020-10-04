---
title: "NginxForwindows"
date: 2020-09-30T07:03:04+08:00
draft: true
categories:
 - "Nginx"
tags:
 - "Nginx"
toc: true
---

# 筆記
<!--more-->





### NGINX 基礎入門(Windows 版)

# NGINX 基礎入門(Windows 版)

當我們啟用 nginx.exe 之後，需要透過 `-s signal` 來與 nginx.exe 溝通。

```dos
nginx.exe -s signal
```

signal 值可以是：

- stop： fast shutdown
- quit： graceful shutdown
- reload：reloading the configuration file
- reopen：reopening the log files

## nginx.conf 組態

nginx.conf 是整個 NGINX 核心，管理者透過 nginx.conf 來調整 NGINX 運作行為。

> 在測試階段，最常用的是 `nginx.exe -s reload` 來重新載入 nginx.conf。

nginx.conf 最基本組成語法：

```nginx
<section> {
    <directive> <parameters>;
}
```

注意，每一行指令都需要由*分號(;)*結束。例如：`events` 設置：

```nginx
events {
    worker_connections  1024;
}
```



### main context

nginx.conf 最上層包含 `events` 與 `http` 兩個 Directive，稱 **main** context，`http` 包含 `server`，`server` 包含 `location`。

```nginx
events {
}

http {
    server {
        location / {
        }
    }
}
```

`http` Directive 能包含多組 `server` Directive，例如：

```nginx
http {
    # HTTP
    server {
        listen 80;
        server_name localhost;
    }
    
    # HTTPS
    server {
        listen 443;
        server_name localhost;
    }
    
    # PHP
    server {
        listen 8080;
        server_name localhost;
    }
}
```

> - `#` 是註解。

`server {}` 段落稱**虛擬伺服器**，通常會配合 `listen` 與 `server_name` 兩者來使用。

```nginx
# .org
server {
    listen      80;
    server_name example.org www.example.org;
}

# .net
server {
    listen      80;
    server_name example.net www.example.net;
}

# .com
server {
    listen      80;
    server_name example.com www.example.com;
}
```

這是基於 `server_name` 的配置，如果都沒有符合的名稱，那麼第一個會成為預設 `server`，也能明確指定 `default_server` 來指定。

```nginx
server {
    listen      80 default_server;
    server_name example.net www.example.net;
}
```

如果伺服器是多網卡(多 IP Address)，也是基於 IP Address 來配置：

```nginx
server {
    listen      192.168.1.1:80;
    server_name example.org www.example.org;
}

server {
    listen      192.168.1.1:80;
    server_name example.net www.example.net;
}

server {
    listen      192.168.1.2:80;
    server_name example.com www.example.com;
}
```

也可以多組 `server_name` 做組合：

```nginx
server {
    listen       80;
    server_name  example.org
                 www.example.org
                 ""
                 192.168.1.1
                 ;
}
```

如果是多組相同**次網域名稱**，例如：`server_name example.org www.example.org *.example.org;` 也能使用 wildcard names 的方式，改用 `server_name .example.org;` 即可。

在 nginx.conf 組態中，`include` 可以載入其他共用組態，而文件的位置可以是任何地方。

```nginx
http {
    include mime.types;
}
```

`location` Directive 指定 URI 與實體目錄的對應關係。

```nginx
# URL 的根路由指向 /data/www 目錄
location / {
    root html;
    index  index.html index.htm;
}

location /images/ {
    root /data/images;
}
```

> - 在 html 目錄放置 index.html 或 index.htm 會自然成為首頁。
> - `server` Directive 能包含多組 `location` Directive。

### Proxy Server 入門

在 Windows 環境，NGINX 不能取代 IIS 的位置，所以通常 NGINX 很大一部分是拿來當 Proxy Server。

首先看整體流程圖：request ⇆ proxy:80 ⇆ server:8080

正常 HTTP 透過 80 Port 請求，80 Port 的 Proxy 將請求轉至 8080 Port 執行。

```nginx
server {
    listen 8080;
    root html;

    location / {
    }
}
```

8080 Port 的 Server 是實際處理請求的位置。

```nginx
server {
    location / {
        proxy_pass http://localhost:8080;
    }

    location /images/ {
        root /data/images;
    }
}
```

此 `server` 預設監想 80 Port。要設置 Proxy Server 要使用 `proxy_pass` Directive 組態，當我們請求 80 Port 的根路由時，將這個請求轉移至 `http://localhost:8080` 去，如果是 `/images` 路由，那就到直接到 `/data/images` 去讀取。`location` Directive 的路由也能配合 Regular Expression 來設置：

```nginx
server {
    location / {
        proxy_pass http://localhost:8080/;
    }

    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```

`~` 符號指明後面是一段 Regular Expression，符合的 **.gif**、**.jpg**、**.png** 結尾的請求會讀取 `/data/images` 來回應。`proxy_pass` 這種行為又稱 Reverse Proxy。

#### Reverse Proxy

> 在 [ASP.NET Core](https://docs.microsoft.com/zh-tw/aspnet/core/host-and-deploy/linux-nginx) 就是利用此小節學到的 NGINX - Reverse Proxy 技巧來達成讓 NGINX 成為網頁伺服器。

```nginx
location /some/path/ {
    proxy_pass http://www.example.com/link/;
}

location ~ \.php {
    proxy_pass http://127.0.0.1:8000;
}
```

預設 NGINX 在 Proxy 請求會重新定義 **Host** 和 **Connection** Header，並消除其值為空字串。然後 Host 會設定 **$proxy_host** 的值，Connection 設定為 **close**。可以使用 `proxy_set_header` 重新設置：

```nginx
location /some/path/ {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_pass http://localhost:8000;
}
```

`proxy_set_header` 可以設定在 `location` 或更高層級，例如：`server` 或 `http`。

> 參考：[ngx_http_proxy_module](http://nginx.org/en/docs/http/ngx_http_proxy_module.html)

#### 傳遞 Client IP

在使用 Proxy 時，Client 無法接觸至後端主機，這會造成後端主機無法取得 Client 的資訊，例如，IP 等，都必須透過 [proxy_set_header](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header) Header 來傳遞。

```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

另外，在使用 [keepalive](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive) 與 [NTLM Authentication](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#ntlm) 環境，建議指定 `proxy_http_version 1.1;`，預設版本為 1.0。

### Load Balancing

NGINX 另一大重點功能是透過簡單的設置，它就能成為一台強大的 Load Balance 伺服器。

```nginx
http {
    upstream myapp1 {
        server srv1.example.com;
        server srv2.example.com;
        server srv3.example.com;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://myapp1;
        }
    }
}
```

在 `server` 設定 `proxy_pass` 至一個虛擬位置，虛擬位置由 `upstream` 提供，`upstream` 是一或一群 `server` 的組合。 預設採用 round-robin 方式負載平衡。

> `http {}` 中可包含多組 `upstream` 設置。

另一種採用最少連線數(Least connected)來負載平衡，意思是，有些請求會需要較長處理時間，而最少連線數則能更公平進行 `server` 的負載平衡。

```nginx
upstream myapp1 {
    least_conn;
    server srv1.example.com;
    server srv2.example.com;
    server srv3.example.com;
}
```

另一種 Web 常見的情境是 Session 的使用，如果應用程式使用 Session 的話，那麼不同 `server` 連線可能會造成問題。換句話說，雖然是負載平衡，但希望 Client 與 Server 能保持一種 sticky 或 persistent 關係，`ip-hash` 提供此種機制，它會依照 Client IP Address 去計算一個 Hash 碼，提供 Hash 與 `server` 之間一致的連線關係，同一個來源 IP Address 的 Client 被確保導向同一台 `server`。

```nginx
upstream myapp1 {
    ip_hash;
    server srv1.example.com;
    server srv2.example.com;
    server srv3.example.com;
}
```

upstream 總共有三個模式：

- round-robin (default)
- least_conn
- ip_hash

假設，各 `server` 主機等級不同，你可能想要分配不同的權重，可以使用 `weight` 來指定：

```nginx
upstream myapp1 {
    server srv1.example.com weight=3;
    server srv2.example.com;
    server srv3.example.com;
}
```

如此，每 5 次請求，有 3 次會被分配至 srv1 主機上。另外，我們也能在 NGINX 的 Load Balance 上做健康檢查，以防 Client 連線至不正常的主機上。例如：`max_fails` 等。

```nginx
upstream dynamic {
    zone upstream_dynamic 64k;

    server backend1.example.com      weight=5;
    server backend2.example.com:8080 fail_timeout=5s slow_start=30s;
    server 192.0.2.1                 max_fails=3;
    server backend3.example.com      resolve;
    server backend4.example.com      service=http resolve;

    server backup1.example.com:8080  backup;
    server backup2.example.com:8080  backup;
}
```

> 更多細節參考 [server Directives](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server) 文件。

### 全域參數

在 nginx.conf 裡 `events` 與 `http` 之外有一些全域參數，以下列出幾個常調整的參數：

- [worker_processes](http://nginx.org/en/docs/ngx_core_module.html#worker_processes)：worker 執行緒數量，預設 1。目前支援 `auto` 值。
- [worker_connections](http://nginx.org/en/docs/ngx_core_module.html#worker_connections)：worker 最大連線數。
- [error_log](http://nginx.org/en/docs/ngx_core_module.html#error_log)：日誌的路徑與等級的指定。
- [gzip](http://nginx.org/en/docs/http/ngx_http_gzip_module.html)：預設為 off。可修改為 on。其中，[gzip_proxied](http://nginx.org/en/docs/http/ngx_http_gzip_module.html#gzip_proxied) 影響 Proxy 的 gzip 行為。

### 小結

有了以上的基礎，你可以看一下 NGINX 官方有一份比較大型的配置 [Full Configuration](https://www.nginx.com/resources/wiki/start/topics/examples/full/) 範例，絕大部分你現在應該都能看得懂。

另外，NGINX 還有二個優秀的功能，我們未能介紹：

- HTTP 伺服器：這在 Windows - IIS 環境中作用不大。
- Rewrite 模組：進階議題，它和 Regular Expression 比較關係。



參考

KingKong Bruce記事: NGINX 基礎入門(Windows 版)

https://blog.kkbruce.net/2018/06/nginx-basic-for-windows-based.html?m=1#.XxwnEZ4vNPY