# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def link(a, b):
    for l in range(1, min(len(a), len(b))):
        if a[-l:] == b[:l]:
            return l
    return 0


def dfs(curr, wlen, vis, path):
    # print(wlen, path)
    tlen = wlen
    for neib in range(N):
        if vis[neib] >= 2:
            continue
        c = link(A[curr], A[neib])
        if c > 0:
            vis[neib] += 1
            tlen = max(tlen, dfs(neib, wlen+len(A[neib])-c, vis, path+[A[neib]]))
            vis[neib] -= 1
    
    return tlen


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    start = input()
    
    ans = 0
    for i, a in enumerate(A):
        if a.startswith(start):
            vis = [0 for _ in range(N)]
            vis[i] = 1
            ans = max(ans, dfs(i, len(a), vis, [a]))
            
    print(ans)