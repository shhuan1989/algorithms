# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

T = int(input())

def dist(a, b):
    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)



def solve(start, ab, cd, ef, N, M, K):
    s = start
    dsab = [dist(s, v) for v in ab]
    decd = []
    for i in range(M):
        mind = float('inf')
        mi = -1
        for j in range(K):
            d = dist(cd[i], ef[j])
            if d < mind:
                mind = d
                mi = j
        decd.append((mi, mind))
    
    ans = float('inf')
    for n in range(N):
        d1 = dsab[n]
        for m in range(M):
            k, d3 = decd[m]
            d2 = dist(ab[n], cd[m])
            ans = min(ans, d1+d3+d2)
    
    return ans


for ti in range(T):
    x, y = map(int, input().split())
    N, M, K = map(int, input().split())
    ab = [int(v) for v in input().split()]
    cd = [int(v) for v in input().split()]
    ef = [int(v) for v in input().split()]

    ab = [(ab[2*i], ab[2*i+1]) for i in range(len(ab)//2)]
    cd = [(cd[2*i], cd[2*i+1]) for i in range(len(cd)//2)]
    ef = [(ef[2*i], ef[2*i+1]) for i in range(len(ef)//2)]



    start = (x, y)
    ans = float('inf')
    ans = min(ans, solve(start, ab, cd, ef, N, M, K))
    ans = min(ans, solve(start, cd, ab, ef, M, N, K))
    
    print(ans)
