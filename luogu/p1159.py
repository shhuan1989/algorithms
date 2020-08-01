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
    N = int(input())

    A = []
    G = collections.defaultdict(list)
    for i in range(N):
        name = input().strip()
        order = input().strip()
        if order == 'UP':
            G[i] = [j for j in range(i + 1, N)]
        elif order == 'DOWN':
            G[i] = [j for j in range(i)]
        else:
            G[i] = [i]
        A.append(name)

    MARK = [-1 for _ in range(N)]
    VIS = [-1 for _ in range(N)]


    def dfs(u, tim):
        for v in G[u]:
            if VIS[v] == tim:
                continue
            VIS[v] = tim
            if MARK[v] < 0 or dfs(MARK[v], tim):
                MARK[v] = u
                return True

        return False


    tim = 1
    for i in range(N):
        dfs(i, tim)
        tim += 1

    # print(MARK)
    # print(ans)
    # print(A)
    print('\n'.join([A[i] for i in MARK]))