#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/2 8:18
# @Author : CN-JackZhang
# @File: 42.py
'''选择排序
很适合用来从低到高放书'''

def select_sort(nums,n):
    if n==0:
        return
    max_index = n
    print(max_index)
    #找出最大值的索引
    for i in range(n):
        if nums[i] > nums[max_index]:
            max_index = i
    print(max_index)
    #将最大值索引的值放到最后一个
    nums[n],nums[max_index] = nums[max_index],nums[n]
    print(nums)
    #再比较前n-1个
    select_sort(nums,n-1)
nums = [4,2,1,3,]
test = select_sort(nums,len(nums)-1)



