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
created by shhuan at 2019/12/20 19:46

"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = []
        for i, v in enumerate(s):
            if not q or v != q[-1][0]:
                q.append((v, 1))
            else:
                u, c = q.pop()
                if c + 1 < k:
                    q.append((v, c+1))
                elif c + 1 > k:
                    q.append((v, c+1-k))
                else:
                    pass

        ans = ''
        for u, c in q:
            ans += u * c
        return ans

s = Solution()
print(s.removeDuplicates(s = "abcd", k = 2))
print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))