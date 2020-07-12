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
created by shhuan at 2020/7/11 19:10

"""


if __name__ == '__main__':
    N = int(input())
    S = list(input())
    S = ''.join([v for v in S if v in {'0', '1'}])


    def gettype(l, r):
        v = S[l]
        for i in range(l, r+1):
            if S[i] != v:
                return 'F'
        return 'I' if v == '1' else 'B'

    def dfs(l, r):
        if l == r:
            return gettype(l, r)

        m = (l + r) // 2
        return dfs(l, m) + dfs(m+1, r) + gettype(l, r)



    print(dfs(0, len(S) - 1))
