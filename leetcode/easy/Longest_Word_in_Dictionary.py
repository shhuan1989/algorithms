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
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        words = set(words)

        def check(w):
            while w:
                if w not in words:
                    return False
                w = w[:-1]

            return True

        ans = collections.defaultdict(list)
        maxl = 0
        for w in words:
            if check(w):
                l = len(w)
                maxl = max(maxl, l)
                ans[l].append(w)

        ans = list(sorted(ans[maxl]))

        return ans[0] if ans else ''

s = Solution()
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))