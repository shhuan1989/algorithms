# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N, M = map(int, input().split())

G = collections.defaultdict(set)

nodes = set()
for _ in range(N):
  u, v = map(int, input().split())
  nodes.add(u)
  nodes.add(v)
  G[u].add(v)


def find_cycle(graph, u, edges, vis):
  for v in graph[u]:
    if v not in vis:
      ans = find_cycle(graph, v, edges | {(u, v)}, vis | {v})
      if ans:
        return ans
    else:
      return edges | {(u, v)}

  return set()


def have_cycle(graph, nodes):
  for u in nodes:
    if find_cycle(graph, u, set(), {u}):
      return True

  return False

for u in nodes:
  cycle = find_cycle(G, u, set(), {u})
  if cycle:
    for u, v in cycle:
      G[u].discard(v)
      if not have_cycle(G, nodes):
        # print(e)
        print("YES")
        exit(0)
      G[u].add(v)

    print("NO")
    exit(0)

print("YES")

