# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/15 22:16

"""


class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        digits = int(math.log(N, 10))
        resLen = 0
        for i in range(digits+1, 0, -1):
            if int('1' * i) <= N:
                resLen = i
                break

        res = ''
        last = 0
        for i in range(resLen):
            for d in range(9, last-1, -1):
                if int(res + str(d) * (resLen-i)) <= N:
                    res = res + str(d)
                    last = d
                    break

        return int(res)





s = Solution()
# print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(100))
print(s.monotoneIncreasingDigits(187918369))
t0 = time.time()
print(s.monotoneIncreasingDigits(521596916))
print(time.time() - t0)