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
created by shhuan at 2020/7/8 19:31

"""

if __name__ == '__main__':
    N, K = map(int, input().split())

    def dfs(val, parts, lastv):
        # print(val, parts, lastv)
        if parts >= K:
            return 0

        if parts == K-1:
            return 1 if val >= lastv else 0

        ans = 0
        for v in range(lastv, val+1):
            ans += dfs(val-v, parts+1, v)

        return ans

    print(dfs(N, 0, 1))

