# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/10 01:15


TLE, java version is accepted
"""

# N = int(input())
# A = [int(x) for x in input().split()]

N = 200000
A = [random.randint(2**10, 2**30) for _ in range(N)]

t0 = time.time()

trie = {}
for v in A:
    t = trie
    for i in range(32, -1, -1):
        if (v >> i) & 1 == 1:
            if 1 not in t:
                t[1] = {}
            t = t[1]
        else:
            if 0 not in t:
                t[0] = {}
            t = t[0]
    t['#'] = v


def min_xor_trie(a, b):
    if not a or not b:
        return float('inf'), float('inf'), float('inf')
    if '#' in a and '#' in b:
        return a['#'] ^ b['#'], a['#'], b['#']

    ans = min(min_xor_trie(a.get(0, None), b.get(0, None)), min_xor_trie(a.get(1, None), b.get(1, None)))
    if ans[0] == float('inf'):
        return min(min_xor_trie(a.get(0, None), b.get(1, None)), min_xor_trie(a.get(1, None), b.get(0, None)))
    return ans

E = []
def dfs_trie(trie):
    if not trie:
        return 0

    if 0 in trie and 1 in trie:
        a = trie[0]
        b = trie[1]
        xor = min_xor_trie(a, b)
        # print(xor)
        E.append((xor[1:]))
        xor = xor[0]
        xor = (0 if xor == float('inf') else xor)
        return dfs_trie(a) + dfs_trie(b) + xor
    elif 1 in trie:
        return dfs_trie(trie[1])
    elif 0 in trie:
        return dfs_trie(trie[0])
    else:
        return 0

def min_xor(a, b, bi):
    if not a or not b:
        return float('inf')
    if bi < 0:
        return min([u^v for u in a for v in b] or [float('inf')])
    aa = [v for v in a if (v >> bi) & 1 == 1]
    ab = [v for v in a if (v >> bi) & 1 == 0]
    ba = [v for v in b if (v >> bi) & 1 == 1]
    bb = [v for v in b if (v >> bi) & 1 == 0]

    ans = min(min_xor(aa, ba, bi-1), min_xor(ab, bb, bi-1))

    if ans == float('inf'):
        # print(a, b, bi, min([u ^ v for u in a for v in b] or [float('inf')]))
        return min([u ^ v for u in a for v in b] or [float('inf')])

    # print(a, b, bi, ans)
    return ans



def dfs(bi, vals):
    if bi < 0 or not vals:
        return 0

    a = [v for v in vals if (v >> bi) & 1 == 1]
    b = [v for v in vals if (v >> bi) & 1 == 0]

    xor = min_xor(a, b, bi-1)

    return dfs(bi-1, a) + dfs(bi-1, b) + (xor if xor != float('inf') else 0)


# print(dfs(31, A))

print(dfs_trie(trie))
# print(E)
print(time.time() - t0)