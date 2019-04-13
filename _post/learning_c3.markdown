---
layout: post
title: "A byte of C After After"
date: 2013-03-17 10:17
comments: true
categories: [Headstream,  C]
---

目标  
白话C，最短时间内写出简单C程序(*终极篇*)  

关键字  

+ 1.宏
+ 2.指针
+ 3.++函数


上期解答[问题传送门](/archives/learning_c2.markdown)

    #include <stdio.h>
    int fib(int x){
        if(x <= 1)  //边界返回
            return 1;        
        else 
            return fib(x-1) + fib(x-2); //递归调用
    }
    int main(){
        int i;
        for(i = 0;i < 10;i++)
            printf("fib(%d) = %d\n", i, fib(i));
        return 0;    
    }

###宏

考虑以下情形:    
编程时有重复出现的数值常量，分散与程序的各个角落，要对其值修改时，情形将困囧起来。条件编译，按需求编译程序的不同部分，低成本程序移植。本质上说，宏是在预编译时的纯替换。

    #include <stdio.h>
    #define MAX 20 //即增加可读性，又便于修改
    int main(){
        int stu[MAX], i;
        for(i = 0;i < MAX;i++){
            printf("%d\t%d", i, stu[i]);        
        }
        return 0;
    }

###指针

C的魅力所在，也是C coder的噩梦

指针也是C的类型，于是乎有*指针常量* *指针变量*。我理解的*指针类型是标识地址的一种类型*，就像通过“经纪人”找“歌手”，我们通过“指针”来访问“变量”。指针本身的*值*是地址，通过地址，我们可以访问其他变量、函数。

两个操作符 `*` `&`    

+ 1.&是取地址操作符
+ 2.\*是地址访问操作符

指针变量的声明、初始化、访问

    #include <stdio.h>
    int main(){
        int a = 0;
        int *pa; //声明指针变量pa
        pa = &a;    //为pa初始化为a的地址
        //此时pa存储a的地址，可以说pa指向a 
        printf("%d %d\n", a, *pa);
        printf("%d %d\n", &a, pa);
        return 0;
    }

指针变量是变量也可以被指向

    #include <stdio.h>
    int main(){
        int a;
        int *pa = &a;
        int **ppa = &pa; //ppa是指向pa的指针
        printf("%d %d %d\n", a, *pa, **ppa);
        printf("%d %d %d\n", &a, pa, *ppa);
        printf("%d %d\n", &pa, pa);
        return 0;
    }

常量指针与指针的运算

    #include <stdio.h>
    int main(){
        int a[] = {1, 2, 3, 4, 5, 6};    //a是数组名，数组名的值是数组在内存的首地址，所以数组名是指针;编译后数组在内存里的位置确定，a的值不会改变，所以*数组名是常量指针*
        int *p = a;
        printf("%d %d\n", a, *p);
        printf("%d %d\n", a[1], *(p+1));//a[i] <==> *(p+i)
        return 0;
    }    

指针相关运算

+ a.指针+/-整型
+ b.指针+/-指针
+ c.指针关系运算符
+ d.指针sizeof

指针算数运算的自调节机制：  

a.指针在与整型运算前会进行调整，将指针指向类型的大小来与整型相乘，再加。结果为指针类型

    #include <stdio.h>
    int main(){
        int a[] = {1, 2, 3};
        int *pa = a;
        int *pb = pa + 1; 
        //int *pb = &a[1]; 与上条等效
        return 0;
    }

b.指针与指针类型算术运算，只有二者指向相同数组，结果才是定义了的。结果为整型

    #include <stdio.h>
    int main(){
        int a[] = {1, 2, 3};
        int *pa = a;
        int *pb = &a[2]; 
        printf("pa - pb = %d", pa - pb);
        return 0;
    }


c.指针与指针类型关系运算，只有二者指向相同数组，结果才是定义了的。结果为真或假

    #include <stdio.h>
    int main(){
        int a[] = {1, 2, 3};
        int *pa = a;
        int *pb = &a[2]; 
        printf("pa > pb = %d", pa > pb);
        return 0;
    }

d.指针的sizeof运算：直接作用于指针变量，返回指针变量的大小(4或8);对于数组名,会返回该数组的大小

    #include <stdio.h>
    int main(){
        int a[] = {1, 2, 3};
        int *pa = a;
        int *pb = pa + 1; 
        printf("sizeof(a) = %d sizeof(pa) = %d", sizeof(a), sizeof(pa));
        return 0;
    }

先告一段落，还待完善。若有问题，敬请指出。
