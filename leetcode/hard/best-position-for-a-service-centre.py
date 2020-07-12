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
created by shhuan at 2020/7/12 10:40

"""



class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)

        def fa(x, y):
            return sum([(x-a)/(1e-7+math.sqrt((x-a)**2 + (y-b)**2)) for a, b in positions])

        def fb(x, y):
            return sum([(y - b) / (1e-7+math.sqrt((x - a) ** 2 + (y - b) ** 2)) for a, b in positions])

        def dist(x, y):
            return sum([math.sqrt((x-a)**2+(y-b)**2) for a, b in positions])

        avgx = sum([a for a, b in positions]) / n
        avgy = sum([b for a, b in positions]) / n

        ans = 100000
        for i in range(100):
            xl, xr = 0, 101
            while xl <= xr and abs(xl-xr) > 1e-7:
                dx = (xr - xl) / 3
                l, r = xl+dx, xl+2*dx
                fx1 = fa(l, avgy)
                fx2 = fa(r, avgy)
                fx0 = fa(xl, avgy)
                # fx3 = fa(xr, avgx)

                if fx1 * fx2 < 0:
                    xl, xr = l, r
                elif fx0 * fx2 > 0:
                    xl = r
                else:
                    xr = l
            ans = min(ans, dist(xl, avgy))

            avgx = xl

            yl, yr = 0, 101
            while yl <= yr and abs(yl-yr) > 1e-7:
                dy = (yr-yl) / 3
                l, r = yl+dy, yl+2*dy
                fy0 = fb(avgx, yl)
                fy1 = fb(avgx, l)
                fy2 = fb(avgx, r)
                if fy1 * fy2 < 0:
                    yl, yr = l, r
                elif fy0 * fy2 > 0:
                    yl = r
                else:
                    yr = l
            ans = min(ans, dist(avgx, yl))
            avgy = yl

        return ans




if __name__ == '__main__':

    s = Solution()
    print(s.getMinDistSum(positions = [[0,1],[1,0],[1,2],[2,1]]))
    print(s.getMinDistSum(positions = [[1,1],[3,3]]))
    print(s.getMinDistSum([[1, 1]]))
    print(s.getMinDistSum([[1,1],[0,0],[2,0]]))
    print(s.getMinDistSum([[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]))