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
created by shhuan at 2020/7/25 13:46

"""


if __name__ == '__main__':
    A = []
    for i in range(4):
        w, h = map(int, input().split())
        A.append((w, h))


    def getmin(a):
        minw = sum([w for w, h in a])
        minh = max([h for w, h in a])
        mina = minw * minh
        wh = [(minw, minh)]

        cw = max(a[0][0], sum([w for w, h in a[1:]]))
        ch = a[0][1] + max([h for w, h in a[1:]])
        ca = cw * ch
        if ca < mina:
            mina = ca
            wh = [(cw, ch)]
        elif ca == mina:
            wh.append((cw, ch))

        cw = max(a[0][0], sum([w for w, h in a[1:3]])) + a[-1][0]
        ch = max(a[0][1] + max(h for w, h in a[1:3]), a[-1][1])
        ca = cw * ch
        if ca < mina:
            mina = ca
            wh = [(cw, ch)]
        elif ca == mina:
            wh.append((cw, ch))

        cw = a[0][0] + a[-1][0] + max(a[1][0], a[2][0])
        ch = max(a[0][1], a[-1][1], a[1][1] + a[2][1])
        ca = cw * ch
        if ca < mina:
            mina = ca
            wh = [(cw, ch)]
        elif ca == mina:
            wh.append((cw, ch))

        cw = max(a[0][0], a[1][0]) + a[2][0] + a[3][0]
        ch = max(a[0][1] + a[1][1], a[2][1], a[3][1])
        ca = cw * ch
        if ca < mina:
            mina = ca
            wh = [(cw, ch)]
        elif ca == mina:
            wh.append((cw, ch))


        if a[0][0] >= a[1][0] and a[-1][0] >= a[-2][0] and a[0][0] + a[2][0] >= a[1][0] + a[-1][0] and a[2][1] >= a[0][1]:
            cw = a[0][0] + a[2][0]
            ch = max(a[0][1] + a[1][1], a[2][1] + a[3][1])
            ca = ch * cw
            if ca < mina:
                mina = ca
                wh = [(cw, ch)]
            elif ca == mina:
                wh.append((cw, ch))


        return mina, wh


    minarea = 50*50*5*5
    ans = []

    for i in range(2**4):
        ca = A.copy()
        for j in range(4):
            if i & (1 << j) > 0:
                ca[j] = (ca[j][1], ca[j][0])

        for a in itertools.permutations(ca):
            area, wh = getmin(a)
            # print(a, area, wh)
            if area < minarea:
                minarea = area
                ans = wh
            elif area == minarea:
                ans += wh

    ans = {(min(w, h), max(w, h)) for w, h in ans}
    ans = list(sorted(ans))

    print(minarea)
    print('\n'.join(['{} {}'.format(w, h) for w, h in ans]))