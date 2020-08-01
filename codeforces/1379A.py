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
created by shhuan at 2020/7/19 17:00

"""

mark = 'abacaba'
nmark = len(mark)
def check(s):
    if len(s) != nmark:
        return False
    for i in range(len(mark)):
        if s[i] != mark[i] and s[i] != '?':
            return False

    return True


def count(s):
    return sum([1 for i in range(len(s)) if s[i:i+nmark] == mark])


def solve(N, S):
    for i in range(N):
        if check(S[i: i+len(mark)]):
            s = S[:i] + mark + S[i+nmark:]
            t = s.replace('?', 'x')
            if count(t) == 1:
                return 'YES\n{}'.format(t)

    return 'NO'


if __name__ == '__main__':

    T = int(input())
    ans = []
    for ti in range(T):
        N = int(input())
        S = input()
        ans.append(solve(N, S))

    print('\n'.join(ans))

