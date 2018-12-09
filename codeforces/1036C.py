# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""

import math



nums = [i for i in range(10)]
for l in range(1, 19):
    for d in range(1, 10):
        nums.append(d * (10 ** l))
    
    x = [0 for _ in range(l)]
    for s in range(1, 10):
        x[0] = s
        for i in range(1, l):
            for t in range(1, 10):
                x[i] = t
                nums.append(int(''.join(map(str, x))))
            x[i] = 0
        
        if l > 2:
            for i in range(1, l):
                for t in range(1, 10):
                    x[i] = t
                    for j in range(i+1,l):
                        for u in range(1, 10):
                            x[j] = u
                            nums.append(int(''.join(map(str, x))))
                        x[j] = 0
                    x[i] = 0

nums.sort()

# print(nums[:1001])

for v in range(1001):
    if v not in nums[:1001]:
        print(v)

import bisect

T = int(input())
ans = []
for ti in range(T):
    l, r = map(int, input().split())
    
    a = bisect.bisect_left(nums, l)
    b = bisect.bisect_right(nums, r)
    ans.append(b-a)
    
print('\n'.join(map(str, ans)))