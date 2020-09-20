# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/10 21:36

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


if __name__ == '__main__':

    N = int(input())

    A = [1 for _ in range(N)]

    def check(maxv):
        vis = [False for _ in range(maxv+1)]
        vis[0] = True

        b = A + A
        for l in range(N):
            s = 0
            for r in range(l, l+N):
                s += b[r]
                if s > maxv:
                    break
                vis[s] = True

        return all([vis[i] for i in range(maxv+1)])

    def dfs(index, maxv, vis):

        if index >= N:
            if check(maxv):
                return [' '.join(map(str, A))]

            return []

        # if (maxv-presum) // (N-index) > maxv:
        #     return []

        c = 0
        for i in range(N-index+1):
            c += index + i + 1
        if c < maxv - len(vis):
            return []

        ans = []
        for i in range(1, 22+1):
            A[index] = i

            s = 0
            nc = set()
            for j in range(index, -1, -1):
                s += A[j]
                nc.add(s)

            ans += dfs(index+1, maxv, vis | nc)

        return ans

    for i in range(N*(N-1)+1, -1, -1):
        x = dfs(1, i, {1})
        if x:
            print(i)
            print('\n'.join(x))
            break
