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
created by shhuan at 2020/1/5 10:43

"""


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        current = 0
        q = [id]
        vis = {id}
        while q:
            if current == level:
                watched = []
                for v in q:
                    watched.extend(watchedVideos[v])
                wc = [(c, w) for w, c in collections.Counter(watched).items()]
                wc.sort()
                return [w for c, w in wc]
            nq = []
            for u in q:
                for v in friends[u]:
                    if v not in vis:
                        vis.add(v)
                        nq.append(v)
            q = nq
            current += 1

        return []

s = Solution()
print(s.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))
print(s.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))
print(s.watchedVideosByFriends([["m"],["xaqhyop","lhvh"]], [[1],[0]], 1, 1))




