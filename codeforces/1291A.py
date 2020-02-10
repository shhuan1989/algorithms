# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(val):
    s = [int(v) for v in list(val)]
    odds = [i for i, v in enumerate(s) if v % 2 != 0]
    
    if len(odds) < 2:
        return '-1'
    
    return ''.join(map(str, [v for v in s[:odds[1]+1]]))
    

T = int(input())
ans = []
for i in range(T):
    n = input()
    s = input()
    ans.append(solve(s))

print('\n'.join(ans))

