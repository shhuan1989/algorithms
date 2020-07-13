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
created by shhuan at 2020/7/12 12:36

"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]
        dp[1] = True

        for i in range(2, n+1):
            j = 1
            win = False
            while j ** 2 <= i:
                if not dp[i-j**2]:
                    win = True
                    break
                j += 1
            dp[i] = win

        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.winnerSquareGame(1))
    print(s.winnerSquareGame(2))
    print(s.winnerSquareGame(4))
    print(s.winnerSquareGame(7))
    print(s.winnerSquareGame(17))

