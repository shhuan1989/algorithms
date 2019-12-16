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
created by shhuan at 2019/12/11 22:02

"""


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S:
            return ''

        N = len(S)
        pos = 0
        s = list(S)
        pre = pos
        one = 0
        presub = []
        for i in range(N):
            if s[i] == '1':
                one += 1
            elif s[i] == '0':
                one -= 1
            if one == 0:
                presub.append('1' + self.makeLargestSpecial(s[pre+1 : i]) + '0')
                pre = i + 1

        return ''.join(sorted(presub, reverse=True))

s = Solution()
print(s.makeLargestSpecial('11011000'))
print(s.makeLargestSpecial('1010101100'))
print(s.makeLargestSpecial('101100101100'))
t0 = time.time()
print(s.makeLargestSpecial('10111110001011000011101000101110100100110010'))
print(time.time() - t0)