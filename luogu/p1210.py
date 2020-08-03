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
created by shhuan at 2020/7/25 15:15

"""



if __name__ == '__main__':
    # sys.stdin = open('p1210.in', 'r')
    text = ''
    for line in sys.stdin:
        text += line

    index = []
    w = []
    for i, v in enumerate(text):
        v = v.lower()
        if ord('a') <= ord(v) <= ord('z'):
            w.append(v)
            index.append(i)

    # print(w)
    # print(index)
    def manacher(s):
        # print(s)
        t = '#'.join(list(s))
        t = '#' + t + '#'
        nt = len(t)
        width = [1 for _ in range(nt)]

        mid = 0
        r = 0
        ansi = -1
        answ = 0
        for i in range(nt):
            if i < r:
                width[i] = min(width[2*mid-i], r-i+1)
            while width[i] <= min(i, nt-i-1) and t[i+width[i]] == t[i-width[i]]:
                width[i] += 1

            if i + width[i] - 1 > r:
                r = width[i] + i - 1
                mid = i
            if width[i] > answ:
                answ = width[i]
                ansi = i

        return (ansi-answ+2)//2, (ansi+answ+1)//2 - 2

    l, r = manacher(w)
    # while l >= 0 and not text[l].isalpha():
    #     l -= 1
    # l += 1
    # while r < len(text) and not text[r].isalpha():
    #     r += 1
    # r -= 1
    print(r-l+1)
    pl, pr = index[l], index[r]
    print(text[pl: pr+1])