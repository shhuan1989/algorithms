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
created by shhuan at 2019/12/22 01:21

"""

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        def dfs(index, pre):
            if index >= len(word):
                return [''.join(map(str, [x[0] for x in pre]))]

            ans = []

            ans.extend(dfs(index+1, pre+[(word[index], 0)]))
            if not pre or pre[-1][1] != 1:
                ans.extend(dfs(index+1, pre+[(1, 1)]))
            if pre and pre[-1][1] == 1:
                npre = pre.copy()
                npre.pop()
                npre.append((pre[-1][0]+1, 1))
                ans.extend(dfs(index+1, npre))
            return ans

        return dfs(0, [])

s = Solution()
print(s.generateAbbreviations('word'))