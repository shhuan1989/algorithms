# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-07

"""

import collections
import time
import os
import sys
import bisect
import heapq

T = int(input())
for ti in range(T):
    N = int(input())
    S, X = input().split()
    
    idx = [i for i in range(N) if S[i] == X]
    # print(idx)
    ans = 0
    for l in range(N):
        r = bisect.bisect_left(idx, l)
        if r >= len(idx):
            break
        # print(l, r)
        ans += N - idx[r]
        

    print(ans)