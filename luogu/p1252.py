# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/10 21:12

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

    A = []
    for i in range(5):
        row = [int(x) for x in input().split()]
        A.append(row)



    def dfs(index, cost, rest, path):
        if index >= 5:
            return (cost if rest == 0 else float('inf'), path)

        if rest <= 0:
            return float('inf'), []


        minCost = float('inf')
        ans = []
        for i in range(10):
            nc, np = dfs(index+1, cost + A[index][i], rest-i-1, path+[i+1])
            if nc < minCost:
                minCost = nc
                ans = np

        return minCost, ans

    c, p = dfs(0, 0, 25, [])
    print(c)
    print(' '.join(map(str, p)))