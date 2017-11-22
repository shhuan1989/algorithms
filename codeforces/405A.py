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
created by shhuan at 2017/11/22 01:21

"""

N = int(input())
A = [int(x) for x in input().split()]

A.sort()

print(" ".join(map(str, A)))