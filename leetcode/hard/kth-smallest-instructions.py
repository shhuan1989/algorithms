# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/1 10:56

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
    def kthSmallestPath(self, destination: List[int], k: int) -> str:

        v, h = destination

        ans = []

        pii = [1 for _ in range(31)]
        for i in range(2, 31):
            pii[i] = i * pii[i-1]

        for i in range(v+h):
            if h == 0:
                ans += ['V'] * v
                break
            elif v == 0:
                ans += ['H'] * h
                break
            else:
                if pii[v+h-1] // pii[v] // pii[h-1] < k:
                    ans.append('V')
                    k -= pii[v+h-1] // pii[v] // pii[h-1]
                    v -= 1
                else:
                    ans.append('H')
                    h -= 1

        return ''.join(ans)



if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPath([2, 2], 4))
    # print(s.kthSmallestPath([2, 3], 1))
    # print(s.kthSmallestPath([2, 3], 2))
    # print(s.kthSmallestPath([2, 3], 3))
    # print(s.kthSmallestPath([15, 15], 13))