# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import random

class Node:
    def __init__(self, key):
        self.key = key
        self.prior = random.randint(0, 10**9+7)
        self.left = 0
        self.right = 0
        self.size = 1

MAXN = 5 * 10**5 + 5
tre = [Node(i) for i in range(MAXN)]

def update(now):
    tre[now].size = tre[tre[now].left].size + tre[tre[now].right].size + 1

def split(now, key):
    if now <= 0:
        return 0, 0

    if tre[now].key >= key:
        l, r = split(tre[now].left, key)
        tre[now].left = r
        update(now)
        return l, now
    else:
        l, r = split(tre[now].right, key)
        tre[now].right = l
        update(now)
        return now, r


def merge(t1, t2):
    if t1 == 0 or t2 == 0:
        return t1 + t2

    if tre[t1].prior <= tre[t2].prior:
        tre[t1].right = merge(tre[t1].right, t2)
        update(t1)
        return t1
    else:
        tre[t2].left = merge(t1, tre[t2].left)
        update(t2)
        return t2

def insert(now, newnode):
    if now <= 0:
        return newnode

    if tre[now].prior <= tre[newnode].prior:
        l, r = split(now, tre[newnode].key)
        tre[newnode].left = l
        tre[newnode].right = r
        update(newnode)
        return newnode
    else:
        if tre[now].key >= tre[newnode].key:
            tre[now].left = insert(tre[now].left, newnode)
        else:
            tre[now].right = insert(tre[now].right, newnode)
        update(now)
        return now

def search(now, key):
    if now <= 0:
        return 0
    if tre[now].key == key:
        return now
    elif tre[now].key > key:
        return search(tre[now].left, key)
    else:
        return search(tre[now].right, key)

def searchpre(now, key):
    if now <= 0:
        return 0

    if tre[now].key >= key:
        return searchpre(tre[now].left, key)
    else:
        r = searchpre(tre[now].right, key)
        return r if r > 0 else now

def searchafter(now, key):
    if now <= 0:
        return 0

    if tre[now].key <= key:
        return searchafter(tre[now].right, key)
    else:
        l = searchafter(tre[now].left, key)
        return l if l > 0 else now



INF = 10 ** 9 + 7
if __name__ == '__main__':
    # sys.stdin = open('p1110_1.in', 'r')
    N, M = map(int, input().split())
    A = []
    while len(A) < N:
        A += [[int(x)] for x in input().split()]

    tre[0].key = -INF
    tre[0].size = 0
    root = 0
    id = 1
    minSortGap = INF
    for v in A:
        if minSortGap > 0:
            x = v[0]
            if search(root, x) > 0:
                minSortGap = 0
            else:
                tre[id].key = x
                root = insert(root, id)
                id += 1
                minSortGap = min(minSortGap, abs(x - tre[searchpre(root, x)].key), abs(x - tre[searchafter(root, x)].key))


    q1, q2 = [], []
    for i in range(N-1):
        heapq.heappush(q1, abs(A[i][0]-A[i+1][0]))

    ans = []
    for i in range(M):
        line = input().strip()
        # op = random.randint(0, 2)
        # line = 'INSERT {} {}'.format(random.randint(0, N-1), random.randint(0, 10**8))

        if line == 'MIN_SORT_GAP':
            ans.append(minSortGap)
        elif line == 'MIN_GAP':
            while q1 and q2 and q1[0] == q2[0]:
                heapq.heappop(q1)
                heapq.heappop(q2)
            ans.append(q1[0])
        else:
            a, b, x = line.split()
            b = int(b)
            x = int(x)
            if minSortGap > 0:
                if search(root, x) > 0:
                    minSortGap = 0
                else:
                    tre[id].key = x
                    root = insert(root, id)
                    id += 1
                    minSortGap = min(minSortGap, abs(x - tre[searchpre(root, x)].key),
                                     abs(x - tre[searchafter(root, x)].key))

            b -= 1
            if b + 1 < N:
                heapq.heappush(q2, abs(A[b][-1] - A[b+1][0]))
                heapq.heappush(q1, abs(x - A[b+1][0]))
            heapq.heappush(q1, abs(A[b][-1] - x))
            A[b].append(x)

    print('\n'.join(map(str, ans)))