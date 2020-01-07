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
created by shhuan at 2020/1/5 10:30

"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        if not s:
            return ''
        ans = []
        i = 0
        while i < len(s):
            v = s[i]
            if i + 2 < len(s) and s[i+2] == '#':
                u = int(s[i:i+2])
                ans.append(chr(ord('j') + u - 10))
                i += 3
            else:
                ans.append(chr(int(v) + ord('a') - 1))
                i += 1
        return ''.join(ans)



s = Solution()
print(s.freqAlphabets('10#11#12'))
print(s.freqAlphabets('1326#'))
print(s.freqAlphabets('25#'))
print(s.freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'))