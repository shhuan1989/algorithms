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
created by shhuan at 2020/7/29 20:39

"""

if __name__ == '__main__':
    s = input().strip()
    t = input().strip()

    def getv(a):
        b = [ord(v)-ord('A') + 1 for v in a]
        c = 1
        for v in b:
            c *= v

        return c % 47

    if getv(s) == getv(t):
        print('GO')
    else:
        print('STAY')