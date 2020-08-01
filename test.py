import math
import os
import random
import re
import sys
from typing import List
import bisect
import collections
import heapq

import numpy as np


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
        if len(s) <= K:
            return 0
        if len(set(s)) == 1:
            n = len(s) - K
            if n < 0:
                return 0
            if n == 1:
                return 1
            elif n < 10:
                return 2
            elif n < 100:
                return 3
            else:
                return 4

        s += '#'
        n = len(s)
        dp = [[[n for _ in range(12)] for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i][1][1] = i - 1
            dp[i][0][0] = i

        for i in range(1, n+1):
            for j in range(2, i+1):
                for pi in range(1, i):
                    d = i - pi - 1
                    if s[i-1] == s[pi-1]:
                        for k in range(1, 12):
                            if k in [2, 10, 100]:
                                dp[i][j][k] = min(dp[i][j][k], dp[pi][j-1][k-1] + d)
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[pi][j][k-1] + d)
                    else:
                        dp[i][j][1] = min(dp[i][j][1], min([dp[pi][j-1][k] for k in range(1, 12)]) + d)


        for j in range(n+1):
            if min(dp[n][j]) <= K:
                return j - 1





if __name__ == '__main__':

    s = Solution()
    print(s.getLengthOfOptimalCompression('a', 1))
    print(s.getLengthOfOptimalCompression('aaabcccd', 2))
    print(s.getLengthOfOptimalCompression('aabbaa', 2))
    print(s.getLengthOfOptimalCompression('aaaaaaaaaaa', 0))
    print(s.getLengthOfOptimalCompression("bbabbbabbbbcbb", 4))