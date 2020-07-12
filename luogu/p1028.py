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
created by shhuan at 2020/7/8 22:46

"""


from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(first):
    if first <= 0:
        return 0

    ans = 1
    for a in range(1, first//2+1):
        ans += dfs(a)
    return ans


if __name__ == '__main__':
    N = int(input())
    print(dfs(N))
