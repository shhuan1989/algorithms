# -*- coding: utf-8 -*-

import math
import collections
import random
import time
import os


def getInput():
    N, M = map(int, input().split())

    A = []
    for i in range(N):
        x, y, r = map(int, input().split())
        A.append((x, y, r))

    qs = []
    for i in range(M):
        qs.append(int(input()))

    return N, A, qs


def distance(circlea, circleb):
    """
    计算两个圆上的点之间的距离的最小值和最大值
    :param circlea:
    :param circleb:
    :return:
    """
    x1, y1, r1 = circlea
    x2, y2, r2 = circleb

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    mxd = d + r1 + r2
    mnr, mxr = min(r1, r2), max(r1, r2)
    mnd = max(0, d - r1 - r2, mxr - d - mnr)

    return mnd, mxd


def preprocess(N, circles):
    """
    计算所有两个圆之间的距离区间，得到起始点和结束点的集合，用map存储来消除重复
    :param N:
    :param circles:
    :return:
    """
    starts = collections.defaultdict(int)
    ends = collections.defaultdict(int)
    for i in range(N):
        for j in range(i + 1, N):
            a, b = distance(circles[i], circles[j])
            starts[a] += 1
            ends[b] += 1

    return starts, ends


def query(queries, starts, ends):
    """
    把所有的点放到一个列表中排序，要注意的如果点的值一样的情况下，要查询的点要排在起始点之后，结束点之前，代码中第二位用012来保证

    :param queries:
    :param starts:
    :param ends:
    :return:
    """
    points = [(p, 0, 0) for p in starts.keys()]
    points += [(p, 2, 0) for p in ends.keys()]
    points += [(p, 1, i) for i, p in enumerate(queries)]

    ans = [0 for _ in range(len(queries))]
    counts = 0  # 当前有多少个区间
    for p, a, pi in sorted(points):
        if a == 1:
            # 当前点是要查询的点，包含当前点的区间的数量就是counts值
            ans[pi] = counts
        else:
            counts += starts[p] - ends[p]

    return ans


def solve(N, circles, queries):
    starts, ends = preprocess(N, circles)
    ans = query(queries, starts, ends)

    # don't print one element per time, very slow
    # print函数很慢，所以要一次调用
    print('\n'.join(map(str, ans)))


def genInput():
    N = 1000
    A = [(random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(1, 300)) for _ in range(N)]
    qs = [random.randint(0, 1000) for _ in range(5 * 10 ** 5)]

    return N, A, qs


def test():
    N, a, qs = genInput()
    t0 = time.time()
    solve(N, a, qs)
    print(time.time() - t0)


test()
#
# N, A, qs = getInput()
# solve(N, A, qs)