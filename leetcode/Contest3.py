# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/9/24 09:55

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        A = grid
        N = len(A)

        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2*N)]
        dp[0][0][0] = A[0][0]

        for k in range(1, 2*N-2):
            for i in range(N):
                for j in range(i, N):
                    ci = k-i
                    cj = k-j
                    if not (0 <= ci < N and 0 <= cj < N):
                        continue
                    if A[i][ci] < 0 or A[j][cj] < 0:
                        continue

                    d = A[i][ci] if i == j else A[i][ci]+A[i][cj]
                    if i-1 >= 0 and j-1 >= 0:
                        if dp[k-1][i-1][j-1] >= 0:
                            dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-1][j-1] + d)

                    if i-1 >= 0 and cj - 1 >= 0:
                        if dp[k-1][i-1][j] >= 0:
                            dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-1][j] + d)

                    if ci - 1 >= 0 and j - 1 >= 0:
                        if dp[k-1][i][j-1] >= 0:
                            dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j-1] + d)

                    if ci-1 >= 0 and cj-1 >= 0:
                        if dp[k-1][i][j] >= 0:
                            dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j] + d)


        ans = dp[2*N-2][N-1][N-1]
        if ans < 0:
            ans = 0

        return ans

s = Solution()
print(s.cherryPickup([
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]]))

