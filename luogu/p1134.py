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
created by shhuan at 2020/7/18 13:10

"""


if __name__ == '__main__':
    N = int(input())
    v, v2, v5 = 1, 0, 0
    for b in [2, 5]:
        count = 0
        x = b
        while x <= N:
            count += N // x
            x *= b
        if b == 2:
            v2 = count
        else:
            v5 = count

    ans = 1
    for v in range(1, N+1):
        while v % 2 == 0:
            v //= 2

        while v % 5 == 0:
            v //= 5

        ans *= v
        ans %= 10

    ans *= pow(2, v2-v5, 10)
    ans %= 10

    print(ans)