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
created by shhuan at 2020/7/8 22:15

"""


def solve(a, b):
    if not a:
        return ''

    root = b[-1]
    ai = -1
    for i, v in enumerate(a):
        if v == root:
            ai = i
            break

    return root + solve(a[:ai], b[:ai]) + solve(a[ai+1:], b[ai:-1])


if __name__ == '__main__':
    inorder = input()
    suforder = input()
    print(solve(inorder, suforder))