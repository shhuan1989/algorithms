# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/7/18

"""


def solve2(num, step, out):
    if num <= 1:
        return 1

    if step == 0:
        return 1/num

    left = 0
    if out > 0 or num % 2 != 0:
        left = (num+1) // 2
    else:
        half = num // 2
        if half % 2 == 0:
            left = half
        else:
            left = half + 1

    return solve(left, step-1, out + num - left)


def solve(num, step):
    out = 0
    while True:
        if num <= 1:
            return 1
    
        if step == 0:
            return 1 / num
    
        left = 0
        if out > 0 or num % 2 != 0:
            left = (num + 1) // 2
        else:
            half = num // 2
            if half % 2 == 0:
                left = half
            else:
                left = half + 1
    
        # return solve(left, step - 1, out + num - left)
        out += num - left
        num = left
        step -= 1

ans = []
T = int(input())
for ti in range(T):
    N, K = map(int, input().split())
    ans.append(solve(N, K))

print('\n'.join(map(str, ans)))
    