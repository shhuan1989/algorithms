# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/11

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
matplotlib.use('MacOSX')
from scipy.stats import entropy
import numpy as np


def parseJson(val, prefix=''):
    if not val:
        return {}
    
    if type(val) is dict:
        ret = {}
        for k, v in val.items():
            if type(v) is set:
                v = list(v)
            if type(v) is list:
                for i, u in enumerate(v):
                    sub = parseJson(u, '{}.{}.{}'.format(prefix, k, i))
                    for sk, sv in sub.items():
                        ret[sk] = sv
            else:
                sub = parseJson(v, '{}.{}'.format(prefix, k))
                for sk, sv in sub.items():
                    ret[sk] = sv
        
        return ret
    
    try:
        w = json.loads(val)
        if type(w) is str:
            w = json.loads(w)
        ret = {}
        for k, v in w.items():
            sub = parseJson(v, '{}-{}'.format(prefix, k))
            for sk, sv in sub.items():
                ret[sk] = sv
        
        return ret
    except:
        try:
            nval = val.replace('\\"', '\"')
            nval = nval.replace('\\\\\"', '\\\"')
            nval = nval[1:-1]
            w = json.loads(nval)
            if type(w) is str:
                w = json.loads(w)
            
            ret = {}
            for k, v in enumerate(w):
                sub = parseJson(v, '{}-{}'.format(prefix, k))
                for sk, sv in sub.items():
                    ret[sk] = sv
            return ret
        except:
            pass
    
    return {prefix: val}
    

def loadData(path):
    df = pd.read_csv(path)
    columns = df.columns.tolist()
    data = []
    for i, row in df.iterrows():
        drow = {}
        for i, v in enumerate(row):
            w = parseJson(v, columns[i])
            if type(w) is dict:
                for k, v in w.items():
                    drow[k] = v
            else:
                drow[columns[i]] = w
                
        data.append(drow)

    keys = set()
    for d in data:
        keys |= {k for k, v in d.items()}
    
    keys = list(sorted(keys))
    dfdata = []
    for d in data:
        row = []
        for k in keys:
            row.append(d.get(k, ''))
        dfdata.append(row)
    
    df = pd.DataFrame(data=dfdata, columns=keys)
    # print(keys)
    # print(df.head())
    df = df.fillna(0)
    return df


def analyze(df, pre=''):
    if df.empty:
        return
    columns = df.columns.tolist()
    n = len(df)
    ret = []
    for name in columns:
        vals = df[name].tolist()
        wc = collections.Counter(vals)
        ps = np.array(list(wc.values())) / n
        e = entropy(ps)
        if e > 0:
            ret.append((e, name))
    
    ret.sort()
    # print('\n'.join(['{} {}'.format(u, v) for v, u in ret]))
    if not ret:
        return
    
    print('=' * 80)
    split = ret[0][1]
    print('split by {}-{}'.format(pre, split))
    
    wc = collections.Counter(df[split].tolist())
    print(wc)
    maxval = max(wc.values())
    maxkey = [w for w, c in wc.items() if c == maxval][0]
    
    analyze(df[df[split] == maxkey], '{}-{}'.format(pre, split))
    
    return ret
    
    
        
    
        



def showToken():
    df = pd.read_csv('~/Downloads/extract-2020-06-12_10-06-17.csv')
    playlistBody = df['@error.extras.playlistBody']
    
    tokenLens = collections.defaultdict(int)
    for log in playlistBody:
        log = log.replace('\\"', '\"')
        log = log.replace('\\\\\"', '\\\"')
        log = log[1:-1]
        val = json.loads(log)
        # print(val)
        # print(val, val['token'])
        token = val.get('token', '')
        if token:
            tokenLens[len(token)] += 1
        else:
            tokenLens[0] += 1

    
    wc = [(w, c) for w, c in tokenLens.items()]
    cw = [(c, w) for w, c in tokenLens.items()]
    cw.sort(reverse=True)
    print('\n'.join(['{} {}'.format(w, c) for c, w in cw]))
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()
    

def showParentDevice():
    df = pd.read_csv('~/Downloads/extract-2020-06-12_10-06-01.csv')
    parents = df['@error.extras.parent_device_family'].tolist()
    wc = collections.Counter(parents)
    wc = [(w, c) for w, c in wc.items()]
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()
    
def showParentiOSAppVersion():
    df = pd.read_csv('~/Downloads/extract-2020-06-11_23-06-78.csv')
    parents = df[df['@error.extras.parent_device_family']=='iOS']['error.extras.parent_app_version'].tolist()
    wc = collections.Counter(parents)
    wc = [(w, c) for w, c in wc.items()]
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()
    
def showParentOsVersion():
    df = pd.read_csv('~/Downloads/extract-2020-06-11_23-06-17.csv')
    parents = df['@error.extras.parent_device_os'].tolist()
        
    wc = collections.Counter(parents)
    wc = [(w, c) for w, c in wc.items()]
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()


def showParentDeviceModel():
    df = pd.read_csv('~/Downloads/extract-2020-06-12_09-06-59.csv')
    parents = df['@error.extras.parent_device_model'].tolist()
    
    wc = collections.Counter(parents)
    wc = [(w, c) for w, c in wc.items()]
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()
    
def showAppVersion():
    df = pd.read_csv('~/Downloads/extract-2020-06-12_09-06-59.csv')
    parents = df['context.app_version'].tolist()
    
    wc = collections.Counter(parents)
    wc = [(w, c) for w, c in wc.items()]
    plt.pie(x=[c for w, c in wc], labels=[w for w, c in wc])
    plt.show()
    

def showdata(df, column):
    row = df[column].tolist()
    wc = collections.Counter(row)
    cw = [(c, w if w else 'NaN') for w, c in wc.items()]
    cw.sort(reverse=True)
    cw = cw[:10]
    
    plt.pie(x=[c for c, w in cw], labels=[w for c, w in cw], autopct='%1.1f%%',)
    plt.show()
    
    
    
if __name__ == '__main__':
    # showToken()
    # showParentDevice()
    #
    # showParentiOSAppVersion()
    # showParentOsVersion()
    # showParentDeviceModel()
    # showAppVersion()

    v = {'values': [
        {'mimeType': 'video/mp4', 'codecs': 'avc1.64002a', 'type': 'H264', 'tier': None, 'width': 1920, 'heigh': 1080,
         'framerate': 60, 'profile': 'HIGH', 'level': '4.2'}]}

    # print(parseJson(v))
    path = '~/Downloads/extract-2020-06-12_22-06-65.csv'
    df = loadData(path)
    print(df.columns.tolist())
    # analyze(df, '')
    # print(df['@error.extras.playlistBody-content_eab_id'].tolist())
    df = df[df['context.app_version'] == '2.27.4']
    showdata(df, 'Context Build Number')
    
