# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/19

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
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        vis = {s}
        q = [s]
        while q:
            u = q.pop()
            # for ai in range(1, 10):
            nx = ''.join(map(str, [(int(x) + (0 if i % 2 == 0 else a)) % 10 for i, x in enumerate(u)]))
            if nx not in vis:
                vis.add(nx)
                q.append(nx)
            
            x = u
            while True:
                x = x[-b:] + x[:-b]
                if x not in vis:
                    vis.add(x)
                    q.append(x)
                else:
                    break
            
        
        # print(len(vis))
        return min(vis)
        
if __name__ == '__main__':
    s = Solution()
    # print(s.findLexSmallestString('5525', 9, 2))
    # print(s.findLexSmallestString('74', 5, 1))
    # print(s.findLexSmallestString('0011', 4, 2))
    print(s.findLexSmallestString("4055071965067542983054516830405179644958942683787418860108635866", 1, 49))
    # import random
    # print(s.findLexSmallestString(''.join(map(str, [random.randint(0, 10) for _ in range(100)])), 7, 3))
    
    
    