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
created by shhuan at 2020/7/8 21:00

"""


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    avg = sum(A) // N

    left = 0
    step = 0
    for i, v in enumerate(A):
        u = v + left
        left = u - avg
        if left != 0:
            step += 1

    print(step)
