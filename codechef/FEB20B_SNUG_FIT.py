
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


def solve(N, A, B):
    A.sort()
    B.sort()
    s = sum([min(a, b) for a, b in zip(A, B)])
    return s


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans.append(solve(N, A, B))

print('\n'.join(map(str, ans)))