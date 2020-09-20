# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/9 11:26

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

    s = input().strip()
    s += '    '
    a, b = 0, 0
    for i in range(len(s)-3):
        if s[i] == 'b' or s[i+1] == 'o' or s[i+2] == 'y':
            a += 1
        if s[i] == 'g' or s[i+1] == 'i' or s[i+2] == 'r' or s[i+3] == 'l':
            b += 1

    print(a)
    print(b)

