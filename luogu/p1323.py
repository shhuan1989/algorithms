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
    K, M = map(int, input().split())
    q = [1]
    a = []
    for _ in range(K):
        a.append(heapq.heappop(q))
        heapq.heappush(q, a[-1] * 2 + 1)
        heapq.heappush(q, a[-1] * 4 + 5)
    
    a = ''.join(map(str, a))
    print(a)
    a = [int(x) for x in a]
    index = [[] for _ in range(10)]
    for i, v in enumerate(a):
        index[v].append(i)
    
    b = []
    i = -1
    while M > 0:
        for v in range(9, -1, -1):
            j = bisect.bisect_right(index[v], i)
            if j < len(index[v]):
                k = index[v][j]
                remove = k - i - 1
                if remove <= M:
                    M -= remove
                    i = k
                    b.append(v)
                    break
                    
    b += a[i+1:]
    print(''.join(map(str, b)))