# -*- coding:utf-8 -*-
import pandas as pd
from scipy.fftpack import fft
from math import floor
import sys

params={}
params['path'] = 'E:/EXweek3/test.csv'
params['opath'] = 'E:/EXweek3/test_tiqu.csv'
params['clusters'] = 32
params['overlap'] = 0.750
params['len_piece'] = 2048
argvs=sys.argv

try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])

    lenth = params['len_piece']
    step = floor(lenth/params['clusters']/2)
    overlap=floor(lenth*(1-params['overlap']))
    data1 = pd.read_csv(params['path'])
    data = data1[['DE_time','FE_time']]
    label = -1
    rpm = -1
    
    if data.__contains__('Label'):
        label = int(data['Label'].mean())
        del data['Label']
    if data.__contains__('RPM'):
        rpm=int(data['RPM'].mean())
        del data['RPM']
    odata=pd.DataFrame()
    for j in data.columns:
        y=pd.DataFrame()
        for k in range(0,len(data[j]),overlap):
            x=data[j][k:k+lenth]
            if len(x)<lenth:
                break
            fft_y=2*abs(fft(x,lenth)/lenth)[0:int(lenth/2)]
            y=y.append({j+'_p'+str(l):(fft_y[l*step:(l+1)*step]**2).mean() for l in range(0,params['clusters'])},
                        ignore_index=True)
        odata=pd.concat([odata,y],axis=1)
    if not rpm==-1:
        odata['RPM']=rpm
    if not label==-1:
        odata['Label']=label
    
    array = []
    array1 = data1['label'].tolist()
    a = int(len(data)/len(odata))
    length = len(array1) - 1 - a
    judge = a / 2
    for i in range (0, length, a):
        last = i + a - 1
    
        if array1[i: last].count(array1[i]) >= judge:
            array.append(array1[i])
        
        else:
            r = i + a
            array.append(array1[r])
    
    odata['label'] = array[0:len(odata)]
    odata.to_csv(params['opath'],index=False)
except Exception as e:
    print(e)