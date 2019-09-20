# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/13 09:57

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


MAXN = 10**5+5
MAXK = 10**6+5


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x
#
# for a in range(1, 1000):
#     for b in range(a+1, 1000):
#         # if b % a == 0:
#         #     continue
#         if a % gcd(a, b) == 0 or b % gcd(a, b) == 0:
#             continue
#         # if a % 2 == 0 and b % 2 == 0:
#         #     continue
#         f = False
#         for x in range(-1000, 1000):
#             #a*x-b*y == 1
#             #y = (a*x-1) // b
#             if (a*x-1) % b == 0:
#                 f = True
#                 break
#         if not f:
#             print(a, b)
#             break
#
# print('done')

def solve(N, A, Q, B):
    MAXK = max(B) + 5
    dp = [0] * MAXK
    g = 0
    for i in range(N):
        marked = [0] * MAXK
        markede = [0] * MAXK
        v = A[i]
        q = {v}
        while v < MAXK:
            dp[v] += N-i
            marked[v] = 1
            v += A[i]

        for j in range(i+1, N):
            u = A[j]
            ds = {gcd(u, v) for v in q}
            if any([u % d != 0 for d in ds]) or any([v % d != 0 for d, v in zip(ds, q)]):
                g += N-j
                break

            q |= ds

            for d in ds:
                if markede[d] == 1:
                    continue
                markede[d] = 1

                e = d
                while e < MAXK:
                    if marked[e] == 0:
                        marked[e] = 1
                        dp[e] += N-j
                    e += d


    # print(dp2[8], dp[8])
    return [dp[b] + g for b in B]


# N = int(input())
# A = [int(x) for x in input().split()]
# Q = int(input())
# B = []
# for qi in range(Q):
#     B.append(int(input()))

import random
N = 500
A = [random.randint(1, 20) for _ in range(N)]
Q = 1000
B = [random.randint(1, 10) for _ in range(Q)]
print(A)
print(B)

# N, Q = 10, 10
# A = [5, 12, 5, 16, 3, 15, 3, 15, 5, 15]
# B = [86, 52, 69, 8, 3, 6, 13, 82, 96, 55]

print('\n'.join(map(str, solve(N, A, Q, B))))
