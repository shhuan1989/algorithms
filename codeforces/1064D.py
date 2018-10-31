# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/17/18

"""

import collections

visited = [[False for _ in range(2001)] for _ in range(2001)]

N, M = map(int, raw_input().split())
R, C = map(int, raw_input().split())
X, Y = map(int, raw_input().split())

R -= 1
C -= 1

A = []
for i in range(N):
    A.append([x for x in raw_input()])



def solve(A, N, M, R, C, X, Y):
    
    q = collections.deque([])
    q.append((R, C, X, Y))
    ans = 0
    while q:
        r, c, x, y = q.popleft()
        visited[r][c] = True
        ans += 1
        if r > 0 and not visited[r-1][c] and A[r-1][c] == '.':
            visited[r-1][c] = True
            q.appendleft((r-1, c, x, y))
        if r < N-1 and not visited[r+1][c] and A[r+1][c] == '.':
            visited[r+1][c] = True
            q.appendleft((r+1, c, x, y))
        
        if x >= y:
            if x > 0 and not visited[r][c-1] and c > 0 and A[r][c-1] == '.':
                visited[r][c-1] = True
                q.append((r, c-1, x-1, y))
            if y > 0 and not visited[r][c+1] and c < M-1 and A[r][c+1] == '.':
                visited[r][c+1] = True
                q.append((r, c+1, x, y-1))
        else:
            if y > 0 and not visited[r][c + 1] and c < M - 1 and A[r][c + 1] == '.':
                visited[r][c + 1] = True
                q.append((r, c + 1, x, y - 1))
            if x > 0 and not visited[r][c-1] and c > 0 and A[r][c-1] == '.':
                visited[r][c-1] = True
                q.append((r, c-1, x-1, y))
            
        
    return ans
        
    
print(solve(A, N, M, R, C, X, Y))
