# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/12 15:26

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
    S, A, B = map(int, input().split())
    x = A**2 - B**2 + A**2 * (B - A) / (A + B) - A*B*(B-A)/(B+A)
    t = (A-B)*S/x
    t += (S-B*t) / A
    print('{:.6f}'.format(t))