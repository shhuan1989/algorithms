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
created by shhuan at 2020/7/11 18:44

"""


if __name__ == '__main__':

    A = []
    for i in range(12):
        A.append(int(input()))


    v = 0
    saved = 0
    for i in range(12):
        v += 300
        if v < A[i]:
            print('-{}'.format(i+1))
            exit(0)
        v -= A[i]
        saved += v // 100
        v %= 100

    saved *= 100
    print(saved // 5 + saved + v)
