# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/13 10:53

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
    def isTransformable(self, s: str, t: str) -> bool:
        q = [[] for _ in range(10)]
        for i, v in enumerate(s):
            q[int(s[i])].append(i)

        for i in range(len(t)-1, -1, 0-1):
            c = int(t[i])
            if not q[c]:
                return False
            for v in range(c+1, 10):
                if q[v] and q[v][-1] > q[c][-1]:
                    return False
            q[c].pop()

        return True

    def isTransformable2(self, s: str, t: str) -> bool:

        s = [int(x) for x in s]
        t = [int(x) for x in t]

        wcs = collections.Counter(s)
        wct = collections.Counter(t)
        if wcs != wct:
            return False

        rs = [[] for _ in range(10)]
        fs = [0 for _ in range(10)]
        for i in range(len(s)):
            c = s[i]
            rs[c].append(fs.copy())
            fs[c] += 1

        ft = [0 for _ in range(10)]
        for i in range(len(t)):
            c = t[i]
            idx = ft[c]
            for j in range(c):
                if ft[j] < rs[c][idx][j]:
                    return False
            ft[c] += 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isTransformable('84532', '34852'))
    print(s.isTransformable('34521', '23415'))
    print(s.isTransformable('12345', '12435'))
    print(s.isTransformable('1', '2'))