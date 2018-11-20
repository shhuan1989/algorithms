# -*- coding:utf-8 -*-
la, ra, ta = map(int, input().split())
lb, rb, tb = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


# [la+ka*ta, ...]
# [lb+kb*tb, ...]

g = gcd(ta, tb)
l0 = la % g
l1 = lb % g
r0 = l0 + ra - la
r1 = l1 + rb - lb

res = 0
l = max(l0, l1)
r = min(r0, r1)
res = max(res, r - l + 1)

l = max(l0, l1 + g)
r = min(r0, r1 + g)
res = max(res, r - l + 1)

l = max(l0 + g, l1)
r = min(r0 + g, r1)
res = max(res, r - l + 1)

print(res)