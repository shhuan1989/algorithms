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
created by shhuan at 2017/11/17 12:00

"""

class SymmetryDetection:
    def __init__(self):
        pass

    def detect(self, board):
        if not board:
            return "Neither"

        M = len(board)
        N = len(board[0])


        h, v = True, True
        for r in range(M//2):
            if board[r] != board[M-r-1]:
                h = False
                break

        for c in range(N//2):
            if [board[r][c] for r in range(M)] != [board[r][N-c-1] for r in range(M)]:
                v = False
                break

        if h and v:
            return "Both"
        elif h:
            return "Horizontally symmetric"
        elif v:
            return "Vertically symmetric"
        else:
            return "Neither"


s = SymmetryDetection()

print(s.detect(["#####",
 "#...#",
 "#####"]))