# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/29 10:55

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
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        m = n // 2
        a = nums[:m]
        b = nums[m:][::-1]

        add = [0 for _ in range(limit * 2 + 10)]
        for i in range(m):
            u, v = a[i], b[i]
            x = [
                [1 + min((u, v)), limit + max(u, v)],
                [2, min((u, v))],
                [2, min((u, v))],
                [limit + 1 + max(u, v), 2 * limit],
                [limit + 1 + max(u, v), 2 * limit],
            ]
            w = u + v
            # print(u, v, '-')
            for start, end in x:
                if start > end or end > limit * 2:
                    continue
                if start <= w <= end:
                    s1, e1 = start, w-1
                    s2, e2 = w + 1, end
                    if s1 <= e1:
                        add[s1] += 1
                        add[e1+1] -= 1
                        # print(s1, e1)
                    if s2 <= e2:
                        add[s2] += 1
                        add[e2+1] -= 1
                        # print(s2, e2)
                else:
                    add[start] += 1
                    add[end+1] -= 1
                    # print(start, end)

        ans = n
        curr = 0
        for i in range(2, limit*2+1):
            curr += add[i]
            ans = min(ans, curr)

        return ans







if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([1, 2, 4, 3], 4))
    print(s.minMoves([1, 2, 2, 1], 2))
    print(s.minMoves([1, 2, 1, 2], 2))

