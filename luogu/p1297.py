# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

# if __name__ == '__main__':
#     N, A, B, C, a1 = map(int, input().split())
#     MOD = 100000001
#     Q = [a1]
#     for i in range(N - 1):
#         Q.append((Q[-1] * A + B) % MOD)
#
#     Q = [v % C + 1 for v in Q]
#
#     ans = 0
#     for i in range(N):
#         a, b = Q[i], Q[(i + 1) % N]
#         ans += min(a, b) / a / b
#
#     print('{:.3f}'.format(ans))
#
if __name__ == '__main__':
    N, A, B, C, a1 = map(int, input().split())
    MOD = 100000001
    ans = 0
    a, b = a1, (a1*A+B) % MOD
    for i in range(N):
        c, d = a % C + 1, (b % C + 1) if i < N-1 else (a1 % C + 1)
        a = b
        b = (b * A + B) % MOD
        ans += 1/max(c, d)
    
    print('{:.3f}'.format(ans))