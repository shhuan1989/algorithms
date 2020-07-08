# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(A):
    if any([v <= 0 for v in A]):
        return 0
    
    N = sum(A)
    ans = (N-6) * 5040
    for i in range(7):
        ans *= A[i]
    for i in range(7):
        ans /= N-i
        
    return ans


if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    print('{:.3f}'.format(solve(A)))
