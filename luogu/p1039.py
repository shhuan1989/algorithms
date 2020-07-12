# -*- coding: utf-8 -*-

import math
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/9 18:41

"""

import itertools
import collections

if __name__ == '__main__':
    M, N, P = map(int, input().split())
    names = []
    for i in range(M):
        names.append(input())

    votes = collections.defaultdict(list)
    for i in range(P):
        line = input()
        name, vote = line.split(': ')
        if name not in names:
            continue

        if vote == 'I am guilty.':
            votes[name].append((name, True))
        elif vote == 'I am not guilty.':
            votes[name].append((name, False))
        elif vote.endswith('is guilty.'):
            vname = vote.split(' ')[0]
            if vname in names:
                votes[name].append((vname, True))
        elif vote.endswith('is not guilty.'):
            vname = vote.split(' ')[0]
            if vname in names:
                votes[name].append((vname, False))
        else:
            pass

    for liars in itertools.combinations([i for i in range(M)], N):
        isguilty = {}
        invalid = False

        for person in range(M):
            name = names[person]
            if invalid:
                break
            isliar = person in liars
            vs = votes[name]

            for i, v in vs:
                g = (1 if not v else 0) if isliar else (1 if v else 0)
                if i not in isguilty:
                    isguilty[i] = g
                else:
                    if isguilty[i] != g:
                        invalid = True
                        break
            if invalid:
                break
        if invalid:
            continue

        count = len([v for v in isguilty.values() if v])
        if count == 1:
            for k, v in isguilty.items():
                if v:
                    print(k)
                    exit(0)
        elif count > 0:
            print('Cannot Determine')
            exit(0)
    print('Impossible')