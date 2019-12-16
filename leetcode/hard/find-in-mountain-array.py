# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import random

class MountainArray:
    def __init__(self, a):
        self.data = a
    
    def get(self, index: int) -> int:
        return self.data[index]
    
    def length(self) -> int:
        return len(self.data)


class Solution:
    def findInMountainArray(self, target: int, mt: MountainArray) -> int:
        n = mt.length()
        
        if n < 100:
            for i in range(n):
                if mt.get(i) == target:
                    return i
            # return -1
        
        def dfs(target, left, right, ops):
            if left > right:
                return -1
            
            if right - left + 1 < ops:
                for i in range(left, right + 1):
                    if mt.get(i) == target:
                        return i
                return -1
            a, b = mt.get(left), mt.get(right)
            ops -= 2
            if a > target and b > target:
                return -1
            elif a == target:
                return left
            elif a > target:
                lo, hi = left, right
                while lo <= hi:
                    m = (lo + hi) // 2
                    v = mt.get(m)
                    if v > target:
                        lo = m + 1
                    else:
                        hi = m - 1
                return lo
            elif b >= target:
                lo, hi = left, right
                while lo <= hi:
                    m = (lo + hi) // 2
                    v = mt.get(m)
                    if v >= target:
                        hi = m - 1
                    else:
                        lo = m + 1
                return lo
            else:
                seq = []
                step = (right - left + 1) // 10
                for i in range(left, right, step):
                    ops -= 1
                    v = mt.get(i)
                    if v >= target:
                        return dfs(target, left, i, ops)
                    if not seq or v >= seq[-1]:
                        seq.append(v)
                    else:
                        return dfs(target, max(left, i - step), i, ops)
                
                segs = [v for v in range(left, right, step)]
                if segs[-1] < right:
                    segs.append(right)
                if len(segs) > 2:
                    ans = dfs(target, segs[-3], segs[-2], ops)
                    if ans >= 0:
                        return ans
                
                ops -= 1
                ans = dfs(target, segs[-2], segs[-1], ops)
                return ans
                    
        return dfs(target, 0, n-1, 99)
        
s = Solution()
# mt = MountainArray([1,2,3,4,5,3,1])
# print(s.findInMountainArray(3, mt))
#
# mt = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2])
# print(s.findInMountainArray(1, mt))

# mt = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2])
# print(s.findInMountainArray(21, mt))

# mt = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2])
# print(s.findInMountainArray(22, mt))

mt = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82])
print(s.findInMountainArray(102, mt))