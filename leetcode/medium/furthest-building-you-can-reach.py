# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/1 10:43

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
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights)
        topk = []
        lower = 0
        ans = 0
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                d = heights[i] - heights[i-1]
                heapq.heappush(topk, d)

                if len(topk) > ladders:
                    v = heapq.heappop(topk)
                    lower += abs(v)
                    if lower > bricks:
                        break
                    else:
                        ans = max(ans, i)
                else:
                    ans = max(ans, i)
            else:
                ans = max(ans, i)

        return ans







if __name__ == '__main__':
    s = Solution()
    print(s.furthestBuilding([3, 19], 87, 1))
    # print(s.furthestBuilding([1, 2], 0, 0))
    # print(s.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
    # print(s.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
    # print(s.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))