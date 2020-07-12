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
created by shhuan at 2020/7/8 23:24

"""

memo = {}

def countworkds(s, l, r, words, maxlen):
    key = (l, r)
    if key in memo:
        return memo[key]

    count = 0
    for i in range(l, r+1):
        for j in range(i+1, min(r+1, i+maxlen+1)+1):
            t = s[i: j]
            if t in words:
                count += 1
                break

    memo[key] = count
    return count


def have(s, i, j, words, maxlen):
    for a in range(i, j+1):
        for b in range(i+1, min(j+1, i+maxlen+1)+1):
            if s[a:b] in words:
                return True

    return False


def find(s, i, trie):
    t = trie
    while i < len(s):
        v = s[i]
        if v not in t:
            return -1
        t = t[v]
        if '#' in t:
            return i
        i += 1

    return -1


if __name__ == '__main__':
    P, K = map(int, input().split())
    S = []
    for i in range(P):
        S.append(input())
    S = ''.join(S)
    M = int(input())
    words = []
    for i in range(M):
        words.append(input())


    trie = {}
    for word in words:
        t = trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = True

    N = len(S)
    W = []
    for i in range(N):
        j = find(S, i, trie)
        if j > 0:
            W.append((i, j))

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][1] = len([(l, r) for l, r in W if 0 <= l <= r <= i-1])


    for i in range(1, N+1):
        for k in range(2, min(i, K)+1):
            for pi in range(k-1, i):
                dp[i][k] = max(dp[i][k], dp[pi][k - 1] + len([(l, r) for l, r in W if pi <= l <= r <= i - 1]))

    # for k in range(2, K+1):
    #     for i in range(k, N+1):
    #         for pi in range(k-1, i):
    #             dp[i][k] = max(dp[i][k], dp[pi][k-1] + len([(l, r) for l, r in W if pi <= l <= r <= i-1]))

    # print(W)
    # for row in dp:
    #     print(row)

    print(dp[N][K])