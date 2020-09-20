# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/12 19:02

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


from functools import lru_cache

class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        n = len(edges)
        def get_cycle(g, start):
            cycle = set()
            father = [-1 for _ in range(n+1)]
            depth = [-1 for _ in range(n+1)]
            father[start] = start
            depth[start] = 0
            q = collections.deque([start])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if depth[v] < 0:
                        depth[v] = depth[u] + 1
                        father[v] = u
                        q.append(v)
                    else:
                        if father[u] == v:
                            continue

                        while depth[u] > depth[v]:
                            cycle.add(u)
                            u = father[u]
                        while depth[v] > depth[u]:
                            cycle.add(v)
                            v = father[v]
                        while u != v:
                            cycle.add(u)
                            cycle.add(v)
                            u = father[u]
                            v = father[v]
                        cycle.add(u)
                        return cycle

        def bfs(g, cycle, start):
            cycle_pos = -1
            min_arrival = float('inf')
            dist = [-1 for _ in range(n+1)]
            dist[start] = 0
            q = collections.deque([start])
            while q:
                u = q.popleft()
                if u in cycle and dist[u] < min_arrival:
                    min_arrival = dist[u]
                    cycle_pos = u
                for v in g[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        q.append(v)

            return dist, cycle_pos


        g = [[] for _ in range(n+1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # graph have n nodes and n edges, means it has one and only one cycle
        cycle = get_cycle(g, startA)
        dista, posa = bfs(g, cycle, startA)
        distb, posb = bfs(g, cycle, startB)

        if dista[startB] <= 1:
            return dista[startB]

        if dista[posb] > distb[posb] + 1 and len(cycle) >= 4:
            return -1

        ans = dista[startB]
        q = collections.deque([startB])
        arrived = {startB}
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in arrived and dista[v] > distb[v] + 1:
                    arrived.add(v)
                    q.append(v)
                    ans = max(ans, dista[v])
                else:
                    ans = max(ans, dista[v])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.chaseGame(edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5))
    print(s.chaseGame(edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3))
    print(s.chaseGame([[1,2],[2,3],[3,1],[3,6],[2,4],[4,5],[5,8],[4,7]], 6, 7))
