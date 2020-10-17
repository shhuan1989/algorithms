# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/20 10:36

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def maxUniqueSplit(self, s: str) -> int:



        def dfs(index, pre, vis):
            if index >= len(s):
                return len(pre)

            ans = 0
            for i in range(index+1, len(s)+1):
                v = s[index: i]
                if v not in vis:
                    ans = max(ans, dfs(i, pre + [v], vis | {v}))

            return ans


        return dfs(0, [], set())


if __name__ == '__main__':
    s = Solution()
    print(s.maxUniqueSplit('ababccc'))
    print(s.maxUniqueSplit('aba'))
    print(s.maxUniqueSplit('aa'))





