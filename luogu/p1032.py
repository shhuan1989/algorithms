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
created by shhuan at 2020/7/8 20:50

"""


def trans(G, s):
    t = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            a = s[i:j]
            if a in G:
                for b in G[a]:
                    t.append(s[:i] + b + s[j:])

    return t


def solve(G, start, target):
    step = 0
    q = [start]
    vis = {start}
    while True:
        step += 1
        if step > 10:
            return 'NO ANSWER!'
        nq = []
        for a in q:
            after = trans(G, a)
            for b in after:
                if b == target:
                    return step
                if b not in vis:
                    vis.add(b)
                    nq.append(b)
        q = nq


if __name__ == '__main__':
    A, B = '', ''
    G = collections.defaultdict(list)
    i = 0
    for line in sys.stdin:
        a, b = line.split()
        if i == 0:
            A, B = a, b
        else:
            G[a].append(b)
        i += 1


    print(solve(G, A, B))

