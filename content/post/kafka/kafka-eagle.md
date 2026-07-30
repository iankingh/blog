---
title: "Kafka Eagle"
date: 2023-08-29T10:50:12Z
categories:
- "筆記"
tags:
- "tag1"
- "tag2"
toc: true
draft: true
---

<!-- 簡介 -->
<!--more-->

# kafka-eagle Kafka 視覺化工具

## 步驟一：配置 KE_HOME

### windows ke.bat 可以指定路徑

```bat

set KE_HOME=D:\efak-web
set JAVA_HOME=D:\tools\jdk1.8.0_73

```

## 步驟二：配置檔案修改


kafka 0.9.x以後的版本新增了advertised.listeners配置，kafka 0.9.x以後的版本不要使用 advertised.host.name 和 advertised.host.port 已經deprecated  
host.name 和 port 為 deprecated，使用listeners代替。  

listeners：就是主要用來定義Kafka Broker的Listener的配置項，listeners是kafka真正bind的地址。  
advertised.listeners：引數的作用就是將Broker的Listener資訊發布到Zookeeper中，是暴露給外部的listeners，如果沒有設定，會用listeners。  
listener.security.protocol.map：配置監聽者的安全協議的，主要有以下幾種協議：  
PLAINTEXT => PLAINTEXT 不需要授權,非加密通道  
SSL => SSL 使用SSL加密通道  
SASL_PLAINTEXT => SASL_PLAINTEXT 使用SASL認證非加密通道  
SASL_SSL => SASL_SSL 使用SASL認證並且SSL加密通道  

### system-config.properties

```properties
######################################
# multi zookeeper & kafka cluster list
# Settings prefixed with 'kafka.eagle.' will be deprecated, use 'efak.' instead
######################################
efak.zk.cluster.alias=cluster1
#cluster1.zk.list=tdn1:2181,tdn2:2181,tdn3:2181
cluster1.zk.list=localhost:2181
#cluster2.zk.list=xdn10:2181,xdn11:2181,xdn12:2181

######################################
# zookeeper enable acl
# Zookeeper是否啟用ACL
######################################
#cluster1.zk.acl.enable=false
#cluster1.zk.acl.schema=digest
#cluster1.zk.acl.username=test
#cluster1.zk.acl.password=test123

######################################
# broker size online list
######################################
cluster1.efak.broker.size=20

######################################
# zk client thread limit
######################################
kafka.zk.limit.size=16

######################################
# EFAK webui port
######################################
efak.webui.port=8048

######################################
# EFAK enable distributed
# EFAK enable distributed，啟用分散式部署
######################################
efak.distributed.enable=false
# 設定節點型別slave or master
# master worknode set status to master, other node set status to slave
efak.cluster.mode.status=master
efak.worknode.master.host=localhost
efak.worknode.port=8085

######################################
# kafka jmx acl and ssl authenticate
######################################
#cluster1.efak.jmx.acl=false
#cluster1.efak.jmx.user=keadmin
#cluster1.efak.jmx.password=keadmin123
#cluster1.efak.jmx.ssl=false
#cluster1.efak.jmx.truststore.location=/data/ssl/certificates/kafka.truststore
#cluster1.efak.jmx.truststore.password=ke123456

######################################
# kafka offset storage
######################################
cluster1.efak.offset.storage=kafka
#cluster2.efak.offset.storage=zk

######################################
# kafka jmx uri
# kafka jmx 地址，預設Apache發布的Kafka基本是這個預設值，
# 對於一些公有云Kafka廠商，它們會修改這個值，
# 比如會將jmxrmi修改為kafka或者是其它的值，
# 若是選擇的公有云廠商的Kafka，可以根據實際的值來設定該屬性
######################################
cluster1.efak.jmx.uri=service:jmx:rmi:///jndi/rmi://%s/jmxrmi

######################################
# kafka metrics, 15 days by default
######################################
efak.metrics.charts=true
efak.metrics.retain=15

######################################
# kafka sql topic records max
######################################
efak.sql.topic.records.max=5000
efak.sql.topic.preview.records.max=10

######################################
# delete kafka topic token
######################################
efak.topic.token=keadmin

######################################
# kafka sasl authenticate
# kafka ssl 安全認證是否開啟
######################################
#cluster1.efak.sasl.enable=false
#cluster1.efak.sasl.protocol=SASL_PLAINTEXT
#cluster1.efak.sasl.mechanism=SCRAM-SHA-256
#cluster1.efak.sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="kafka" password="kafka-eagle";
#cluster1.efak.sasl.client.id=
#cluster1.efak.blacklist.topics=
#cluster1.efak.sasl.cgroup.enable=false
#cluster1.efak.sasl.cgroup.topics=
#cluster2.efak.sasl.enable=false
#cluster2.efak.sasl.protocol=SASL_PLAINTEXT
#cluster2.efak.sasl.mechanism=PLAIN
#cluster2.efak.sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="kafka" password="kafka-eagle";
#cluster2.efak.sasl.client.id=
#cluster2.efak.blacklist.topics=
#cluster2.efak.sasl.cgroup.enable=false
#cluster2.efak.sasl.cgroup.topics=

######################################
# kafka ssl authenticate
######################################
#cluster3.efak.ssl.enable=false
#cluster3.efak.ssl.protocol=SSL
#cluster3.efak.ssl.truststore.location=
#cluster3.efak.ssl.truststore.password=
#cluster3.efak.ssl.keystore.location=
#cluster3.efak.ssl.keystore.password=
#cluster3.efak.ssl.key.password=
#cluster3.efak.ssl.endpoint.identification.algorithm=https
#cluster3.efak.blacklist.topics=
#cluster3.efak.ssl.cgroup.enable=false
#cluster3.efak.ssl.cgroup.topics=

######################################
# kafka sqlite jdbc driver address
# 關閉自帶的sqlite資料庫，使用外部的mysql資料庫
######################################
#efak.driver=org.sqlite.JDBC
#efak.url=jdbc:sqlite:/hadoop/kafka-eagle/db/ke.db
#efak.username=root
#efak.password=www.kafka-eagle.org

######################################
# kafka mysql jdbc driver address
# 生產環境建議使用MySQL來儲存相關資料
######################################
efak.driver=com.mysql.cj.jdbc.Driver
efak.url=jdbc:mysql://localhost:3306/ke_schema?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&serverTimezone=UTC
efak.username=root
efak.password=<YOUR_DATABASE_PASSWORD>
```

五、kafka eagle的啟動
cmd 進入到 kafka eagle的 bin 目錄下，輸入 ke.bat，按回車鍵即可。

web UI：http://192.168.0.113:8048/
賬號密碼：admin/123456

預設埠號是 8048
使用者名稱預設：admin
密碼：123456

2）EFAK常用命令
$KE_HOME/bin/ke.sh啟動指令碼中包含以下命令：

命令	描述
ke.sh 啟動	啟動EFAK 伺服器。
ke.sh狀態	檢視EFAK 執行狀態。
ke.sh 停止	停止EFAK 伺服器。
ke.sh 重新啟動	重新啟動EFAK 伺服器。
ke.sh統計資料	檢視linux 作業系統中的EFAK 控制程式碼數。
ke.sh 查詢 [類名]	在jar 中找到類名的位置。
ke.shGC	檢視EFAK 程式gc。
ke.sh版本	檢視EFAK 版本。
ke.sh jdk	檢視EFAK 安裝的jdk 詳細資訊。
ke.sh 日期	檢視EFAK 啟動日期。
ke.sh叢集啟動	檢視EFAK 叢集分散式啟動。
ke.sh叢集狀態	檢視EFAK 叢集分散式狀態。
ke.sh叢集停止	檢視EFAK 叢集分散式停止。
ke.sh叢集重啟	檢視EFAK 叢集分散式重啟



## Summary

## 參考  


[Kafka Eagle分散式模式 - 哥不是小蘿莉 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/15732794.html)

[Kafka Eagle 3.0.1功能預覽 - 哥不是小蘿莉 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/16728995.html)

[大資料Hadoop之——Kafka 圖形化工具 EFAK（EFAK環境部署） - 大資料老司機 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16307589.html)

[大資料Hadoop之——EFAK和Confluent KSQL簡單使用（kafka listeners 和 advertised.listeners） - 大資料老司機 - 部落格園 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16898002.html)

[(2條訊息) 【kafka視覺化工具】kafka-eagle在windows環境的下載、安裝、啟動與訪問_kafka eagle windows_No8g攻城獅的部落格-CSDN部落格](https://blog.csdn.net/weixin_44299027/article/details/125378413)

[【kafka視覺化工具】kafka-eagle在windows環境的下載、安裝、啟動與訪問_51CTO部落格_kafka 視覺化工具](https://blog.51cto.com/no8g/6344266)
