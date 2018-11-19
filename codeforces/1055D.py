# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/13/18

Alice has written a program and now tries to improve its readability.
One of the ways to improve readability is to give sensible names to the variables,
so now Alice wants to rename some variables in her program. In her IDE there is a command called "massive refactoring",
which can replace names of many variable in just one run. To use it, Alice needs to select two strings 𝑠 and 𝑡
and after that for each variable the following algorithm is performed:
if the variable's name contains 𝑠 as a substring, then the first (and only first) occurrence of 𝑠 is replaced with 𝑡.
If the name doesn't contain 𝑠, then this variable's name stays the same.

The list of variables is known and for each variable both the initial name and the name Alice wants this variable
change to are known. Moreover, for each variable the lengths of the initial name and the target name are equal
(otherwise the alignment of the code could become broken). You need to perform renaming of all variables in exactly one
 run of the massive refactoring command or determine that it is impossible.


Input
The first line contains the only integer 𝑛 (1≤𝑛≤3000) — the number of variables in Alice's program.

The following 𝑛 lines contain the initial names of variables 𝑤1,𝑤2,…,𝑤𝑛, one per line.
After that, 𝑛 more lines go, the 𝑖-th of them contains the target name 𝑤′𝑖 for the 𝑖-th variable.
It is guaranteed that 1≤|𝑤𝑖|=|𝑤′𝑖|≤3000.

It is guaranteed that there is at least one variable having its target name different from the initial name.
Both initial and target names consist of lowercase English letters only.
For each variable the length of its initial name is equal to the length of its target name.

Output
If it is impossible to rename all variables with one call of "massive refactoring", print "NO" (quotes for clarity).

Otherwise, on the first line print "YES" (quotes for clarity) and on the following lines print 𝑠 and 𝑡 (1≤|𝑠|,|𝑡|≤5000),
which should be used for replacement. Strings 𝑠 and 𝑡 should consist only of lowercase letters of English alphabet.

If there are multiple ways to perform a "massive refactoring", you can use any of them.



"""

# N = int(input())
#
# A, B = [], []
# for i in range(N):
#     A.append(input())
# for i in range(N):
#     B.append(input())

# import time
# import random
# def genInput():
#     N = 3000
#     A = []
#     B = []
#
#     # s = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(5000)])
#     # t = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(5000)])
#     # for i in range(N):
#     #     A.append(s)
#     #     B.append(t)
#
#     for i in range(N):
#         s = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(1, random.randint(10, 2000))])
#         t = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(len(s))])
#
#         left = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(1, random.randint(10, 2000))])
#         right = ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(5000 - len(s) - len(left))])
#
#         if random.randint(1, 10) < 2:
#             A.append(left + right)
#             B.append(left + right)
#         else:
#             A.append(left + s + right)
#             B.append(left + s + right)
#
#     return N, A, B
#
# N, A, B = genInput()
# print('starting')
#
import time

t0 = time.time()

N = 3000
A = ['a' * (4999 - i) + 'b' for i in range(N)]
B = ['a' * (4999 - i) + 'c' for i in range(N)]


#

def isSamePrefix(vals, n):
    return all(vals[i][:n] == vals[0][:n] for i in range(len(vals)))


def maxSame(vals):
    if not vals or not vals[0]:
        return 0

    lo, hi = 0, len(vals[0]) + 1

    while lo < hi:
        m = (lo + hi) // 2

        if isSamePrefix(vals, m):
            lo = m + 1
        else:
            hi = m

    return lo - 1


def solve(A, B):
    same = []

    left, right = '', ''
    s, t = '', ''
    for i in range(N):
        if A[i] == B[i]:
            same.append(A[i])
            continue

        a, b = A[i], B[i]
        l, r = 0, len(a) - 1
        while l < len(a) and a[l] == b[l]:
            l += 1
        while r >= 0 and a[r] == b[r]:
            r -= 1

        if s == '':
            s, t = a[l: r + 1], b[l: r + 1]
            left = a[:l]
            right = a[r + 1:]
        else:
            tmps = a[l: r + 1]
            if tmps != s:
                print('NO')
                return

            ll = 0
            while ll < min(l, len(left)) and a[l - ll - 1] == left[len(left) - ll - 1]:
                ll += 1
            lr = 0
            while r + lr + 1 < len(a) and lr < len(right) and a[r + lr + 1] == right[lr]:
                lr += 1

            left = a[l - ll: l]
            right = a[r + 1: r + 1 + lr]

    s = left + s + right
    t = left + t + right

    if any([a.find(s) >= 0 for a in same]):
        print('NO')
        return

    print('YES')
    print(s)
    print(t)


def solve2(A, B):
    st = []
    same = []
    for i in range(N):
        if A[i] != B[i]:
            st.append((A[i], B[i]))
        else:
            same.append((A[i], B[i]))

    s, t = '', ''

    mxLen = 0
    for i in range(len(st)):
        a, b = st[i]

        l, r = 0, len(a) - 1
        while l < len(a) and a[l] == b[l]:
            l += 1

        while r >= 0 and a[r] == b[r]:
            r -= 1

        ts = a[l: r + 1]
        tt = b[l: r + 1]
        if len(ts) > len(s):
            s = ts
            t = tt
        if 0 < mxLen < len(s):
            print('NO')
            return

        mxLen = max(mxLen, len(a))

    lefts, rights = [], []
    for i in range(len(st)):
        a, b = st[i]
        ai = a.find(s)
        if ai < 0:
            print('NO')
            return
        if a[:ai] + t + a[ai + len(s):] != b:
            print('NO')
            return

        lefts.append(a[:ai])
        rights.append(a[ai + len(s):])

    # print(time.time() - t0)
    minLenLeft = min([len(x) for x in lefts] or [0])
    minLenRight = min([len(x) for x in rights] or [0])

    rights = [x[:minLenRight] for x in rights]
    lefts = [x[len(x) - minLenLeft:][::-1] for x in lefts]

    xl = maxSame(lefts)
    xr = maxSame(rights)

    left = lefts[0][:xl][::-1] if lefts else ''
    right = rights[0][:xr] if rights else ''

    s = left + s + right
    t = left + t + right

    if any([a.find(s) >= 0 for a, b in same]):
        print('NO')
        return

    print('YES')
    print(s)
    print(t)


solve(A, B)

print(time.time() - t0)