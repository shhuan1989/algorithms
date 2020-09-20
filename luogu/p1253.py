# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/10 21:23

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
    N = int(input())
    A = []
    for i in range(N):
        c, f = map(int, input().split())
        A.append((c*f, -i-1))

    A.sort(reverse=True)
    print(' '.join(map(str, [-v[1] for v in A])))

