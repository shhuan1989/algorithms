# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

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
    cost = [[float('inf') for _ in range(N)] for _ in range(N)]
    
    for s in range(N-1):
        row = [int(x) for x in input().split()]
        for t in range(len(row)):
            cost[s][s+t+1] = row[t]
    
    # for row in cost:
    #     print(row)
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])
    
    print(cost[0][-1])