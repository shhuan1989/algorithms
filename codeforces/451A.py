# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/22 00:10

"""

N, M = map(int, input().split())


if min(N, M) % 2 == 1:
    print("Akshat")
else:
    print("Malvika")