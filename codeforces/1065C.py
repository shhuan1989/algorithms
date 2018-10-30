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
created by shhuan at 2018/10/19 23:16

"""

def canSliceToHeight(highest, targetHeight, start, heights, maxSlicedHeight):
    """
    判断能否横向切一刀之后所有建筑的高度都低于targetHeight
    :param highest: 当前最高建筑的高度
    :param targetHeight: 目标高度
    :param start: start左边的建筑的高度都是highest
    :param heights: 所有建筑的高度，降序排列
    :param maxSlicedHeight: 横向切一刀之后，建筑被切掉的高度的和不能超过maxSlicedHeight
    :return:
    """
    total = (highest - targetHeight) * start
    if total > maxSlicedHeight:
        return False

    for i in range(start, len(heights)):
        h = heights[i]
        if h <= targetHeight:
            break
        total += heights[i] - targetHeight

    return total <= maxSlicedHeight

def findNextHighest(currentHighest, start, heights, maxSlicedHeight):
    """
    采用二分查找，横向切一刀之后最高建筑的最低高度
    :param currentHighest: 当前所有建筑的最高高度
    :param start: start左边的建筑的高度都等于currentHighest
    :param heights: 所有建筑的高度
    :param maxSlicedHeight: 横向切一刀之后，建筑被切掉的高度的和不能超过maxSlicedHeight
    :return:
    """

    lo, hi = 0, currentHighest

    while lo < hi:
        m = (lo + hi) // 2
        if canSliceToHeight(currentHighest, m, start, heights, maxSlicedHeight):
            hi = m
        else:
            lo = m + 1


    return lo

def solve(N, K, H):
    H.sort(reverse=True)
    target = H[-1]
    steps = 0

    start = 1
    highest = H[0]
    done = False
    while highest > target and not done:
        nextHighest = findNextHighest(highest, start, H, K)

        if H[start] < nextHighest:
            # 如果当位置的建筑的高度低于切一刀之后的高度，需要切多次才能使得最高高度低于当前建筑的高度
            slicedHeightPerStep = highest - nextHighest
            localSteps = (highest - H[start]) // slicedHeightPerStep
            steps += localSteps
            highest -= slicedHeightPerStep * localSteps
        else:
            # 否则只切一刀， 完成之后最高建筑的高度是nextHighest
            # 找到下一个比nextHighest低的建筑
            nextStart = start
            for i in range(start, N):
                if H[i] < nextHighest:
                    nextStart = i
                    break

            start = nextStart
            steps += 1
            highest = nextHighest


    return steps


N, K = map(int, input().split())
H = [int(x) for x in input().split()]

print(solve(N, K, H))
