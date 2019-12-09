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
created by shhuan at 2019/12/8 22:51

"""

import re

class Solution:
    def maskPII(self, S: str) -> str:

        i = S.find('@')
        if i >= 0:
            return S[0].lower() + '*****' + S[i-1].lower() + S[i:].lower()
        else:
            S = re.sub('\D', '', S)
            if len(S) == 10:
                return '***-***-' + S[-4:]
            return '+' + '*'*(len(S)-10) + '-***-***-' + S[-4:]

s = Solution()
print(s.maskPII('LeetCode@LeetCode.com'))
print(s.maskPII('AB@qq.com'))
print(s.maskPII('1(234)567-890'))
print(s.maskPII('86-(10)12345678'))
