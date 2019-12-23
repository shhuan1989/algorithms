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
created by shhuan at 2019/12/22 19:33

"""

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if len(set(s)) == 1:
            return [s]

        wc = collections.Counter(s)
        nodds = sum([c % 2 == 1 for w, c in wc.items()])
        if nodds > 1:
            return []

        odd, oddcount = [(w, c) for w, c in wc.items() if c % 2 == 1][0] if nodds > 0 else (None, 0)
        wc = {w:c for w, c in wc.items() if c % 2 == 0}
        if oddcount > 1:
            wc[odd] = oddcount-1

        def dfs(curwc, left):
            if not curwc:
                if left:
                    return [left + left[::-1]] if odd is None else [left + odd + left[::-1]]
                return [odd] if odd is not None else []

            ans = []
            for w, c in curwc.items():
                if left and w == left[-1]:
                    continue
                nwc = curwc.copy()
                for i in range(1, c // 2 + 1):
                    nwc[w] = c - i * 2
                    if nwc[w] == 0:
                        del nwc[w]
                    ans.extend(dfs(nwc, left + w * i))
            return ans

        return dfs(wc, '')


s = Solution()
print(s.generatePalindromes("aaaabbbb"))
# print(s.generatePalindromes('aaa'))
# print(s.generatePalindromes('aab'))
# print(s.generatePalindromes('a'))
# print(s.generatePalindromes('aabb'))
# print(s.generatePalindromes('abcd'))