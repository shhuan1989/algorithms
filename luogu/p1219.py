# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
# from memory_profiler import profile


# @profile
def solve(N):
    ans = []
    # visc = []
    
    def dfs(row, prec):
        if row >= N:
            if len(ans) < 3:
                ans.append(' '.join(map(str, [c + 1 for c in prec])))
            else:
                ans.append('')
            return
        
        for c in range(N):
            if c in prec:
                continue
            
            if any(abs(pr - row) == abs(pc - c) for pr, pc in enumerate(prec)):
                continue
                
            dfs(row + 1, prec+[c])
            
    
    t0 = time.time()
    dfs(0, [])
    print('\n'.join(ans[:3]))
    print(len(ans))
    print(time.time() - t0)


if __name__ == '__main__':
    N = int(input())
    solve(N)
    
    