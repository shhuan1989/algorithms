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
created by shhuan at 2017/11/22 01:23

"""

s = input()

ans = {x for x in {x.strip() for x in s[1:-1].split(",")} if x}

print(len(ans))