---
layout: post
title: "Linux shell 总结"
date: 2018-02-13 13:16
comments: true
categories: Wiki
---

    常用命令汇总：

    文本处理：
    cat
    less
    head/tail
    sort
    vim
    wc
    grep
    cp/mv/rm
    awk
    sed
    diff
    echo
    printf

    文件处理：
    ls
    ln
    tree
    tar
    du
    find
    file
    ldd
    iconv

    任务管理：
    ctrl + z/c/r/b/f
    jobs/fg/bg
    source
    date
    xargs

    系统处理：
    sudo
    chmod
    passwd
    bashrc/bash_profile
    export
    netstat

    文件传输：
    scp
    wget
    lftp

文本处理相关：

    vim

        vim regex 匹配使用group: `s/\(xx\)ad\(xx\)/xx\1\2/g`
        vim 显示隐藏字符：`set list`
        vim 扩大文件之间的copy行数到100 `:set viminfo='100,<100,s10,h`
        vim case casting:
            vim to UPPER CASE gU
            vim to downcase  gu
            vim to opposite case g~
        vim 换行 %s/html:/&\r/g
        vim buffer:
        set noexpa
        shift+3  高亮当前代码
        :g/^$/d   去除空行
        %s/xx/&\r/g 换行
        vim移动窗口位置
          Control + w && shitf + hjkl
          vim 在窗口间移动光标 Control + w && hjkl
        vim 忽略大小写，/simple\c
        
        vim restore the cursor position:
        " put those line to .vimrc
        au BufReadPost *
            \ if line("'\"") > 0 && line("'\"") <= line("$") && &filetype != "gitcommit" |
                \ execute("normal `\"") |
            \ endif

    sed
        sed 's/[\t]//g' test.txt > out.txt
        sed 's/[\x09]//g' test.txt > out.txt
        sed -e 's/^A/xxx/g' file > newFile

    iconv
        iconv -f encoding -t encoding inputfile
        iconv -f GBK -t UTF-8 file1 -o file2

	grep/awk # TODO


任务管理：

    进程前后台操作相关:
		Ctrl + C 	# 退出前台命令执行，回到shell
    	Ctrl + Z 	# 暂停前台命令执行，回到shell
    	jobs 		# 查看当前在后台执行命令，可查看进程号码
    	&			# 运行命令时，在末尾添加&,使得命令在后台执行
    	fg N 		# 将命令进程号码为N的进程，放到前台执行
    	bg N		# 将命令进程号码为N的进程，放到后台执行
		2>&1 		# 将标准错误输出 输出到标准输出
		nohup		# 使程序后台执行，并忽略HUP信号（用户注销，网络端口引起）

    date
        date -d
        date -d "1 day ago" 
        date -d "1 day ago" +%Y%m%d
        date +%Y%m%d
        date --date='20140902 2 day' +%Y%m%d
        date --date='20140902 2 days ago' +%Y-%m-%d

    source
    	source demo.sh 	# 逐行读取demo.sh并逐行执行，在当前shell环境中
    	. demo.sh 		# 与source demo.sh等同
    	./demo.sh 		# 将demo.sh当做可执行文件，并建立新shell环境来执行

文件处理：

    文件压缩解压
		tar -zcvf xx.tgz xx 	# 将xx压缩至xx.tgz，xx可以为一批文件
		tar -zxvf xx.tgz		# 解压xx.tgz
		unzip xx.tar.bz2
		bzip2 -d xx.tar.bz2 => xx.tar
		tar -xvf  xx.tar => xx

    链接文件
        ln -s path/to/file linkName # 建立指向路径path/to/file的软链
        unlink linkName				# 
        rm linkName
        ln -rf linkName
        Not!!! ln -fr linkName/

    文件查找
        find start_path -name file_to_find
        find /home/work -name my.sh
        find . -name "*py" | xargs cat | wc -l
        find . -type d -name ".svn" | xargs rm -fr 
        find . -type f -exec rm -v {} \;
        find . -type f -print -delete
        find . -name "*.md5" -exec md5sum -c {} \;
        find . -name "*.md5" | xargs -i md5sum -c {}

	文件传输：
        lftp -u user,pwd host:/path/to/file	# 查看带user/pwd的内容
        wget --ftp-user=xxx --ftp-password=xxx ftp://host:/path/to/file # 指明user、passwd
        wget --no-check-certificate ftp://host:/path/to/file # 不验证https安全性
		scp local_file remote_username@remote_ip:remote_folder
		scp -r local_dir remote_username@remote_ip:remote_folder

系统状态：

    show machine hardware info
        lscpu
        cat /proc/meminfo		# 空闲内存情况
		cat /etc/redhat-release # 查看centos版本
		cat /etc/issue 	 		# 查看centos版本
		free -h					# 空闲内存情况
      

    show user login info:
    	last 	# Show a list of last logged in user
    	uptime 	# Tell how long system been running

	添加用户
		sudo adduser thegeek    


Mysql相关：

    mysql dump
        mysqldump -u root -ppassword tablename --no-data > tablename.sql
        mysql -u root -ppassword tablename < tablename.sql
        mysql set name gbk

    mysql alter table
        alter table aka_audit_output_hour change   ideaid ideaid bigint;
        alter table aka_audit_output_hour change   audit_pipe audit_type string

    mysql function
        select count(distinct idvisit) AS counted,
            FROM_UNIXTIME(TRUNCATE(UNIX_TIMESTAMP(server_time)/900.0,0)*900)
            AS sv_time_d
            FROM visits group by server_time_ed
        select lpad(id, 4, '0000') from t1;
        select substring_index("/test/examplepath/use/rlo/g.txtasdf", '/', 3);


shell语言：

    目录是否存在
    if [ -d "$DIRECTORY" ]; then
      # Control will enter here if $DIRECTORY exists.
    fi

    shell 获取命令的输出值
    count=$(ls |　wc -l)

    shell 的参数
		$# 参数个数  
		$1 $2 .. $n 第一、第二、第n个参数

    '' 与 "" 的区别 

    数组
		shell里变量的类型不是特别明确，字符串和变量可以混用，关键是看参与什么运算；
    	数组可以用字符串来表示  
		days="1 2 3 4 5"
    	for day in days;do
         	echo $day;
    	done

    	## declare an array variable
    	declare -a arr=("element1" "element2" "element3")
    	## now loop through the above array
    	for i in "${arr[@]}"do
    	    echo "$i"
    	# or do whatever with individual element of the array
		done

	> 和 >>
    	> 	# write to，清除旧内容
		>> 	# write append，不清除旧内容 
 
    sleep
    	sleep <nubmer>s/m/h/d   #sleep number秒/分钟/小时/天 
    
    执行一条字符串
    	cmd="date +Y%m%d"
    	eval $cmd
    	val=$(eval $cmd)


    printf与echo
		printf会对\n做转义的echo
    	echo -e "Hello\nworld"
    	echo -e 'Hello\nworld'
    	echo Hello$'\n'world
    	echo $'hello\nworld'
    	printf "hello\nworld\n"

    base64 in terminal
    	openssl enc -base64 <<< fengkong-hadoop #hadoop的密码居然不能有等号
    	openssl enc -base64 <<< fengkonghadoop
    	echo `echo xxxx | base64 --decode`

小技巧：

    ssh keep alive login
    	o@o:~$ cat ~/.ssh/config 
    	Host *
    	ServerAliveInterval 60
    	ControlMaster auto
    	ControlPath ~/.ssh/master-%r@%h:%p
    	ControlPersist yes

	ssh-keygen 
		ssh key生成

