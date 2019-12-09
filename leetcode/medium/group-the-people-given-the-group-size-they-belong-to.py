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
created by shhuan at 2019/12/8 10:33

"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = collections.defaultdict(list)

        for i, v in enumerate(groupSizes):
            groups[v] .append(i)

        ans = []

        for k, v in groups.items():
            if len(v) == k:
                ans.append(v)
            else:
                for i in range(0, len(v), k):
                    ans.append(v[i: i+k])
        return ans


s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
print(s.groupThePeople([2,1,3,3,3,2]))