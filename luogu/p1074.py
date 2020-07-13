# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

if __name__ == '__main__':
    A = []
    zeros = 0
    for i in range(9):
        row = [int(x) for x in input().split()]
        A.append(row)
        zeros += row.count(0)

    ROW_USED = [[False for _ in range(10)] for i in range(9)]
    COL_USED = [[False for _ in range(10)] for _ in range(9)]
    REG_USED = [[False for _ in range(10)] for _ in range(9)]


    def agrmin(a):
        v = float('inf')
        vi = -1
        for i, u in enumerate(a):
            if u < v:
                v = u
                vi = i
        return vi


    def check():
        for r in range(9):
            vs = set()
            for c in range(9):
                if A[r][c] != 0 and A[r][c] in vs:
                    return False
                vs.add(A[r][c])
        for c in range(9):
            vs = set()
            for r in range(9):
                if A[r][c] != 0 and A[r][c] in vs:
                    return False
                vs.add(A[r][c])

        for sr in range(3):
            for sc in range(3):
                vs = set()
                for r in range(3 * sr, 3 * sr + 3):
                    for c in range(3 * sc, 3 * sc + 3):
                        if A[r][c] != 0 and A[r][c] in vs:
                            return False
                        vs.add(A[r][c])
        return True


    def getposs(r, c):
        if A[r][c] > 0:
            return [A[r][c]]

        # used = ROW_USED[r] | COL_USED[c] | REG_USED[getregion(r, c)]
        a = ROW_USED[r]
        b = COL_USED[c]
        c = REG_USED[getregion(r, c)]

        return [i for i in range(1, 10) if not a[i] and not b[i] and not c[i]]


    def permpss(pss, index, pre):
        if index >= len(pss):
            return [pre]

        x = []
        for v in pss[index]:
            if v not in pre:
                x += permpss(pss, index + 1, pre + [v])
        return x


    def checkrow(ri):
        sr = ri // 3

        for sc in range(3):
            vs = set()
            for r in range(sr * 3, sr * 3 + 3):
                for c in range(sc * 3, sc * 3 + 3):
                    if A[r][c] != 0 and A[r][c] in vs:
                        return False
                    vs.add(A[r][c])

        return True


    def getregion(r, c):
        sr, sc = r // 3, c // 3
        return sr * 3 + sc


    def getscore():
        x = 0
        for r in range(9):
            for c in range(9):
                d = dist2center(r, c)
                x += (10 - d) * A[r][c]
        # for row in A:
        #     print(' '.join(map(str, row)))
        # print(x)
        return x


    def dist2center(r, c):
        return max(abs(r - 4), abs(c - 4))

    def getpoint(r, c):
        return 10 - dist2center(r, c)


    ANS = [0]
    REST_NUM = [9 for _ in range(10)]
    DIST = [1, 8, 16, 24, 32]


    def getmaxrestscore():
        vs = []
        for i in range(1, 10):
            vs += [i] * REST_NUM[i]

        ds = []
        for i in range(4, -1, -1):
            ds += [10 - i] * DIST[i]

        return sum([a * b for a, b in zip(vs, ds)])


    def dfs(rest, zeros, score):
        # print(rest)
        if not rest:
            ANS[0] = max(score, ANS[0])
            return score

        if score + getmaxrestscore() < ANS[0]:
            return 0

        xr = rest[0]
        rest = rest[1:]
        zis = [i for i in range(9) if A[xr][i] == 0]
        pss = [getposs(xr, c) for c in zis]
        x = 0
        for row in permpss(pss, 0, []):
            sdelta = 0
            for c, v in zip(zis, row):
                A[xr][c] = v
                ROW_USED[xr][v] = True
                COL_USED[c][v] = True
                REG_USED[getregion(xr, c)][v] = True
                sdelta += getpoint(xr, c) * v
                REST_NUM[v] -= 1
                DIST[dist2center(xr, c)] -= 1

            x = max(x, dfs(rest, zeros - len(zis), score + sdelta))
            for c, v in zip(zis, row):
                A[xr][c] = 0
                ROW_USED[xr][v] = False
                COL_USED[c][v] = False
                REG_USED[getregion(xr, c)][v] = False
                REST_NUM[v] += 1
                DIST[dist2center(xr, c)] += 1

        return x


    if not check():
        print(-1)
        exit(0)

    zeros = 0
    rowzeros = []
    for r in range(9):
        rz = 0
        for c in range(9):
            v = A[r][c]
            rid = getregion(r, c)
            if COL_USED[c][v] or ROW_USED[r][v] or REG_USED[rid][v]:
                print(-1)
                exit(0)
            COL_USED[c][v] = True
            ROW_USED[r][v] = True
            REG_USED[getregion(r, c)][v] = True
            if A[r][c] == 0:
                zeros += 1
                rz += 1
            REST_NUM[A[r][c]] -= 1
            if A[r][c] > 0:
                DIST[dist2center(r, c)] -= 1
        if rz > 0:
            rowzeros.append((rz, r))

    rowzeros.sort()
    searchrows = [r for z, r in rowzeros]
    ans = dfs(searchrows, zeros, getscore())
    ans = ans if ans > 0 else -1
    print(ans)