# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/21 22:57

"""


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        def iskey(val):
            return 'a' <= val <= 'z'

        def islock(val):
            return 'A' <= val <= 'Z'

        def lockofkey(key):
            return key.upper()

        def keyoflock(lock):
            return lock.lower()

        def keytoid(key):
            return ord(key) - ord('a')

        def addkey(state, key):
            return state | (1 << keytoid(key))

        def unlock(lock, keys):
            key = keyoflock(lock)
            return keys & (1 << keytoid(key)) > 0

        N, M = len(grid), len(grid[0])

        start = None
        keys = {}
        locks = {}
        for r in range(N):
            for c in range(M):
                v = grid[r][c]
                if v == '@':
                    start = (r, c)
                elif iskey(v):
                    keys[v] = (r, c)
                elif islock(v):
                    locks[v] = (r, c)

        nkeys = len(keys)
        dist = [[[float('inf') for _ in range(2**nkeys)] for _ in range(M)] for _ in range(N)]
        r, c = start
        dist[r][c][0] = 0
        q = [(0, 0, r, c, 0)]
        heapq.heapify(q)
        ans = float('inf')
        while q:
            kc, d, r, c, k = heapq.heappop(q)
            print(r, c, k, d)
            if k == (1 << nkeys) - 1:
                ans = min(ans, d)

            if d > dist[r][c][k]:
                continue

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != '#':
                    v = grid[nr][nc]
                    if iskey(v):
                        nk = addkey(k, v)
                        if d < dist[nr][nc][nk]:
                            dist[nr][nc][nk] = d + 1
                            # q.append((nr, nc, nk, d + 1))
                            heapq.heappush(q, (kc-1, d+1, nr, nc, nk))
                    elif islock(v):
                        if unlock(v, k) and d < dist[nr][nc][k]:
                            dist[nr][nc][k] = d + 1
                            # q.append((nr, nc, k, d + 1))
                            heapq.heappush(q, (kc, d + 1, nr, nc, k))
                    elif d < dist[nr][nc][k]:
                            dist[nr][nc][k] = d + 1
                            # q.append((nr, nc, k, d + 1))
                            heapq.heappush(q, (kc, d + 1, nr, nc, k))

        return ans if ans < float('inf') else -1


s = Solution()
for row in ["@...a",".###A","b.BCc"]:
    print(row)
print(s.shortestPathAllKeys(["@...a",".###A","b.BCc"]))
# print(s.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
# print(s.shortestPathAllKeys( ["@..aA","..B#.","....b"]))
# print(s.shortestPathAllKeys([".#........","......#..#",".#B#.#..#.","##...D.#..",".#.......#","##.....a..","...C.#...#","A...#.e.E#","c.@..#...d","#..#.#.b.#"]))

# print(s.shortestPathAllKeys([".#......###..#.",".###C..#...b...","..#..#.........",".........#.....",".....@#.#......","#.##...#..##...","..d#...a...#...","..###..........","........#....#.","..#.#..#...c#.#","D#..........#.#","............#A.","..#..##...#....","#...#..#..B....",".....##.....#.."]))



