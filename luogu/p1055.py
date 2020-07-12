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
created by shhuan at 2020/7/9 21:43

"""


def check(s):
    mod = '0123456789X'
    v = 0
    d = 1
    for i in range(12):
        if s[i] == '-':
            continue
        v += d * (ord(s[i]) - ord('0'))
        d += 1

    v %= 11
    w = mod[v]
    if w == s[12]:
        return 'Right'

    s[12] = w
    return ''.join(s)


if __name__ == '__main__':
    s = list(input())
    print(check(s))

