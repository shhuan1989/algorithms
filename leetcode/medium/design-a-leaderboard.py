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
created by shhuan at 2019/12/19 21:58

"""


class Leaderboard:
    leaders = None
    def __init__(self):
        self.leaders = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaders:
            self.leaders[playerId] = score
        else:
            self.leaders[playerId] = self.leaders[playerId] + score

    def top(self, K: int) -> int:
        players, sum_score = sorted(self.leaders, key=lambda x:self.leaders[x], reverse=True), 0
        K = min(K, len(self.leaders))
        for p in players[:K]:
            sum_score += self.leaders[p]
        return sum_score

    def reset(self, playerId: int) -> None:
        self.leaders[playerId] = 0