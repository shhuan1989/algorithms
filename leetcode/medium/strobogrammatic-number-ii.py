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
created by shhuan at 2019/12/18 23:03

"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1', '8']
        def dfs(s):
            if len(s) == (n+1) // 2:
                if n % 2 == 0:
                    return [s+''.join([v if v not in {'6', '9'} else ('6' if v == '9' else '9') for v in s[::-1]])]
                else:
                    if s[-1] in {'6', '9'}:
                        return []
                    return [s+''.join([v if v not in {'6', '9'} else ('6' if v == '9' else '9') for v in s[:-1][::-1]])]

            ans = []
            for v in ['0', '1', '6', '8', '9']:
                ans.extend(dfs(s+v))

            return ans

        ans = []
        for v in ['1', '6', '8', '9']:
            ans.extend(dfs(v))

        return ans

s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(4))
print(s.findStrobogrammatic(3))
