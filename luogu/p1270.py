# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MAXN = 1001
cost = [0 for _ in range(MAXN)]
count = [0 for _ in range(MAXN)]
f = [[0 for _ in range(2001)] for _ in range(1001)]

pi = [0]


def read(curr, path):
    i = pi[0]
    d = path[i]
    c = path[i + 1]
    pi[0] += 2
    cost[curr] = d * 2
    count[curr] = c
    if c == 0:
        read(curr * 2, path)
        read(curr * 2 + 1, path)


def dfs(curr, t):
    if count[curr] > 0:
        i = 0
        while i // 5 <= count[curr] and cost[curr] + i <= t:
            f[curr][cost[curr]+i] = i // 5
            i += 1
    else:
        dfs(curr * 2, t)
        dfs(curr * 2 + 1, t)
        
        for costincurr in range(cost[curr], t+1):
            leftcost = 0
            while leftcost + cost[curr] <= costincurr:
                f[curr][costincurr] = max(f[curr][costincurr], f[curr * 2][leftcost] + f[curr * 2 + 1][costincurr - cost[curr] - leftcost])
                leftcost += 1
    

if __name__ == '__main__':
    # sys.stdin = open('p1270.in', 'r')
    t = int(input()) - 1
    A = [int(x) for x in input().split()]
    
    read(1, A)
    dfs(1, t)
    print(f[1][t])
