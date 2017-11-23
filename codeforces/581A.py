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
created by shhuan at 2017/11/22 11:42

"""

a, b = map(int, input().split())


print(min(a, b), abs(a-b) // 2)