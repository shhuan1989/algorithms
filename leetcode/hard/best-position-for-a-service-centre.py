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
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        eps = 1e-7
        step = 1.0
        decay = 0.5
        
        n = len(positions)
        
        x = sum(pos[0] for pos in positions) / n
        y = sum(pos[1] for pos in positions) / n
        
        # 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        getDist = lambda xc, yc: sum(((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 for x, y in positions)
        
        while step > eps:
            modified = False
            for dx, dy in dirs:
                xNext = x + step * dx
                yNext = y + step * dy
                if getDist(xNext, yNext) < getDist(x, y):
                    x, y = xNext, yNext
                    modified = True
                    break
            if not modified:
                step *= (1.0 - decay)
        
        return getDist(x, y)
    
    def getMinDistSum4(self, positions: List[List[int]]) -> float:
        n = len(positions)
        eps = 1e-7
        
        def dx(x, y, batch):
            return sum([(x - a) / (eps + math.sqrt((x - a) ** 2 + (y - b) ** 2)) for a, b in positions])
        
        def dy(x, y, batch):
            return sum([(y - b) / (eps + math.sqrt((x - a) ** 2 + (y - b) ** 2)) for a, b in positions])
        
        def dist(x, y):
            return sum([math.sqrt((x - a) ** 2 + (y - b) ** 2) for a, b in positions])
        
        cx = sum([a for a, b in positions]) / n
        cy = sum([b for a, b in positions]) / n
        
        r = 0.99
        batchsize = 100
        while True:
            random.shuffle(positions)
            
            xpre = cx
            ypre = cy
            cx -= r * dx(cx, cy, positions[:batchsize])
            cy -= r * dy(cx, cy, positions[:batchsize])
            r *= 0.999
            
            if ((cx - xpre) ** 2 + (cy - ypre) ** 2) ** 0.5 < eps:
                break
        
        return dist(cx, cy)
    
    
    def getMinDistSum3(self, positions: List[List[int]]) -> float:
        n = len(positions)
        eps = 1e-7
        def dx(x, y):
            return sum([(x - a) / (eps + math.sqrt((x - a) ** 2 + (y - b) ** 2)) for a, b in positions])

        def dy(x, y):
            return sum([(y - b) / (eps + math.sqrt((x - a) ** 2 + (y - b) ** 2)) for a, b in positions])
        
        def dist(x, y):
            return sum([math.sqrt((x-a)**2+(y-b)**2) for a, b in positions])

        cx = sum([a for a, b in positions]) / n
        cy = sum([b for a, b in positions]) / n
        
        
        r = 0.99
        while True:
            xpre = cx
            ypre = cy
            cx -= r * dx(cx, cy)
            cy -= r * dy(cx, cy)
            r *= 0.999

            if ((cx - xpre) ** 2 + (cy - ypre) ** 2) ** 0.5 < eps:
                break
        
        return dist(cx, cy)
            
        
    
    def getMinDistSum2(self, positions: List[List[int]]) -> float:
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