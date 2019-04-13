---
layout: post
title: "My Little Tips"
date: 2013-07-19 16:09
comments: true
categories: [Skill, Languages]
---
*1.How to copy between two terminals using vim?*

    1.open file a
    2.copy the items (using yy)
    3.close file a (Main point)
    4.open file b
    5.paste the items
    6.save and exist file b

*2.How to open a url in python*
{% highlight python %}
url = urllib2.quote(url.encode("utf8"))
{% endhighlight %}

*3.How to load json in python*
{% highlight python %}
f = urllib2.urlopen(url)
ff = f.read()
jdata = simplejson.loads(ff)
{% endhighlight %}

Or

{% highlight python %}
f = urllib2.urlopen(url)
jdata = simplejson.load(f)
{% endhighlight %}

*4.How to reverse a Hash table in ruby*

1.convert the Hash to an Array
2.reverse the Array 
3.convert the Array to a Hash 
{% highlight ruby %}
reversed_h = Hash[h.to_a.reverse]
{% endhighlight %}

*5.How to view the System version*

	cat /etc/issue

*6.How to unzip xx.tar.bz2 file*

	unzip xx.tar.bz2
	bzip2 -d xx.tar.bz2 ===> xx.tar
	tar -xvf  xx.tar ===> xx

*7.Why markdown List don't work correctly with Chinese*

**code**

	1. 得到这个世界中已经创建好的账
	2. 不断接收这个世界被广播出
	3. 猜一个幸运随机

**result**

1. 得到这个世界中已经创建好的账
2. 不断接收这个世界被广播出
3. 猜一个幸运随机

*Don't work as we wish. _I found when there is an Endlish word or a digit it would work fine._*

**code**

	1. 得到这个世界中已经创建好的账x 
	2. 不断接收这个世界被广播出23
	3. 猜一个幸运随机n

**result**

1. 得到这个世界中已经创建好的账x 
2. 不断接收这个世界被广播出23
3. 猜一个幸运随机n


*8.How to get public key?*

**Don't have one**

	guest-K9BGsj@ubuntu:~$ ssh-keygen 
	Generating public/private rsa key pair.
	Enter file in which to save the key (/tmp/guest-K9BGsj/.ssh/id_rsa): 
	Created directory '/tmp/guest-K9BGsj/.ssh'.
	Enter passphrase (empty for no passphrase): 
	Enter same passphrase again: 
	Your identification has been saved in /tmp/guest-K9BGsj/.ssh/id_rsa.
	Your public key has been saved in /tmp/guest-K9BGsj/.ssh/id_rsa.pub.
	The key fingerprint is:
	ff:99:ec:33:35:ae:d8:8a:9f:20:06:13:11:1b:56:e6 guest-K9BGsj@ubuntu
	The key's randomart image is:
	+--[ RSA 2048]----+
	|    =oo          |
	|   . *           |
	|    o E          |
	|     .           |
	|    o   S        |
	|     o   .    o  |
	|      o . .  o . |
	|     . . o *oo.  |
	|        ..=oO+   |
	+-----------------+
	guest-K9BGsj@ubuntu:~$ 

**Have one**

	guest-K9BGsj@ubuntu:~$ cd .ssh/
	guest-K9BGsj@ubuntu:~/.ssh$ ls
	id_rsa  id_rsa.pub
	guest-K9BGsj@ubuntu:~/.ssh$ cat id_rsa.pub 
	ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGiRONM/cuVGJxcTDSdPbs8WvnGNSKbxIZtK5pX8CIlSXl8+k67GOJygk5QO2uTp35+SohVHS9z4+4grTmVSBLKrDTv6eE0p9H0WV0RUJZsfoS+GG6aa+Omc8pweG/WsDzcDzUpFzCRz+BT7iQs+AXE/mdKgTjm0aRmBSLkpq0pXYmp49WK205MCInD5tiKd9o8CTrmXhy31IjO4qa8Nh+lJ9NYHvA4TH4fBSTAkYyzz12uymfmQ4J5ZeLxmLZDBbm7V7fJQZwNe4uKKUu0DeQ3gvVBZqqjnbTXJm2qR1sMPM9393EtP+E20FskgE9g3lONxA7ZtR8nW7SUyvGLWzN guest-K9BGsj@ubuntu
	guest-K9BGsj@ubuntu:~/.ssh$ 

*9.How to ssh and get a file form the host*

**Login to the server using _ssh_**

	lo@ubuntu:~$ ssh aaa@10.10.7.41
	aaa@10.10.7.41's password: 
	Linux 111012d102 2.6.35-32-server #67-Ubuntu SMP Mon Mar 5 21:13:25 UTC 2012 x86\_64 GNU/Linux
	Ubuntu 10.10
	
	Welcome to the Ubuntu Server!
	 * Documentation:  http://www.ubuntu.com/server/doc
	New release 'natty' available.
	Run 'do-release-upgrade' to upgrade to it.
	
	Last login: Wed Aug  7 17:38:51 2013 from 120915d101.aaa.com
	aaa@111012d102:~$ 
	
**Get the file from sever using _scp_**

	lo@ubuntu:~$ scp aaa@10.10.7.41:/directory/to/somefile ./
	aaa@10.10.7.41's password: 
	somefile		100% 1675     1.6KB/s   00:00    
	lo@ubuntu:~$ 

*10.Copy and Paste from terminal with keyboard in linux*

	`shift` + `ctrl` + c		#to copy
	`shift` + `ctrl` + v		#to paste

