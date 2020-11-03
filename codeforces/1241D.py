# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/23

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



if __name__ == '__main__':
    
    delta = [(1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, 0)]
    
    def solve(cs, x, y):
        
        for (i1, c1), (i2, c2) in itertools.combinations(cs, 2):
            
            dx1, dy1 = delta[i1]
            dx2, dy2 = delta[i2]
            
            
            
        
    
    T = int(input())
    ans = []
    for _ in range(T):
        x, y = map(int, input().split())
        cs = map(int, input().split())
        ans.append(solve([(i, c) for i, c in enumerate(cs)], x, y))
    
    print('\n'.join(map(str, ans)))
    
    