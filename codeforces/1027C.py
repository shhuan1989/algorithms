# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""

import collections



def solve(sticks):
    sticks.sort()
    
    i = 0
    b = []
    while i < len(sticks)-1:
        j = i + 1
        while j < len(sticks) and sticks[i] == sticks[j]:
            j += 1
        
        if j-i >= 4:
            return '{} {} {} {}'.format(sticks[i], sticks[i], sticks[i], sticks[i])
        elif j-i >= 2:
            b.append(sticks[i])
            
        i = j
    
    sticks = b
    recti = 0
    if len(sticks) > 2:
        areas = [sticks[i] * sticks[i + 1] for i in range(len(sticks) - 1)]
        p2 = [sticks[i] ** 2 for i in range(len(sticks))]
        perimeters = [p2[i] + p2[i + 1] for i in range(len(sticks) - 1)]
    
        for i in range(1, len(sticks) - 1):
            if areas[i] * perimeters[recti] > areas[recti] * perimeters[i]:
                recti = i

    return '{} {} {} {}'.format(sticks[recti], sticks[recti], sticks[recti + 1], sticks[recti + 1])


def solve2(sticks):
    wc = collections.Counter(sticks)
    for w, c in wc.items():
        if c >= 4:
            return '{} {} {} {}'.format(w, w, w, w)
        
    sticks = [w for w, c in wc.items() if c >= 2]
    
    recti = 0
    if len(sticks) > 2:
        sticks.sort()
        areas = [sticks[i] * sticks[i+1] for i in range(len(sticks)-1)]
        p2 = [sticks[i]**2 for i in range(len(sticks))]
        perimeters = [p2[i] + p2[i+1] for i in range(len(sticks)-1)]
        
        for i in range(1, len(sticks)-1):
            if areas[i] * perimeters[recti] > areas[recti] * perimeters[i]:
                recti = i
            
    return '{} {} {} {}'.format(sticks[recti], sticks[recti], sticks[recti+1], sticks[recti+1])
    

T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(A))

print('\n'.join(ans))