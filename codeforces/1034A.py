# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/22/18

"""
import collections
import time

# t0 = time.time()
#
MAXN = 3 * 10 ** 7 // 2 + 100
# primes = [True for _ in range(MAXN)]
# primes[0] = primes[1] = False
# for i in range(2, MAXN):
#     if primes[i]:
#         v = i * 2
#         while v < MAXN:
#             primes[v] = False
#             v += i
# primes = [i for i in range(MAXN) if primes[i]]
#
# print(time.time() - t0)
# print(len(primes))


# for v / dtoprev[v] == prev[v]


def gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x


def gcda(vals):
    d = gcd(vals[0], vals[1])
    for i in range(2, len(vals)):
        d = gcd(d, vals[i])
        if d == 1:
            return d
    
    return d


def decomp2(val):
    cs = set()
    
    p = 2
    while p <= val:
        if val % p == 0:
            cs.add(p)
            while val % p == 0:
                val //= p
        p += 1
    
    return cs


primes = [True for _ in range(MAXN)]
prev = [0 for _ in range(MAXN)]
dtoprev = [0 for _ in range(MAXN)]

primes[0] = primes[1] = False
for i in range(2, MAXN):
    if primes[i]:
        v = i * 2
        prev[i] = i
        dtoprev[i] = 1
        while v < MAXN:
            primes[v] = False
            prev[v] = v//i
            dtoprev[v] = i
            
            v += i

    
N = int(input())
A = [int(x) for x in input().split()]


def decomp(val):
    cs = set()
    while prev[val] != val:
        cs.add(dtoprev[val])
        val = prev[val]
    cs.add(val)
    
    return cs



d = gcda(A)
pcounts = collections.defaultdict(int)
for x in A:
    print(decomp(x//d))
    for c in decomp(x//d):
        pcounts[c] += 1
    
ans = min([N-v for k, v in pcounts.items()] or [-1])
print(ans)