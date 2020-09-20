# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/23 10:44

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        wc = collections.defaultdict(int)
        n = len(arr)
        a = [0 for _ in range(n + 1)]
        s = [i for i in range(n + 1)]
        t = [i for i in range(n + 1)]
        ans = -1
        for step, i in enumerate(arr):
            a[i] = 1
            if i-1 >= 0 and a[i-1] == 1 and i+1 <= n and a[i+1] == 1:
                wc[t[i+1] - s[i-1] + 1] += 1
                wc[i - s[i-1]] -= 1
                wc[t[i+1] - i] -= 1
                s[t[i+1]] = s[i-1]
                t[s[i-1]] = t[i+1]
            elif i-1 >= 0 and a[i-1] == 1:
                wc[i-s[i-1] + 1] += 1
                wc[i-s[i-1]] -= 1
                s[i] = s[i-1]
                t[s[i]] = i
            elif i+1 <= n and a[i+1] == 1:
                wc[t[i+1]-i+1] += 1
                wc[t[i+1]-i] -= 1
                t[i] = t[i+1]
                s[t[i]] = i
            else:
                s[i] = i
                t[i] = i
                wc[1] += 1

            if wc[m] > 0:
                ans = step + 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findLatestStep([3, 5, 1, 2, 4], 1))
    print(s.findLatestStep([3, 1, 5, 4, 2], 2))
    print(s.findLatestStep([1], 1))
    print(s.findLatestStep([2, 1], 2))