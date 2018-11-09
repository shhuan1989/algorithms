# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/7 19:30

"""

N, M = map(int, input().split())
A, Q = [], []
for ai in range(N):
    A.append(input())
for qi in range(M):
    l, r, v = input().split()
    Q.append((int(l), int(r), v))

# import random
# import time
# N, M = 10**5, 10**5
# A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))]) for _ in range(N)]
# Q = []
# for i in range(M):
#     l = random.randint(1, N // 2)
#     r = random.randint(l, N)
#     v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))])
#     Q.append((l, r, v))
#
# print('starting')
import time
t0 = time.time()

tree = {'idx': [], 'vals': ''}


def buildTree(num, idx, maxlen):
    if len(num) < maxlen:
        num = '0' * (maxlen - len(num)) + num

    t = tree
    i = 0
    while i < len(num):
        t['idx'].append(idx)
        tv = t['vals']
        vi = i
        extend = False
        if tv:
            j = 0
            while j < len(tv) and i+j < len(num) and num[i+j] == tv[j]:
                j += 1
            if j >= len(tv):
                vi = i + j
                extend = True
            else:
                c0 = t['0'] if '0' in t else None
                c1 = t['1'] if '1' in t else None
                vj = tv[j]
                t['vals'] = tv[:j]
                t[vj] = {'idx': [x for x in t['idx'][:-1]], 'vals': tv[j+1:]}
                if c0:
                    t[vj]['0'] = c0
                if c1:
                    t[vj]['1'] = c1

                t[num[i+j]] = {'idx': [idx], 'vals': num[i+j+1:]}
                return
        else:
            extend = True

        if extend and vi < len(num):
            v = num[vi]
            if v in t:
                t = t[v]
                i = vi + 1
            else:
                t[v] = {'idx': [idx], 'vals': num[vi+1:]}
                return
        else:
            return

# A = [(len(v), v) for v in A]
# A.sort(reverse=True)
# A = [x[1] for x in A]

maxLen = max(len(v) for v in A)
for i, v in enumerate(A):
    # print(i)
    buildTree(v, i+1, maxLen)

# import json
# print(json.dumps(tree))

# print('tree built')


def check(l, r, idx):
    if not idx:
        return False

    if idx[0] > r or idx[-1] < l:
        return False

    if l <= idx[0] <= idx[-1] <= r:
        return True

    # idx is sorted
    a, b = 0, len(idx)
    while a < b:
        c = (a + b) // 2
        v = idx[c]
        if l <= v <= r:
            return True
        if v < l:
            a = c + 1
        elif v > r:
            b = c

    return False


def find(l, r, idx):
    a, b = 0, len(idx)

    while a < b:
        c = (a + b) // 2
        v = idx[c]
        if v < l:
            a = c + 1
        elif v > r:
            b = c
        else:
            b = c

    return idx[a]


def query(l, r, val, maxLen):
    vl = len(val)
    if vl > maxLen:
        val = val[vl - maxLen:]
    elif vl < maxLen:
        val = '0' * (maxLen-vl) + val

    vi = 0
    t = tree
    while vi < len(val):
        tidx = t['idx']
        if len(tidx) <= 1:
            break

        v = val[vi]
        u = '1' if v == '0' else '0'
        tv = t['vals']
        if tv:
            vi += len(tv) + 1
        else:
            if u in t and check(l, r, t[u]['idx']):
                t = t[u]
                vi += 1
            else:
                if v in t and check(l, r, t[v]['idx']):
                    t = t[v]
                else:
                    break
                vi += 1

    return find(l, r, t['idx'])


ans = []
for l, r, v in Q:
    ans.append(query(l, r, v, maxLen))
print('\n'.join(map(str, ans)))



# print(time.time() - t0)