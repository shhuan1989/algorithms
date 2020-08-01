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
created by shhuan at 2020/7/16 22:00

"""

def get_state(A, B, C):
    return '-'.join([''.join(A), ''.join(B), ''.join(C)])

def bfs(N, S):
    q = [([chr(ord('a') + i) for i in range(N)], [], [], 0, [])]
    out = list(reversed(S))
    # step = 0
    vis = {get_state(q[0][0], [], [])}
    while q:
        # print(step, len(q))
        # step += 1
        nq = []
        for A, B, C, oi, pre in q:
            if oi >= len(out):
                return pre
            ops = []
            if A:
                # A => D
                if A[-1] == out[oi]:
                    ops.append(('0', '{} A D'.format(A[-1]), 0, 3))
                # A => B
                ops.append((A[-1], '{} A B'.format(A[-1]), 0, 1))

                # A => C
                if not C or out.index(A[-1]) < out.index(C[-1]):
                    ops.append((A[-1], '{} A C'.format(A[-1]), 0, 2))

            if B:
                # B => D
                if B[-1] == out[oi]:
                    ops.append(('0', '{} B D'.format(B[-1]), 1, 3))

                # B => C
                if not C or out.index(B[-1]) < out.index(C[-1]):
                    ops.append((B[-1], '{} B C'.format(B[-1]), 1, 2))

            # C => D
            if C and C[-1] == out[oi]:
                ops.append(('0', '{} C D'.format(C[-1]), 2, 3))
            ops.sort()
            for w, v, s, t in ops:
                SS = [A.copy(), B.copy(), C.copy(), []]
                a = SS[s].pop()
                SS[t].append(a)
                na, nb, nc, nd = SS
                ns = get_state(na, nb, nc)
                if ns not in vis:
                    nq.append((na, nb, nc, oi+1 if t == 3 else oi, pre+[v]))
                    vis.add(ns)
                if w == '0':
                    break
        q = nq

    return ['NO']



if __name__ == '__main__':
    N = int(input())
    S = input().strip()
    print('\n'.join(bfs(N, S)))
