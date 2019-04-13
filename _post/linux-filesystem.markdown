---
layout: post
title: "常见文件系统性能"
date: 2013-04-25 21:26
comments: true
categories: [Tech]
---

######本文为一篇译文，[原文](http://oss.sgi.com/projects/xfs/papers/filesystem-perf-tm.pdf)
Linux上流行的文件系统：*Ext2, Ext3, ReiserFS,XFS, and JFS*(2002)

###Filesystem Descriptions

####2.1 Ext2
由Wayne Davidson设计, 是ext文件系统的加强版。Ext2 是standard Linux filesystem. 

####2.2 Ext3
Ext3是一种日志式文件系统，是对ext2系统的扩展，它兼容ext2。

####2.3 ReiserFS
由Hans Reiser开发, ReiserFS 成为standard Linux Kernel的部分（自2.4.1起）。
ReiserFS 使用B\*平衡树来组织 描述符、文件、数据。ReiserFS 支持节省空间策略(tailpacking),把小文件移到B\*树的叶子。

####2.4 XFS

XFS 是journaling filesystem支持*元数据journaling*
XFS 使用allocation groups 和 extentbased allocations 来提高磁盘上数据的Locality(空间局部性).目前XFS并不是标准Linux 的一部分。

####2.5 JFS
IBM的JFS [JFS], 起源于AIX,被移植到OS/2‚后又回到AIX并支持Linux.
JFS的技术优势有：extent-based storage allocation, variable block
sizes, dynamic disk inode allocation, and sparse and dense file support. 

JFS 是一个journaling 文件系统支持metadata logging.
尽管JFS不属于 standard Linux kernel，但是有patchsets.


###优势对比

1) 总体而言,Ext2的表现要优于Ext3.
一般情况下，Ext3 在data=writeback时和
data=ordered时效率一样. 在某些特定条件下，
Ext3 data=ordered 时快些；而有些时候，
data=writeback快. 当系统比较大时，Ext3(data=writeback)表现优于Ext2.

2) 对小文件(平均<=5KB)和频繁的文件操作,ReiserFS能表现最好。

3) 对File-I/O频繁的工作，如pgmeter，所有的文件系统表现相近。

4) 当性能次重要时，对小系统和频繁文件操作的系统，XFS和JFS都不是好选择。

5) 对小的SMP systems 如medium system,对顺序读工作，XFS和JFS都是很好的选择

6) JFS对SMP(对称多处理)随线程数增加而表现乏力。

7) 对于有大量的I/O操作的大系统，XFS性能最优.

###日志文件系统(Journaling file system)
Journaling file system is a file system that keeps track of the changes that will be made in a journal (usually a circular log in a dedicated area of the file system) before committing them to the main file system. In the event of a system crash or power failure, such file systems are quicker to bring back online and less likely to become corrupted.    

日志文件系统是跟踪磁盘内容的变化，记录文件改变到一个日志里，而记录动作是在将改变提交到主文件系统前的发生的。即当系统意外（如断电）中断时，下次启动时读取日志记录文件就可以恢复未完成的写操作，而这只需几秒。
