# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/27 10:33

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
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        ans = 0

        q = []
        for day in range(len(apples)):
            a, b = apples[day], days[day]
            while q and q[0][0] < day:
                heapq.heappop(q)

            if a > 0:
                heapq.heappush(q, (b + day - 1, a))

            if q:
                x, y = heapq.heappop(q)
                y -= 1
                ans += 1
                if y > 0:
                    heapq.heappush(q, (x, y))
            # else:
            #     return ans
        day = len(apples)
        while q:
            while q and q[0][0] < day:
                heapq.heappop(q)
            if q:
                x, y = heapq.heappop(q)
                y -= 1
                ans += 1
                if y > 0:
                    heapq.heappush(q, (x, y))
            # else:
            #     break
            day += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
    # print(s.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))
    print(s.eatenApples([9,10,1,7,0,2,1,4,1,7,0,11,0,11,0,0,9,11,11,2,0,5,5], [3,19,1,14,0,4,1,8,2,7,0,13,0,13,0,0,2,2,13,1,0,3,7]))


