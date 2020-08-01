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
created by shhuan at 2020/7/24 21:36

"""

def main():
    MAXN = 5*10**5+5
    parent = [i for i in range(MAXN)]
    tail = [i for i in range(MAXN)]
    dist = [0 for _ in range(MAXN)]

    def find(u):
        if parent[u] == u:
            return parent[u], 0

        pu, pd = find(parent[u])
        dist[u] += pd
        parent[u] = pu
        return pu, dist[u]

    def merge(u, v):
        pu, du = find(u)
        pv, dv = find(v)
        parent[pu] = tail[pv]
        dist[pu] = 1
        tail[pv] = tail[pu]



    N = int(input())
    ans = []
    for i in range(N):
        a, b, c = input().strip().split()
        b, c = int(b), int(c)

        if a == 'M':
            merge(b, c)
        else:
            pb, db = find(b)
            pc, dc = find(c)
            if pb == pc:
                ans.append(abs(db-dc)-1)
            else:
                ans.append(-1)
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()