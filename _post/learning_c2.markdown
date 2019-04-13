---
layout: post
title: "A byte of C After"
date: 2013-03-16 20:42
comments: true
categories: [Headstream,  C]
---

目标  
白话C，最短时间内写出简单C程序(*进阶篇*)

关键字  

+ 1.数据聚合
+ 2.运算符
+ 3.函数++

上期解答[问题传送门](/archives/learningc.markdown)

    #include <stdio.h>
    int is_prime(int x) // 1
    {
        int i;
        for(i = 2;i * i < x;i++)
            if((x % i) == 0) 
                return 0;
        return 1;
    }
    int main() 
    {
        int i, count, sum;
        for(i = 500, sum = 0, count = 0;i < 1000;i++){ // 2
            if(is_prime(i)){
                count++;        
                sum += i;
            }            
        }
        printf("There are %d primes, sum is %d\n", count, sum);
        return 0;
    }

解释两处：  
1.自己定义的函数`is_prime`用于判断数的素性;  
2.for循环的初始部分有错？？NO!逗号运算符[]   

数据聚合
>问题：已知每个人的成绩，求每个人与平均分间的差。
如果只有几个人，可以定义几个变量解决问题。可是若有成百上千的个体，定义变量使用将是多么痛苦。`数组`应运而生，数组是解决同类个体聚合的利器。

####数组 []

    #include <stdio.h>
    int main(){
        float scores[6] = {3, 4, 8, 9, 5, 7};//数组的定义
        //float scores[] = {3, 4, 8, 9, 5, 7};也可以 
    
        float average = 0;
        int i;
        for(i = 0;i < 6;i++)
            average += scores[i];
    
        average /= 6.0;
    
        for(i = 0;i < 6;i++){
             scores[i] -= average;
             printf("%f\t", scores[i]);
        }    
    }

上面解答只针对一门成绩，如果有多门呢？ 建立多个数组？？如果可以把名字，学号成绩合起来定义一种类型，处理将简单，直接。

####结构 struct

    #include <stdio.h>
    int main(){
        struct student{        //定义结构类型
            char name[20];        
            int id;
            float score1, score2;
        }; //此处分号不要丢
        struct student s1 = {"Lili", 201006, 5.5, 6.6};  //定义一个结构变量
        printf("name:%s id:%d score:%f %f\n", s1.name, s1.id, s1.score1, s1.score2);
    
        struct student stu[6] = {        //定义结构数组
                {"Lili", 201001, 5.5, 6.6},
                {"Lilk", 201002, 5.5, 2.6},
                {"Lile", 201003, 8.5, 9.6},
                {"Lils", 201004, 9.5, 8.6},
                {"Lilz", 201005, 3.5, 2.6},
                {"Lilw", 201006, 2.5, 8.6}
                                };
        int i;
        float aver1, aver2;
        for(i = 0, aver1 = 0, aver2 = 0;i < 6;i++){
            aver1 += stu[i].score1;        
            aver2 += stu[i].score2;        
        }
        aver1 /= 6.0;
        aver2 /= 6.0;
        for(i = 0;i < 6;i++){
            stu[i].score1 -= aver1; 
            stu[i].score2 -= aver2;
        }
        for(i = 0;i < 6;i++)
            printf("name:%s id:%d stucore:%f %f\n", stu[i].name, stu[i].id, stu[i].score1, stu[i].score2);
    }


#### 运算符

注意几点   

+ 1.位运算(& | ^)符优先级**高于**逻辑运算符(&& || );
+ 2.取模运算符(%) 的两个操作数都要是 **整型** ;
+ 3.运算符用于构成表达式,*表达式产生值*;
+ 4.赋值运算符(=),赋值表达式产生值，结合型自右向左;
+ 5.函数调用也是表达式(上表不全),表达式产生值。

####函数(递归)
阶乘的计算

    #include <stdio.h>
    int f(int x){
        if(x <= 1) //递归返回边界
            return 1;
        else return x * f(x -1);
    }
    int main()
    {
        printf("%d\n", f(6));
        return 0;
    }

递归就是函数调用本身，递归一定有返回边界；

####小结，有码有真相
写出求斐波那契数的函数fib(n)

    int fib(int n){
         //-------
    }

[答案戳这里](/archives/learning_c3.markdown)

下期将有指针、宏、常用函数

PS:本来打算都写在这期的，结果太多了...
