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
created by shhuan at 2019/12/19 23:45

"""


class Solution:
    def similarRGB(self, color: str) -> str:

        a, b, c = int(color[1: 3], 16), int(color[3: 5], 16), int(color[5: 7], 16)

        diff = float('inf')
        ans = ''
        for na in range(16):
            for nb in range(16):
                for nc in range(16):
                    nav, nbv, ncv = na*16+na, nb*16+nb, nc*16+nc
                    d = (nav-a)**2 + (nbv-b)**2 + (ncv-c)**2
                    if d < diff:
                        diff = d
                        sa, sb, sc = hex(na)[2:], hex(nb)[2:], hex(nc)[2:]
                        ans = '#{}{}{}{}{}{}'.format(sa, sa, sb, sb, sc, sc)
        return ans

s = Solution()
print(s.similarRGB('#09f166'))