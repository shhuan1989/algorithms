# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

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
    A = [0] + [int(x) for x in input().strip().split()]
    left = [-1 for _ in range(N+1)]
    right = [-1 for _ in range(N+1)]
    a = {v: i for i, v in enumerate(A)}
    # print(a)
    q = []
    for i in range(1, N+1):
        parent = -1
        while q and a[q[-1]] > a[i]:
            parent = q.pop()
        
        if parent >= 0:
            left[i] = parent
        if q:
            right[q[-1]] = i
        q.append(i)
        # print(left)
        # print(right)
    
    
    q = collections.deque([1])
    ans = []
    while q:
        i = q.popleft()
        ans.append(A[i])
        if left[i] >= 0:
            q.append(left[i])
        if right[i] >= 0:
            q.append(right[i])
    
    print(' '.join(map(str, ans)))
    