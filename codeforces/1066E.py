# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/3/18


A的每个是1的位会被加到结果几次？
假设A[i]是'1'， 那么会被加B[:i].count('1')次，所以结果增加 2^i * (B[:i].count('1'))。
使用数组预处理计算B的每个区间[0, i]包含的'1'的个数

"""

N, M = map(int, input().split())

A = input()
B = input()

ai = A.find('1')
bi = B.find('1')
A = A[ai:] if ai >= 0 else ''
B = B[bi:] if bi >= 0 else ''

A = A[::-1]
B = B[::-1]
MOD = 998244353


boneCount = [0] * (len(B)+1)
for i in range(len(B)-1, -1, -1):
    boneCount[i] += boneCount[i+1] + (1 if B[i] == '1' else 0)
    
ans = 0
add = 1
for ai in range(min(len(A), len(B))):
    if A[ai] == '1':
        ans += boneCount[ai] * add
        ans %= MOD
        
    add *= 2
    add %= MOD
    

print(ans)

