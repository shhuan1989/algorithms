# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10**9+7
MAXN = 10**5 + 5
isprime = [True for _ in range(MAXN)]
for i in range(2, MAXN):
    if not isprime:
        continue
    v = i + i
    while v < MAXN:
        isprime[v] = False
        v += i

primes = [i for i in range(2, MAXN) if isprime[i]]
primes = []


def gcd(x, y):
    while y:
        x, y = y, x%y
        
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def defac(v):
    wc = collections.defaultdict(int)
    pi = 0
    while pi < len(primes) and v > 1:
        p = primes[pi]
        if v < p:
            break
        while v % p == 0:
            wc[p] += 1
            v //= p
        pi += 1
    if v > 1:
        wc[v] += 1
    
    return wc


def solve(a, b, c, d):
    # gcd(x, a) = b
    # lcm(x, c) = d
    
    if a < b or c > d or d % c != 0 or a % b != 0:
        return 0
        
    da, db, dc, dd = defac(a), defac(b), defac(c), defac(d)
    base = set(da.keys()) | set(db.keys()) | set(dc.keys()) | set(dd.keys())

    minxi = {i: 0 for i in base}
    maxxi = {i: INF for i in base}
    f = d // c
    # print(f)
    if f > 1:
        # lcm(x, c) == d => x*c/gcd(x, c) == d
        # x/gcd(x, c) == d/c == f
        # 1. f == 1 => x = gcd(x, c)
        # 2. xi-min(xi, ci) = fi
        
        df = defac(f)
        for bf in base:
            pf = df[bf]
            if pf == 0:
                # xi - min(xi, ci) == 0 => xi <= ci
                # px in [0, pf]
                minxi[bf] = 0
                maxxi[bf] = dc[bf]
            else:
                # xi - min(xi, ci) > 0 => xi > ci and xi-ci=f => xi = f+ci
                # px = pf
                minxi[bf] = pf + dc[bf]
                maxxi[bf] = pf + dc[bf]
    else:
        # gcd(x, c) == x => x <= c and c % x == 0
        for bb in base:
            maxxi[bb] = dc[bb]

    # gcd(x,a) ==  b
    for bb in base:
        pb = db[bb]
        if pb == da[bb]:
            # px in [pb, +]
            minxi[bb] = max(minxi[bb], pb)
        else:
            # px == pb
            if pb < minxi[bb] or pb > maxxi[bb]:
                return 0
        
            minxi[bb] = pb
            maxxi[bb] = pb

    # print(maxxi)
    # print(minxi)

    if any([v >= INF for v in maxxi.values()]):
        return 0

    ans = 1
    for i in base:
        ans *= maxxi[i] - minxi[i] + 1

    return ans


import math
def solve2(a, b, c, d):
    if a < b or c > d or d % c != 0 or a % b != 0:
        return 0
    
    ans = 0
    
    for i in range(1, int(math.sqrt(d))+10):
        if d % i == 0:
            if i > d//i:
                break
            for x in [i, d//i] if i != d//i else [i]:
                if x % b == 0 and gcd(x, a) == b and lcm(x, c) == d:
                    # print(x)
                    ans += 1
    
    return ans


if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(N):
        a, b, c, d = map(int, input().split())
        ans.append(solve2(a, b, c, d))
    print('\n'.join(map(str, ans)))
