# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/17 10:57

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List



if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += N // i
    print(ans)