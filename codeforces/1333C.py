# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, A):
    presum = [0]
    for v in A:
        presum.append(presum[-1] + v)
        
    start, end = 0, 0
    ans = 0
    s = {0}
    while start < N:
        while end < N and presum[end+1] not in s:
            end += 1
            s.add(presum[end])
        ans += end - start
        s.remove(presum[start])
        start += 1
    
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(N, A))