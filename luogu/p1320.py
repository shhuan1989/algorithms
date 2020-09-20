# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/9 11:17

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

if __name__ == '__main__':

    A = []
    row = input().strip()
    A.append(row)
    N = len(row)
    for i in range(N-1):
        row = input().strip()
        A.append(row)

    s = ''.join(A)
    ans = [N]
    if s[0] != '0':
        ans.append(0)
    q = []
    for v in s:
        if not q or q[-1][0] != v:
            q.append([v, 1])
        else:
            q[-1][1] += 1

    for v, c in q:
        ans.append(c)
    print(' '.join(map(str, ans)))
