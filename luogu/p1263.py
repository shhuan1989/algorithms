# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10 ** 9 + 7
MAXN = 10**5

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)


    def toxy(id):
        id %= (N + 2) * (M + 2)
        id -= 1
        r = id // (M+1)
        c = id % (M+1)
        return r, c

    def getid(r, c, t):
        v = r * (M + 1) + c + 1 + t * (N + 2) * (M + 2)
        return v

    bottom = collections.defaultdict(list)
    for c in range(M):
        wall = N
        vis = set()
        # add(start, getid(wall, c), 1)
        for r in range(N - 1, -1, -1):
            if A[r][c] == 2:
                wall = r
                # add(start, getid(wall, c), 1)
            elif A[r][c] == 0:
                # if wall not in vis:
                #     add(start, getid(wall, c, 0), 1)
                #     vis.add(wall)
                # add(getid(wall, c, 0), getid(r, c, 0), 1)
                bottom[getid(r, c, 0)].append(getid(wall, c, 0))
            else:
                pass

    right = collections.defaultdict(list)
    for r in range(N):
        wall = M
        vis = set()
        for c in range(M - 1, -1, -1):
            if A[r][c] == 2:
                wall = c
            elif A[r][c] == 0:
                # if wall not in vis:
                #     add(getid(r, wall, 1), end, 1)
                #     vis.add(wall)
                # add(getid(r, c, 0), getid(r, wall, 1), 1)
                right[getid(r, c, 0)].append(getid(r, wall, 1))

    # draw()
    # print(dinic(start, end))

    g = collections.defaultdict(list)
    for r in range(N):
        for c in range(M):
            id = getid(r, c, 0)
            for a in bottom[id]:
                for b in right[id]:
                    g[a].append(b)
                    g[b].append(a)

    vis = [0 for _ in range(MAXN)]
    match = [-1 for _ in range(MAXN)]
    def dfs(u, tim):
        for v in g[u]:
            if vis[v] == tim:
                continue
            vis[v] = tim
            if match[v] < 0 or dfs(match[v], tim):
                match[u] = v
                match[v] = u
                return True

        return False

    tim = 1
    for i in range(MAXN):
        if match[i] < 0:
            tim += 1
            dfs(i, tim)

    ans = []
    for u in range(MAXN):
        if match[u] > u:
            v = match[u]
            ru, cu = toxy(u)
            rv, cv = toxy(v)

            ans.append((rv+1, cu+1))

    print(len(ans))
    print('\n'.join(['{} {}'.format(r, c) for r, c in ans]))





