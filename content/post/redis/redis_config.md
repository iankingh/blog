---
title: "Redis_config"
date: 2021-04-06T10:22:06+08:00
draft: true
categories:
 - "筆記"
tags:
 - "redis"
toc: true
typora-root-url: ..\..\..\static
---

## redis config
<!-- 簡介 -->
<!--more-->

windows : 

redis.windows-service.conf

linux : 







**redis設定檔**

```conf

1. Redis預設不是以守護進程的方式運行，可以通過該配置項修改，使用yes啟用守護進程
　　　　daemonize yes
 
  　　2. 當Redis以守護進程方式運行時，Redis預設會把pid寫入/var/run/redis.pid檔，可以通過pidfile指定
  
   　　　　pidfile /var/run/redis.pid
   
   　　3. 指定Redis監聽埠，默認埠為6379，作者在自己的一篇博文中解釋了為什麼選用6379作為默認埠，因為6379在手機按鍵上MERZ對應的號碼，而MERZ取自義大利歌女Alessia Merz的名字
 
  　　　　port 6379
  
  　　4. 綁定的主機位址
 
  　　　　bind 127.0.0.1 這個Ip要設置成你伺服器的Ip
  
  　　5.當 用戶端閒置多長時間後關閉連接，如果指定為0，表示關閉該功能
  
  　　　　timeout 300
 
  　　6. 指定日誌記錄級別，Redis總共支援四個級別：debug、verbose、notice、warning，默認為verbose
  
  　　　　loglevel verbose
 
  　　7. 日誌記錄方式，預設為標準輸出，如果配置Redis為守護進程方式運行，而這裡又配置為日誌記錄方式為標準輸出，則日誌將會發送給/dev/null
  
  　　　　logfile stdout
  
  　　8. 設置資料庫的數量，預設資料庫為0，可以使用SELECT <dbid>命令在連接上指定資料庫id
  
  　　　　databases 16
  
  　　9. 指定在多長時間內，有多少次更新操作，就將資料同步到資料檔案，可以多個條件配合
  
  　　　　save <seconds> <changes>
  
  　　　　Redis默認設定檔中提供了三個條件：
  　　　　　　save 900 1
  　　　　　　save 300 10
  　　　　　　save 60 10000
  　　　　分別表示900秒（15分鐘）內有1個更改，300秒（5分鐘）內有10個更改以及60秒內有10000個更改。
  
  　　10. 指定存儲至本地資料庫時是否壓縮資料，預設為yes，Redis採用LZF壓縮，如果為了節省CPU時間，可以關閉該選項，但會導致資料庫檔變的巨大
  
  　　　　rdbcompression yes
 
  　　11. 指定本地資料庫檔案名，預設值為dump.rdb
  
  　　　　dbfilename dump.rdb
  
  　　12. 指定本地資料庫存放目錄
  
  　　　　dir ./
  
  　　13. 設置當本機為slav服務時，設置master服務的IP位址及埠，在Redis啟動時，它會自動從master進行資料同步
  
  　　　　slaveof <masterip> <masterport>
  
  　　14. 當master服務設置了密碼保護時，slav服務連接master的密碼
  
  　　　　masterauth <master-password>
  
  　　15. 設置Redis連接密碼，如果配置了連接密碼，用戶端在連接Redis時需要通過AUTH <password>命令提供密碼，預設關閉
 
  　　　　requirepass foobared
  
  　　16. 設置同一時間最大用戶端連接數，默認無限制，Redis可以同時打開的用戶端連接數為Redis進程可以打開的最大檔描述符數，如果設置 maxclients 0，表示不作限制。當用戶端連接數到達限制時，Redis會關閉新的連接並向用戶端返回max number of clients reached錯誤資訊
  
  　　　　maxclients 128
  
  　　17. 指定Redis最大記憶體限制，Redis在啟動時會把資料載入到記憶體中，達到最大記憶體後，Redis會先嘗試清除已到期或即將到期的Key，當此方法處理 後，仍然到達最大記憶體設置，將無法再進行寫入操作，但仍然可以進行讀取操作。Redis新的vm機制，會把Key存放記憶體，Value會存放在swap區
 
  　　　　maxmemory <bytes>
  
  　　18. 指定是否在每次更新操作後進行日誌記錄，Redis在預設情況下是非同步的把資料寫入磁片，如果不開啟，可能會在斷電時導致一段時間內的資料丟失。因為 redis本身同步資料檔案是按上面save條件來同步的，所以有的資料會在一段時間內只存在於記憶體中。默認為no
  
  　　　　appendonly no
 
  　　19. 指定更新日誌檔案名，預設為appendonly.aof
  
  　　　　appendfilename appendonly.aof
  
  　　20. 指定更新日誌條件，共有3個可選值：
  
  　　　　no：表示等作業系統進行資料緩存同步到磁片（快） 
  　　　　always：表示每次更新操作後手動調用fsync()將資料寫到磁片（慢，安全） 
  　　　　everysec：表示每秒同步一次（折衷，預設值）
  　　　　appendfsync everysec
  
  　　21. 指定是否啟用虛擬記憶體機制，預設值為no，簡單的介紹一下，VM機制將資料分頁存放，由Redis將訪問量較少的頁即冷資料swap到磁片上，訪問多的頁面由磁片自動換出到記憶體中（在後面的文章我會仔細分析Redis的VM機制）
  
  　　　　vm-enabled no
  
  　　22. 虛擬記憶體檔路徑，預設值為/tmp/redis.swap，不可多個Redis實例共用
  
 　　　　vm-swap-file /tmp/redis.swap
  
  　　23. 將所有大於vm-max-memory的資料存入虛擬記憶體,無論vm-max-memory設置多小,所有索引資料都是記憶體存儲的(Redis的索引資料 就是keys),也就是說,當vm-max-memory設置為0的時候,其實是所有value都存在於磁片。預設值為0
  
 　　　　vm-max-memory 0
 
 　　24. Redis swap檔分成了很多的page，一個物件可以保存在多個page上面，但一個page上不能被多個物件共用，vm-page-size是要根據存儲的 資料大小來設定的，作者建議如果存儲很多小物件，page大小最好設置為32或者64bytes；如果存儲很大大物件，則可以使用更大的page，如果不 確定，就使用預設值
 
 　　　　vm-page-size 32

 　　25. 設置swap檔中的page數量，由於頁表（一種表示頁面空閒或使用的bitmap）是在放在記憶體中的，，在磁片上每8個pages將消耗1byte的記憶體。
 
 　　　　vm-pages 134217728
 
 　　26. 設置訪問swap檔的執行緒數,最好不要超過機器的核數,如果設置為0,那麼所有對swap檔的操作都是串列的，可能會造成比較長時間的延遲。預設值為4
 
 　　　　vm-max-threads 4
 
 　　27. 設置在向用戶端應答時，是否把較小的包合併為一個包發送，默認為開啟
 
 　　　　glueoutputbuf yes
 
 　　28. 指定在超過一定的數量或者最大的元素超過某一臨界值時，採用一種特殊的雜湊演算法

 　　　　hash-max-zipmap-entries 64
 
 　　　　hash-max-zipmap-value 512
 
 　　29. 指定是否啟動重置雜湊，默認為開啟（後面在介紹Redis的雜湊演算法時具體介紹）
 
 　　　　activerehashing yes
 
 　　30. 指定包含其它的設定檔，可以在同一主機上多個Redis實例之間使用同一份設定檔，而同時各個實例又擁有自己的特定設定檔
 
　　　　include /path/to/local.conf
 
注意：protected-mode參數是為了禁止外網訪問redis，如果需要外網訪問，需要設置為 no



```





## 參考
