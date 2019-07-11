# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-30

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, Q = map(int, input().split())
pattern = input()
INF = 1000000
AN = 26
MAXN = 10**5 + 5
MAXM = 255
words = [[] for _ in range(3)]
NEXT_OCR = [[INF for _ in range(AN)] for _ in range(MAXN)]
DP = [[[N for _ in range(MAXM)] for _ in range(MAXM)] for _ in range(MAXM)]

DP[0][0][0] = -1
for i in range(AN):
    NEXT_OCR[N][i] = NEXT_OCR[N+1][i] = N
for pos in range(N-1, -1, -1):
    for i in range(AN):
        NEXT_OCR[pos][i] = pos if pattern[pos] == chr(ord('a')+i) else NEXT_OCR[pos+1][i]


def recomp(a, b, c):
    val = DP[a][b][c]
    if a > 0:
        val = min(val, NEXT_OCR[DP[a-1][b][c]+1][ord(words[0][a-1]) - ord('a')])
    if b > 0:
        val = min(val, NEXT_OCR[DP[a][b-1][c]+1][ord(words[1][b-1]) - ord('a')])
    if c > 0:
        val = min(val, NEXT_OCR[DP[a][b][c-1]+1][ord(words[2][c-1]) - ord('a')])
    
    DP[a][b][c] = val
    

for qi in range(Q):
    line = input().split()
    wordId = int(line[1]) - 1
    if line[0] == '+':
        words[wordId].append(line[2])
        max0, max1, max2 = len(words[0]), len(words[1]), len(words[2])
        min0 = max0 if wordId == 0 else 0
        min1 = max1 if wordId == 1 else 0
        min2 = max2 if wordId == 2 else 0
        
        for a in range(min0, max0+1):
            for b in range(min1, max1+1):
                for c in range(min2, max2+1):
                    recomp(a, b, c)
        
    else:
        words[wordId].pop()
    
    if DP[len(words[0])][len(words[1])][len(words[2])] < N:
        print('YES')
    else:
        print('NO')
        
    



