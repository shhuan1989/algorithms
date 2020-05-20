# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, M, edges, K, path):

  s, t = path[0], path[-1]

  after = [[] for _ in range(N+1)]
  dist = [N+1 for _ in range(N+1)]
  dist[t] = 0

  d = 0
  q = [t]
  while q:
    d += 1
    nq = []
    for u in q:
      for v in edges[u]:
        if dist[v] > d:
          dist[v] = d
          after[v] = [u]
          nq.append(v)
        elif dist[v] == d:
          after[v].append(u)

    q = nq


  minRebuild, maxRebuild = 0, 0

  for i in range(len(path)-1):
    if path[i+1] in after[path[i]]:
      if len(after[path[i]]) > 1:
        maxRebuild += 1
    else:
      minRebuild += 1
      maxRebuild += 1


  return [minRebuild, maxRebuild]



N, M = map(int, input().split())
edges = collections.defaultdict(list)
for i in range(M):
  u, v = map(int, input().split())
  edges[v].append(u)

K = int(input())
path = [int(x) for x in input().split()]

print(' '.join(map(str, solve(N, M, edges, K, path))))
