# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/20 20:14

"""


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """

        vi = collections.defaultdict(list)
        for i, v in enumerate(A):
            vi[v].append(i)

        vs = list(sorted(vi.keys()))

        ans = 0
        for ia, a in enumerate(vs):
            for ib in range(ia, len(vs)):
                b = vs[ib]
                c = target - a - b
                if c < b:
                    break
                if c in vi:
                    ais, bis, cis = vi[a], vi[b], vi[c]


        return ans






s = Solution()
print(s.threeSumMulti(A = [1,1,2,2,3,3,4,4,5,5], target = 8))
# print(s.threeSumMulti(A = [1,1,2,2,2,2], target = 5))
# print(s.threeSumMulti([0,2,0], 2))
# print(s.threeSumMulti([0,0,0], 0))
# print(s.threeSumMulti([2,1,3], 6))