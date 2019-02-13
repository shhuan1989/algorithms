# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())
P = [0, 0] + [int(x) for x in input().split()]
S = [0] + [int(x) for x in input().split()]


isLeaf = [True] * (N+1)
for p in P:
    isLeaf[p] = False

leafs = [i for i in range(1, N+1) if isLeaf[i]]
for leaf in leafs:
    node = leaf
    x = -1
    while node > 0:
        if x < 0:
            x = S[node]
        elif S[node] > x:
            print(-1)
            exit(0)
        node = P[node]
        



G = collections.defaultdict(list)

for node in range(1, N+1):
    G[P[node]].append(node)
    
V = [0] * (N+1)
V[1] = S[1]


for leaf in leafs:
    node = leaf
    while node > 0:
        if S[node] < 0:
            V[node] = min([S[child]-S[P[node]] for child in G[node]] or [0])
            S[node] = S[P[node]] + V[node]
        node = P[node]
        
q = [1]
while q:
    node = q.pop(0)
    if S[node] >= 0:
        V[node] = S[node] - S[P[node]]
    
    q.extend(G[node])
    
    
    
# print(S)
# print(V)
print(sum(V[1:]))