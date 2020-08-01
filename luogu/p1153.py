# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List, Tuple

"""
created by shhuan at 2020/7/19 15:16

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#
def cross(a: Point, b:Point, c:Point) -> float:
    return (a.x-c.x) * (b.y-c.y) - (a.y-c.y) * (b.x-c.x)


def seg_cross(a: Point, b:Point, c:Point, d:Point) -> bool:
    return cross(c, d, a) * cross(c, d, b) < 0 and cross(a, b, c) * cross(a, b, d) < 0


def dfs(inorder: List[Point], rest: List[Point]) -> int:
    if not rest:
        c, d = inorder[-1], inorder[0]
        return 1 if all([not seg_cross(a, b, c, d) for a, b in zip(inorder[:-1], inorder[1:])]) else 0

    ans = 0
    c = inorder[-1]
    for i, v in enumerate(rest):
        d = v
        if all([not seg_cross(a, b, c, d) for a, b in zip(inorder[:-1], inorder[1:])]):
            ans += dfs(inorder + [d], rest[:i] + rest[i+1:])
    return ans


if __name__ == '__main__':
    points = []
    while True:
        x, y = map(int, input().split())
        points.append(Point(x, y))
        if x == 0 and y == 0:
            break
    ans = dfs([points[0]], points[1:])
    print(ans // 2)