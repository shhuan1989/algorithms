# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/3 23:20

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:

        lv = [(a, b) for a, b in zip(values, labels)]
        lv.sort(reverse=True)

        lm = collections.defaultdict(int)
        cnt = 0
        ans = 0
        for a, b in lv:
            if cnt >= num_wanted:
                break
            if lm[b] < use_limit:
                lm[b] += 1
                cnt += 1
                ans += a

        return ans


s = Solution()
print(s.largestValsFromLabels( values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1))


