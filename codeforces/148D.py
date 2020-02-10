# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache


@lru_cache(maxsize=None)
def solve(w, b):
    if w <= 0:
        return 0
    if b <= 0:
        return 1
    
    # current is player 1's turn
    # win prob
    ans = w / (w + b)
    # draw black
    p = b / (w + b)
    b -= 1
    # probability of continuing after player 2's turn
    p *= b / (w + b)
    b -= 1
    if p > 1e-13:
        # mouse jumps is either white or black
        pblack = solve(w, b-1) * b / (w + b)
        pwthite = solve(w-1, b) * w / (w + b)
        ans += p * (pblack + pwthite)
    
    return ans


        
w, b = map(int, input().split())
print(solve(w, b))