# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        s1, s2 = 0, 0
        n1, n2 = len(slots1), len(slots2)
        slots1.sort()
        slots2.sort()
        while s1 < n1 and s2 < n2:
            a, b = slots1[s1], slots2[s2]
            l = max(a[0], b[0])
            r = min(a[1], b[1])
            if r - l >= duration:
                return [l, l + duration]
            if a[1] < b[1]:
                s1 += 1
            else:
                s2 += 1
                
        return []

s = Solution()
# print(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
# print(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
print(s.minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]], [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]], 456085))