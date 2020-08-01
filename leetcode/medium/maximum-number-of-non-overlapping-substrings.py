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
created by shhuan at 2020/7/19 13:06

"""



class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        chs = set()

        for i, v in enumerate(s):
            if v not in left:
                left[v] = i
                right[v] = i
            else:
                right[v] = i

            chs.add(v)




        lr = {}
        for ch in chs:
            l, r = left[ch], right[ch]
            others = set(s[l: r+1])
            while len(others) > 0:
                nl = min([left[o] for o in others])
                nr = max([right[o] for o in others])

                nothers = set()
                for i in range(nl, l):
                    nothers.add(s[i])
                for i in range(r+1, nr+1):
                    nothers.add(s[i])
                others = nothers
                l = min(l, nl)
                r = max(r, nr)
            lr[ch] = (l, r)

        a = [(v[1]-v[0]+1, k, v[0], v[1]) for k, v in lr.items()]
        a.sort()

        # print(a)

        ans = []
        n = len(s)
        used = [False for _ in range(n)]
        for d, cj, l, r in a:
            if any([used[i] for i in range(l, r+1)]):
                continue

            for i in range(l, r+1):
                used[i] = True
            ans.append(s[l: r+1])
        return ans