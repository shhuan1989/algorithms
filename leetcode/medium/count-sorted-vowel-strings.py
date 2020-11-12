# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/1 10:40

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
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(5):
                # dp[i][j] = sum(dp[i-1][:j])
                for pi in range(j+1):
                    dp[i][j] += dp[i-1][pi]

        return sum(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.countVowelStrings(1))
    print(s.countVowelStrings(2))
    print(s.countVowelStrings(33))