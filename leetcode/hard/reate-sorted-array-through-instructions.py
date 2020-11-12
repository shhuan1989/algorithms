# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/12

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        uniq = list(sorted(set(instructions)))
        vi = {v:i for i, v in enumerate(uniq)}
        instructions = [vi[v] for v in instructions]
        maxv = len(uniq)
        
        bits = [0 for _ in range(maxv)]
        
        
        def query(index):
            s = 0
            while index >= 0:
                s += bits[index]
                index = (index & (index + 1)) - 1
            return s
        
        def update(index, val):
            while index < maxv:
                bits[index] += val
                index |= index + 1
                
        ans = 0
        mod = 10 ** 9 + 7
        for i, v in enumerate(instructions):
            a = query(v-1)
            b = query(v)
            c = i - b
            ans += min(a, c)
            ans %= mod
            update(v, 1)
        
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.createSortedArray([1, 5, 6, 2]))
    print(s.createSortedArray([1,2,3,6,5,4]))
    print(s.createSortedArray([1,3,3,3,2,4,2,1,2]))
    