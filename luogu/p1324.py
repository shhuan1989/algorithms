# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N, M = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    ai, bi = 0, 0
    ans = 0
    a = a + [0]
    b = b + [0]
    for i in range(2, N+M):
        if a[ai] > b[bi]:
            ans += (bi+1) * a[ai]
            ai += 1
        else:
            ans += (ai+1) * b[bi]
            bi += 1
    # print(ai, bi)
    print(ans)
    