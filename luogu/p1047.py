# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    L, M = map(int, input().split())
    start = [0 for _ in range(L+10)]
    end = [0 for _ in range(L+10)]
    for i in range(M):
        s, e = map(int, input().split())
        start[s] += 1
        e = min(e, L)
        end[e+1] += 1
    
    ans = 0
    scount = 0
    for i in range(L+1):
        scount += start[i]
        scount -= end[i]
        ans += 1 if scount > 0 else 0
        
    print(L + 1 - ans)
    
