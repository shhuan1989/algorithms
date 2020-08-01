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
created by shhuan at 2020/7/17 22:10

"""


if __name__ == '__main__':
    N = int(input())

    ans = []
    s = [0 for _ in range(N)]
    for i in range(N):
        op = [1 for _ in range(N)]
        op[i] = 0

        for j in range(N):
            if op[j]:
                s[j] ^= 1
        ans.append(''.join(map(str, s)))
    print(N)
    print('\n'.join(ans))