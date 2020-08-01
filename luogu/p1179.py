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
created by shhuan at 2020/7/21 20:31

"""

if __name__ == '__main__':
    L, R = map(int, input().split())

    ans = 0
    for i in range(L, R+1):
        v = i
        while v > 0:
            if v % 10 == 2:
                ans += 1
            v //= 10

    print(ans)