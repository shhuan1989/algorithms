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
created by shhuan at 2017/11/21 22:55

"""

K, N, W = map(int, input().split())

# K, 2K, 3K,..., K*W
# (K+KW)*W//2


total = (K + K*W)*W //2

print(max(0, total-N))