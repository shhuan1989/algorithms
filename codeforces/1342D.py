# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    C = [0] + [int(x) for x in input().split()]
    
    A.sort()
    
    greater = [0 for _ in range(K+1)]
    for v in A:
        greater[min(v, K)] += 1
    
    for i in range(K-1, 0, -1):
        greater[i] += greater[i+1]

    m = max([greater[i]//C[i] if greater[i] % C[i] == 0 else greater[i]//C[i] + 1 for i in range(1, K+1)])
    ans = [[] for _ in range(m)]
    for i, v in enumerate(A):
        ans[i % m] .append(v)
    
    print(m)
    for v in ans:
        print('{} {}'.format(len(v), ' '.join(map(str, v))))
