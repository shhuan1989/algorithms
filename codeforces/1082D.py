# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/3/18

"""


N = int(input())
D = [int(x) for x in input().split()]

if sum(D) < 2*(N-1):
    print("NO")
else:
    D = [0] + D
    gt2 = [i for i in range(1, N+1) if D[i] > 1]
    gt1 = [i for i in range(1, N + 1) if D[i] == 1]
    
    ans = []
    if len(gt2) > 1:
        for i in range(len(gt2) - 1):
            ans.append((gt2[i], gt2[i + 1]))
        for i in range(1, len(gt2) - 1):
            D[gt2[i]] -= 2
        D[gt2[0]] -= 1
        D[gt2[-1]] -= 1
    diameter = len(gt2)
    
    
    if len(gt1) >= 2:
        ans.append((gt1[0], gt2[0]))
        ans.append((gt1[1], gt2[-1]))
        D[gt2[0]] -= 1
        D[gt2[-1]] -= 1
        diameter += 2
    elif len(gt1) >= 1:
        ans.append((gt1[0], gt2[0]))
        D[gt2[0]] -= 1
        diameter += 1
    else:
        pass
    
    t2i = 0
    for v in gt1[2:]:
        while t2i < len(gt2) and D[gt2[t2i]] <= 0:
            t2i += 1
        if t2i >= len(gt2):
            print('NO')
            exit(0)
        u = gt2[t2i]
        D[u] -= 1
        ans.append((v, u))
    print('YES {}'.format(diameter-1))
    print(len(ans))
    print('\n'.join(["{} {}".format(u, v) for (u, v) in ans]))
            
            
    
    
    

