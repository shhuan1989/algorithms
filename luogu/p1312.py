# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def finished(board):
    for c in range(5):
        if sum(board[c]) > 0:
            return False
    return True


def drop(board):
    for c in range(5):
        for r in range(7):
            if board[c][r] == 0:
                find = False
                for nr in range(r + 1, 7):
                    if board[c][nr] != 0:
                        board[c][r], board[c][nr] = board[c][nr], board[c][r]
                        find = True
                        break
                if not find:
                    break


def explode(board):
    mark = [[False for _ in range(7)] for _ in range(5)]
    
    for c in range(5):
        l, r = 0, 0
        while r < 7 and board[c][r] > 0:
            if board[c][r] != board[c][l]:
                if r - l >= 3:
                    for i in range(l, r):
                        mark[c][i] = True
                l = r
            r += 1
        if r - l >= 3 and board[c][l] > 0:
            for i in range(l, r):
                mark[c][i] = True
    
    for r in range(7):
        s, t = 0, 0
        while t < 5:
            if board[t][r] != board[s][r]:
                if t - s >= 3 and board[s][r] > 0:
                    for i in range(s, t):
                        mark[i][r] = True
                s = t
            t += 1
        if t - s >= 3 and board[s][r] > 0:
            for i in range(s, t):
                mark[i][r] = True
    
    have = False
    for c in range(5):
        for r in range(7):
            if mark[c][r]:
                board[c][r] = 0
                have = True
    
    return have


def collapse(board):
    while True:
        drop(board)
        if not explode(board):
            break


def copy(board):
    newboard = [[0 for _ in range(7)] for _ in range(5)]
    for c in range(5):
        for r in range(7):
            newboard[c][r] = board[c][r]
    
    return newboard


def desc(board):
    print('=' * 80)
    for r in range(6, -1, -1):
        print(' '.join(map(str, [board[c][r] for c in range(5)])))


def dfs(board, ops, steps):
    if steps <= 0:
        if finished(board):
            for x, y, g in ops:
                print('{} {} {}'.format(x, y, g))
            exit(0)
        return
    
    for c in range(5):
        for r in range(7):
            if board[c][r] == 0:
                break
            
            # move to right
            if c + 1 < 5:
                newboard = copy(board)
                newboard[c + 1][r], newboard[c][r] = newboard[c][r], newboard[c + 1][r]
                collapse(newboard)
                # if ops == [(2, 1, 1), (3, 1, 1)] and (c, r, 1) == (3, 0, 1):
                #     desc(newboard)
                dfs(newboard, ops + [(c, r, 1)], steps - 1)
            
            # move to left
            if c - 1 >= 0:
                newboard = copy(board)
                newboard[c - 1][r], newboard[c][r] = newboard[c][r], newboard[c - 1][r]
                collapse(newboard)
                dfs(newboard, ops + [(c, r, -1)], steps - 1)


def test():
    import random
    N = random.randint(1, 5)
    A = [[0 for _ in range(7)] for _ in range(5)]
    for c in range(5):
        for r in range(7):
            A[c][r] = random.randint(1, 10)
    collapse(A)
    print(N)
    desc(A)
    dfs(A, [], N)
    print(-1)
    
                
if __name__ == '__main__':
    # sys.stdin = open('P1312.in', 'r')
    for i in range(10):
        test()
    # N = int(input())
    # A = [[0 for _ in range(7)] for _ in range(5)]
    # for i in range(5):
    #     col = [int(x) for x in input().split()]
    #     for j in range(len(col)):
    #         A[i][j] = col[j]
    #
    # collapse(A)
    # dfs(A, [], 0)
    # print(-1)

