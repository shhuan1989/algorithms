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
created by shhuan at 2020/7/10 19:05

"""

if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    A = list(sorted(set(A)))
    print(len(A))
    print(' '.join(map(str, A)))