# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/29 10:32

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
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []

        N = len(nums)
        for i in range(N-k):
            v = nums[i]
            heapq.heappush(q, (v, i))

        left = 0
        for i in range(N-k, N):
            v = nums[i]
            while q and q[0][1] < left:
                heapq.heappop(q)
            heapq.heappush(q, (v, i))
            prev, prei = heapq.heappop(q)
            ans.append(prev)
            left = prei + 1

        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
    # print(s.mostCompetitive([3, 5, 2, 6], 2))
    # print(s.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
    # print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))
    # print(s.mostCompetitive([84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71], 24))