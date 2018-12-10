# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""


s = input()

ans = 0
n = len(s)
i = 0
while i < len(s):
    j = i + 1
    
    while j != i and s[(j-1+n) % n] != s[j % n]:
        j = (j+1)%n
    
    if j == i:
        ans = n
        break
    elif j > i:
        ans = max(j-i, ans)
    else:
        ans = max(ans, n-i+j)
        break
        
    i = j

print(ans)
