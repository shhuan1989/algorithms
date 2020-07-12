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
created by shhuan at 2020/7/11 18:33

"""



if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]

    q = A
    heapq.heapify(q)
    ans = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a + b
        heapq.heappush(q, a+b)

    print(ans)


