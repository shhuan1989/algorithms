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
created by shhuan at 2019/12/19 20:53

"""

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:


        g = collections.defaultdict(list)
        ds = set()
        for u, v in synonyms:
            g[u].append(v)
            g[v].append(u)
            ds.add(u)
            ds.add(v)


        vis = set()
        groups = []

        for w in ds:
            if w not in vis:
                group = [w]
                q = [w]
                vis.add(w)
                while q:
                    u = q.pop()
                    for v in g[u]:
                        if v not in vis:
                            vis.add(v)
                            group.append(v)
                            q.append(v)
                groups.append(list(sorted(group)))

        root = {}
        for i, group in enumerate(groups):
            for w in group:
                root[w] = i

        def syn(w):
            return groups[root[w]]

        def dfs(s, index, pre):
            if index >= len(s):
                return [' '.join(pre)]

            if s[index] in ds:
                ans = []
                for u in syn(s[index]):
                    ans.extend(dfs(s, index+1, pre + [u]))
                return ans
            else:
                return dfs(s, index+1, pre+[s[index]])


        return dfs(text.split(' '), 0, [])


s = Solution()
print(s.generateSentences(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
                          text = "I am happy today but was sad yesterday"))