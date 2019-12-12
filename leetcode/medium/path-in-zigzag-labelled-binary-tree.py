# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 10:17

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
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 1
        while 2**level - 1 < label:
            level += 1

        left = True if level % 2 == 1 else False
        ans = [label]
        parent = label // 2
        if not left:
            parent = (2**level-1-(label-2**(level-1)+1)+1) // 2
        while parent > 1:
            left = not left
            level -= 1
            if left:
                ans.append(parent)
            else:
                up = 2 ** (level - 1) - 1
                cur = 2 ** level - 1
                ans.append(up + cur - parent + 1)
            parent = parent // 2
        
        if parent == 1:
            ans.append(parent)

        return ans[::-1]




s = Solution()
print(s.pathInZigZagTree(14))
print(s.pathInZigZagTree(1))
print(s.pathInZigZagTree(3))
print(s.pathInZigZagTree(5))
print(s.pathInZigZagTree(7))
print(s.pathInZigZagTree(26))

