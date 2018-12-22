# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 17:07

"""

class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        nrnc = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 5, 1],
            5: [4, 2],
        }

        def state_to_index(state):
            ans = 0
            m = 1
            for i in range(5, -1, -1):
                ans += state[i] * m
                m *= 10

            return ans

        def next_state(state, index):
            js = nrnc[index]
            for j in js:
                s = [x for x in state]
                s[index], s[j] = s[j], s[index]
                yield s, j

        row, col = 0, 0
        for r in range(2):
            for c in range(3):
                if board[r][c] == 0:
                    row, col = r, c
                    break


        state = board[0] + board[1]
        target = [1, 2, 3, 4, 5, 0]
        q = collections.deque([(state, state_to_index(state), row*3 + col)])
        revq = collections.deque([(target, state_to_index(target), 5)])
        steps = [float('inf')] * 543211
        revsteps = [float('inf')] * 543211
        steps[q[0][1]] = 0
        revsteps[revq[0][1]] = 0

        while q or revq:
            if q:
                state, si, index = q.popleft()
                if revsteps[si] + steps[si] < float('inf'):
                    return revsteps[si] + steps[si]

                step = steps[si] + 1
                for ns, ni in next_state(state, index):
                    nsi = state_to_index(ns)
                    if steps[nsi] > step:
                        steps[nsi] = step
                        q.append((ns, nsi, ni))
            if revq:
                state, si, index = revq.popleft()
                if revsteps[si] + steps[si] < float('inf'):
                    return revsteps[si] + steps[si]

                step = revsteps[si] + 1
                for ns, ni in next_state(state, index):
                    nsi = state_to_index(ns)
                    if revsteps[nsi] > step:
                        revsteps[nsi] = step
                        revq.append((ns, nsi, ni))

        return -1




s = Solution()
print(s.slidingPuzzle([[3,0,1],[4,2,5]]))
print(s.slidingPuzzle([[1,2,3],[4,0,5]]))
print(s.slidingPuzzle( [[1,2,3],[5,4,0]]))
print(s.slidingPuzzle([[4,1,2],[5,0,3]]))
print(s.slidingPuzzle( [[3,2,4],[1,5,0]]))