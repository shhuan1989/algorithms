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
created by shhuan at 2020/7/14 20:42

"""



if __name__ == '__main__':

    N, M, P = map(int, input().split())
    C = [[0 for _ in range(N)] for _ in range(M+1)]
    for i in range(N):
        c = [0] + [int(x) for x in input().split()]
        for t in range(1, M+1):
            C[t][i] = c[t]

    cost = [int(x) for x in input().split()]


    coins = [[[0 for _ in range(P+1)] for _ in range(N)] for _ in range(M+1)]
    for s in range(N):
        for t in range(1, P+1):
            coins[1][s][t] = coins[1][s][t-1] + C[t][(s+t-1)%N]

    for t in range(2, M+1):
        for s in range(N):
            coins[t][s][1] = C[t][s]
            for p in range(2, min(P-1, M+1-t)+1):
                coins[t][s][p] = coins[t-1][(s-1)%N][p+1] - C[t-1][(s-1)%N]
            if t + P - 1 <= M:
                coins[t][s][P] = coins[t-1][(s-1)%N][P] - C[t-1][(s-1)%N] + C[t+P-1][(s+P-1)%N]

    dp = [0 for _ in range(M+1)]
    dp[1] = max([coins[1][s][1]-cost[s] for s in range(N)])
    for t in range(2, M+1):
        for pt in range(max(t-P, 0), t):
            dp[t] = max(dp[t], dp[pt] + max([coins[pt+1][s][t-pt]-cost[s] for s in range(N)]))



    print(dp[M])