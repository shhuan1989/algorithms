# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ans = 0

        for i in range(len(s)-1):
            a, b = i, i+1
            if s[a] == '0':
                if s[b] == '1':
                    while a >= 0 and b < len(s) and s[a] == '0' and s[b] == '1':
                        ans += 1
                        a -= 1
                        b += 1
            else:
                if s[b] == '0':
                    while a >= 0 and b < len(s) and s[a] == '1' and s[b] == '0':
                        ans += 1
                        a -= 1
                        b += 1
        return ans

s = Solution()

print(s.countBinarySubstrings("000111000"))