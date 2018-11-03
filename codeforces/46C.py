# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/2/18

"""



def steps(start, target):
    
    ans = 0
    for i, v in enumerate(start):
        u = target[i]
        if v != u:
            for j in range(i+1, len(start)):
                a, b = start[j], target[j]
                if a != b and a == u:
                    start[i], start[j] = start[j], start[i]
                    break
            ans += 1
    
    return ans


def solve(seq):
    hc = seq.count('H')
    tc = len(seq) - hc
    ans = float('inf')
    for i in range(tc+1):
        s = ['T'] * i + ['H'] * hc + ['T'] * (tc-i)
        ans = min(steps(seq.copy(), s), ans)
    for i in range(hc+1):
        s = ['H'] * i + ['T'] * tc + ['H'] * (hc-i)
        ans = min(steps(seq.copy(), s), ans)
    return ans
    
    
N = int(input())
line = list(input())
print(solve(line))