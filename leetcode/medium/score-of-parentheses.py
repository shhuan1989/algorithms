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
created by shhuan at 2019/12/24 23:19

"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        def dfs(s):
            if not s:
                return 0
            if s[:2] == '()':
                return 1 + dfs(s[2:])

            k = 0
            for i, v in enumerate(s):
                if v == '(':
                    k += 1
                else:
                    k -= 1
                if k == 0:
                    return 2 * dfs(s[1: i]) + dfs(s[i+1:])

        return dfs(S)

s = Solution()
print(s.scoreOfParentheses('()'))
print(s.scoreOfParentheses('(())'))
print(s.scoreOfParentheses('()()'))
print(s.scoreOfParentheses('(()(()))'))