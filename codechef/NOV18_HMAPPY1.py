# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/5/18

"""

import bisect

N, Q, K = map(int, input().split())
A = [int(x) for x in input().split()]
qs = input()


ones = []
i = 0
while i < N:
    if A[i] == 1:
        j = i + 1
        while j < N and A[j] == 1:
            j += 1
        ones.append((i, j-i))
        i = j
    else:
        i += 1

# print(ones)

first, last = 0, 0
firstToStart = ones[0][0] == 0 if ones else  False
lastToEnd = ones[-1][0] + ones[-1][1] >= N if ones else False

if firstToStart:
    first = ones[0][1]
if lastToEnd:
    last = ones[-1][1]


ol = len(ones)
left, right = [0] * (ol+1), [0] * (ol+1)

# print(first, last)


mxone = 0
for i in range(1 if firstToStart else 0, ol):
    mxone = max(mxone, ones[i][1])
    left[i] = mxone

mxone = 0
for i in range(ol-2 if lastToEnd else ol-1, -1, -1):
    mxone = max(mxone, ones[i][1])
    right[i] = mxone
    
# print(left)
# print(right)

memo = {}
def query(start):
    if start in memo:
        return memo[start]
    
    ans = 0
    
    i = bisect.bisect_right(ones, (start, float('inf')))
    l = 0
    if i > 0:
        if ones[i-1][0] + ones[i-1][1] <= start:
            l = left[i-1]
        else:
            if i-2 >= 0:
                l = left[i-2]
    r = right[i] if i < ol else 0
    
    ans = max(l, r)
    if 0 < i < ol:
        # split one segment
        s, t = ones[i - 1]
        if s + t > start:
            l = start-s
            r = t-l
            ans = max(ans, l, r)
    
    if firstToStart and lastToEnd:
        if ones[0][1] < ones[-1][0]:
            if ones[0][1] < start < ones[-1][0]:
                ans = max(ans, first + last)
            elif start <= ones[0][1]:
                ans = max(ans, start+last, ones[0][1]-start)
            else:
                l = start - ones[-1][0]
                ans = max(ans, l, first + last-l)
        else:
            ans = ones[0][1]
    elif firstToStart:
        if start < ones[0][1]:
            ans = max(ans, start, ones[0][1]-start)
        else:
            ans = max(ans, ones[0][1])
    elif lastToEnd:
        if start >= ones[-1][0]:
            l = start-ones[-1][0]
            ans = max(ans, l, ones[-1][1] - l)
        else:
            ans = max(ans, ones[-1][1])
            
    
    ans = min(ans, K)
    memo[start] = ans
    return ans


start = 0
ans = []
for q in qs:
    if q == '?':
        ans.append(query(start))
    else:
        start = (start + N - 1) % N

print('\n'.join(map(str, ans)))

    
    
    
    
    
