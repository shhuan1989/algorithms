# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""


import collections
import heapq

import bisect


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """

        mxs = sum(rods) // 2
        states = {(0, 0)}
        for i, v in enumerate(rods):
            nstates = set()
            for a, b in states:
                if a + v <= mxs:
                    nstates.add((a+v, b))
                if b + v <= mxs:
                    nstates.add((a, b+v))
            states |= nstates

        ans = 0
        for a, b in states:
            if a == b:
                ans = max(ans, a)

        print(len(states))
        return ans




s = Solution()
print(s.tallestBillboard( [1,2,3,6]))
print(s.tallestBillboard([1,2,3,4,5,6]))
print(s.tallestBillboard([1,2]))
print(s.tallestBillboard([175,145,180,156,151,132,131,150,154,144,137,128,156,161,150]))
print(s.tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))