# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(start, rules):
    link = [[False for _ in range(10)] for _ in range(10)]
    for u, v in rules.items():
        for w in v:
            link[u][w] = True
    
    for i in range(10):
        link[i][i] = True
        
    for k in range(10):
        for i in range(10):
            for j in range(10):
                link[i][j] = link[i][j] or (link[i][k] and link[k][j])
    
    W = [0 for _ in range(10)]
    for i in range(10):
        W[i] = sum([1 if link[i][j] else 0 for j in range(10)])
    
    
    ans = 1
    for i, v in enumerate(start):
        ans *= W[int(v)]
    
    return ans
    

if __name__ == '__main__':
    N, K = map(int, input().split())
    rules = collections.defaultdict(set)
    for i in range(K):
        a, b = map(int, input().split())
        if b != 0 and b != a:
            rules[a].add(b)

    print(solve(str(N), rules))
