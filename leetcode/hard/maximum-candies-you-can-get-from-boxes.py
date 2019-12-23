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
created by shhuan at 2019/12/22 10:55

"""


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        ans = 0
        opened = set()
        ks = set()
        boxes = set(initialBoxes)

        while boxes:
            newboxes = set()
            newkeys = False
            for b in boxes:
                if status[b] == 1 or b in ks:
                    ans += candies[b]
                    ks |= set(keys[b])
                    if keys[b]:
                        newkeys = True
                    newboxes |= set(containedBoxes[b])
                    opened.add(b)
            if not newboxes and not newkeys:
                break
            boxes |= newboxes
            boxes -= opened

        return ans

s = Solution()
print(s.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
print(s.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
print(s.maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]))
print(s.maxCandies(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []))
print(s.maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]))


