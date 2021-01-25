# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/25
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def minimumDeletions(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        # counta = [0 for _ in range(n + 1)]
        # countb = [0 for _ in range(n + 1)]
        # a = s.count('a')
        # for i in range(n):
        #     counta[i + 1] = counta[i] + (1 if s[i] == 'a' else 0)
            # countb[i + 1] = countb[i] + (1 if s[i] == 'b' else 0)
        
        ans = n
        ca = 0
        for i, v in enumerate(s):
            # ans = min(ans, i - counta[i] + counta[-1] - counta[i])
            ans = min(ans, i - ca - ca)
            ca += 1 if v == 'a' else 0
            
        ans = min(ans + ca, ca, n-ca)
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumDeletions('aababbab'))
    print(s.minimumDeletions('bbaaaaabb'))
    print(s.minimumDeletions('a'))
