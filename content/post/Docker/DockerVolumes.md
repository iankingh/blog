---
title: "DockerVolumes"
date: 2020-09-20T20:29:24+08:00
categories:
  - "筆記"
tags:
 - "docker"
toc: true
draft: true
---

## Docker-Volume
<!--more-->

## 什麼是 docker volume



volume是Docker資料持久化機制。

bind mounts依賴主機目錄結構，volume完全由Docker管理。

Volumes有以下優點：

```
§ Volumes更容易備份和移植。

§ 可以通過Docker CLI或API進行管理

§ Volumes可以無區別的工作中Windows和Linux下。

§ 多個容器共用Volumes更安全。

§ Volume驅動可以允許你把資料儲存到遠端主機或者雲端，並且加密資料內容，以及新增額外功能。

§ 一個新的資料內容可以由容器預填充。
```



而且，volumes不會增加容器的大小，生命週期獨立與容器。

**選擇使用 -v還是—mount**

起初，-v或者—volume用於獨立容器，--mount用於swarm services。然而，從Docker 17.06開始，也可是使用--mount用於獨立容器。—mount命令更精準詳細。-v將選項進行了合併。使用—mount。

如果你需要制定volume驅動選項，你必須使用 —mount。

```
§ -v或者**--volume**:由3部分引數組成，使用“：”間隔。順序不能顛倒。

§ 第一個部分是volumes名字，在宿主機上具有唯一性。匿名卷名字系統給出。

§ 第二部分是掛載到容器裡的檔案或資料夾路徑。

§ 第三部分是可選項清單分隔符號號號號號號號，例如“or”，這些可選項在下麵會討論。

§   —mount：由多個鍵值對組成，<key>=<value>。—mount要比-v或者--volume命令更長，但是更容易理解。

§ type，可以是bind,volume或者tmpfs。這篇文章主要討論volumes，所以type一直使用volume.

§ source,volumes的名字，匿名volume可以省略。source可縮寫為src.

§ destination,掛載到容器中的檔案或目錄路徑。可也縮寫為dst或者使用target。

§ readonly,指定掛載在容器中為只讀。

§ volume-opt,可選屬性，可以多次使用。
```





下面是—mount和-v的例子。

**-v****和—mount的不同行為**

與bind mounts不同，對於—mount和-v所有的選項都可以使用。

當使用volumes服務時，只支援—mount.

**建立和管理volumes**

不像bind mount,你可以在容器外建立和管理volumes。

**建立一個volume:**

```
$ docker volume create my-vol
```

**顯示所有volumes**

```
$ docker volume ls
```

**檢視volumes**

```
$ docker volume inspect my-vol

# 執行結果
[

{

"Driver": "local",

"Labels": {},

"Mountpoint": "/var/lib/docker/volumes/my-vol/_data",

"Name": "my-vol",

"Options": {},

"Scope": "local"

}

]
```

**刪除一個volume**

```
$ docker volume rm my-vol
```

**啟動一個帶volume的容器**

如果你啟動一個帶有volume容器，volume還沒有建立，Docker會為你建立。下面的例子掛載myvol2到容器中的/app/下。

下面的例子-v和—mount結果是一樣的。

—mount:

$ docker run -d\

--name devtest \

--mountsource=myvol2,target=/app \

 nginx:latest

-v:

$ docker run -d\

--name devtest \

-v myvol2:/app \

 nginx:latest

使用inspect檢視掛載是否正確，檢視Mounts部分：

"Mounts":[

{

"Type":"volume",

"Name":"myvol2",

"Source":"/var/lib/docker/volumes/myvol2/_data",

"Destination":"/app",

"Driver":"local",

"Mode":"",

"RW":true,

"Propagation":""

}

],

可以看出掛載正確，並且是可讀寫的。

停止容器然後刪除volume

```
$ docker container stop devtest

$ docker container rm devtest

$ docker volume rm myvol2
```



### **啟動一個帶有volumes服務**

當你啟動服務定義一個volume，每個服務可以使用自己本地人volume.如果你使用local volume，容器不能分享資料，但是一些volume驅動支援分享儲存。Docker for AWS and Docker for Azure使用Cloudstor外掛都支援持久化儲存。

下面的例子啟動4份nginx服務，每個使用一個本地儲存myvol2。

$ docker service create -d\

--replicas=4 \

--name devtest-service \

--mountsource=myvol2,target=/app \

 nginx:latest

使用docker service ps devtest-service 檢視服務是否執行：

$ docker service ps devtest-service

ID         NAME        IMAGE        NODE        DESIRED STATE    CURRENT STATE      ERROR        PORTS

4d7oz1j85wwn    devtest-service.1  nginx:latest    moby        Running       Running 14 seconds ago  

刪除服務

$ docker service rm devtest-service

**服務標識的不同**

docker service create 命令不支援-v或者—volume。必須使用—mount。

**使用容器載入一個volume**

和上面一樣，如果你啟動一個容器建立一個新的volume，在容器被掛載的目錄（/app/）中有檔案或者資料夾，這個目錄中的內容會被拷貝到volume中。然後容器掛載使用volume，其他容器使用這個volume也可以訪問預載入內容。

為了說明這個，這個例子啟動一個nginx容器並且載入一個新volume nginx-vol，裡面包括容器中/usr/share/nginx/html 目錄中的內容，裡面儲存的是nginx預設的HTML內容。

—mount and -v具有相同結果

—mount:

$ docker run -d\

--name=nginxtest \

--mountsource=nginx-vol,destination=/usr/share/nginx/html \

 nginx:latest

-v

$ docker run -d\

--name=nginxtest \

-v nginx-vol:/usr/share/nginx/html \

 nginx:latest

以下是執行後清理命令

$ docker container stop nginxtest

$ docker container rm nginxtest

$ docker volume rm nginx-vol

**使用只讀volume**

對於一些開發應用，容器需要回寫資料到Docker主機。但有時容器只需要讀資料。請記住多個容器可以掛載相同volume，一個掛載讀寫容器，也可以掛載只讀容器，還可以兩種同時掛載。

這個例子修改上面的例子，但是掛載的是隻讀容器，使用’or’分隔符號號號號號號號處理選項列表，

—mount and -v具有相同結果

—mount

$ docker run -d\

--name=nginxtest \

--mountsource=nginx-vol,destination=/usr/share/nginx/html,readonly \

 nginx:latest

-v

$ docker run -d\

--name=nginxtest \

-v nginx-vol:/usr/share/nginx/html:ro \

 nginx:latest

使用 docker inspect nginxtest 命令檢視是否掛載正確，檢視Mounts部分

"Mounts":[

{

"Type":"volume",

"Name":"nginx-vol",

"Source":"/var/lib/docker/volumes/nginx-vol/_data",

"Destination":"/usr/share/nginx/html",

"Driver":"local",

"Mode":"",

"RW":false,

"Propagation":""

}

],

清理命令

$ docker container stop nginxtest

$ docker container rm nginxtest

$ docker volume rm nginx-vol

**機器間共用資料**

當構建高可用應用程式，你需要配置多個相同的服務訪問相同檔案。

​                                 

有幾種方法可以達到這種效果。一種是在你的應用中新增對雲端儲存檔案的訪問，如Amazon S3。另一種是使用支援外服儲存驅動（NFS， Amazon S3）的volume。

Volume驅動允許你在應用中抽象下層的儲存系統。例如，如果你的服務使用NFS驅動volume，你可以使用不同的驅動更新服務，就像儲存在雲中的資料，不需要修改應用邏輯。

**使用volume驅動**

當你使用docker volume create建立一個volume，或者當你啟動一個帶有沒建立volume的容器，你可以指定volume驅動。下面例子使用vieux/sshfs volume驅動 ，首先建立一個獨立的volume，然後啟動一個建立新volume的容器。

**初始化設定**

這個例子假設你有兩個節點，第一個是Docker主機而且可以連線到第二個的ssh.

在Docker主機中安裝vieux/sshfs外掛：

$ docker plugin install --grant-all-permissions vieux/sshfs

**使用volume驅動建立volume**

這個樣例指定一個SSH密碼，但是如果兩個主機共用keys配置，你可以省略密碼。每個volume驅動可以沒有或者更多配置選項，可以使用-o標識。

$ docker volume create --driver vieux/sshfs \

-osshcmd=test@node2:/home/test \

-opassword=testpassword \

 sshvolume

test@node2:/home/test 為遠端主機掛載點

**啟動一個帶有使用volume驅動建立volume的容器**

這個樣例指定一個SSH密碼，但是如果兩個主機共用keys配置，你可以省略密碼。每個volume驅動可以沒有或者更多配置選項。如果volume驅動要穿可選引數，你必須使用—mount。

$ docker run -d\

--name sshfs-container \

--volume-driver vieux/sshfs \

--mountsrc=sshvolume,target=/app,volume-opt=sshcmd=test@node2:/home/test,volume-opt=password=testpassword \

 nginx:latest

 



### 使用 postgres

```
docker pull postgres:9.5
```



## 基本 Volume 使用方法

先來基本的使用方法，就是透過 volume command 以及它的 sub-commands 來操作。前面說到 volume 是一個獨立於 container 之外的檔案，那麼就來練習

·    產生一個空的 volume

·    在 container foo 裡面塞個檔案進去 volume

·    再新開一個 container bar 觀察一下是不是一樣有該檔案

還有一些基本觀察 volume 的指令

```
`# 產生一個 volume，假設它的 id 是 AABBCCDDEE  
$ docker volume create  AABBCCDDEE   
# 用 busybox image 生出一個 container，把 volume 掛到 /foo 底下，並且新增一個空白檔案 Blah 
$ docker run -v AABBCCDDEE:/foo --name foo -it busybox /bin/sh  /
# cd /foo  /foo 
# ls  /foo # touch Blah  /foo # exit    
# 把原來的 container 砍掉，重開一個，把 volume 掛進去還是可以看見該檔案 Blah 被放在 /foobar 底下  $ docker run -v AABBCCDDEE:/foobar --name bar -it busybox /bin/sh`
```



````
$ docker volume ls  $ docker volume inspect THE_VOLUME_ID   
$ docker inspect -f '{{.Mounts}}' foo #查看某一個 container 的 volume 狀況
````



## 啟動 container 自動產生 volume

除了前面的作法，要使用 volume 還有兩種方法，一個是在 Dockerfile 裡面使用 `VOLUME`，另一個是啟動 container 的時候加上選項 `-v` 並不指定 mountpoint(要拿哪一個 volume 來用)，這樣就會自動產生一個新的 volume

`````
# 方法一  FROM debian:wheezy  VOLUME /data    # 方法二  $docker run -v /tmp --name foo busybox ls /tmp`
`````



## 移除 volume

既然 volume 是獨立於 container 而存在的檔案，移除 container 的時候要記得一併把沒用到的 volume 拿掉。或是一段時間把孤苦無依的 volume 清空一遍

```
$ docker rm -v the_container_id    
$ docker volume rm `docker volume ls -f 'dangling=true' -q` # clean up`
```



## 自製 pg data image

前面簡介了 docker volume 的用法，知道怎麼把玩之後，回到我原來的需求。

因為 pg 會把資料庫的內容放在 `/var/lib/postgres`，我的想法是把該目錄的資料 commit 到一個很小的 container 裡面，產生一個幾乎只有純 data 的 image 來做到 snapshot 的功能。接著利用這個 image 生出 container，產生的同時也生成一個 volume，最後啟動 pg 的時候把 volume 掛上去就行了

先透過官方的 pg 產生出合用的 **/var/lib/postgresql**

````
$ mkdir /tmp/db  # 匯出的檔案將放在 host 的 /tmp/db  
$ docker run -d -v /tmp/db/:/tmp/db --name upstream -e POSTGRES_PASSWORD=thepwd postgres  # 這時候已經跑起 pg 了，可以透過 psql 進去做一些操作，把我們的測試資料放進去，密碼就是 thepwd  
$ psql -U postgres -h 172.17.0.2  .......(to add fixture data)........    
# 用 tar 打包資料，保留 file permission  
$ docker exec -it upstream /bin/bash  root@bfb8bc37341e:/
# cd /  root@bfb8bc37341e:/
# tar cvvf /tmp/db/archive.tar /var/lib/postgresql    
$ docker rm -vf upstream`
````



接著用已經夠小的 busybox image 來做 snapshot。其實也可以再用一次掛 volume 的方式讓 staging 找到 archive.tar，但是這樣 commit image 之後會留一點渣渣，我選擇在 host 跑 http server，再從 container 裡面用 wget 抓，效果一樣

```
$ docker pull busybox  
$ docker run --name staging -it busybox    
# wget 192.168.42.100:8000/archive.tar  / 
# tar xvf archive.tar  
# 解開 fixture data  /
# rm /tmp/archive.tar  / 
# exit    $ docker commit staging data_img
```



接下來就是真正使用 snapshot 了。跑起一個 data_provider container 只是為了產生 volume，它後來就這樣關掉也沒關係，只要 volume 還在就好。

啟動 pg image 的時候，只要說「我要從 data_provider 而來的 volume」即可



```
$ docker run -v /var/lib/postgresql/data --name data_provider data_img  
$ docker volume ls   
$ docker run -d --name running_pg --volumes-from data_provider postgres 
$ docker exec -it running_pg /bin/bash`
```



# Docker Volume 屬主設置

最近在測試 Volume 掛載時候有點問題，描述如下：

1. Docker 啟動時候，設置掛載目錄使用者為     foo
2. 宿主機原始目錄屬主為 smallfish

嘗試了幾種辦法，比如：

1. container 啟動後執行 `chown`
2. 構建鏡像時候加入 `RUN chown foo /data`，這裡不僅僅是這種嘗試

不管是在 container 或者宿主機裡進行設置，都會發現要麼裡面屬主成數位或者宿主機的屬主成數字。

原因無非是兩個系統裡使用者 `uid/gid` 不一樣，也可以很猥瑣的在 container 裡面 `adduser` 指定 `--uid` 參數。

百無聊賴的放狗繼續搜啊搜，竟然搜到一篇：[**Understanding Volumes in Docker**](http://container-solutions.com/2014/12/understanding-volumes-docker/)

嘗試了下，竟然可以：

```
RUN useradd foo
RUN mkdir /data && touch /data/a.txt
RUN chown foo:foo /data
VOLUME /data
```

上面要注意 `VOLUME` 一定要放在最後，然後要先建立目錄，再寫個檔，文件隨意。

重新構建之後，進入互動式：

```
# docker run -t -i -v /home/smallfish/xxx:/data testubuntu /bin/bash
root@527f8eceacca:/# ls -al /data
drwxr-xr-x  1 foo  staff  136 Dec 26 06:17 .
drwxr-xr-x 51 root root  4096 Dec 26 06:17 ..
drwxr-xr-x  1 foo  staff  170 Jul  4 15:57 xxx
```

很驚喜的發現竟然屬主變成 foo 了，我了個呵呵。。。

官方文檔：[**https://docs.docker.com/userguide/dockervolumes/**](https://docs.docker.com/userguide/dockervolumes/)，其實也有提到一些描述，還是貼下之前參考那篇博客的原文：

```
Docker is clever enough to copy any files that exist in the image under the volume mount into the volume and set the ownership correctly. This won’t happen if you specify a host directory for the volume (so that host files aren’t accidentally overwritten).
```

 

 

參考

Docker的volumes的使用 - IT閱讀

https://www.itread01.com/content/1548752791.html

Docker volume 簡單用法 | 只放拖鞋的鞋櫃

https://julianchu.net/2016/04/19-docker.html

Docker Volume 屬主設置 · smallfish's blog

http://chenxiaoyu.org/2014/12/26/docker-volume-chown/

 

 

# Docker學習筆記之存儲篇



### 一、存儲

docker的鏡像使用一層一層檔組成的，docker的一些存儲引擎可以處理怎麼樣存儲這些檔。使用docker inspect這個命令可以查詢鏡像或者容器的詳細資訊，比如要查看centos這個鏡像：

```
docker inspect centos
```

展示資訊下方的Layers，就是centos的檔，這些東西都是唯讀的不能去修改，我們基於這個鏡像去創建的鏡像和容器也會共用這些檔層，而docker會在這些層上面去添加一個可讀寫的檔層。如果需要修改一些檔層裡面的東西的話，docker會複製一份到這個可讀寫的檔層裡面，如果刪除容器的話，那麼也會刪除它對應的可讀寫的檔層的檔。

#### 演示

###### 1、先創建一個帶交互的容器，管它名字叫test1

```
docker run -i -t --name test1 centos /bin/bash
```

###### 2、然後在裡面新建一個檔，hello.txt

###### 3、接著退出容器，使用centos創建第二個容器叫test2，試著輸出根目錄下的hello.txt檔的內容。

發現沒有找到此檔，雖然test1，test2都是基於centos鏡像創建的，但他們都擁有各自的可讀寫的檔層，新創建的檔或者修改的已有的檔都會放到這個檔層，不會影響到鏡像本身和使用這個鏡像創建的容器。

**刪除容器的時候，這些容器層上面的檔也會被刪除掉。**

### 二、數據卷：Data Volumes

如果有些資料你想一直保存的話，比如：web伺服器上面的日誌，資料庫管理系統裡面的資料，那麼我們可以把這些資料放到data volumes資料盤裡面。它上面的資料，即使把容器刪掉，也還是會永久保留。創建容器的時候，我們可以去指定資料盤。其實就是去指定一個特定的目錄，剩下的docker會幫你做。

#### 指定資料盤的命令

```
docker run --volume /mnt -i -t --name db centos /bin/bash
```

說明：—volume簡寫形式 -v，指定資料盤的目錄，注意目錄是要絕對路徑。

   

###### 查看容器信息：

   

Mounts下Source表示資料存在宿主機上的真實位置，Destination表示資料盤在docker中對應的位置。及時刪除容器，Source下的資料也還會存在。

#### 指定主機目錄作為資料盤

我們還可以手工指定主機上的目錄作為資料盤，比如，新建一個資料夾叫data，讓它作為資料盤，然後使用centos鏡像創建容器，命名為db，指定資料盤位置：

```
docker run -v /Users/beckjiang/Desktop/data:/mnt --name db -i -t centos /bin/bash
```

進入容器後，在/mnt/ 目錄下創建檔data1，然後刪除容器，查看主機上/Users/beckjiang/Desktop/data 裡面，仍然會保留容器裡面創建的資料。

   

### 三、數據容器

我們可以創建一個資料容器，也就是再創建容器是指定這個容器的資料盤，然後讓其他容器可以使用這個容器作為他們的資料盤，有點像繼承了這個資料容器指定的資料盤作為資料盤。

###### 先來創建一個資料容器：

```
docker create -v /mnt -i -t --name dbcenter centos /bin/bash
```

   

###### 接著使用這個資料容器，去創建一個容器 db1：

```
docker run --volumes-from dbcenter --name db1 -i -t centos bash
```

在/mnt/目錄下創建data1檔：

   

完成以後退出容器，基於dbcenter這個資料容器去創建第二個容器 db2：

```
docker run --volumes-from dbcenter --name db2 -i -t centos bash
```

   

查看/mnt/目錄下的檔，會看到在db1容器中創建的data1文件。同樣的，你在db2中的/mnt/目錄創建的資料檔案，也會被其他使用了dbcenter作為資料容器的容器所看到。

### 四、管理資料盤

###### 查看主機上面創建的資料盤

```
docker volume ls
```

   

在刪除容器時，docker預設不會刪除其資料盤。這裡可以 查看沒有容器在使用的資料盤:

```
docker volume ls -f dangling=true
```

   

出現的就是沒有容器在使用的資料盤，想要 刪除資料盤 可以使用：

```
docker volume rm VOLUME NAME
```

   

把沒有容器使用的資料盤都刪除掉以後，還剩下1個正在被使用的資料盤，就是上面創建的資料容器。

如果想要刪除容器時，同時刪除掉其資料盤，那麼可以使用-v參數。(db1，db2使用dbcenter作為資料盤，先將其刪掉)

```
docker rm -v dbcenter
```

   

參考

Docker學習筆記之存儲篇-眼眸刻著你的微笑-51CTO博客

https://blog.51cto.com/dengaosky/1854568

 

# [docker學習筆記18：Dockerfile 指令 VOLUME 介紹](https://www.cnblogs.com/51kata/p/5266626.html)

在介紹VOLUME指令之前，我們來看下如下場景需求：

1）容器是基於鏡像創建的，最後的容器檔案系統包括鏡像的唯讀層+可寫層，容器中的進程操作的資料持久化都是保存在容器的可寫層上。一旦容器刪除後，這些資料就沒了，除非我們人工備份下來（或者基於容器創建新的鏡像）。能否可以讓容器進程持久化的資料保存在主機上呢？這樣即使容器刪除了，資料還在。

2）當我們在開發一個web應用時，開發環境是在主機本地，但運行測試環境是放在docker容器上。

這樣的話，我在主機上修改檔（如html，js等）後，需要再同步到容器中。這顯然比較麻煩。

3）多個容器運行一組相關聯的服務，如果他們要共用一些資料怎麼辦？

對於這些問題，我們當然能想到各種解決方案。而docker本身提供了一種機制，可以將主機上的某個目錄與容器的某個目錄（稱為掛載點、或者叫卷）關聯起來，容器上的掛載點下的內容就是主機的這個目錄下的內容，這類似linux系統下mount的機制。 這樣的話，我們修改主機上該目錄的內容時，不需要同步容器，對容器來說是立即生效的。 掛載點可以讓多個容器共用。

下麵我們來介紹具體的機制。

**一、通過docker run命令**

1、運行命令：docker run --name test -it -v /home/xqh/myimage:/data ubuntu /bin/bash

其中的 -v 標記 在容器中設置了一個掛載點 /data（就是容器中的一個目錄），並將主機上的 /home/xqh/myimage 目錄中的內容關聯到 /data下。

這樣在容器中對/data目錄下的操作，還是在主機上對/home/xqh/myimage的操作，都是完全即時同步的，因為這兩個目錄實際都是指向主機目錄。

2、運行命令：docker run --name test1 -it -v /data ubuntu /bin/bash

上面-v的標記只設置了容器的掛載點，並沒有指定關聯的主機目錄。這時docker會自動綁定主機上的一個目錄。通過docker inspect 命令可以查看到。

[     ](javascript:void(0);)

```
xqh@ubuntu:~/myimage$ docker inspect test1
[
{
    "Id": "1fd6c2c4bc545163d8c5c5b02d60052ea41900a781a82c20a8f02059cb82c30c",
.............................
    "Mounts": [
        {
            "Name": "0ab0aaf0d6ef391cb68b72bd8c43216a8f8ae9205f0ae941ef16ebe32dc9fc01",
            "Source": "/var/lib/docker/volumes/0ab0aaf0d6ef391cb68b72bd8c43216a8f8ae9205f0ae941ef16ebe32dc9fc01/_data",
            "Destination": "/data",
            "Driver": "local",
            "Mode": "",
            "RW": true
        }
    ],
...........................
```

[     ](javascript:void(0);)

上面 Mounts下的每條資訊記錄了容器上一個掛載點的資訊，"Destination" 值是容器的掛載點，"Source"值是對應的主機目錄。

可以看出這種方式對應的主機目錄是自動創建的，其目的不是讓在主機上修改，而是讓多個容器共用。

 

**二、通過dockerfile創建掛載點**

上面介紹的通過docker run命令的-v標識創建的掛載點只能對創建的容器有效。

通過dockerfile的 VOLUME 指令可以在鏡像中創建掛載點，這樣只要通過該鏡像創建的容器都有了掛載點。

還有一個區別是，通過 VOLUME 指令創建的掛載點，無法指定主機上對應的目錄，是自動生成的。

```
#test
FROM ubuntu
MAINTAINER hello1
VOLUME ["/data1","/data2"]
```

上面的dockfile檔通過VOLUME指令指定了兩個掛載點 /data1 和 /data2.

我們通過docker inspect 查看通過該dockerfile創建的鏡像生成的容器，可以看到如下資訊

 

[     ](javascript:void(0);)

```
    "Mounts": [
        {
            "Name": "d411f6b8f17f4418629d4e5a1ab69679dee369b39e13bb68bed77aa4a0d12d21",
            "Source": "/var/lib/docker/volumes/d411f6b8f17f4418629d4e5a1ab69679dee369b39e13bb68bed77aa4a0d12d21/_data",
            "Destination": "/data1",
            "Driver": "local",
            "Mode": "",
            "RW": true
        },
        {
            "Name": "6d3badcf47c4ac5955deda6f6ae56f4aaf1037a871275f46220c14ebd762fc36",
            "Source": "/var/lib/docker/volumes/6d3badcf47c4ac5955deda6f6ae56f4aaf1037a871275f46220c14ebd762fc36/_data",
            "Destination": "/data2",
            "Driver": "local",
            "Mode": "",
            "RW": true
        }
    ],
```

[     ](javascript:void(0);)

可以看到兩個掛載點的資訊。

**三、容器共用卷（掛載點）**

docker run --name test1 -it myimage /bin/bash

上面命令中的 myimage是用前面的dockerfile文件構建的鏡像。 這樣容器test1就有了 /data1 和 /data2兩個掛載點。

下面我們創建另一個容器可以和test1共用 /data1 和 /data2卷 ，這是在 docker run中使用 --volumes-from標記，如：

可以是來源不同鏡像，如：

docker run --name test2 -it --volumes-from test1 ubuntu /bin/bash

也可以是同一鏡像，如：

docker run --name test3 -it --volumes-from test1 myimage /bin/bash

上面的三個容器 test1 , test2 , test3 均有 /data1 和 /data2 兩個目錄，且目錄中內容是共用的，任何一個容器修改了內容，別的容器都能獲取到。

 

**四、最佳實踐：數據容器**

如果多個容器需要共用資料（如持久化資料庫、設定檔或者資料檔案等），可以考慮創建一個特定的資料容器，該容器有1個或多個卷。

其它容器通過--volumes-from 來共用這個資料容器的卷。

因為容器的卷本質上對應主機上的目錄，所以這個資料容器也不需要啟動。

如： docker run --name dbdata myimage echo "data container"

 

說明：有個卷，容器之間的資料共用比較方便，但也有很多問題需要解決，如許可權控制、資料的備份、卷的刪除等。這些內容後續文章介紹。

 

參考

docker學習筆記18：Dockerfile 指令 VOLUME 介紹 - 51kata - 博客園

https://www.cnblogs.com/51kata/p/5266626.html



## Docker 實戰系列（三）：使用 Volume 保存容器內的數據

這是 Docker 實戰系列文的第三篇，如果還沒看過上一篇的可以先看看 [Docker 實戰系列（二）：在 DockerHub 上分享自己的 image](https://larrylu.blog/share-image-on-dockerhub-ccb7d9b26fa8)

*之前說過**每個 container 都是獨立**的，那如果今天我想升級 mysql 的版本，於是我把正在跑的* *mysql:5.5* *關掉，然後重新跑一個* *mysql:5.7* *的 container，那資料庫裡面的資料不就不見了嗎？*

沒錯，這時候就需要 volume 了，簡單來說 Volume 就是用來保存容器內的資料的，看看下面這張圖

當你使用 volume 時，docker 會在你的本機上隨機新增一個資料夾（Local storage area），大部分會在 `/var` 底下，然後讓這個資料夾跟 container 裡面的某個資料夾互通。

因為他們是互通的，所以當你 container 裡面那個資料夾有任何變更時，本地的資料夾也會跟著變，而且很重要的一點是：***container*** ***被刪掉時那個資料夾還會原封不動保留在那邊***

我們就可以利用這個特性保留容器裡面的資料

## 1. 新增一個 volume

我們新增了一個 volume 叫做 db-data，完成之後可以看到多一個 volume，這時候 docker 已經在本機上新增一個資料夾要給 volume 用

```
> docker volume create --name db-data
> docker volume ls
```

## 2. 使用 volume

在啟動時加一個 `-v` 參數，就可以指定 volume 要跟容器內哪一個資料夾連通，這邊用的是 `/db/data`，實際上使用時可以換成資料庫存放資料的路徑

demo 一下：
 \1. 剛開始先確認 `/db/data` 裡面什麼檔案都沒有
 \2. 接著在容器內新增一個檔案 `file`
 \3. 最後再確認檔案在不在

```
> docker run -v db-data:/db/data -it ubuntu ls -l /db/data
> docker run -v db-data:/db/data -it ubuntu touch /db/data/file
> docker run -v db-data:/db/data -it ubuntu ls -l /db/data
```



值得留意的是***這三個指令是跑在不同的容器裡面***，所以也就證明瞭***當容器被關掉時，資料確實還有保存在 volume 內***，而且下個容器可以成功讀到上個容器留下的資料



# Host Volume

上面那種先 `create` 再使用的 volume 稱作 **named volume**，而現在要介紹另外一種叫做 **host volume**，用來直接***指定某個資料夾***跟容器內的資料夾連通

來一段 demo：
 \1. 檢查 `~/app` 內沒有 `package.json`
 \2. 指定本機的 `~/app` 跟容器內的 `/app` 連通，接著在容器內跑 `yarn init`
 \3. 跑完再回本機確認有沒有生出 `package.json`

```
> ls app
> docker run -v ~/app:/app --workdir /app node yarn init -y
> ls app
```



上面例子中的 `package.json` 其實是在容器內生成的，所以有了 volume 之後就可以不用裝 yarn 卻還是可以跑 `yarn init`

同理，你也可以不用裝 `g++` 就能編譯 C++ 原始碼、不用裝 JDK 就可以開發 Java 程式、甚至不用裝 mongodb 就可以用他來存資料，整台電腦只要裝一個 docker，真是太神了🎉🎉



## 總結

這篇講了兩種 volume 希望大家都有看懂，如果想更深入瞭解可以看看[官方文件](https://docs.docker.com/storage/volumes/)，在往後的章節為了保存資料將會很常用到他

下一篇要講的是如何將一個應用拆分成多個 container，讓他們分工合作構成你的應用程式，有興趣的人歡迎追蹤我，謝謝大家～

**參考**

**Docker** **實戰系列（三）：使用 Volume 保存容器內的數據 – Larry・Blog**

https://larrylu.blog/using-volumn-to-persist-data-in-container-a3640cc92ce4