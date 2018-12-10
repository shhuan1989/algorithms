# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""

import collections

N = int(input())
A = set()
counts = collections.defaultdict(int)
left = {}
right = {}
for i in range(N):
    l, r = map(int, input().split())
    A.add((l, r))
    counts[(l, r)] += 1

if len(A) == 1:
    A = list(A)
    l, r = A[0]
    print(r - l)
else:
    itl, itr = max([l for l, r in A]), min([r for l, r in A])
    ans = max(0, itr-itl)
    
    removes = {(l, r) for l, r in A if l == itl or r == itr}
    for seg in removes:
        if counts[seg] == 1:
            itl, itr = max([l for l, r in A - {seg}]), min([r for l, r in A - {seg}])
            ans = max(ans, itr-itl)
    
    print(ans)






