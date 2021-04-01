#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/1 11:34
# @Author : CN-JackZhang
# @File: 41.py
'''递归完成斐波那契数列'''

a = [1,2,3,5,8,13,21,34]
def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fibo(n-1)+fibo(n-2)
print(fibo(7))




