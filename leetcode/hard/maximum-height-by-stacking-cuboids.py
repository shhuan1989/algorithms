# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/13 10:45

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
sys.setrecursionlimit(100000000)
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:


        def getkey(cub):
            return '-'.join(map(str, list(sorted(cub))))

        wc = collections.defaultdict(int)
        uniq = []
        for cub in cuboids:
            key = getkey(cub)
            wc[key] += 1
            if wc[key] == 1:
                uniq.append(cub)

        cuboids = uniq

        n = len(cuboids)

        g = collections.defaultdict(list)


        start = 100000

        for i in range(n):
            ica = 0
            for cuba in itertools.permutations(cuboids[i]):
                ida = i * 10 + ica
                ica += 1
                g[start].append((ida, cuba[2] * wc[getkey(cuba)]))
                for j in range(n):
                    if i == j:
                        continue
                    icb = 0
                    for cubb in itertools.permutations(cuboids[j]):
                        idb = j * 10 + icb
                        icb += 1
                        if all([cuba[k] <= cubb[k] for k in range(3)]):
                            g[ida].append((idb, cubb[2] * wc[getkey(cubb)]))



        # def dfs(u, vis):
        #     ans = 0
        #
        #     for v, w in g[u]:
        #         if v not in vis:
        #             ans = max(ans, w + dfs(v, vis | {v}))
        #
        #     return ans
        #
        #
        # return dfs(start, {start})

        q = [(0, start)]
        dist = collections.defaultdict(int)
        while q:
            d, u = heapq.heappop(q)
            for v, w in g[u]:
                nd = w-d
                if nd > dist[v]:
                    dist[v] = nd
                    heapq.heappush(q, (-nd, v))
            # print(dist)

        return max(dist.values())




if __name__ == '__main__':
    s = Solution()
    print(s.maxHeight([[50,45,20],[95,37,53],[45,23,12]]))
    print(s.maxHeight([[38,25,45],[76,35,3]]))
    print(s.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))


