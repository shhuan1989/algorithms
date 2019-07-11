# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-30

"""

import collections
import time
import os
import sys
import bisect
import heapq




# print(primes)

N = int(input())
s1, s2 = 0, 0

vals = [int(x) for x in input().split()]
for v in vals:
    if v == 1:
        s1 += 1
    else:
        s2 += 1

MAXN = s1 + 2*s2 + 10

# MAXN = 200000 * 2 + 10
ip = [True for _ in range(MAXN)]
ip[0] = ip[1] = False

for i in range(2, MAXN):
    if ip[i]:
        v = i + i
        while v < MAXN:
            ip[v] = False
            v += i

primes = [i for i in range(MAXN) if ip[i]]





pi = 0
p = primes[pi]
ans = []
presum = 0
while pi < len(primes) and s1 > 0 and s2 > 0:
    p = primes[pi] - presum
    s2need = p // 2
    if s2 >= s2need:
        s2 -= s2need
        ans.extend([2] * s2need)
        if p % 2 == 1:
            s1 -= 1
            ans.append(1)
    else:
        ans.extend([2] * s2)
        s1need = p - 2*s2
        if s1 >= s1need:
            s1 -= s1need
            ans.extend([1] * s1need)
        else:
            ans.extend([1] * s1)
            s1 = 0
        
        s2 = 0
    presum += p
    pi += 1

if s1 > 0:
    ans.extend([1] * s1)

if s2 > 0:
    ans.extend([2] * s2)
    
print(' '.join(map(str, ans)))

