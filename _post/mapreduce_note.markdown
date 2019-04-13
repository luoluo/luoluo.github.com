---
layout: post
title: "MapReduce框架详解"
date: 2018-02-19 10:40
comments: true
categories: [BigData, Note]
---

####Apache Hadoop简介

>The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. 

Apache Hadoop是一个分布式计算框架，采用极简的表述模型，在由多台计算机组成的机器集群上，分布式处理计算任务。

Apache Hadoop由以下几部分组成：

* Hadoop Common: 通用组件，以此来构建其他基础模块
* Hadoop Distributed File System (HDFS™): 分布式文件系统，提供数据访问高吞吐
* Hadoop YARN: 任务调度&集群资源管理器
* Hadoop MapReduce: 基于yarn实现的大数据并行处理框架

本文讲重点介绍Hadoop MapReduce。


####编程模型

MapReduce提供两种抽象：

	Map：
	（k1, v1）=> list(k2, v2)
	Reduce:
	  (k2, list(v2)) => list(v3)

抽象的好处:程序员只需专注业务，调度、分发、容错均由集群保证，大大降低研发成本及门槛。

屏蔽细节:

+  map输入分partition，reduce输入划分
+  计算资源、存储相关map和reduce的调度
+  Failover
+  数据分发

####举个栗子

最最经典的word-count

	map(String key, String value):
		// key: document name
		// value: document contents
		for each word w in value:
			EmitIntermediate(w, "1");

	reduce(String key, Iterator values):
		// key: a word
		// values: a list of counts
		int result = 0;
		for each v in values:
			result += ParseInt(v);
		Emit(AsString(result));

过程简述
<div class="image-div"> <img class="content-image" src="/static/img/mapreduce1.png" alt="x" /> </div>

1. 获取输入，并将输入分片
2. mapper读取输入，处理，输出
3. 将mapper输出按key排序，发送至对应reducer
4. reducer处理，输出


####更多例子

+ 分布式grep
+ 站点PV统计
+ 站点内链反向链接统计
+ 搜索引擎倒排索引构建
+ 分布式排序
+ ...

####执行过程概述
<div class="image-div"> <img class="content-image" src="/static/img/mapreduce2.png" alt="x" /> </div>

组成部分

+ an input reader
+ a Map function
+ a partition function
+ a compare function
+ a Reduce function
+ an output writer


####执行过程详述
<div class="image-div"> <img class="content-image" src="/static/img/mapreduce3.png" alt="x" /> </div>

+ Split: split input into M pieces, key space into R pieces.
+ Assign: M mapper task & R reducer task to idle workers.
+ Map run: read splitted input, transform by map function, buffer to memory.
+ Spill: Map write to local disk (partition) => pass info to master, then master info the reducer.
+ Shuffle: when notified, reducer start to read. On read end, reducer sort input.
+ Reducer run: iterate over the sorted key and corresponding value set pass to reduce function. Output is appended to the final output file.
+ Weak up user program, program returns to user code.

####Master 数据结构

Master存储的信息：map任务、reduce任务的执行状态；集群worker机器的状态（以供调度）   
Task的状态集：idle，in-process，complete

Master是map处理结果流转到reduce的中间人

+ 对于已完成的map任务，master存储R个分片结果地址
+ 每当map处理完成后，结果信息便存储至master
+ master立即将信息推送至处理中的reducer任务

####容错机制

Worker容错：

心跳检查来发现故障worker，master周期性ping所有worker，以发现故障worker。   
当worker故障，机器上的处理结果将无法访问，计算任务无法执行。故需其上`complete` map重置为`idle`，`in-process` map、reduce重置为`idle`，供重新调度执行。
当故障worker被新worker替代后，map任务重新执行信息将周知对应reduce。

Master容错：

通过check point机制来容错。

一致性保证：

对于map和reduce为`de-terministic functions`，则不论中间过程是否存在失败task，处理结果应相同。
通过`atomic commits`机制来保证处理一致性。    

+ map、reduce均将结果写至临时文件
+ map任务完成后，将结果文件信息提交至master，若master已接受过此map任务的信息，则后续信息将被忽略
+ reduce任务完成后，则重命名临时结果文件为最终输出文件，重命名过程具有原子性，由底层文件系统保证

####相关项目

+ Hive [http://hive.apache.org/](http://hive.apache.org/)
+ Hadoop [http://hadoop.apache.org/](http://hadoop.apache.org/)
+ Spark  [http://spark.apache.org/](http://spark.apache.org/)
+ Pig  [http://pig.apache.org/](http://pig.apache.org/)
+ Tez [http://tez.apache.org/](http://tez.apache.org/)
+ Hbase [http://hbase.apache.org/](http://hbase.apache.org/)
