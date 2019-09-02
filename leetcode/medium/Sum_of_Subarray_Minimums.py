# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/26 00:23

假设当前值是x,左边有a个值比x大,右边有b个值比x大,以x为最小值的区间的个数为(a+1)*(b+1)

问题变成对于每个x,求左右有多少个值比它大


使用stack 求解,复杂度O(N)


"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys


class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        N = len(A)

        # prev has i* - 1 in increasing order of A[i* - 1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * N
        for i in range(N):
            # 比A[i] 大或等的都pop
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1

            # 把A[i]push进去,因为下次是找比A[i+1]小的值
            # 如果A[i] < A[i+1] 那么就找到了
            # 如果A[i] >= A[i+1],因为之前pop出去的都是大于等于A[i]的,所以也不符合要求
            # 故而继续往前找即可
            stack.append(i)

        # next has k* + 1 in increasing order of A[k* + 1]
        # where k* is the answer to query j
        stack = []
        next_ = [None] * N
        for k in range(N-1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        print(prev)
        print(next_)
        # Use prev/next array to count answer
        return sum((i - prev[i]) * (next_[i] - i) * A[i]
                   for i in range(N)) % MOD


s = Solution()

print(s.sumSubarrayMins([10, 5, 3, 7, 0, 4, 5, 2, 1, 8]))