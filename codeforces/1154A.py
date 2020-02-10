# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/6/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

def solve(a, b, c, d):
    
    for u, v, w, x in itertools.permutations([a, b, c, d]):
        i = x - u
        j = x - v
        k = x - w
        if all([d > 0 for d in [i, j, k]]):
            return list(sorted([i, j, k]))
        
        

a, b, c, d = map(int, input().split())
ans = solve(a, b, c, d)
print(' '.join(map(str, ans)))
