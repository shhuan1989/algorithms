# -*- coding: utf-8 -*-


"""
created by shhuan at 2018/11/3 11:15

"""


N, T = map(int, input().split())

A = [int(x) for x in input().split()]

ans = 0
while A and T > 0:
    sa = sum(A)
    if T >= sa:
        ans += T // sa * len(A)
        T %= sa
    else:
        for i, a in enumerate(A):
            if T <= 0:
                break

            if T >= a:
                T -= a
                ans += 1

        A = [a for a in A if a <= T]

print(ans)
