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
created by shhuan at 2020/7/21 19:45

"""


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    A = set()
    for i in range(N):
        A.add(input().strip())

    ans = 0
    for i in range(M):
        v = input().strip()
        if v in A:
            ans += 1

    print(ans)
