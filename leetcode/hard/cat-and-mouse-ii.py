# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/19
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List

sys.setrecursionlimit(100000)


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        n, m = len(grid), len(grid[0])
        foodx, foody = -1, -1
        catx, caty = -1, -1
        mousex, mousey = -1, -1
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 'F':
                    foodx, foody = x, y
                if grid[x][y] == 'C':
                    catx, caty = x, y
                if grid[x][y] == 'M':
                    mousex, mousey = x, y
                    

        @lru_cache(maxsize=None)
        def caneat(currx, curry, targetx, targety, jump):
            if currx == targetx and curry == targety:
                return True
            
            if currx == targetx and abs(curry - targety) <= jump:
                if all(grid[currx][y] != '#' for y in range(curry, targety, 1 if curry <= targety else -1)):
                    return True
            
            if curry == targety and abs(currx - targetx) <= jump:
                if all(grid[x][curry] != '#' for x in range(currx, targetx, 1 if currx <= targetx else -1)):
                    return True
                
            return False
        
        
        @lru_cache(maxsize=None)
        def dist(currx, curry, targetx, targety, jump):
            mindist = [[float('inf') for _ in range(m)] for _ in range(n)]
            mindist[currx][curry] = 0
            q = [(0, currx, curry)]
            while q:
                _, x, y = heapq.heappop(q)
                if x == targetx and y == targety:
                    return mindist[x][y]
                
                for nx, ny in nextpos(x, y, jump):
                    if mindist[nx][ny] > mindist[x][y] + 1:
                        mindist[nx][ny] = mindist[x][y] + 1
                        heapq.heappush(q, (mindist[nx][ny], nx, ny))
            
            return mindist[targetx][targety]
            
            
        
        @lru_cache(maxsize=None)
        def nextpos(currx, curry, jump):
            ans = [(currx, curry)]
            # right
            for y in range(curry, min(m, curry+jump+1)):
                if grid[currx][y] == '#':
                    break
                ans.append((currx, y))
            # left
            for y in range(curry, max(-1, curry-jump-1), -1):
                if grid[currx][y] == '#':
                    break
                ans.append((currx, y))
            # up
            for x in range(currx, max(-1, currx-jump-1), -1):
                if grid[x][curry] == '#':
                    break
                ans.append((x, curry))
            # down
            for x in range(currx, min(n, currx+jump+1)):
                if grid[x][curry] == '#':
                    break
                ans.append((x, curry))
            
            return ans

        @lru_cache(maxsize=None)
        def move(xcat, ycat, xmouse, ymouse, catmove, mousesteps):
            if not catmove and mousesteps > 100:
                return False

            if catmove:
                if caneat(xcat, ycat, foodx, foody, catJump):
                    return True
                if caneat(xcat, ycat, xmouse, ymouse, catJump):
                    return True
                
                if dist(xcat, ycat, foodx, foody, catJump) <= dist(xmouse, ymouse, foodx, foody, mouseJump):
                    return True
                
                if any(not move(nx, ny, xmouse, ymouse, False, mousesteps) for nx, ny in nextpos(xcat, ycat, catJump)):
                    return True
                    
                return False
            else:
                if xmouse == xcat and ymouse == ycat:
                    return False
                
                if caneat(xmouse, ymouse, foodx, foody, mouseJump):
                    return True
                
                if any(not move(xcat, ycat, nx, ny, True, mousesteps+1) for nx, ny in nextpos(xmouse, ymouse, mouseJump)):
                    return True
                
                return False
        
        return move(catx, caty, mousex, mousey, False, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.canMouseWin(grid=["####F", "#C...", "M...."], catJump=1, mouseJump=2))
    print(s.canMouseWin(grid=["M.C...F"], catJump=1, mouseJump=4))
    print(s.canMouseWin(grid=["M.C...F"], catJump=1, mouseJump=3))
    print(s.canMouseWin(grid=["C...#", "...#F", "....#", "M...."], catJump=2, mouseJump=5))
    print(s.canMouseWin(grid=[".M...", "..#..", "#..#.", "C#.#.", "...#F"], catJump=3, mouseJump=1))
    print(s.canMouseWin(["..F", "#C#", "#..", "#.M"], 1, 2))
    print(s.canMouseWin(["##....#","..##.M#","...#...","..#.#F.","##...#.",".C.....",".###..."], 3, 1))
