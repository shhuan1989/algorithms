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
created by shhuan at 2019/12/19 22:11

"""

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        ans = ''.join(strs)
        for i, u in enumerate(strs):
            mid = ''.join([max(v, v[::-1]) for v in strs[i+1:] + strs[:i]])
            for s in [u, u[::-1]]:
                for j in range(len(s)):
                    t = s[j:] + mid + s[:j]
                    ans = max(ans, t)
        return ans


s = Solution()
print(s.splitLoopedString(['abc', 'xyz']))
print(s.splitLoopedString(["ab","xy","cd","aaa","bab"]))
print(s.splitLoopedString(['a', 'b', 'c']))
print(s.splitLoopedString(["awef","eawf","zdaeff","awefzewaf","awefzewaf"]) == "zfewafewafwaezdaefffawezfewafawe")