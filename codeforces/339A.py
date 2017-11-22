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
created by shhuan at 2017/11/21 20:39

"""

s = input()
s = s.split("+")

s.sort()

print("+".join(s))