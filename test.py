# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""


import collections
import heapq

import bisect
import re



def rep(pattern, repl, line):
    i = 0
    p = re.compile(pattern, re.IGNORECASE)
    while i < len(line):
        m = p.search(line, i)
        if m:
            s, e = m.start(), m.end()
            line = line[:s] + repl + line[e:]
            i = e
        else:
            break
    
    return line



wds = ['>Extensions', 'AdTitle', 'Brand', 'AdvertiserId', 'AgencyId', 'AdFeedId', 'AdFeedbackId', 'FlightId', 'AdUnitId', 'IsViewability', 'AdUnitType', 'Shareable', 'FreePass', 'AdUIMode', 'Swappable', 'HideAdRelevance', 'RecommendationTracking', 'AddOnInformation', 'DetachedCompanionAds', 'SwapToken', 'IsBlankAd', 'IsPlusUpsellAuditParam', 'Linear', 'Linear', 'CompanionAds', 'AuditParam', 'key', 'UserState', 'SessionState', 'AdTargetingValidation', 'AdTargetingUserInfo', 'upid', 'AdType', 'Cdns', 'VAST']

with open('/Users/shuangquan.huang/Desktop/template.xml', 'r') as f:
    for line in f:
        for w in re.findall('<\w+ ', line):
            wds.append(w[1:-1])
    
print(wds)




ps = [re.compile('<(\w)(\w)+'), re.compile('</(\w)(\w)+')]
ans = []
with open('/Users/shuangquan.huang/Desktop/adplaylist.xml', 'r') as f:
    for line in f:
        nline = list(line)
        for p in ps:
            m = p.search(line)
            if m:
                i = m.start(1)
                nline[i] = nline[i].upper()
        nline = ''.join(nline)
        for w in wds:
            nline = rep(w, w, nline)
        ans.append(nline)
        
with open('/Users/shuangquan.huang/Desktop/adplaylist_2.xml', 'w') as f:
    f.writelines(ans)

