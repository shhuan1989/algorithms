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
created by shhuan at 2020/7/21 19:58

"""


if __name__ == '__main__':
    N = int(input())

    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)


    ans = sum([(X[i] * Y[(i+1) % N]) - Y[i] * X[(i+1) % N] for i in range(N)]) // 2
    print(ans)