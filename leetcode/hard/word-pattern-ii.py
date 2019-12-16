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
created by shhuan at 2019/12/15 19:05

"""

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def dfs(p, s, pi, si, pre, rev):
            if si >= len(s) and pi >= len(p):
                return True

            if si >= len(s):
                return False
            if pi >= len(p):
                return False

            pc = p[pi]
            if pc in pre:
                sc = pre[pc]
                k = len(sc)
                if s[si: si+k] == sc:
                    return dfs(p, s, pi+1, si+k, pre, rev)
                return False
            else:
                for k in range(1, len(s)-si+1):
                    v = s[si: si+k]
                    if v not in rev or rev[v] == pc:
                        npre = pre.copy()
                        nrev = rev.copy()
                        nrev[v] = pc
                        npre[pc] = v
                        if dfs(p, s, pi+1, si+k, npre, nrev):
                            return True
            return False

        return dfs(pattern, s, 0, 0, {}, {})


s = Solution()
print(s.wordPatternMatch('ab', 'aa'))
print(s.wordPatternMatch('abab', 'redblueredblue'))
print(s.wordPatternMatch('aaaa', 'asdasdasdasd'))
print(s.wordPatternMatch('aabb', 'xyzabcxzyabc'))