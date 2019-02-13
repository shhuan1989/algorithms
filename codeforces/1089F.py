# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math


def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

# N = int(input())
import random
N = random.randint(100, 10**9)
print(N)

N = 619335746

sqn = int(math.sqrt(N))
primes = [True] * (2 + sqn)
primes[0] = False
primes[1] = False

divisors = []
for i in range(2, 2 + sqn):
    if primes[i]:
        if N % i == 0:
            divisors.append(i)
        v = i
        while v + i < 2 + sqn:
            v += i
            primes[v] = False

print(divisors)
X = [0] * len(divisors)


def dfs(index, total):
    if index >= len(divisors):
        if total == N-1:
            return True
        else:
            return False
    if total > N-1:
        return False
    
    for v in range((N-total-1)//divisors[index], -1, -1):
        X[index] = v
        if dfs(index+1, total + v * divisors[index]):
            return True
        
    return False

dfs(0, 0)

print(X)


ans = []
for i in range(len(divisors)):
    xi = X[i]
    yi = divisors[i]
    
    g = gcd(xi*yi, N)
    ai, bi = xi*yi//g, N//g
    if ai > 0:
        ans.append((ai, bi))
    
print(len(ans))
print('\n'.join([' '.join(map(str, x)) for x in ans]))

    
        




        