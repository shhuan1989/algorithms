# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/10 23:19

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

    if N < 1:
        print(0)
    elif N == 1:
        print(1)
    else:
        a, b = 1, 2
        for i in range(2, N):
            c = a + b
            a, b = b, c

        print(b)