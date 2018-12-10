# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/7/18

"""
import collections

N, M = map(int, input().split())

A = []
S = collections.defaultdict(list)
subjects = set()
for i in range(N):
    s, r = map(int, input().split())
    S[s].append(r)
    subjects.add(s)

P = collections.defaultdict(list)
maxl = 0
for i in subjects:
    S[i].sort(reverse=True)
    maxl = max(maxl, len(S[i]))
    
    

T = collections.defaultdict(int)
for i in subjects:
    levels = S[i]
    t = 0
    for j in range(len(levels)):
        t += levels[j]
        if t < 0:
            break
        T[j] += t

# print(T)
print(max(0, max(T.values() or [0])))