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
created by shhuan at 2020/7/30 20:13

"""



if __name__ == '__main__':
    N = int(input())
    G = {}

    A = []
    for i in range(N):
        a, b = input().strip().split('->')
        G[a] = b
        A.append((a, b))


    def bfs(s, t, index):
        pre = collections.defaultdict(set)
        vis = set(s)
        visi = set()

        for i, (a, b) in enumerate(A):
            if all([c in s for c in a]):
                vis

        q = []
        while True:
            more = False
            for i, (a, b) in enumerate(A):
                if i in visi:
                    continue
                more = True
                visi.add(i)
                if all([c in vis for c in a]):
                    vis |= set(b)
                    p = {pre[c] for c in a}
                    for c in b:
                        pre[c] = p
            if not more:
                break

        if all([c in vis for c in t]):
            return {pre[c] for c in t}

        return None



    hasred = False
    for i, (a, b) in enumerate(A):
        x = bfs(a, b, i)
        if x:
            y = ' '.join(map(str, [v+1 for v in sorted(x)]))
            print('FD {} is redundant using FDs: {}'.format(i+1, y))
            hasred = True
    if not hasred:
        print('No redundant FDs')


