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
created by shhuan at 2020/7/25 20:15

"""


if __name__ == '__main__':
    B = int(input())

    CH = [str(i) for i in range(10)] + [chr(ord('A')+i) for i in range(26)]
    def to_dim(x, b):
        y = []
        while x > 0:
            y.append(CH[x % b])
            x //= b

        # print(''.join(y))
        return y == y[::-1], ''.join(y[::-1])

    for v in range(1, 301):
        u = v * v
        a, b = to_dim(u, B)
        if a:
            c, d = to_dim(v, B)
            print(d, b)
