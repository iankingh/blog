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

# kafka-eagle Kafka 可視化工具

## 步驟一：配置 KE_HOME

### windows ke.bat 可以指定路徑

```bat

set KE_HOME=D:\efak-web
set JAVA_HOME=D:\tools\jdk1.8.0_73

```

## 步驟二：配置文件修改


kafka 0.9.x以后的版本新增了advertised.listeners配置，kafka 0.9.x以后的版本不要使用 advertised.host.name 和 advertised.host.port 已经deprecated  
host.name 和 port 为 deprecated，使用listeners代替。  

listeners：就是主要用来定义Kafka Broker的Listener的配置项，listeners是kafka真正bind的地址。  
advertised.listeners：参数的作用就是将Broker的Listener信息发布到Zookeeper中，是暴露给外部的listeners，如果没有设置，会用listeners。  
listener.security.protocol.map：配置监听者的安全协议的，主要有以下几种协议：  
PLAINTEXT => PLAINTEXT 不需要授权,非加密通道  
SSL => SSL 使用SSL加密通道  
SASL_PLAINTEXT => SASL_PLAINTEXT 使用SASL认证非加密通道  
SASL_SSL => SASL_SSL 使用SASL认证并且SSL加密通道  

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
# EFAK enable distributed，启用分布式部署
######################################
efak.distributed.enable=false
# 设置节点类型slave or master
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
# kafka jmx 地址，默认Apache发布的Kafka基本是这个默认值，
# 对于一些公有云Kafka厂商，它们会修改这个值，
# 比如会将jmxrmi修改为kafka或者是其它的值，
# 若是选择的公有云厂商的Kafka，可以根据实际的值来设置该属性
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
# 关闭自带的sqlite数据库，使用外部的mysql数据库
######################################
#efak.driver=org.sqlite.JDBC
#efak.url=jdbc:sqlite:/hadoop/kafka-eagle/db/ke.db
#efak.username=root
#efak.password=www.kafka-eagle.org

######################################
# kafka mysql jdbc driver address
# 生產環境建議使用MySQL來存儲相關數據
######################################
efak.driver=com.mysql.cj.jdbc.Driver
efak.url=jdbc:mysql://localhost:3306/ke_schema?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&serverTimezone=UTC
efak.username=root
efak.password=ian22982
```

五、kafka eagle的启动
cmd 进入到 kafka eagle的 bin 目录下，输入 ke.bat，按回车键即可。

web UI：http://192.168.0.113:8048/
賬號密碼：admin/123456

默认端口号是 8048
用户名默认：admin
密码：123456

2）EFAK常用命令
$KE_HOME/bin/ke.sh啟動腳本中包含以下命令：

命令	描述
ke.sh 啟動	啟動EFAK 服務器。
ke.sh狀態	查看EFAK 運行狀態。
ke.sh 停止	停止EFAK 服務器。
ke.sh 重新啟動	重新啟動EFAK 服務器。
ke.sh統計數據	查看linux 操作系統中的EFAK 句柄數。
ke.sh 查找 [類名]	在jar 中找到類名的位置。
ke.shGC	查看EFAK 進程gc。
ke.sh版本	查看EFAK 版本。
ke.sh jdk	查看EFAK 安裝的jdk 詳細信息。
ke.sh 日期	查看EFAK 啟動日期。
ke.sh集群啟動	查看EFAK 集群分佈式啟動。
ke.sh集群狀態	查看EFAK 集群分佈式狀態。
ke.sh集群停止	查看EFAK 集群分佈式停止。
ke.sh集群重啟	查看EFAK 集群分佈式重啟



## Summary

## 參考  


[Kafka Eagle分布式模式 - 哥不是小萝莉 - 博客园 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/15732794.html)

[Kafka Eagle 3.0.1功能预览 - 哥不是小萝莉 - 博客园 (cnblogs.com)](https://www.cnblogs.com/smartloli/p/16728995.html)

[大数据Hadoop之——Kafka 图形化工具 EFAK（EFAK环境部署） - 大数据老司机 - 博客园 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16307589.html)

[大数据Hadoop之——EFAK和Confluent KSQL简单使用（kafka listeners 和 advertised.listeners） - 大数据老司机 - 博客园 (cnblogs.com)](https://www.cnblogs.com/liugp/p/16898002.html)

[(2条消息) 【kafka可视化工具】kafka-eagle在windows环境的下载、安装、启动与访问_kafka eagle windows_No8g攻城狮的博客-CSDN博客](https://blog.csdn.net/weixin_44299027/article/details/125378413)

[【kafka可视化工具】kafka-eagle在windows环境的下载、安装、启动与访问_51CTO博客_kafka 可视化工具](https://blog.51cto.com/no8g/6344266)
