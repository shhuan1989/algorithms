# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, A):
    s = sum([v % K for v in A])
    
    return s % K


T = int(input())
ans = []
for ti in range(T):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    ans.append(solve(N, K, A))

print('\n'.join(map(str, ans)))
