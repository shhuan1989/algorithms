# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    # sys.stdin = open('p1180.in', 'r')
    D = int(input())
    L, V, init, N = input().split()
    L = float(L)
    V = float(V)
    init = float(init)
    N = int(N)
    INF = 10 ** 9

    A = []
    for i in range(N):
        d, p = map(float, input().split())
        A.append((d, p))
    A.sort()
    A.append((D, INF))


    def round1(v):
        v *= 100
        if v % 10 < 5:
            v //= 10
        else:
            v //= 10
            v += 1

        return v / 10


    ans = [float('inf')]
    def dfs(curr, oil, cost):
        if curr >= N:
            ans[0] = min(ans[0], cost)
            return

        if cost > ans[0]:
            return

        dist = A[curr+1][0] - A[curr][0]
        add = round1(20 + (L - oil) * A[curr][1])
        oc = dist / V
        if oil * V < dist:
            dfs(curr+1, L-oc, cost+add)
        else:
            if oil * 2 >= L:
                dfs(curr+1, oil-oc, cost)
            else:
                dfs(curr+1, oil-oc, cost)
                dfs(curr+1, L-oc, cost+add)


    dfs(0, L, init + 20 + A[0][0] / V * A[0][1])
    print('{:.1f}'.format(round1(ans[0])))
