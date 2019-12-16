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
created by shhuan at 2019/12/12 22:17

"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        g = collections.defaultdict(set)
        d = collections.defaultdict(int)
        N = len(words)
        chs = set()
        for i in range(N):
            chs |= set(words[i])
            for j in range(i+1, N):
                a, b = words[i], words[j]
                for k in range(min(len(a), len(b))):
                    if a[k] != b[k]:
                        g[a[k]].add(b[k])
                        d[b[k]] += 1
                        break

        s = [k for k in chs if d[k] == 0]
        if s:
            # BFS计算最长路径，长度超过26代表有环
            def topo(start):
                dist = collections.defaultdict(int)
                q = [(-1, v) for v in g[start]]

                heapq.heapify(q)
                while q:
                    d, v = heapq.heappop(q)
                    d = abs(d)
                    if d > 26:
                        return False, []
                    dist[v] = max(dist[v], d)
                    for u in g[v]:
                        if dist[u] < d + 1:
                            dist[u] = d + 1
                            heapq.heappush(q, (-(d+1), u))
                dv = [(d, v) for v, d in dist.items()]
                dv.sort()
                return True, [start] + [v for d, v in dv]

            paths = []
            for u in s:
                c, p = topo(u)
                if not c:
                    return ''
                paths.append(p)

            # 合并路径
            def merge(pa, pb):
                for i in range(len(pa)):
                    for j in range(len(pb)):
                        if pa[i] == pb[j]:
                            k = 1
                            while k < min(len(pa)-i, len(pb)-i):
                                if pa[i+k] != pb[i+k]:
                                    break
                                k += 1
                            return pa[:i] + pb[:j] + pa[i:i+k] + merge(pa[i+k:], pb[j+k:])
                return pa + pb

            paths.sort()
            path = paths[0]
            for i in range(1, len(paths)):
                path = merge(path, paths[i])
            path = ''.join(path)

            # 如果有闭环，不会被便利，所以路径不会包含所有字符
            if len(path) != len(chs):
                return ''
            return path

        return ''


s = Solution()
print(s.alienOrder(["dvpzu","bq","lwp","akiljwjdu","vnkauhh","ogjgdsfk","tnkmxnj","uvwa","zfe","dvgghw","yeyruhev","xymbbvo","m","n"]))
print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(s.alienOrder(['z', 'x']))
print(s.alienOrder(['z', 'x', 'z']))
print(s.alienOrder(['zy', 'zx']))
print(s.alienOrder(['ac', 'ab', 'b']))
print(s.alienOrder(['a', 'b', 'c', 'b']))
print(s.alienOrder(["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]))