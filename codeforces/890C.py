# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/12 23:57

"""

# N = int(input())
#
# T = [int(x) for x in input().split()]


def funcA(N, T):
    # time:room
    E = collections.defaultdict(int)
    E[0] = 1

    # room: time
    last = collections.defaultdict(int)
    last[1] = 0

    roomNo = 1
    for i in range(N):
        t = T[i]
        ct = i + 1
        if t in E:
            room = E[t]
            if last[room] == t:
                last[room] = ct
                E[ct] = room
            else:
                roomNo += 1
                E[ct] = roomNo
                last[roomNo] = ct
        else:
            roomNo += 1
            E[ct] = roomNo
            last[roomNo] = ct

    # print(roomNo)
    return roomNo

def funcB(N, T):
    vis = set()
    ans = 1
    for v in T:
        if v in vis:
            ans += 1
        vis.add(v)
    # print(ans)
    return ans




for i in range(10000):
    N = random.randint(1, 2000)
    T = [random.randint(0, i-1) for i in range(1, N+1)]
    if funcA(N, T) != funcB(N, T):
        print(N)
        print(T)
