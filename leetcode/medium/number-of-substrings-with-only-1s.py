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
created by shhuan at 2020/7/12 10:31

"""



class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0

        MOD = 10**9+7
        ans = 0
        N = len(s)
        i = 0
        c = 0
        while i < N:
            if s[i] == '1':
                c += 1
            else:
                ans += c * (c+1) // 2
                ans %= MOD
                c = 0
            i += 1

        ans += c * (c + 1) // 2
        ans %= MOD
        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.numSub('0110111'))
    print(s.numSub('101'))
    print(s.numSub('111111'))
    print(s.numSub('000'))