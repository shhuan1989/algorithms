# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""

N = int(input())
X = []
Y = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    X.append((x1, x2))
    Y.append((y1, y2))
    

xl, xr = max([x1 for x1, x2 in X]), min([x2 for x1, x2 in X])
yb, yt = max([y1 for y1, y2 in Y]), min([y2 for y1, y2 in Y])

if xl <= xr and yb <= yt:
    print('{} {}'.format(xl, yb))
else:

    xlremoves = {i for i in range(N) if X[i][0] == xl}
    xrmin = min([X[i][1] for i in xlremoves])
    xlremoves = {i for i in xlremoves if X[i][1] == xrmin}
    
    xrremoves = {i for i in range(N) if X[i][1] == xr}
    xlmax = max([X[i][0] for i in xrremoves])
    xrremoves = {i for i in xrremoves if X[i][0] == xlmax}
    
    
    ybremoves = {i for i in range(N) if Y[i][0] == yb}
    ytmin = min([Y[i][1] for i in ybremoves])
    ybremoves = {i for i in ybremoves if Y[i][1] == ytmin}
    
    ytremoves = {i for i in range(N) if Y[i][1] == yt}
    ybmax = max([Y[i][0] for i in ytremoves])
    ytremoves = {i for i in ytremoves if Y[i][0] == ybmax}
    
    
    removes = []
    if xl > xr and yb > yt:
        # removes = xlremoves | xrremoves | ybremoves | ytremoves
        if xlremoves and xrremoves:
            if len(xlremoves) < len(xrremoves):
                removes = xlremoves
            elif len(xlremoves) > len(xrremoves):
                removes = xrremoves
            else:
                removes = xlremoves | xrremoves
        else:
            removes = xlremoves | xrremoves
        
        if ybremoves and ytremoves:
            if len(ybremoves) < len(ytremoves):
                removes &= ybremoves
            elif len(ybremoves) > len(ytremoves):
                removes &= ytremoves
            else:
                removes &= ybremoves | ytremoves
        else:
            removes &= ybremoves | ytremoves
            
    elif xl > xr:
        if xlremoves and xrremoves:
            if len(xlremoves) < len(xrremoves):
                removes = xlremoves
            elif len(xlremoves) > len(xrremoves):
                removes = xrremoves
            else:
                removes = xlremoves | xrremoves
        else:
            removes = xlremoves | xrremoves
    else:
        if ybremoves and ytremoves:
            if len(ybremoves) < len(ytremoves):
                removes = ybremoves
            elif len(ybremoves) > len(ytremoves):
                removes = ytremoves
            else:
                removes = ybremoves | ytremoves
        else:
            removes = ybremoves | ytremoves
        
    for i in removes:
        xl = max([x[0] for j, x in enumerate(X) if j != i])
        xr = min([x[1] for j, x in enumerate(X) if j != i])
        yb = max([y[0] for j, y in enumerate(Y) if j != i])
        yt = min([y[1] for j, y in enumerate(Y) if j != i])
        if xl <= xr and yb <= yt:
            print('{} {}'.format(xl, yb))
            break