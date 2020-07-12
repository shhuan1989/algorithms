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
created by shhuan at 2020/7/11 17:10

"""




if __name__ == '__main__':
    N = int(input())
    A = [ord(v)-ord('A') for v in input()]
    B = [ord(v)-ord('A') for v in input()]
    C = [ord(v)-ord('A') for v in input()]
    V = [-1 for _ in range(N)]
    W = [False for _ in range(N)]
    VIS = [False for _ in range(N)]

    def check(a, va, b, vb):
        if a == b and va != vb:
            return False
        if a != b and va == vb:
            return False
        return True


    def dfs(index, cap):
        if index <= 0:
            return True

        a, b, c = A[index], B[index], C[index]
        # hasa, hasb, hasc = a in keys, b in keys, c in keys
        rest = [v for v in range(N) if not VIS[v]]
        for va in rest if not W[a] else [V[a]]:
            bp = [va] if b == a else [v for v in (rest if not W[b] else [V[b]]) if v != va]
            for vb in bp:
                cp = [va] if c == a else ([vb] if c == b else [v for v in (rest if not W[c] else [V[c]]) if v != va and v != vb])
                for vc in cp:
                    if cap and vc != (va + vb + 1) % N:
                        continue
                    if not cap and vc != (va + vb) % N:
                        continue

                    if not W[a]:
                        V[a] = va
                    if not W[b]:
                        V[b] = vb
                    if not W[c]:
                        V[c] = vc

                    added = [x for x in [a, b, c] if not W[x]]
                    for x in added:
                        W[x] = True
                    addedv = [x for x in [va, vb, vc] if not VIS[x]]
                    for x in addedv:
                        VIS[x] = True
                    ncap = va + vb + (1 if cap else 0) >= N
                    if dfs(index-1, ncap):
                        return True
                    for x in added:
                        W[x] = False
                    for x in addedv:
                        VIS[x] = False
                    if not W[a]:
                        V[a] = -1
                    if not W[b]:
                        V[b] = -1
                    if not W[c]:
                        V[c] = -1
        return False

    def solve():
        a, b, c = A[0], B[0], C[0]
        for va in range(N):
            for vb in range(N):
                if not check(a, va, b, vb):
                    continue
                for vc in range(N):
                    if not check(a, va, c, vc):
                        continue
                    if not check(b, vb, c, vc):
                        continue
                    V[a] = va
                    V[b] = vb
                    V[c] = vc
                    for x in [a, b, c]:
                        W[x] = True
                    for x in [va, vb, vc]:
                        VIS[x] = True
                    if dfs(N-1, False):
                        return True

                    for x in [a, b, c]:
                        V[x] = -1
                        W[x] = False
                    for x in [va, vb, vc]:
                        VIS[x] = False

        return False

    solve()
    print(' '.join(map(str, V)))
