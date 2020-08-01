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
created by shhuan at 2020/7/20 20:00

"""


if __name__ == '__main__':
    N = int(input())

    q = []
    p = []
    ans = []
    for i in range(N):
        op = [int(x) for x in input().strip().split()]
        x = op[0]
        if x == 0:
            q.append(op[1])
            if not p:
                p.append(op[1])
            else:
                p.append(max(p[-1], op[1]))
        elif x == 1:
            if q:
                q.pop()
                p.pop()
        else:
            ans.append(p[-1] if p else 0)

    print('\n'.join(map(str, ans)))