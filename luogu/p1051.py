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
created by shhuan at 2020/7/10 21:33

"""


if __name__ == '__main__':
    N = int(input())

    order = {}
    scholarship = collections.defaultdict(int)
    for i in range(N):
        name, s1, s2, a, b, c = input().split()
        s1 = int(s1)
        s2 = int(s2)
        c = int(c)
        a = True if a == 'Y' else False
        b = True if b == 'Y' else False
        order[name] = i

        if s1 > 80 and c > 0:
            scholarship[name] += 8000

        if s1 > 85 and s2 > 80:
            scholarship[name] += 4000

        if s1 > 90:
            scholarship[name] += 2000

        if s1 > 85 and b:
            scholarship[name] += 1000

        if s2 > 80 and a:
            scholarship[name] += 850

    sname = [(s, -order[n], n) for n, s in scholarship.items()]
    sname.sort(reverse=True)
    print(sname[0][2])
    print(sname[0][0])
    total = sum([s for s, o, n in sname])
    print(total)

