# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/12/1

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

import collections


class Solution:
    def LIS(self, a):
        uniq = list(sorted(set(a)))
        vmap = {v: i for i, v in enumerate(uniq)}
        a = [vmap[v] for v in a]
        
        na = len(a)
        #         dp = [0 for _ in range(na)]
        
        bits = [0 for _ in range(na + 1)]
        
        def update(index, val):
            while index < na:
                bits[index] = max(bits[index], val)
                index |= index + 1
        
        def query(index):
            s = 0
            while index >= 0:
                s = max(s, bits[index])
                index = (index & (index + 1)) - 1
            return s
        
        lenindex = collections.defaultdict(int)
        prex = {}
        maxlen, maxv = -1, float('inf')
        for i, v in enumerate(a):
            pre = query(v - 1)
            x = pre + 1
            if x not in lenindex:
                lenindex[x] = v
            else:
                lenindex[x] = min(lenindex[x], v)
            #             lenindex[x].append(v)
            #             lenindex[x].sort()
            prex[v] = lenindex[pre]
            if x > maxlen or (x == maxlen and v < maxv):
                maxlen = x
                maxv = v
            #             dp[i] = pre + 1
            update(v, x)
        
        # print(lenindex)
        # print(maxlen, maxv)
        ans = []
        v = maxv
        while True:
            ans.append(v)
            if v not in prex or v <= 0:
                break
            v = prex[v]
        
        return [uniq[x] for x in ans[::-1]]

if __name__ == '__main__':
    s = Solution()
    print(s.LIS([2,1,5,3,6,4,8,9,7]))
    print(s.LIS([1,2,8,6,4]))
    
    import random
    a = [random.randint(0, 10**9) for _ in range(10**5)]
    t0 = time.time()
    print(s.LIS(a))
    print(time.time() - t0)
    # print(s.LIS())