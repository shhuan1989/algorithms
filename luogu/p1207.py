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
created by shhuan at 2020/7/25 20:11

"""


if __name__ == '__main__':
    N, S = map(int, input().split())

    def to_dim(x, b):
        y = []
        while x > 0:
            y.append(x % b)
            x //= b

        return y == y[::-1]

    s = S + 1
    ans = []
    while True:
        if len([1 for b in range(2, 11) if to_dim(s, b)]) >= 2:
            ans.append(s)
            if len(ans) >= N:
                break
        s += 1
    print('\n'.join(map(str, ans)))


