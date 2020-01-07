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
import functools
import operator

"""
created by shhuan at 2020/1/4 19:00

"""

MOD = 1000000007


def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n
    numer = functools.reduce(operator.mul, range(n, n-r, -1))
    denom = functools.reduce(operator.mul, range(1, r+1))
    return numer//denom



def bruteforce(N, A):

    presum = [0] * N
    suffix = [0] * N
    wc = collections.Counter(A)

    def dfs(index, cwc, total):
        if index >= N-1:
            for i, v in enumerate(presum):
                if i < N-1:
                    suffix[i+1] = total-v
            suffix[0] = total

            x = collections.defaultdict(int)
            for i, v in enumerate(presum):
                x[v] += 1
            for i, v in enumerate(suffix):
                x[v] += 1
            if any([x[w] != c for w, c in wc.items()]):
                return 0
            # print(presum)
            return 1

        ans = 0
        for w, c in cwc.items():
            presum[index] = w
            nwc = {nw: nc for nw, nc in cwc.items() if nw != w and nw != total - w}
            if c > 1:
                nwc[w] = c - 1
                nwc[total-w] = c - 1
            ans += dfs(index+1, nwc, total)
        return ans

    ans = 0
    for w, c in wc.items():
        if c >= 2:
            nwc = {nw: nc for nw, nc in wc.items() if nw != w}
            if c > 2:
                nwc[w] = c - 2
            presum[-1] = w
            ans += dfs(0, nwc, w)

    return ans


def solve(N, A):
    wc = collections.Counter(A)
    ans = 0
    for suma, sc in wc.items():
        if sc < 2:
            continue
        awc, ewc = [], []
        if suma == 0:
            if sc % 2 != 0:
                continue
            else:
                if sc - 2 > 0:
                    ewc.append((suma, (sc-2)//2))
        else:
            if 0 in wc:
                if wc[0] != sc - 2:
                    continue
                else:
                    awc.append((0, sc-2))
            if any([suma-w not in wc or wc[suma-w] != c for w, c in wc.items() if w != 0 and w != suma]):
                continue

            if any([suma-w == w and wc[w] % 2 != 0 for w, c in wc.items() if w != 0 and w != suma]):
                continue

            for w, c in wc.items():
                if w == 0 or w == suma:
                    continue
                if w < suma-w:
                    awc.append((w, c))
                elif w == suma-w:
                    ewc.append((w, c//2))

        s = 1
        n = 2 * N - 2
        for aw, ac in awc:
            s *= ncr(n, ac)
            s %= MOD
            n -= ac * 2

        n //= 2
        for ew, ec in ewc:
            s *= ncr(n, ec)
            s %= MOD
            n -= ec

        ans += s
        ans %= MOD
    return ans



def test():
    import random
    while True:
        print('=' * 40)
        N = random.randint(1, 2)
        A = [random.randint(-100, 100) for _ in range(N)]
        print(A)
        print(N)

        presum = []
        for v in A:
            if not presum:
                presum.append(v)
            else:
                presum.append(presum[-1] + v)
        suffix = []
        for v in reversed(A):
            if not suffix:
                suffix.append(v)
            else:
                suffix.append(suffix[-1] + v)
        B = presum + suffix
        A, B = B, A
        print(A)


        print('brute force')
        ba = bruteforce(N, A)
        print(ba)
        print('solve')
        sa = solve(N, A)
        print(sa)
        if ba != sa:
            break


# test()

# bruteforce(3, [5, 3, 7, 10, 5, 10])

T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    # ans.append(solve(N, A))
    ans.append(bruteforce(N, A))

print('\n'.join(map(str, ans)))
