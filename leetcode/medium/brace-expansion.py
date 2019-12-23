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
created by shhuan at 2019/12/22 23:27

"""


class Solution:
    def expand(self, S: str) -> List[str]:

        def dfs(exp):
            if not exp:
                return ['']

            if '{' not in exp:
                return exp.split(',')

            if exp[0] != '{':
                i = exp.find('{')
                left = exp[:i]
                right = dfs(exp[i:])
                return [left + v for v in right]

            r = 0
            c = 0
            while r < len(exp):
                if exp[r] == '{':
                    c += 1
                elif exp[r] == '}':
                    c -= 1
                if c == 0:
                    left = dfs(exp[1: r])
                    right = dfs(exp[r+1:])
                    ans = []
                    for u in left:
                        for v in right:
                            ans.append(u + v)
                    return ans
                r += 1

        return list(sorted(dfs(S)))


s = Solution()
print(s.expand("{a,b}{z,x,y}"))
print(s.expand('{a,b}c{d,e}f'))
print(s.expand('a'))
