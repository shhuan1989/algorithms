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
created by shhuan at 2020/7/11 15:44

"""


def check(a, b):
    return (a.isdigit() and b.isdigit()) or (a.isalpha() and b.isalpha())


if __name__ == '__main__':
    p1, p2, p3 = map(int, input().split())
    s = input()
    ans = [s[0]]
    i = 1
    while i < len(s)-1:
        v = s[i]
        a, b = s[i-1], s[i+1]
        oa, ob = ord(a), ord(b)
        if v == '-':
            if not check(a, b):
                ans.append(v)
            elif oa >= ob:
                ans.append(v)
            elif oa + 1 == ob:
                pass
            else:
                if p1 == 3:
                    count = p2 * (ob - oa - 1)
                    for j in range(count):
                        ans.append('*')
                else:
                    if p3 == 1:
                        for v in range(oa+1, ob):
                            for j in range(p2):
                                ans.append(chr(v) if p1 == 1 else chr(v).upper())
                    else:
                        for v in range(ob-1, oa, -1):
                            for j in range(p2):
                                ans.append(chr(v) if p1 == 1 else chr(v).upper())
        else:
            ans.append(v)
        i += 1
    if i < len(s):
        ans.append(s[-1])
    print(''.join(ans))