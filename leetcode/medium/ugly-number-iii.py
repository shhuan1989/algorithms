# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 12:25

请你帮忙设计一个程序，用来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数。


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
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lo, hi = 0, 2*10**9+1
        gab, gac, gbc, gabc = gcd(a, b), gcd(a, c), gcd(b, c), gcd(gcd(a, b), c)
        while lo <= hi:
            m = lo + (hi-lo)//2
            ab, ac, bc = a*b//gab, a*c//gac, b*c//gbc
            abc = ab*c//gcd(ab, c)

            # 能被a整除的数 + 能被b整除的数 + 能被c整除的数 - 同时能被两个数字整除的数 + 同时能被三个数字整除的数
            count = m // a + m // b + m // c - (m//ab+m//ac+m//bc) + m//abc
            if count >= n:
                hi = m - 1
            else:
                lo = m + 1

        return lo


s = Solution()
print(s.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))
print(s.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))