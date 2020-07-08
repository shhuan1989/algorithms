# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import re
import pandas as pd

model_excludes = {'Chromecast'}
versions = ['2.26.2', '2.27.4']
MODELS = ['Chromecast Gen 1', 'Chromecast Gen 2', 'Chromecast Gen 3', 'Chromecast Ultra', 'Google Nest Hub', 'Chromecast']


def calv3(path):
    print(path.split('.')[0])
    f = open(path, 'r')
    lines = [v.strip() for v in f.readlines()]
    
    lines = [re.sub('\s+', ' ', v) for v in lines]
    lines = [v.replace(',', '') for v in lines]
    
    data = []
    version, model = None, None
    for line in lines:
        parts = line.split(' ')
        key = ' '.join(parts[:-1])
        if key in versions:
            version = key
        elif key in MODELS:
            model = key
        else:
            name, val = ' '.join(parts[:-1]), float(parts[-1])
            data.append((version, model, name, val))
    
    # print(data)
    # print('\n'.join([' '.join(map(str, v)) for v in data]))
    
    
    bymodel = collections.defaultdict(list)
    for version, model, name, val in data:
        bymodel[model].append((version, name, val))
    
    print(bymodel)
    
    ans = []
    for model, mdata in bymodel.items():
        if model in model_excludes:
            continue
        bysender = collections.defaultdict(dict)
        names = set()
        for version, name, val in mdata:
            bysender[name][version] = val
            names.add(name)
        
        names = list(sorted(names))
        
        for name in names:
            va, vb = versions
            if name not in bysender:
                continue
            v = bysender[name]
            a, b = v[va] if va in v else 0, v[vb] if vb in v else 0
            ans.append((model, name, a, b, int((b-a)/a*10000)/100))
    
    # print(ans)
    df = pd.DataFrame(columns=['Device Model', 'Sender', versions[0], versions[1], 'Delta'], data=ans)
    print(pd.pivot_table(df, index=['Device Model', 'Sender']))
    # print(df)
            
        
    
    
    


def calculate(path):
    print(path.split('.')[0])
    f = open(path, 'r')
    lines = [v.strip() for v in f.readlines()]
    
    lines = [re.sub('\s+', ' ', v) for v in lines]
    lines = [v.replace(',', '') for v in lines]
    
    data = []
    version = None
    for line in lines:
        parts = line.split(' ')
        if parts[0] in versions:
            version = parts[0]
            data.append((version, 'AOverall', float(parts[-1])))
        else:
            if version is None:
                continue
            name, val = ' '.join(parts[:-1]), float(parts[-1])
            data.append((version, name, val))
    
    df = pd.DataFrame(columns=['App Version', 'Device Model', 'value'], data=data)
    # print(df)
    
    # print(pd.pivot_table(df, index=['App Version', 'Device Model']))
    
    
    models = list(sorted(set(df['Device Model'].tolist())))
    models = [v for v in models if v not in model_excludes]
    # print(models)
    
    bymodel = collections.defaultdict(dict)
    for version, model, val in data:
        if model in models:
            bymodel[model][version] = val
    
    # print(bymodel)
    compare = ['{:<20} {:<20} {:<20} {:<20}'.format("Device Model", versions[0], versions[1],"Delta")]
    for name in models:
        v = bymodel[name]
        va, vb = versions
        a, b = v[va] if va in v else 0, v[vb] if vb in v else 0
        compare.append('{:<20} {:<20} {:<20} {:<20.2%}'.format(name, a, b, (b-a)/a if a != 0 else b))
        
    print('\n'.join(compare))
    
    
    
    
    
    



def calculatev1(path):
    print(path.split('.')[0])
    wc = collections.defaultdict(list)
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.replace(',', '').strip()
            parts = line.split(' ')
            name = ' '.join(parts[:-1])
            if name not in model_excludes:
                wc[name].append(float(parts[-1]))
    
    change = []
    for k, v in wc.items():
        change.append('{} {:.2%}'.format(k, (v[1]-v[0])/v[0]))
    change.sort()
    return '\n'.join(change)


calculate('vpf.txt')
# calv3('vpf_by_device_model.txt')
# calculate('vpf_web_sender.txt')
# calculate('session_count_web_sender.txt')
# calculate('session_count_android_sender.txt')
# calculate('session_count_ios_sender.txt')
calculate('vsf.txt')
# calculate('vsf_android.txt')
# calculate('vsf_ios.txt')
# calculate('vsf_web.txt')
# calculate('vst_android.txt')
# calculate('vst_ios.txt')
# calculate('vst_web.txt')
calculate('cirr.txt')
# calculate('cirr_android.txt')
# calculate('cirr_ios.txt')
# calculate('cirr_web.txt')
# calculate('cireph.txt')
# calculate('cireph_android.txt')
# calculate('cireph_ios.txt')
# calculate('cireph_web.txt')
# calculate('cirr_by_model.txt')
calculate('vst.txt')