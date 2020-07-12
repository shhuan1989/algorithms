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
created by shhuan at 2020/7/11 17:07

"""


if __name__ == '__main__':

    N = int(input())
    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append((a+b+c, a, -i-1, b, c))

    A.sort(reverse=True)
    for a, b, c, d, e in A[:5]:
        print('{} {}'.format(-c, a))
