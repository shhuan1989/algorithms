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
created by shhuan at 2020/7/9 19:14

"""


from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(stack, params):
    if params <= 0:
        return 1

    if stack <= 0:
        return dfs(1, params-1)

    ans = 0
    for i in range(stack+1):
        ans += dfs(stack-i+1, params-1)

    return ans


if __name__ == '__main__':
    N = int(input())
    print(dfs(0, N))