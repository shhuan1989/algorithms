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
created by shhuan at 2020/7/14 18:37

"""

if __name__ == '__main__':
    N, M = map(int, input().split())
    K = M + M // 2
    A = []
    for i in range(N):
        i, s = map(int, input().split())
        A.append((-s, i))

    A.sort()
    score = abs(A[K-1][0])
    ans = []
    for s, i in A:
        if abs(s) >= score:
            ans.append((abs(s), i))
        else:
            break

    print('{} {}'.format(score, len(ans)))
    for s, i in ans:
        print('{} {}'.format(i, s))
