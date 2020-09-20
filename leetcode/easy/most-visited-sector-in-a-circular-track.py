# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/23 10:30

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
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        count = [0 for _ in range(n+1)]
        for i in range(len(rounds)-1):
            s, t = (rounds[i] + 1) if i > 0 else rounds[i], rounds[i+1]

            if s <= t:
                for j in range(s, t+1):
                    count[j] += 1
            else:
                for j in range(s, n+1):
                    count[j] += 1

                for j in range(1, t+1):
                    count[j] += 1

        # print(count)
        c = max(count)
        return [i for i in range(1, n+1) if count[i] == c]


if __name__ == '__main__':
    s = Solution()
    print(s.mostVisited(4, [1, 3, 1, 2]))
    print(s.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]))
    print(s.mostVisited(7, [1, 3, 5, 7]))