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
created by shhuan at 2019/12/26 22:10

"""


class SquareLanguage:
    def howMany(self, abounds, bbounds, cbounds, dbounds):
        b = [abounds[0], abounds[1], bbounds[0], bbounds[1], cbounds[0], cbounds[1], dbounds[0], dbounds[1]]
        b = [int(x) for x in b]
        zeros = [b[2 * i] == 0 for i in range(4)]
        zeros = zeros + zeros
        if all([not v for v in zeros]):
            a, b, c, d = (b[1] - b[0] + 1), (b[3] - b[2] + 1), (b[5] - b[4] + 1), (b[7] - b[6] + 1)
            return a * b * c * d * a * b * c * d

        chs = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
        s = set()
        for i in range(1, 1 << 8):
            t = ''
            for k in range(8):
                v = i & (1 << k) > 0
                if v != zeros[k]:
                    continue
                if v:
                    t += chs[k]
            s.add(t)
        counts = [b[2 * i + 1] - b[2 * i] + (1 if not zeros[i] else 0) for i in range(4)]
        chindex = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3
        }

        s.discard('')
        ans = 0
        for t in s:
            k = [counts[chindex[t[0]]]]
            for i in range(1, len(t)):
                if t[i] == t[i - 1]:
                    pass
                else:
                    k.append(counts[chindex[t[i]]])
            c = 1
            for v in k:
                c *= v
            ans += c

        return ans + 1


s = SquareLanguage()
# print(s.howMany([0, 0], [0, 0], [0, 0], [0, 0]))
# print(s.howMany([0, 100], [0, 0], [0, 0], [0, 0]))
# print(s.howMany([0, 1], [0, 1], [0, 0], [0, 0]))
# print(s.howMany([0, 20], [0, 30], [0, 40], [0, 47]))
print(s.howMany([0, 20], [1, 30], [2, 40], [3, 47]))

import random
for i in range(10000):
    a = [random.randint(0, 100) for _ in range(2)]
    b = [random.randint(0, 100) for _ in range(2)]
    c = [random.randint(0, 100) for _ in range(2)]
    d = [random.randint(0, 100) for _ in range(2)]
    print(s.howMany(a, b, c, d))