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
created by shhuan at 2020/7/12 14:42

"""



if __name__ == '__main__':
    a, b = map(int, input().split())

    # xy = [0, 0]
    def egcd(u, v):
        if v == 0:
            return 1, 0
        x, y = egcd(v, u%v)
        # x, y = xy[0], xy[1]
        x, y = y, x - u//v * y
        return x, y


    x, y = egcd(a, b)
    x = (x%b + b) % b
    print(x)

