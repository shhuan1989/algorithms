# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/28/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

from typing import List
import math

class Solution:
    def uniqueLetterString(self, S: str) -> int:
        MOD, N = 10 ** 9 + 7, len(S)
        wi = collections.defaultdict(list)
        for i, w in enumerate(S):
            wi[w].append(i)

        return sum([sum([(a[i] - (a[i-1] if i > 0 else -1)) * ((a[i+1] if i+1 < len(a) else N) - a[i]) for i in range(len(a))]) % MOD for a in wi.values()]) % MOD
    
s = Solution()
# print(s.uniqueLetterString('ABC'))
print(s.uniqueLetterString('ABA'))
# print(s.uniqueLetterString("AAA"))
# print(s.uniqueLetterString('ABAB'))
# print(s.uniqueLetterString("ABABABAB"))