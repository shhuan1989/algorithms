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
created by shhuan at 2020/1/10 22:02

"""

N = int(input())
S = input()

left = len([v for v in S if v == 'L'])
right = len(S) - left

print(left + right + 1)