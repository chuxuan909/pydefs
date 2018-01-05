#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##简单自定义函数集合####
import math
##解整数和浮点数的一元二次方程
def quadratic(a,b,c):
    t=b*b-4*a*c
    if t>=0 and a!=0:
        x1=(-b+math.sqrt(t))/2*a
        x2=(-b-math.sqrt(t))/2*a
        return x1,x2
    elif a==0:
        x1=x2=-c/b
        return x1
    else:
        return('ivaild input number')
qu=quadratic

###1到100的内基数表单list生成
def jshu():
    L=[]
    n=1
    while n <=99:
        L.append(n)
        n=n+2
    return L
