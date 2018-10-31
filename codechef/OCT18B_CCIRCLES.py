# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/19/18

https://math.stackexchange.com/questions/780784/how-to-find-distance-between-two-different-circles

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


def distance(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    mxr, mnr = max(r1, r2), min(r1, r2)
    dc = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    mxd = dc + r1 + r2
    mnd = max(0, dc-r1-r2, mxr - dc - mnr)
    
    return mnd, mxd

#
# N, Q = 3, 3
# circles = [(0, 0, 4), (10, 0, 4), (5, 3, 5)]


N, Q = 10**3, 5*10**5

circles = [(random.randint(-10000, 10000), random.randint(-10000, 10000), random.randint(2, 10000)) for _ in range(N)]
# qs = [(random.randint(0, 10**6), i) for i in range(Q)]
qs = [random.randint(0, 10**6) for i in range(Q)]

t0 = time.time()


# N, Q = map(int, input().split())
# circles = []
# for ni in range(N):
#     x, y, r = map(int, input().split())
#     circles.append((x, y, r))
    
ds = []
for i in range(N):
    for j in range(i+1, N):
        ds.append(distance(circles[i], circles[j]))

ds.sort()

# print(ds)
#
# qs = [0, 10, 20]

# qs = []
# for qi in range(Q):
#     q = int(input())
#     qs.append((q, qi))
    
# qs.sort()
# ans = [0 for _ in range(Q)]
#
# starts = collections.Counter([l for l, _ in ds])
# ends = collections.Counter([r for _, r in ds])
#
# points = {l for l, _ in ds} | {r for _, r in ds}
# points = list(sorted(points))
#
# pairs = starts[points[0]] - ends[points[0]]
#
print('prepare cost', time.time() - t0)
#
# for pre, cur in zip(points[:-1], points[1:]):
#     # p in [pre, cur] has $paris of pairs
#
#     l = bisect.bisect_left(qs, (pre, float('-inf')))
#     r = bisect.bisect_right(qs, (cur, float('inf')))
#
#     for i in range(l, r):
#         q, qi = qs[i]
#         ans[qi] = max(ans[qi], pairs)
#
#     pairs += starts[cur] - ends[cur]
#
# for v in ans:
#     print(v)


for qi in range(Q):
    # d = int(input())
    d = qs[qi]
    di = bisect.bisect_right(ds, (d, float('inf')))
    
    ans = 0
    for i in range(di - 1, -1, -1):
        mnd, mxd = ds[i]
        if mnd <= d <= mxd:
            ans += 1
    
    print(ans)

print(time.time() - t0)