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
created by shhuan at 2019/12/19 00:42

"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        diffs = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False

        if not diffs:
            return len(set(A)) < len(A)

        a = ''.join([A[i] for i in diffs])
        b = ''.join([B[i] for i in diffs][::-1])
        return a == b

s = Solution()
print(s.buddyStrings('ab', 'ba'))
print(s.buddyStrings('ab', 'ab'))
print(s.buddyStrings('aa', 'aa'))
print(s.buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb"))
print(s.buddyStrings(A = "", B = "aa"))