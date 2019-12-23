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
created by shhuan at 2019/12/22 12:00

"""

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, 0
        n = len(s)
        while right < n:
            if s[right] == ' ':
                for i in range(left, right):
                    j = right - (i-left) - 1
                    if i >= j:
                        break
                    s[i], s[j] = s[j], s[i]
                left = right + 1
            right += 1

        if left < n:
            for i in range(left, n):
                j = right - (i-left) - 1
                if i >= j:
                    break
                s[i], s[j] = s[j], s[i]

        for i in range(n):
            j = n - i - 1
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]

s = Solution()
print(s.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))