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
created by shhuan at 2019/12/5 21:21

"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        ans = 0
        while l <= r:
            ans += 1
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
        return ans

s = Solution()
print(s.numRescueBoats(people = [3,2,2,1], limit = 3))
print(s.numRescueBoats(people = [3,5,3,4], limit = 5))