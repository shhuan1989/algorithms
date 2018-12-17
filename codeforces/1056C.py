# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/14/18

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, M = map(int, input().split())
P = [0] + [int(x) for x in input().split()]
A = [0 for _ in range(2*N+1)]
pairs = []
for i in range(M):
    a, b = map(int, input().split())
    A[a] = b
    A[b] = a
    pairs.append((a, b))


sp = [(P[i], i) for i in range(1, 2*N+1)]
sp.sort(reverse=True)
vis = [False] * (2*N+1)

T = int(input())
if T == 1:
    for a, b in pairs:
        if P[a] >= P[b]:
            print(a)
            sys.stdout.flush()
            input()
        else:
            print(b)
            sys.stdout.flush()
            input()
        vis[a] = True
        vis[b] = True
    
    for p, i in sp:
        if not vis[i]:
            print(i)
            sys.stdout.flush()
            b = int(input())
            vis[b] = True
else:
    selected = 0
    for _ in range(N):
        b = int(input())
        selected += 1
        vis[b] = True
        if A[b] > 0 and not vis[A[b]]:
            print(A[b])
            selected += 1
            vis[A[b]] = True
            sys.stdout.flush()
        else:
            break

    for a, b in pairs:
        if vis[a] or vis[b]:
            continue
        selected += 2
        if P[a] >= P[b]:
            print(a)
            sys.stdout.flush()
            input()
        else:
            print(b)
            sys.stdout.flush()
            input()
        vis[a] = True
        vis[b] = True

    for p, i in sp:
        if not vis[i]:
            print(i)
            sys.stdout.flush()
            selected += 1
            if selected >= 2*N:
                break
            b = int(input())
            vis[b] = True
            selected += 1
    