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
created by shhuan at 2017/11/23 10:30

"""



k2, k3, k5, k6 = map(int, input().split())

k256 = min(k2, k5, k6)
k32 = max(0, min(k3, k2-k256))

print(k32*32 + k256*256)