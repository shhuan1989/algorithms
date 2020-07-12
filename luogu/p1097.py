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
created by shhuan at 2020/7/11 16:04

"""



if __name__ == '__main__':
    N = int(input())
    wc = collections.defaultdict(int)
    for i in range(N):
        v = int(input())
        wc[v] += 1

    nums = list(sorted(wc.keys()))
    print('\n'.join(['{} {}'.format(w, wc[w]) for w in nums]))