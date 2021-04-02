#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/2 10:31
# @Author : CN-JackZhang
# @File: quick_sort.py
'''快速排序
先找一个基准，比它小放左边，比它大放右边'''

def quick_sort(nums):
    if not nums:
        return []
    #以第1个数作为基准
    tmp = nums[0]
    left = []
    right = []
    #比较每个数
    for i in range(1,len(nums)):
        if nums[i] < tmp:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [tmp] + quick_sort(right)

nums = [3,1,6,2,4,7,5]
test = quick_sort(nums)
print(test)


