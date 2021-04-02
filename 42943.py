#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/2 9:43
# @Author : CN-JackZhang
# @File: 42943.py
'''冒泡排序
如果前一个数比后一个数大，交换两者位置'''

def bubble_sort(nums):
    #第一个for循环是前一个数
    for i in range(len(nums)-1):
        #第二个for循环是后一个数
        for j in range(i+1,len(nums)):
            #前一个数i的值，大于，后一个数，交换两者值
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

nums = [2,5,1,3,4,6]
test = bubble_sort(nums)
print(test)