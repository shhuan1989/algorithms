# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2021/1/4

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


def solve(N):
    ops = []
    
    x = N
    for i in range(N-1, 2, -1):
        if i * i <= x:
            x = x // i if x % i == 0 else x // i + 1
            ops.append('{} {}'.format(N, i))

        ops.append('{} {}'.format(i, N))

    while x > 1:
        x = x // 2 if x % 2 == 0 else x // 2 + 1
        ops.append('{} {}'.format(N, 2))
    
    return '{}\n{}'.format(len(ops), '\n'.join(ops))
    

if __name__ == '__main__':
    T = int(input())
    
    ans = []
    for ti in range(T):
        N = int(input())
        ans.append(solve(N))
    
    print('\n'.join(ans))
    
    