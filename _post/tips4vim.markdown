---
layout: post
title: "Tips for vim"
date: 2013-10-26 12:36
comments: true
categories: [Tools, Skill]
---
#####1.How to copy between two terminals using vim?
1. open file a
2. copy the items (using yy)
3. *close file a (Main point)*
4. open file b
5. paste the items
6. save and exist file b

#####2.How to copy to system clipboard?

	if `:echo has('clipboard')` return 0
		install clipboard first by running
		sudo apt-get install vim-gtk
	else `:set clipboard=unnamedplus`
		use "+y | "+2yy to copy and +p to paste

#####3.How to put the current line to the top of the screen?
From time to time, I'm typing at the bottom of the screen.So I need to go back to the top.   
####solution:
	z<return> || zt #to the top
	zb #to the bottom
	zz #to the middle
#####Tips:All of those command keep the cursor where it was
###4.vim moving between windows?
####C-w
###5.Debug using vim?
#### makefile + pyclewn + vim
Use pyclewn to debug C/Python (Using gdb/pdb)    
**See more on **
[pyclewn org](http://pyclewn.sourceforge.net/)
###6.vim paste indent problem?
When I paste code into document from clipboard, I get extra space in new line:    

	line    
		line   
			line
####To solve this:
	:set paste   #turn on the paste mode
	#do the paste you need
	:set nopaste  #turn off the paste mode
###7.using book mark?
	Command	 Description
	ma	 set mark a at current cursor location
	'a	 jump to line of mark a
	`a	 jump to position of mark a
	d'a	 delete from current line to line of mark a
	d`a	 delete from current posi to posi of mark a
	c'a	 change from current line to line of mark a
	y`a	 yank   from cursor to position of mark a (to unnamed buffer)
	:marks	 list all the current marks
	:marks aB	 list marks a, B
	
