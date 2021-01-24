# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/27 10:54

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


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        trie = {}

        def insert(val):
            t = trie
            for i in range(63, -1, -1):
                if (val & (1 << i)) > 0:
                    if 1 not in t:
                        t[1] = {}
                    t = t[1]
                else:
                    if 0 not in t:
                        t[0] = {}
                    t = t[0]
            t[2] = True

        def find(val):
            t = trie
            x = 0
            for i in range(63, -1, -1):
                if (val & (1 << i)) > 0:
                    if 0 in t:
                        x |= 1 << i
                        t = t[0]
                    elif 1 in t:
                        t = t[1]
                    else:
                        return -1
                else:
                    if 1 in t:
                        x |= 1 << i
                        t = t[1]
                    elif 0 in t:
                        t = t[0]
                    else:
                        return -1
            return x


        nums.sort()
        queries = [(y, i, x) for i, (x, y) in enumerate(queries)]
        queries.sort()
        n = len(queries)
        ans = [-1 for _ in range(n)]

        j = 0
        for y, i, x in queries:
            while j < len(nums) and nums[j] <= y:
                insert(nums[j])
                j += 1
            ans[i] = find(x)

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
    # print(s.maximizeXor([5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))
    print(s.maximizeXor([536870912,0,534710168,330218644,142254206], [[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]]))


