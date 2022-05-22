---
title: "DockerFile"
date: 2020-09-20T19:45:16+08:00
categories:
  - "筆記"
tags:
 - "docker"
toc: true
draft: false
---



<!--more-->
# Dockerfile 

Dockerfile 是用來描述映像檔（image）的文件。

所謂的 `Image`，就是生產 `Container` 的模版，你可以從 Docker Hub 官方下載或是根據官方的 Image 自己加工後打包成 Image 或是完全自己使用 Dockerfile 描述 Image 內容來製作 Image。

而 Container 則是透過 Image 產生隔離的執行環境，稱之為 Container，也就是我們一般用來提供 microservice 的最小單位。

### 簡單示例

Dockerfile 一般位於構建上下文的根目錄下，也可以通過-f指定該檔的位置：

````
$ docker build -f /path/to/a/Dockerfile .
````

構建時，還可以通過-t參數指定構建成鏡像的倉庫、標籤。

映像標籤

```
$ docker build -t nginx:v1 .
```

命令最後有一個. 表示目前的目錄

````dockerfile
#從Docker hub 下載基礎的 image，可能是作業系統環境或是程式語言環境
FROM nginx
#維護者資訊
MAINTAINER ianhunag@gmail.com 
# 鏡像操作指令執行 CMD 指令跑的指令
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
````

使用 docker run 命令來啟動容器

```shell
$ docker run --name docker_nginx_v1  -d -p 80:80 nginx:v1
```

這條命令會用 nginx 鏡像啟動一個容器，命名為docker_nginx_v1，並且映射了 80 埠，這樣我們可以用流覽器去訪問這個 nginx 伺服器：

   **緩存**

Docker 守護進程會一條一條的執行 Dockerfile 中的指令，而且會在每一步提交並生成一個新鏡像，最後會輸出最終映像的ID。生成完成後，Docker 守護進程會自動清理你發送的上下文。

Dockerfile檔中的每條指令會被獨立執行，並會創建一個新鏡像，RUN cd /tmp等命令不會對下條指令產生影響。 

Docker 會重用已生成的中間鏡像，以加速docker build的構建速度。以下是一個使用了緩存鏡像的執行過程：

```shell
$ docker build -t svendowideit/ambassador .
```



```shell
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM nginx
 ---> 7e4d58f0e5f3
Step 2/3 : MAINTAINER ianhunag@gmail.com
 ---> Using cache
 ---> d0140a7f8c8e
Step 3/3 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
 ---> Using cache
 ---> 81a660be4e2b
Successfully built 81a660be4e2b
Successfully tagged svendowideit/ambassador:latest

```



構建緩存僅會使用本地父生成鏈上的鏡像，如果不想使用本地緩存的鏡像，也可以通過--cache-from指定緩存。指定後將不再使用本地生成的鏡像鏈，而是從鏡像倉庫中下載。





## 參考

[Dockerfile **使用介紹 -** **純潔的微笑博客**](http://www.ityouknow.com/docker/2018/03/12/docker-use-dockerfile.html)

