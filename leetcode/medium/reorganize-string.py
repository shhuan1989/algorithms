# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/21 23:31

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''

        wc = collections.Counter(S)
        N = len(S)
        if max(wc.values()) > (N + 1) // 2:
            return ''

        ans = ['' for _ in range(N)]
        wc = [(c, w) for w, c in wc.items()]
        wc.sort(reverse=True)

        i = 0
        for c, w in wc:
            for k in range(c):
                ans[i] = w
                i += 2
                if i >= N:
                    i = 1

        return ''.join(ans)


s = Solution()
print(s.reorganizeString('aab'))
print(s.reorganizeString('aaab'))
print(s.reorganizeString('aabbccaaddee'))