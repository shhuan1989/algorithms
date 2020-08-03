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


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    
    nums = set()
    for p in range(M+1):
        for q in range(M+1):
            nums.add(p**2+q**2)
    
    ans = []
    snums = list(sorted(nums))
    ns = len(snums)
    # print(ns)
    for ai, a in enumerate(snums):
        for ci in range(ai+1, ns):
            c = snums[ci]
            b = c-a
            if all([a+x*b in nums for x in range(2, N)]):
                ans.append((b, a))
    ans.sort()
    if ans:
        print('\n'.join(['{} {}'.format(a, b) for b, a in ans]))
    else:
        print('NONE')
    
    