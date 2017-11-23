# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/23 11:21

"""


# S = input()
#
# N = int(input())

N = 10**5
S = ""
for i in range(N):
    if random.randint(1, 10) > 7:
        S += '#'
    else:
        S += '.'

t0 = time.time()
# .... n number of ., ans is n-1

count = []
p = S[0]
c = 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        c += 1
    else:
        count.append(c)
        p = S[i]
        c = 1
count.append(c)
left = [0] * (len(count) + 1)
for i in range(1, len(count)+1):
    left[i] = left[i-1] + count[i-1]


for i in range(N):
    # l, r = map(int, input().split())
    l = random.randint(1, N//2)
    r = random.randint(l, N)
    ans = 0

    bl = bisect.bisect_right(left, l)
    br = bisect.bisect_left(left, r)

    # for i in range(bl, br):
    #     ans += count[i-1]-1
    ans = left[br-1] - left[bl-1] - max(0, br-bl)
    if bl > 0:
        ans -= max(0, l - left[bl-1] - 1)
    if br < len(left):
        ans += max(0, r - left[br-1] - 1)

    print(ans)


print(time.time() - t0)
