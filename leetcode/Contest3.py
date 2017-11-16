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


class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        def cal(exp):
            if not exp:
                return 0

            s = []
            for i, v in enumerate(exp):
                if s and s[-1] == '*':
                    s.pop()
                    a = s.pop()
                    s.append(a * v)
                else:
                    s.append(v)
            exp = s
            s = []
            for i, v in enumerate(exp):
                if s and s[-1] in ['+', '-']:
                    op = s.pop()
                    a = s.pop()
                    if op == '+':
                        s.append(a + v)
                    else:
                        s.append(a - v)
                else:
                    s.append(v)

            return s[0]

        def dfs(A, N, T, I, P):
            if I >= N:
                if cal(P) == T:
                    return ["".join(map(str, P))]
                else:
                    return []

            ans = []
            for op in ['+', '-', '*']:
                ans.extend(dfs(A, N, T, I + 1, P + [op, A[I]]))

            if P and P[-1] != 0:
                last = P[-1] * 10 + A[I]
                ans.extend(dfs(A, N, T, I + 1, P[:-1] + [last]))

            return ans

        return dfs([int(x) for x in list(num)], len(num), target, 1, [int(num[0])])


s = Solution()
print(s.addOperators("123", 6))
print(s.addOperators("105", 5))
print(s.addOperators("232", 8))
print(s.addOperators("00", 0))
print(s.addOperators("3456237490", 9191))