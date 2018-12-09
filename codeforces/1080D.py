# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/24 15:29

"""

T = int(input())

ans = []
for ti in range(T):
    N, K = map(int, input().split())
    a = math.log(3*K+1, 4)
    if N < a:
        ans.append("NO")
    else:
        a = N - int(a)
        if a > 1:
            L = 3 * K - (4**(N-a) - 1)
            b = N - a
            d = 3 * L / (4 ** a - 1) if a <= math.log(3*L+1) else 0
            if b >= math.log(math.sqrt(0.25 + d) + 0.5, 2):
                ans.append('YES {}'.format(a))
            else:
                ans.append('YES {}'.format(a - 1))
        else:
            ans.append('YES {}'.format(a))


print('\n'.join(ans))