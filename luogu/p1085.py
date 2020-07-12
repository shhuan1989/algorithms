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
created by shhuan at 2020/7/11 20:26

"""


if __name__ == '__main__':
    unhappy = -1
    for i in range(1, 7):
        a, b = map(int, input().split())
        if a + b > 8:
            if unhappy < 0:
                unhappy = i

    if unhappy > 0:
        print(unhappy)
    else:
        print(0)