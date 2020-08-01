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
created by shhuan at 2020/7/13 19:42

"""

if __name__ == '__main__':
    A = int(input())
    bits = bin(A)[2:]
    bits = '0' * (32-len(bits)) + bits
    bits = bits[16:] + bits[:16]

    print(int(bits, 2))