# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/6 10:30

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
    def modifyString(self, s: str) -> str:

        t = list(s)
        n = len(t)
        for i, v in enumerate(t):
            if v == '?':
                for u in range(26):
                    ch = chr(ord('a') + u)
                    if (i-1 < 0 or t[i-1] != ch) and (i+1 >= n or t[i+1] != ch):
                        t[i] = ch
                        break
        return ''.join(t)


if __name__ == '__main__':
    s = Solution()
    print(s.modifyString('?zs'))
    print(s.modifyString('ubv?w'))
    print(s.modifyString('j?qg??b'))
    print(s.modifyString('??yw?ipkj?'))
