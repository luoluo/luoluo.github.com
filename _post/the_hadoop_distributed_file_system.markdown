---
layout: post
title: "HDFS分布式文件系统"
date: 2018-03-29 20:45
comments: true
categories: [BigData, Note]
---

####HDFS简介

>HDFS is a filesystem designed for storing very large files with streaming data access patterns, running on clusters of commondity hardware.

####背景
简述一下背景，随着智能设备普及、网络基础升级，全民在生产信息、消费信息、交换信息，信息浩如烟海，却蕴藏着无限的机会。想要挖出金子，先得有座金矿，这里我们要自己建金矿，把数据存下来。但眼前压着几座大山：数据量大，最直接的困难，加机器（最直接的解决办法）；于是集群大、故障频繁；而数据处理往往只读部分数据，大文件的读取太慢；同时数据来自部分机器，大部分机器空闲，资源被充分浪费。为了解决以上种种，先知为我们带来了HDFS。

####目标

+ 大容量、大文件（PB级别）
+ 高容错（无惧宕机）
+ 高带宽利用（读取飞快）

####核心思路

+ 大容量的实现主要依赖于集群，通过构建分布式存储集群，来将存储问题分而治之。    
+ 高容错的实现主要依赖于备份，多备份，跨机器备份、跨机架（rack）备份，同时分块备份。    
+ 高带宽的实现主要依赖于拆分，将单个大文件拆分为若干文件，散步于多机器，读取速度、处理速度正比与集群规模。    
+ 数据块（block/chunk），将大文件拆分，提升读取性能、备份容错效率。   
+ 设计场景为：顺序读，批处理场景，非随机读；读写模型：写一次、读多次、增量写。    
+ 控制流与数据流分离，元信息与数据信息分离。

####主要架构

<div class="image-div"> <img class="content-image" src="/static/img/hdfs_overview.png" alt="x" /> </div>

Block   

+ HDFS上的文件被拆分为固定大小的块，大文件查询次数减少
+ meta信息少，NameNode压力小
+ 存储大文件成为可能，文件可以超过单个硬盘大小
+ 备份、恢复更为容易

Namenode 

+ 管理namespace树（文件系统树及权限信息）
+ block与DataNode对应关系
+ namespace树及元信息全部存于内存
+ namespace树及元信息，持久化至内存由checkpoint（存量base）和journal（增量修改）组成

DataNode    

+ 存储应用数据，即Block
+ Block由数据本身和block元信息组成
+ 集群启动阶段，DataNode向NameNode注册
+ 集群运行中，DataNode向NameNode发送heartbeats，以确认DataNode可用性
+ 若NameNode对DataNode心跳检测失败，则创建新DataNode，并做数据迁移


#### Data Flow
File read     
<div class="image-div"> <img class="content-image" src="/static/img/hdfs_read.png" alt="x" /> </div>
1. HDFS client 请求 NameNode，获取对应文件的 block locations
2. NameNode返回一组DataNode，每个DataNode均包含一份数据副本
3. HDFS client采取就近原则，选取一个DataNode读取数据
4. Client读取同时进行数据校验，若读取交互报错，则选取其他DataNode读取
5. HDFS client直接由DataNode读取数据，NameNode不做数据转发

File write    
<div class="image-div"> <img class="content-image" src="/static/img/hdfs_write.png" alt="x" /> </div>
1. HDFS client 请求 NameNode，在namespace内申请新文件名
2. NameNode若确认可创建，创建文件记录；否则返回失败
3. Client将待写文件拆包，写入到一个内部队列
4. NameNode在DataNode开辟新block，供内容多备份写入
5. DataNode将内容写入新block，完成后答复ack
6. 写入完成后，NameNode已包含全部新block位置信息

#### Replica

<div class="image-div"> <img class="content-image" src="/static/img/hdfs_rack.png" alt="x" /> </div>
大型集群的DataNode组织呈树状结构，而非平铺。同一机架（rack）DataNode共享交换机；不同机架（rack）见通过核心交换机链接.

Replica Placement原则：

1. 任何DataNode均不包含重复Block
2. 任何rack都不会包含同一Block两个以上备份（在rack充足的前提下）
3. 考虑NameNode的负载（Disk使用率、带宽使用率），集群均衡、利用率高

Replica Management:

1. NameNode保证Block的备份数符合标准，解决under-replicated、over-replicated
2. NameNode检查Block在DataNode和Rack上的分布情况
3.


####HA

NameNode:

+ CheckpointNode: 周期性合并当前checkpoint和journal来得到最新image
+ BackUpNode: 订阅journal流来维护NameNode的内存镜像，实现只读NameNode
+ NFS filer: 网络文件系统，共享journal实现ha
+ QJM：为提供ha journal而设计

DataNode:

+ 心跳检测机制，DataNode不可用时，NameNode新建DataNode，数据迁移
+ DataNode周期性数据校验数据，数据不可以时，做数据迁移
+ 数据校验算法支持增量快速重算

####相关项目

+ Hive [http://hive.apache.org/](http://hive.apache.org/)
+ Hadoop [http://hadoop.apache.org/](http://hadoop.apache.org/)
+ Spark  [http://spark.apache.org/](http://spark.apache.org/)
+ Pig  [http://pig.apache.org/](http://pig.apache.org/)
+ Tez [http://tez.apache.org/](http://tez.apache.org/)
+ Hbase [http://hbase.apache.org/](http://hbase.apache.org/)


####参考文献
+ The Hadoop Distributed File System
+ The Google File System
+ Hadoop The definitive Guide 4th Edition
+ apache hadoop [HDFS Architecture](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#Data_Organization)
+ The Hadoop Distributed File System [Slide](https://cs.uwaterloo.ca/~david/cs848s13/alex-presentation.pdf)
