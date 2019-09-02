# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/26 19:56

"""

class Solution:
    def distinctSubseqII(self, S):
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)


s = Solution()

# print(s.distinctSubseqII("abc"))
# print(s.distinctSubseqII("aba"))
# print(s.distinctSubseqII("aaa"))
print(s.distinctSubseqII("pcrdhwdxmqdznbenhwjsenjhvulyve"))