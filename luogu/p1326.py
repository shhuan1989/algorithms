# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    
    def getmax(S, T, N):
        win = min(N - 1, S)
        tie = 0
        lose = 0
        S -= win
        if S > T:
            win += 1
        elif S == T:
            tie += 1
        else:
            lose += 1
    
        tie += max(0, N - win - tie - lose)
        return win * 3 + tie
    
    def getmin(S, T, N):
        # win 0 game
        if T-(N-1) > S:
            return 0
        # win 1 game
        a = 3 + (0 if T >= N-1 else N-1-T)
        # tie 1 game
        if S <= T:
            a = min(a, 1 + (0 if T-S >= N-1 else N-1-(T-S)))
        # tie 2 game
            a = min(a, 2 + (0 if T-S >= N-2 else N-2-(T-S)))
        # tie 3 game
            a = min(a, 3 + (0 if T-S >= N-3 else N-3-(T-S)))
        
        return a
    
        
    for line in sys.stdin:
        S, T, N = map(int, line.split())
        print(getmax(S, T, N), getmin(S, T, N))
        
