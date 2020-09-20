# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 21:23

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
    T = int(input())
    ans = []
    for _ in range(T):
        H, P = map(int, input().split())

        while P > 0:
            H -= P
            P //= 2

        ans.append(1 if H <= 0 else 0)

    print('\n'.join(map(str, ans)))