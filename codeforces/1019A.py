# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/29/19

Let's iterate over final number of votes for The United Party of Berland.
We can see that all opponents should get less votes than our party,
and our party should get at least our chosen number of votes.

We can sort all voters by their costs, and solve the problem in two passes.
First, if we need to get 𝑥 votes, we should definitely buy all cheap votes for parties that have at least 𝑥 votes.
Second, if we don't have 𝑥 votes yet, we should by the cheapest votes to get 𝑥 votes.
We can see that this solution is optimal: consider the optimal answer, and see how many votes The United Party got.
We tried such number of votes, and we tried to achieve this number of votes by cheapest way, so we couldn't miss the
optimal answer. This can be implemented in 𝑂(𝑛2log𝑛) or even 𝑂(𝑛log𝑛).



"""

import collections
import time
import os
import sys
import bisect
import heapq

N, M = map(int, input().split())

voters = collections.defaultdict(list)

for i in range(N):
    p, c = map(int, input().split())
    voters[p].append(c)

for p in voters.keys():
    voters[p] = list(sorted(voters[p], reverse=True))

ans = float('inf')
for x in range(N+1):
    cnt = len(voters[1])
    cost = 0
    a = []
    for i in range(2, M+1):
        a.extend(voters[i][:x])
        cost += sum(voters[i][x:] or [0])
        cnt += max(0, len(voters[i]) - x)
    a.sort()
    
    if cnt <= x and len(a) >= x-cnt+1:
        cost += sum(a[:x-cnt+1])
        ans = min(ans, cost)
    elif cnt > x:
        ans = min(ans, cost)

print(ans)