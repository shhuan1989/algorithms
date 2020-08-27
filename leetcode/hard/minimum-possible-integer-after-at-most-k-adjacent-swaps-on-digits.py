# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if not num:
            return ''
        
        num = [int(v) for v in num]
        n = len(num)
        vi = [collections.deque([]) for _ in range(10)]
        for i, v in enumerate(num):
            vi[v].append(i)
        
        fenwick_bits = [0 for _ in range(n)]
        
        def update(index, val):
            while index < n:
                fenwick_bits[index] += val
                index |= index + 1
        
        def query(index):
            s = 0
            while index >= 0:
                s += fenwick_bits[index]
                index = (index & (index + 1)) - 1
                
            return s
        
        ans = []
        removed = [False for _ in range(n)]
        for i in range(n):
            if k <= 0:
                break
            for v in range(10):
                if vi[v]:
                    j = vi[v][0]
                    dist = j - query(j - 1)
                    if dist <= k:
                        k -= dist
                        ans.append(v)
                        update(j, 1)
                        removed[j] = True
                        vi[v].popleft()
                        break
        
        ans += [num[i] for i in range(n) if not removed[i]]
        return ''.join(map(str, ans))
        
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minInteger("294984148179", 11))
    print(s.minInteger('4321', 4))
    print(s.minInteger('100', 1))
    print(s.minInteger('36789', 1000))
    print(s.minInteger('22', 22))
    print(s.minInteger('9438957234785635408', 23) == '0345989723478563548')
