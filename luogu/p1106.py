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
created by shhuan at 2020/7/12 20:47

"""


if __name__ == '__main__':
    A = [int(x) for x in list(input().strip())]
    K = int(input())
    M = len(A)
    cnt = 0
    start = 0
    ans = []
    needs = M - K
    while cnt < needs:
        mini = start
        for i in range(start, min(start+K+1, M)):
            if A[mini] > A[i]:
                mini = i
        if ans or A[mini] > 0:
            ans.append(A[mini])
        K -= mini - start
        start = mini + 1
        cnt += 1

    if not ans:
        print('0')
    else:
        print(''.join(map(str, ans)))

