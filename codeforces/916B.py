# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/24/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N, K = map(int, input().split())

# if K > N:
#     print('No')
#     exit(0)

def fnk(N, K):
    if K == 1:
        return [int(math.log2(N))]

    i = 0
    k = 0
    c = collections.defaultdict(int)
    nbak = N
    while N > 0:
        if N & 1:
            k += 1
            c[i] = 1
        N >>= 1
        i += 1
    if k > K:
        print('No')
        exit(0)

    while k < K:
        x = max(c.keys())
        c[x] -= 1
        if c[x] == 0:
            del c[x]
        c[x - 1] += 2
        k += 1

    y = max(c.keys())
    k = nbak // (1 << y)
    ans = [y] * k
    ans += fnk(nbak - k*(1 << y), K - k)




ans = fnk(N, K)
print('Yes')
# print(' '.join(map(str, list(sorted(ans, reverse=True)))))
