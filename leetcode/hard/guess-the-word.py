# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

class Solution(object):
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        self.H = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                d = sum([wordlist[i][k] == wordlist[j][k] for k in range(len(wordlist[i]))])
                self.H[i][j] = d
                self.H[j][i] = d
        possible, path = range(N), set()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]):
                return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path.add(guess)

    def solve(self, possible, path):
        if len(possible) <= 2:
            return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                        
                # 让最大值最小
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess