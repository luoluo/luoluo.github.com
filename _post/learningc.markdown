---
layout: post
title: "A byte of C"
date: 2013-03-13 22:22
comments: true
categories: [Headstream,  C]
---
目标    
白话C，最短时间内写出简单C程序(*基础篇*)

关键字

+ 1.变量
+ 2.控制结构
+ 3.函数
+ 4.编程风格

从一段C程序说起

    int main() 
    {
        return 0;
    }

这是一个函数，main是函数名；int是返回值，表示返回整型值；return 0，表示返回0.

C是一个*面向过程*的语言，程序是有函数构成，至少有一个函数main，它是程序的入口。用户可以自己定义函数，程序可以相互调用，实现功能。函数是由*语句*构成的，并约束在`{ }`间，语句要以分号结尾.

    int main() 
    {
        printf("Hello, world\n");//调用函数printf输出"Hello, world"
        return 0;
    }

变量

    int main() 
    {
        int a; //定义变量a
        a = 3; //对a赋值为3  这两句等价于 int a = 3;
        return 0;
    }

命名规则

   函数名和变量名要满足规则：   
	以字母下划线为开头可以混合数字；   
	但不可是关键字(C里的语句如:if while for..)    

变量类型：char/short/int/long；float/double    

    int main() 
    {
        char a = 'x';
        short b = 123;
        int c = 12345;
        float f = 123.4;
        double d = 1234324.2342;
        return 0;
    }

控制结构：顺序、分支、循环

+ 顺序结构即自然的顺序执行结构，是C默认执行的顺序。
+ 分支结构是判断条件，来改变程序的执行顺序的。
+ 循环结构是给定 初始值，终止条件，迭代值，来重复执行。

分支结构的实现 `if` 

    int main() 
    {
        int a;              // 定义变量a
        a = 3;              // 对a赋值为3  这两句等价于 int a = 3;
        if(a > 0){          // 判断条件，满足a > 0来执行
            printf("a 为正数\n");
        }
        return 0;
    } 

分支结构的实现 `if` `else` 

    int main() 
    {
        int a = 3; 
        if(a > 0){        //判断条件，是正数
            printf("a 为正数\n");
        }
        else{        //不满足条件，是负数
            printf("a 为负数\n");
        }
        return 0;
    } 

分支结构的实现 `if` `else if` `else`

    int main() 
    {
        int a = 3; 
        if(a > 0){            //判断条件，是正数
            printf("a 为正数\n");
        }
        else if(a < 0){        //判断条件，是负数
            printf("a 为负数\n");
        }else{                //非负非正为0
            printf("a 为0\n");
        }
        return 0;
    } 

注意此例中的那些`{}`，它们是成对出现的，表示代码块，若满足条件，均会执行。若只有一条语句，可以省略。

分支结构的实现 `switch`实现分支结构

    int main()
    {
        int a = 3;
        switch(a){        //switch的判断数a必须是整型(char short int long)
            case 2: printf("a == 2\n"); break; // 若a==2，则输出
            case 3: printf("a == 3\n"); break; // 若a==3，则输出
            default: printf("not 3 nor 2\n");  //以上均不满足，则输出
        }
    }

case 可以有任意多个，要点是注意每个case以`break`结束，因为一个case 满足执行后并不会主动退出`switch`，而是顺序向下判断之后的case。而情况往往是满足一个case就退出switch，这时就要记得加`break`.

循环结构的实现 for

    int main() 
    {
        int a, i; //定义变量a, i
        a = 0; 
        for(i = 0;i < 10; i++){
            a = a + i;
        }
        return 0;
    } 

循环结构的实现 while 

    int main() 
    {
        int a, i; //定义变量a, i
        a = 0; 
        while(i < 10){
            i++;
            a = a + i;
        }
        return 0;
    } 

循环结构的实现 do-while 

    int main() 
    {
        int a, i; //定义变量a, i
        a = 0; 
        do{
            a = a + i;
            i++;
        }while(i < 10);        //不要忘记分号
        return 0;
    } 

函数 定义及调用

    float caculateArea(float r)
    {
		//定义计算面积函数caculateArea，以float(浮点型)为参数，返回float型
        return r * r * 3.14;
    }
    int main()
    {
        float radius = 2;    
        float area = caculateArea(radius); /* 调用函数,传参radius，radius是实参，替代r来让函数caculateArea计算并返回面积 */
        printf("The area is %f\n", area);
        return 0;
    }
    
编程风格

注释

    注释有两种形式(// 和 /**/)
	//使用于单行注释
	/**/使用于多行注释，从第一个/*到第一个*/之间的内容均为注释，编译时直接当空格处理。

    来一个极端的例子
    int main()
    {
        int x/**/y;//有错么？
        int a/* b;
        float c d;*/ 
        ;
        return 0;
    //如果没错定义了几个变量呢？
    }

缩进

C是一种自由格式的语言，并没有规则要求怎样书写，但是遵循一定约定，可以使代码易读易修改。   
再来一个极端的例子

    int max(int a,int b,int c) {
        if(a>b)
            if(a>c)
                return a;
            else 
                return c;
        else return b;
    }

    int max(int a,int b,int c){
        if(a>b)    
            if(a>c)    
                return a;
            else return c;
        else return b;
    }

以上两个程序均返回3个值里的最大值，缩进的威力应该显然。所以保持好的编程风格大有裨益。

####小结，有码有真相

    写一个计算出500到1000以内有多少素数，并求这些素数的和。
    int main()
    {
        ...//代码下期给出    
    }

[答案戳这里](/archives/learning_c2.markdown)
