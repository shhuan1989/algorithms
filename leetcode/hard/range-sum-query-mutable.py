# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class NumArray:
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0 for _ in range(self.n)]
        self.bit = [0 for _ in range(self.n)]
        
        for i, v in enumerate(nums):
            self.update(i, v)
        
        self.nums = nums
    
    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        while i < self.n:
            self.bit[i] += delta
            i |= i + 1
    
    def query(self, index):
        s = 0
        while index >= 0:
            s += self.bit[index]
            index = (index & (index + 1)) - 1
        
        return s
    
    def sumRange(self, i: int, j: int) -> int:
        return self.query(j) - self.query(i-1)


# nums = [1, 3, 5]
# s = NumArray(nums)
# print(s.sumRange(0, 2))
# s.update(1, 2)
# print(s.sumRange(0, 2))

s = NumArray([])
for op, param in zip(
        ["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"],
        [[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]):
    if op == 'NumArray':
        s = NumArray(param[0])
    elif op == 'update':
        s.update(param[0], param[1])
    else:
        print(s.sumRange(param[0], param[1]))