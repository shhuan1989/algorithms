# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/22/18

"""


def gcd(x, y):
    while y:
        x, y = y, x%y
        
    return x


N, M, K = map(int, input().split())

p = 2 * N * M

if p % K != 0:
    print("NO")
    exit(0)

x = max(gcd(N, K), gcd(M, K))

a, b = 0, 0
if x == 1:
    a, b = N // x, 2 * x * M // K
else:
    # a, b = N // x, x * M // K => a*b = N*M/K = 0.5S => a*2 or b*2
    a, b = N // x, x * M // K
    if b * 2 < M:
        b = x * M * 2 // K
    else:
        a *= 2

print("YES")
print("0 0")
print("{} 0".format(a))
print("0 {}".format(b))
