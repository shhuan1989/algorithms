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
created by shhuan at 2020/7/31 18:00

"""


if __name__ == '__main__':
    N = int(input())
    s = 0
    a = 2
    p = 1
    while s <= N:
        s += a
        p *= a
        a += 1

    p //= s-N

    print(' '.join(map(str, [i for i in range(2, a) if i != s-N])))
    print(p)