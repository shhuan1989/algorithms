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
created by shhuan at 2018/10/20 08:23

"""


def getNextPos(start, chess, size):
    row, col = start
    res = []
    if chess == 0:
        # knight
        for drow in [-2, 2]:
            for dcol in [-1, 1]:
                res.append((row + drow, col + dcol))
        for drow in [-1, 1]:
            for dcol in [-2, 2]:
                res.append((row + drow, col + dcol))
    elif chess == 1:
        # biship
        for d in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row + d[0], col + d[1]
            while 0 <= r < size and 0 <= c < size:
                res.append((r, c))
                r, c = r + d[0], c + d[1]
    else:
        # rook
        for c in range(size):
            res.append((row, c))
        for r in range(size):
            res.append((r, col))

    return [(row, col) for row, col in res if 0 <= row < size and 0 <= col < size and (row, col) != start]



def dist(start, dest, memo, size):
    """

    :param start: (row, col, chess)
    :param dest: (row, col, chess)
    :param memo:
    :param size: size of board
    :return:
    """

    key = '_'.join(map(str, list(start) + list(dest)))
    if key in memo:
        return memo[key]

    res = float('inf'), float('inf')
    visited = {start}

    # steps, replacement, row, col, chess
    q = [(0, 0, start)]
    heapq.heapify(q)
    while q:
        steps, replacement, state = heapq.heappop(q)
        if state == dest:
            res = steps, replacement
            break

        row, col, chess = state
        for chess in range(3):
            nextPositions = getNextPos((row, col), chess, size)
            for pos in nextPositions:
                newState = (pos[0], pos[1], chess)
                if newState not in visited:
                    visited.add(newState)
                    q.append((steps + 1, replacement + (1 if chess != state[2] else 0), newState))

    return res


def solve(board, size):
    maxNum = size * size + 1
    chessType = 3
    dp = [[float('inf') for _ in range(3)] for _ in range(maxNum)]

    # dp[i][j] = min{dp[i-1][j']+dist(i-1, i, j') + replace(j', j)}
    loc = [None for _ in range(maxNum)]
    for r in range(size):
        for c in range(size):
            loc[board[r][c]] = (r, c)

    for i in range(chessType):
        dp[1][i] = 0

    memo = {}
    for num in range(2, maxNum):
        # dp[i][0] = min(dp[i][0], dp[i-1][0] + dist(loc[i-1], loc[i], 0, memo, size), dp[i-1][1])
        start, target = loc[num - 1], loc[num]
        for chess in range(chessType):
            for preChess in range(chessType):
                # replace = 1 if chess != preChess else 0
                replace = 0
                dp[num][chess] = min(dp[num][chess],
                                     dp[num - 1][preChess] + dist(start, target, preChess, memo, size) + replace)
                dp[num][chess] = min(dp[num][chess],
                                     dp[num - 1][preChess] + dist(start, target, chess, memo, size) + replace)

    return min(dp[maxNum - 1])


N = int(input())
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])

print(solve(A, N))
