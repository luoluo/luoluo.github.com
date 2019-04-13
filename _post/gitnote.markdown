---
layout: post
title: "Git note"
date: 2013-08-08 19:50
comments: true
categories: [Tools, Skill]
---
###-1.Error:
	lo@ubuntu:~/try/java/test$ git push origin master
	To git@github.com:luoluo/test.git
	 ! [rejected]        master -> master (non-fast-forward)
	error: failed to push some refs to 'git@github.com:luoluo/test.git'
	hint: Updates were rejected because the tip of your current branch is behind
	hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
	hint: before pushing again.
	hint: See the 'Note about fast-forwards' in 'git push --help' for details.
	lo@ubuntu:~/try/java/test$ git pull
	ssh_exchange_identification: Connection closed by remote host
	fatal: The remote end hung up unexpectedly
	lo@ubuntu:~/try/java/test$ git pull --rebase
	There is no tracking information for the current branch.
	Please specify which branch you want to rebase against.
	See git-pull(1) for details
	
	    git pull <remote> <branch>
	
	If you wish to set tracking information for this branch you can do so with:
	
	    git branch --set-upstream master origin/<branch>
	
	lo@ubuntu:~/try/java/test$ 

####solution1:
	lo@ubuntu:~/try/java/test$ git push -f origin master
	Counting objects: 62, done.
	Compressing objects: 100% (55/55), done.
	Writing objects: 100% (62/62), 31.05 KiB, done.
	Total 62 (delta 12), reused 0 (delta 0)
	To git@github.com:luoluo/test.git
	 + 7cd94a0...7785ccf master -> master (forced update)
	lo@ubuntu:~/try/java/test$ 

####solution2:
	lo@ubuntu:~/config$ git pull --rebase origin master
	From github.com:luoluo/config
	 * branch            master     -> FETCH_HEAD
	First, rewinding head to replay your work on top of it...
	Applying: config
	lo@ubuntu:~/config$ ls
	README.md
	lo@ubuntu:~/config$
###0.Error:fatal: remote origin already exists
	lo@ubuntu:~/try/java/test$ git remote add origin git@github.com:luoluo/test.git
	fatal: remote origin already exists.
####solution:
	git remote rm origin
	git remote add origin git@github.com:luoluo/test.git
###1.Pretty git branch graphs
####Wtire in ~/.gitconfig
{% highlight sh %}
[user]
	name = luoluo
	email = luoluo1920@gmail.com
[alias]
	log1 = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
	log2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
{% endhighlight %}
###2.Error master branch and 'origin/master' have diverged

####Status
	... o --- o --- A --- B origin/master (upstream work)
	                 \
	                  C master (your work)
####Solution 1
	git merge origin/master
	... o --- o --- A --- B origin/master (upstream work)
	                 \     \
	                  C --- M master (your work)

####Solution 2
	git rebase origin master
	... o --- o --- A --- B origin/master (upstream work)
	                       \
	                        C' master (your work)

####Best Solution
	git pull --rebase
###3.Errot Your branch is ahead of 'origin/master' by 2 commits.
####Solution 1
	git reset --hard origin/master  #Not good enough
####Solution 2
	git push origin master
###4.git pull Error
	git pull
	Updating b84f92b..5c60a57
	error: Your local changes to the following files would be overwritten by merge:
		src/appsearch/indexserve/src/main/java/com/dolphin/estore/appsearch/QueryBuilder.java
		src/appsearch/indexserve/src/main/java/com/dolphin/estore/appsearch/test/SearchTest.java
	Please, commit your changes or stash them before you can merge.
	Aborting
	git stash
	git pull
	git stash pop

###5.Error On branch master
####On branch master Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
###6. Error 
	git push -u origin master
	ERROR: Permission to user/repo denied to user/repo
####solution
	This error means the key you are pushing with is attached to another repository as a *deploy key*, and does not have access to the repository you are trying to push to. To remedy this, *remove the deploy key from the repository and attach the key to your user account instead*.
###7. Write .gitignore
	When commit we want git to untrack somefile. If we create a .gitignore file. git will use its rules when we commit.
####Example .gitignore
	# Compiled source #
	###################
	*.com
	*.class
	*.dll
	*.exe
	*.o
	*.so
	
	# Packages #
	############
	# it's better to unpack these files and commit the raw source
	# git has its own built in compression methods
	*.7z
	*.dmg
	*.gz
	*.iso
	*.jar
	*.rar
	*.tar
	*.zip
	
	# Logs and databases #
	######################
	*.log
	*.sql
	*.sqlite
	
	######################
	*~
###.gitconfig
	[user]
		name = luoluo
		email = luoluo1920@gmail.com
	[alias]
		log1 = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
		log2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
	[core]
		editor = vim
####Tips
Note that git will not ignore a file that was already tracked before a rule was added to this file to ignore it. In such a case the file must be un-tracked, usually with 
	
	git rm --cached filename

