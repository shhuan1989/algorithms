# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/21
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        n = len(apples)
        q = []
        ans = 0
        for i in range(n):
            heapq.heappush(q, (i + days[i], apples[i]))
            while q and q[0][0] <= i:
                heapq.heappop(q)
            if q:
                d, v = heapq.heappop(q)
                ans += 1
                v -= 1
                if v > 0:
                    heapq.heappush(q, (d, v))
        
        i = n
        while q:
            while q and q[0][0] <= i:
                heapq.heappop(q)
            
            if not q:
                break
            # can eat in the next k days
            k = min(q[0][0] - i, q[0][1])
            heapq.heappop(q)
            ans += k
            i += k
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
    print(s.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))
    print(s.eatenApples([9,10,1,7,0,2,1,4,1,7,0,11,0,11,0,0,9,11,11,2,0,5,5], [3,19,1,14,0,4,1,8,2,7,0,13,0,13,0,0,2,2,13,1,0,3,7]))

