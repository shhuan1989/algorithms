# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/30 20:11

设x是数组的和，y是数组的xor，
如果 (y ^ a) * 2 >= x + a，且 d=(y ^ a) * 2 - (x + a)是偶数，即可以用b = d//2，使得数组增加三个数组a, b, b之后满足条件；
这样的很好构建，找到x的最高位1，在左移一位，右边全部填0，如果x+a是奇数，a再增加1即可。

"""


def solve(A):
    x = sum(A)

    xor = 0
    for v in A:
        xor ^= v
    if xor * 2 == x:
        return []

    k = x.bit_length()
    a = 1 << k
    if (x + a) % 2 != 0:
        a += 1
    x += a
    xor ^= a
    c = (2 * xor - x) // 2

    return [a, c, c]

T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(A))

print('\n'.join(['\n'.join([str(len(v)), ' '.join(map(str, v))]) for v in ans]))