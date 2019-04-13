---
layout: post
title: "Gdb 使用笔记"
date: 2013-12-19 18:52
comments: true
categories: [Tools, Skill]
---
####1.在Debug之前，编译时允许debug.
    
    g++ -g xxx.cpp -o xxx

####2.使用gdb来debug,常用命令：

    gdb xxx    	# 开始debug
    break   	# 设置断点
        break function-name/line-number/ClassName::funcName
    delete/d  	# 删除断点
        delete 	# 删除所有断点，观察点，捕捉点
        delete breakpoint-number-or-range
    run     	# 开始运行

    where    	# 显示当前执行和所在函数
    next/n    	# 执行下一条语句,不进入函数
    continue/c 	# 执行到下一个 断点 前
    until
        until line-number
    step/s    	# 执行下一条语句，会进入函数
    finish    	# 执行到当前函数结束

    info
        info frame
        info args
        info locals

    list/l    	# 列出代码
        list line-number/function/start#,end#
    
    print/p    	# 打印变量的值
        print variable-name
        print *array-variable@length
        
    quit/q    	# 退出GDB
    
####3.gdb对STL的支持.
使用**GDB**打印*vector*、*stack*等抽象STL数据结构是，打印出的内容是无意义的。而GDB 7.0就支持 pretty-printers. 把pretty-printers 和 libstdc++ 组合起来就产生了打印 C++ 容器的最好工具，具体操作如下：    

    1.将Python libstdc++ printer check out 到本地。
    svn co svn://gcc.gnu.org/svn/gcc/trunk/libstdc++-v3/python
    2.把以下内容加到~/.gdbinit.
    python
    import sys
    sys.path.insert(0, '/path/to/gdb_printers/python')
    from libstdcxx.v6.printers import register_libstdcxx_printers
    register_libstdcxx_printers (None)
    end    
    注意，以上的路径要一致，即.gdbinit里的路径和实际check out的地址要一致。

####4.gdb对多线程的支持.

	1. kill -11 pid			 # 手动触发core： 
	2. gdb bin core.xxx 	 # gdb 调试：
	3. (gdb) info threads    # 展示所以线程
	4. (gdb) thread 4        # 切换至特定线程
	5. (gdb) bt              # 打印栈信息
	6. thread apply [thread-id-list] [all] args   # 打印出所有进程的情况

####5.gdb代码搜索路径

	1. directory 			 		# 重置源码路径为默认值('$cdir:$cwd')
	2. set directories path-list	# 添加path-list到搜索路径
	3. show directories				# 打印当前搜索路径
