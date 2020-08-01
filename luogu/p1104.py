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
created by shhuan at 2020/7/13 20:13

"""


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        name, year, month, day = input().split()
        A.append((int(year), int(month), int(day), -i, name))
    A.sort()
    print('\n'.join([v[-1] for v in A]))