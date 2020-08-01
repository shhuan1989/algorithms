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
created by shhuan at 2020/7/13 21:16

"""


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]

    ans = ''
    for i, v in enumerate(A):
        if v == 0:
            continue
        x = 'x^{}'.format(N-i) if N-i > 1 else ('x' if N-i == 1 else '')
        if v < 0:
            if v == -1:
                ans += '-{}'.format(x) if x else '-1'
            else:
                ans += '{}{}'.format(v, x)
        else:
            if len(ans) == 0:
                if v == 1:
                    ans += '{}'.format(x) if x else '1'
                else:
                    ans += '{}{}'.format(v, x)
            else:
                if v == 1:
                    ans += '+{}'.format(x) if x else '+1'
                else:
                    ans += '+{}{}'.format(v, x)

    print(ans)