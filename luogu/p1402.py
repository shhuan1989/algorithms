# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/17 11:03

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



MAXN = 20000
MAXM = 10000
INF = 10**9+7


head = [-1 for _ in range(MAXN)]
depth = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, c):
    tot[0] += 1
    i = tot[0]

    to[i] = v
    cap[i] = c
    nxt[i] = head[u]
    head[u] = i


def add(u, v, c):
    add_edge(u, v, c)
    add_edge(v, u, 0)
    # print(u, v)

def bfs(start, end):
    for i in range(MAXN):
        depth[i] = -1

    q = collections.deque([start])
    depth[start] = 0

    while q:
        u = q.popleft()
        i = head[u]
        while i >= 0:
            v = to[i]
            if depth[v] < 0 and cap[i] - flow[i] > 0:
                depth[v] = depth[u] + 1
                q.append(v)
            i = nxt[i]

    return depth[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add

    ret = 0
    i = head[curr]
    while i >= 0 and add > 0:
        v = to[i]
        if depth[v] == depth[curr]+1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]))
            if f > 0:
                ret += f
                add -= f
                flow[i] += f
                flow[i ^ 1] -= f
        i = nxt[i]

    return ret


def max_flow(start, end):
    f = 0
    while bfs(start, end):
        f += dfs(start, end, INF)
    return f


if __name__ == '__main__':
    N, P, Q = map(int, input().strip().split())

    start, end = 0, 10000

    def getid(v, type):
        return type * 100 + v

    # room
    for v in range(1, P+1):
        add(start, getid(v, 1), 1)

    # dish
    for v in range(1, Q+1):
        add(getid(v, 2), end, 1)

    # customer
    for v in range(1, N+1):
        add(getid(v, 3), getid(v, 4), 1)

    for person in range(1, N+1):
        row = [0] + [int(x) for x in input().split()]
        for room in range(1, P+1):
            if row[room] == 1:
                add(getid(room, 1), getid(person, 3), 1)

    for person in range(1, N+1):
        row = [0] + [int(x) for x in input().split()]
        for dish in range(1, Q+1):
            if row[dish] == 1:
                add(getid(person, 4), getid(dish, 2), 1)

    print(max_flow(start, end))


