# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/6

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
    N, K, C, W = map(int, input().split())
    A = []
    for _ in range(N):
        type, val = map(int, input().split())
        A.append((type, val))
    
    K /= 100
    C /= 100
    
    ans = 0
    
    for i in range(N-1, -1, -1):
        type, val = A[i]
        if type == 1:
            ans = max(ans, val + ans * (1 - K))
        else:
            ans = max(ans, -val + ans * (1 + C))
    
    print('{:.2f}'.format(ans * W))
    
    
        
    