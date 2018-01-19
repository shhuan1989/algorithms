# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/18


你参加一个考试，考试时长T，共有N道题目，你可以随便做几道题，总时间不能超过T。
解决第i道题目需要时间ti，跳过题目不花时间，题目之间也不需要花时间休息。

老师对每个题目i给定了一个值ai，只要当你做的总题目数量小于等于ai时，题目i会给你一分。


输入T，N和ai，ti，要求计算最多能够得几分。


"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N, T = map(int, input().split())
#
# N, T = 200000, 1000000000

ta = []
for i in range(N):
  a, t = map(int, input().split())
  ta.append((t, a, i+1))
  # ta.append((10000, 200000, i+1))

ta.sort()


score = 0
solvedCount = 0

# 已经解决的题目的a值
aks = []
heapq.heapify(aks)

# 存所以解决的题目，key是a，value是时间和题目编号
sc = collections.defaultdict(list)
for i in range(N):
  t, a, _ = ta[i]
  if T < t:
    break

  T -= t
  solvedCount += 1

  sc[a].append((t, i))
  heapq.heappush(aks, a)
  removed = []
  while aks and aks[0] < solvedCount:
    k = heapq.heappop(aks)
    removed.append(k)
    v = sc[k]
    solvedCount -= len(v)
    for _, j in v:
      T += ta[j][0]

    # 解决题目a=k小于解题数的题目不得分，不做这些题
    del sc[k]

  score = max(score, solvedCount)


print(score)
print(score)

vta = [(t, a, i) for t, a, i in ta if a >= score]
vta.sort()
ans = [i for _, _, i in vta[:score]]
print(" ".join(map(str, ans)))


