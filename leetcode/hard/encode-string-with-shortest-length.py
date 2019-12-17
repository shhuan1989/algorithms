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
created by shhuan at 2019/12/12 20:50

"""


class Solution:
    def encode(self, s: str) -> str:
        N = len(s)
        dp = [['' for _ in range(N+1)] for _ in range(N)]

        for i in range(N):
            dp[i][1] = s[i]

        def same(a, b):
            if a != b:
                return False
            if a[0] != '[':
                return False
            c = 1
            i = 1
            while i < len(a):
                if a[i] == '[':
                    c += 1
                elif a[i] == ']':
                    c -= 1
                if c == 0 and i < len(a)-1:
                    return False
                i += 1
            return True

        def merge(a, b):
            na, nb = len(a), len(b)
            ns = a + b
            if na % nb == 0 and a == b * (na // nb):
                ns = '{}[{}]'.format((na + nb) // nb, b)
            elif nb % na == 0 and b == a * (nb // na):
                ns = '{}[{}]'.format((na + nb) // na, a)
            else:
                ai, bi = a.find('['), b.find('[')
                if any([a[i].isalpha() for i in range(ai)]):
                    ai = -1
                if any([b[i].isalpha() for i in range(bi)]):
                    bi = -1
                if ai > 0 and bi > 0:
                    astr, bstr = a[ai:], b[bi:]
                    if same(astr, bstr):
                        return '{}{}'.format(int(a[:ai]) + int(b[:bi]), astr)
                elif ai > 0:
                    astr = a[ai+1: -1]
                    if astr == b:
                        return '{}[{}]'.format(int(a[:ai])+1, b)
                elif bi > 0:
                    bstr = b[bi+1: -1]
                    if bstr == a:
                        return '{}[{}]'.format(int(b[:bi])+1, a)

            return ns

        for l in range(2, N+1):
            for i in range(N-l+1):
                dp[i][l] = s[i: i + l]
                for k in range(1, l):
                    a, b = dp[i][k], dp[i+k][l-k]
                    ns = merge(a, b)
                    if len(ns) < len(dp[i][l]):
                        dp[i][l] = ns

        return dp[0][N]
        
s = Solution()
print(s.encode('aaa'))
print(s.encode('aaaaaa'))
# print(s.encode('aaaaaaaaaa'))
# print(s.encode('aabcaabcd'))
# print(s.encode('abbbabbbcabbbabbbc'))
# print(s.encode('slkjdfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
# print(s.encode('aaaaaaabbaaabb'))
# print(s.encode('aaaaaaaaaabbbaaaaabbb'))
