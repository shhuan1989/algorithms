# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/20 18:45

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

    def solve(a, b):
        c = 0
        for i in range(32):
            x = 1 << i
            ai = a & x
            bi = b & x

            if ai != bi:
                c |= x

        return c

    T = int(input())
    ans = []
    for _ in range(T):
        a, b = map(int, input().split())
        ans.append(solve(a, b))
    print('\n'.join(map(str, ans)))